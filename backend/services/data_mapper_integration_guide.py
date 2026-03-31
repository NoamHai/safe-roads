"""
INTEGRATION GUIDE: Data Mapper with Model Service

This document shows how to integrate the data_mapper module with your existing
model_service.py to handle frontend-to-backend conversion.

Example Usage in predict route:
    1. Frontend sends JSON with Hebrew strings
    2. Backend calls prepare_model_input() or prepare_model_array()
    3. Result is passed to model.predict_proba()
    4. Returns probability for model consumption
"""

import json
from typing import Dict, Any
import numpy as np

from data_mapper import (
    prepare_model_input,
    prepare_model_array,
    validate_ui_input,
    map_value_to_integer,
)


# ============================================================================
# EXAMPLE 1: Integration with FastAPI Route
# ============================================================================

"""
# In backend/routes/predict.py or backend/app.py:

from fastapi import FastAPI, HTTPException
from data_mapper import prepare_model_array, validate_ui_input, FEATURE_CONFIG

@app.post("/predict")
async def predict_risk(request: PredictRequest):
    '''
    Receive UI input and return prediction.
    '''
    
    # 1. Convert Pydantic model to dictionary
    ui_input = request.model_dump()
    
    # 2. Validate input
    validation = validate_ui_input(ui_input)
    if not validation['valid']:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid input",
                "missing": validation['missing_features'],
                "warnings": validation['warnings']
            }
        )
    
    # 3. Convert to model array
    try:
        model_array = prepare_model_array(ui_input)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # 4. Get prediction from model
    probability = model_service.predict_probability(model_array)
    
    # 5. Return result
    return {
        "probability": probability,
        "risk_percent": int(probability * 100),
        "breakdown": generate_breakdown(ui_input)
    }
"""


# ============================================================================
# EXAMPLE 2: Standalone Conversion Function
# ============================================================================

def convert_frontend_to_model_input(
    frontend_data: Dict[str, Any]
) -> Dict[str, int]:
    """
    Convert frontend form data (Hebrew strings) to model input (integer codes).
    
    This is a wrapper that handles error cases gracefully.
    
    Args:
        frontend_data: Dictionary from frontend form
        Example: {
            "hour": "14:00",
            "month": "5",
            "accident_type": "חזיתי",
            "speed_limit": "עד 80 קמ״ש",
            "road_surface": "יבש"
        }
    
    Returns:
        Dictionary with integer codes ready for model
    
    Raises:
        ValueError: If critical data is missing or invalid
    """
    
    # Validate first
    validation = validate_ui_input(frontend_data)
    
    if validation['errors']:
        raise ValueError(f"Validation errors: {'; '.join(validation['errors'])}")
    
    if validation['warnings']:
        print(f"Validation warnings: {'; '.join(validation['warnings'])}")
    
    # Convert to model format
    try:
        model_input = prepare_model_input(frontend_data)
        return model_input
    except Exception as e:
        raise ValueError(f"Conversion failed: {str(e)}")


# ============================================================================
# EXAMPLE 3: Handling Different Frontend Formats
# ============================================================================

def convert_simple_values(
    hour: int = None,
    month: int = None,
    accident_type: str = None,
    speed_limit: str = None,
    road_surface: str = None,
    **kwargs
) -> Dict[str, int]:
    """
    Convert simple frontend inputs (keyword arguments) to model format.
    
    This is useful if frontend sends individual values instead of a dict.
    
    Args:
        hour: Integer hour (0-23) or formatted string "HH:00"
        month: Integer month (1-12) or string "1"-"12"
        accident_type: Hebrew string like "חזיתי"
        speed_limit: Hebrew string like "עד 80 קמ״ש"
        road_surface: Hebrew string like "יבש"
        **kwargs: Additional features
    
    Returns:
        Dictionary with integer codes
    
    Examples:
        >>> result = convert_simple_values(
        ...     hour=14,
        ...     month=5,
        ...     accident_type="חזיתי",
        ...     speed_limit="עד 80 קמ״ש",
        ...     road_surface="יבש"
        ... )
    """
    
    # Build full feature dictionary
    ui_input = {
        "SHAA": f"{hour:02d}:00" if isinstance(hour, int) else hour,
        "HODESH_TEUNA": str(month) if month else None,
        "SUG_TEUNA": accident_type,
        "MEHIRUT_MUTERET": speed_limit,
        "PNE_KVISH": road_surface,
    }
    
    # Add any additional features
    ui_input.update(kwargs)
    
    # Remove None values and convert
    ui_input = {k: v for k, v in ui_input.items() if v is not None}
    
    return prepare_model_input(ui_input)


# ============================================================================
# EXAMPLE 4: Batch Conversion
# ============================================================================

def convert_batch(
    data_list: list,
    feature_order: list = None
) -> np.ndarray:
    """
    Convert multiple records from frontend format to model format.
    
    Args:
        data_list: List of dictionaries (each is UI input)
        feature_order: Order of features in output array
    
    Returns:
        2D numpy array (n_samples × n_features)
    
    Examples:
        >>> batch_data = [
        ...     {"SHAA": "08:00", "SUG_DEREH": "עירוני בצומת", ...},
        ...     {"SHAA": "14:00", "SUG_DEREH": "לא עירוני לא בצומת", ...},
        ... ]
        >>> model_array = convert_batch(batch_data)
        >>> predictions = model.predict_proba(model_array)
    """
    
    arrays = []
    for record in data_list:
        try:
            arr = prepare_model_array(record, feature_order)
            arrays.append(arr)
        except Exception as e:
            print(f"Warning: Skipping record due to error: {e}")
            continue
    
    if not arrays:
        raise ValueError("No valid records to convert")
    
    return np.vstack(arrays)


# ============================================================================
# EXAMPLE 5: Error Handling & User Feedback
# ============================================================================

def convert_with_detailed_feedback(
    frontend_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Convert frontend data with comprehensive error/warning feedback.
    
    Returns a result dictionary that includes conversion status and any issues.
    
    Returns:
        {
            "success": bool,
            "model_input": Dict or None,
            "errors": List[str],
            "warnings": List[str],
            "suggestions": List[str]
        }
    
    Examples:
        >>> result = convert_with_detailed_feedback(frontend_data)
        >>> if result['success']:
        ...     prediction = model.predict(result['model_input'])
        ... else:
        ...     flash_to_user(result['errors'][0])
    """
    
    validation = validate_ui_input(frontend_data)
    
    result = {
        "success": False,
        "model_input": None,
        "errors": validation['errors'],
        "warnings": validation['warnings'],
        "suggestions": []
    }
    
    # Add helpful suggestions
    if validation['missing_features']:
        result['suggestions'].append(
            f"Missing features: {', '.join(validation['missing_features'])}"
        )
    
    if validation['errors']:
        result['suggestions'].append(
            "Please check your input and correct any errors shown above."
        )
    
    if not validation['valid']:
        return result
    
    # Try conversion
    try:
        result['model_input'] = prepare_model_input(frontend_data)
        result['success'] = True
    except Exception as e:
        result['errors'].append(f"Conversion error: {str(e)}")
        result['suggestions'].append(
            "An unexpected error occurred during conversion. Please try again."
        )
    
    return result


# ============================================================================
# EXAMPLE 6: JSON Serialization for Logging/Debugging
# ============================================================================

def log_conversion(
    frontend_data: Dict[str, Any],
    model_input: Dict[str, int]
) -> str:
    """
    Create a human-readable log entry for conversion tracking.
    
    Useful for debugging and understanding the conversion process.
    
    Args:
        frontend_data: Original UI input
        model_input: Converted model input
    
    Returns:
        Formatted log string
    """
    
    log_entries = [
        "=" * 80,
        "CONVERSION LOG",
        "=" * 80,
        "\nFrontend Input (Hebrew strings):",
        json.dumps(frontend_data, ensure_ascii=False, indent=2),
        "\nModel Input (Integer codes):",
        json.dumps(model_input, indent=2),
        "\nMapping Details:",
    ]
    
    # Show which code each value mapped to
    for feature, ui_value in frontend_data.items():
        model_value = model_input.get(feature)
        log_entries.append(f"  {feature:20s}: {str(ui_value):30s} → {model_value}")
    
    log_entries.append("=" * 80)
    
    return "\n".join(log_entries)


# ============================================================================
# EXAMPLE 7: Reverse Conversion (for display/logging)
# ============================================================================

from data_mapper import REVERSE_MAPPINGS

def convert_model_output_to_display_text(
    model_input: Dict[str, int]
) -> Dict[str, str]:
    """
    Convert model integer codes back to Hebrew display text.
    
    Useful for showing users what was actually predicted/processed.
    
    Args:
        model_input: Dictionary with integer codes
    
    Returns:
        Dictionary with Hebrew display text
    
    Examples:
        >>> model_input = {"MEHIRUT_MUTERET": 4, "PNE_KVISH": 2}
        >>> display = convert_model_output_to_display_text(model_input)
        >>> # display = {"MEHIRUT_MUTERET": "עד 80 קמ״ש", "PNE_KVISH": "רטוב ממים"}
    """
    
    display_text = {}
    
    for feature, integer_code in model_input.items():
        if feature in REVERSE_MAPPINGS:
            reverse_map = REVERSE_MAPPINGS[feature]
            display_text[feature] = reverse_map.get(integer_code, f"Unknown ({integer_code})")
        else:
            display_text[feature] = str(integer_code)
    
    return display_text


# ============================================================================
# TESTING & VALIDATION
# ============================================================================

def test_conversion_pipeline():
    """
    Testing function to verify the entire pipeline works correctly.
    
    Run this to validate all conversion functions.
    """
    
    print("Testing Data Mapper Conversion Pipeline")
    print("=" * 80)
    
    # Test data
    test_input = {
        "SHAA": "14:00",
        "HODESH_TEUNA": "5",
        "YOM_BASHAVUA": "שני",
        "SUG_TEUNA": "חזיתי",
        "ROAD_STRUCTURE": "דו-כיווני",
        "ROHAV": "רחב (מעל 8 מ')",
        "NAFA": "כבד",
        "ZURAT_ISHUV": "עירוני",
        "MEHIRUT_MUTERET": "עד 80 קמ״ש",
        "TEURA": "זהיר",
        "SUG_DEREH": "עירוני בצומת",
        "SIMUN_TIMRUR": "בעל רמזור",
        "MEKOM_HAZIYA": "מרכז כביש",
        "TKINUT": "גשום",
        "OFEN_HAZIYA": "תאונה",
        "PNE_KVISH": "רטוב ממים",
    }
    
    # Test 1: Basic conversion
    print("\n[Test 1] Basic conversion with prepare_model_input()")
    try:
        model_input = prepare_model_input(test_input)
        print("  ✓ Conversion successful")
        print(f"  ✓ Output keys: {len(model_input)}")
        print(f"  ✓ Sample values: {list(model_input.items())[:3]}")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
    
    # Test 2: Array conversion
    print("\n[Test 2] Array conversion with prepare_model_array()")
    try:
        model_array = prepare_model_array(test_input)
        print(f"  ✓ Array shape: {model_array.shape}")
        print(f"  ✓ Array dtype: {model_array.dtype}")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
    
    # Test 3: Validation
    print("\n[Test 3] Validation with validate_ui_input()")
    try:
        validation = validate_ui_input(test_input)
        print(f"  ✓ Valid: {validation['valid']}")
        print(f"  ✓ Errors: {len(validation['errors'])}")
        print(f"  ✓ Warnings: {len(validation['warnings'])}")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
    
    # Test 4: Reverse conversion
    print("\n[Test 4] Reverse conversion")
    try:
        display_text = convert_model_output_to_display_text(model_input)
        print("  ✓ Reverse conversion successful")
        print(f"  ✓ Sample: {list(display_text.items())[:3]}")
    except Exception as e:
        print(f"  ✗ Failed: {e}")
    
    print("\n" + "=" * 80)
    print("Testing complete!")


if __name__ == "__main__":
    test_conversion_pipeline()
