"""
Data Mapper & Preprocessing Module
Handles UI to Backend mapping and feature preparation for the accidents prediction model.

This module provides:
1. Feature mappings (Hebrew UI strings to integer codes)
2. Data validation and edge case handling
3. Conversion functions from frontend inputs to model-ready format
"""

from typing import Dict, Optional, Any, List
import pandas as pd
import numpy as np


# ============================================================================
# FEATURE MAPPINGS: Hebrew UI Strings → Integer Codes
# ============================================================================

# MEHIRUT_MUTERET (Speed Limit) - with custom edge case for 120 km/h
SPEED_LIMIT_MAPPING = {
    "לא ידוע": 0,
    "עד 50 קמ״ש": 1,
    "עד 60 קמ״ש": 2,
    "עד 70 קמ״ש": 3,
    "עד 80 קמ״ש": 4,
    "עד 90 קמ״ש": 5,
    "עד 100 קמ״ש": 6,
    "עד 110 קמ״ש": 7,
    "עד 120 קמ״ש": 8,  # Custom edge case (may not be in original dictionary)
}

# SUG_DEREH (Road Type)
ROAD_TYPE_MAPPING = {
    "לא ידוע": 0,
    "עירוני בצומת": 1,                    # Urban at junction
    "עירוני לא בצומת": 2,                # Urban not at junction
    "לא עירוני בצומת": 3,                # Non-urban at junction
    "לא עירוני לא בצומת": 4,             # Non-urban not at junction
}

# PNE_KVISH (Road Surface Condition)
ROAD_SURFACE_MAPPING = {
    "לא ידוע": 0,
    "יבש": 1,                            # Dry
    "רטוב ממים": 2,                      # Wet from water
    "מרוח בחומר דלק": 3,                 # Covered with fuel
    "מכוסה בבוץ": 4,                      # Covered in mud
}

# SUG_TEUNA (Type of Accident)
ACCIDENT_TYPE_MAPPING = {
    "לא ידוע": 0,
    "חזיתי": 1,                          # Frontal
    "אחורי": 2,                          # Rear-end
    "צדדי": 3,                           # Side
    "הולך רגל": 4,                       # Pedestrian
}

# HOUR (SHAA) - 0-23 format
HOUR_MAPPING = {
    f"{h:02d}:00": h for h in range(24)
}
HOUR_MAPPING["לא ידוע"] = 0

# MONTH (HODESH_TEUNA) - 1-12
MONTH_MAPPING = {
    f"{m}": m for m in range(1, 13)
}
MONTH_MAPPING["לא ידוע"] = 0

# YOM_BASHAVUA (Day of Week) - 1=Sunday to 7=Saturday (Israeli convention)
DAY_OF_WEEK_MAPPING = {
    "ראשון": 1,         # Sunday
    "שני": 2,           # Monday
    "שלישי": 3,         # Tuesday
    "רביעי": 4,         # Wednesday
    "חמישי": 5,         # Thursday
    "שישי": 6,          # Friday
    "שבת": 7,           # Saturday
    "לא ידוע": 0,
}

# TKINUT (Weather Condition)
WEATHER_MAPPING = {
    "לא ידוע": 0,
    "בהיר": 1,                           # Clear
    "מעונן": 2,                          # Cloudy
    "גשום": 3,                           # Rainy
    "ערפילי": 4,                         # Foggy
}

# ZURAT_ISHUV (Settlement Type/Area)
SETTLEMENT_MAPPING = {
    "לא ידוע": 0,
    "עירוני": 1,                         # Urban
    "כפרי": 2,                           # Rural
    "כביש ראשי": 3,                      # Main road/highway
}

# SIMUN_TIMRUR (Traffic Signal/Marking)
TRAFFIC_SIGNAL_MAPPING = {
    "לא ידוע": 0,
    "בעל רמזור": 1,                      # Has traffic light
    "בעל תמרור": 2,                      # Has traffic sign
    "ללא סימונים": 3,                    # No markings
}

# MEKOM_HAZIYA (Accident Location)
LOCATION_TYPE_MAPPING = {
    "לא ידוע": 0,
    "מרכז כביש": 1,                      # Center of road
    "שיץ כביש": 2,                       # Side of road
    "חניה": 3,                           # Parking
    "מדרכה": 4,                          # Sidewalk
}

# OFEN_HAZIYA (Accident Method/Manner)
ACCIDENT_METHOD_MAPPING = {
    "לא ידוע": 0,
    "תאונה": 1,                          # Collision
    "התהפכות": 2,                        # Rollover
    "יציאה מכביש": 3,                    # Leaving road
    "התחזקות": 4,                        # Gripping/Holding (rare accident type)
}

# ROHAV (Road Width) - typically in meters
ROAD_WIDTH_MAPPING = {
    "לא ידוע": 0,
    "צר (עד 6.5 מ')": 1,                 # Narrow (up to 6.5m)
    "בינוני (6.5-8 מ')": 2,              # Medium (6.5-8m)
    "רחב (מעל 8 מ')": 3,                 # Wide (over 8m)
}

# NAFA (Traffic Volume/Density)
TRAFFIC_DENSITY_MAPPING = {
    "לא ידוע": 0,
    "קל": 1,                             # Light
    "בינוני": 2,                         # Medium
    "כבד": 3,                            # Heavy
}

# TEURA (Driving Manner/Behavior)
DRIVING_MANNER_MAPPING = {
    "לא ידוע": 0,
    "זהיר": 1,                           # Careful
    "נורמלי": 2,                         # Normal
    "חפוז": 3,                           # Rushed
    "מסוכן": 4,                          # Dangerous
}

# ROAD_STRUCTURE (Engineered feature from HAD_MASLUL & RAV_MASLUL)
ROAD_STRUCTURE_MAPPING = {
    "לא ידוע": 0,
    "חד-כיווני": 1,                      # Single lane
    "דו-כיווני": 2,                      # Two-way
    "רב-נתיבים דו-כיווני": 3,           # Multi-lane two-way
    "רב-נתיבים חד-כיווני": 4,           # Multi-lane one-way
}


# ============================================================================
# REVERSE MAPPINGS: Integer Codes → Hebrew UI Strings (for visualization)
# ============================================================================

REVERSE_MAPPINGS = {
    "MEHIRUT_MUTERET": {v: k for k, v in SPEED_LIMIT_MAPPING.items()},
    "SUG_DEREH": {v: k for k, v in ROAD_TYPE_MAPPING.items()},
    "PNE_KVISH": {v: k for k, v in ROAD_SURFACE_MAPPING.items()},
    "SUG_TEUNA": {v: k for k, v in ACCIDENT_TYPE_MAPPING.items()},
    "SHAA": {v: k for k, v in HOUR_MAPPING.items()},
    "HODESH_TEUNA": {v: k for k, v in MONTH_MAPPING.items()},
    "YOM_BASHAVUA": {v: k for k, v in DAY_OF_WEEK_MAPPING.items()},
    "TKINUT": {v: k for k, v in WEATHER_MAPPING.items()},
    "ZURAT_ISHUV": {v: k for k, v in SETTLEMENT_MAPPING.items()},
    "SIMUN_TIMRUR": {v: k for k, v in TRAFFIC_SIGNAL_MAPPING.items()},
    "MEKOM_HAZIYA": {v: k for k, v in LOCATION_TYPE_MAPPING.items()},
    "OFEN_HAZIYA": {v: k for k, v in ACCIDENT_METHOD_MAPPING.items()},
    "ROHAV": {v: k for k, v in ROAD_WIDTH_MAPPING.items()},
    "NAFA": {v: k for k, v in TRAFFIC_DENSITY_MAPPING.items()},
    "TEURA": {v: k for k, v in DRIVING_MANNER_MAPPING.items()},
    "ROAD_STRUCTURE": {v: k for k, v in ROAD_STRUCTURE_MAPPING.items()},
}


# ============================================================================
# FEATURE FIELD CONFIGURATION
# ============================================================================

FEATURE_CONFIG = {
    "SHAA": {
        "type": "integer",
        "range": (0, 23),
        "mapping": HOUR_MAPPING,
        "default": 0,
        "description": "Hour of day (0-23)"
    },
    "HODESH_TEUNA": {
        "type": "integer",
        "range": (0, 12),
        "mapping": MONTH_MAPPING,
        "default": 0,
        "description": "Month of accident (1-12, 0=unknown)"
    },
    "YOM_BASHAVUA": {
        "type": "integer",
        "range": (0, 7),
        "mapping": DAY_OF_WEEK_MAPPING,
        "default": 0,
        "description": "Day of week (0=unknown, 1-7)"
    },
    "SUG_TEUNA": {
        "type": "categorical",
        "mapping": ACCIDENT_TYPE_MAPPING,
        "default": 0,
        "description": "Type of accident"
    },
    "ROAD_STRUCTURE": {
        "type": "categorical",
        "mapping": ROAD_STRUCTURE_MAPPING,
        "default": 0,
        "description": "Road structure (engineered from HAD_MASLUL & RAV_MASLUL)"
    },
    "ROHAV": {
        "type": "categorical",
        "mapping": ROAD_WIDTH_MAPPING,
        "default": 0,
        "description": "Road width"
    },
    "NAFA": {
        "type": "categorical",
        "mapping": TRAFFIC_DENSITY_MAPPING,
        "default": 0,
        "description": "Traffic density"
    },
    "ZURAT_ISHUV": {
        "type": "categorical",
        "mapping": SETTLEMENT_MAPPING,
        "default": 0,
        "description": "Settlement type/area"
    },
    "MEHIRUT_MUTERET": {
        "type": "categorical",
        "mapping": SPEED_LIMIT_MAPPING,
        "default": 0,
        "description": "Speed limit"
    },
    "TEURA": {
        "type": "categorical",
        "mapping": DRIVING_MANNER_MAPPING,
        "default": 0,
        "description": "Driving manner/behavior"
    },
    "SUG_DEREH": {
        "type": "categorical",
        "mapping": ROAD_TYPE_MAPPING,
        "default": 0,
        "description": "Road type"
    },
    "SIMUN_TIMRUR": {
        "type": "categorical",
        "mapping": TRAFFIC_SIGNAL_MAPPING,
        "default": 0,
        "description": "Traffic signal/marking"
    },
    "MEKOM_HAZIYA": {
        "type": "categorical",
        "mapping": LOCATION_TYPE_MAPPING,
        "default": 0,
        "description": "Accident location type"
    },
    "TKINUT": {
        "type": "categorical",
        "mapping": WEATHER_MAPPING,
        "default": 0,
        "description": "Weather condition"
    },
    "OFEN_HAZIYA": {
        "type": "categorical",
        "mapping": ACCIDENT_METHOD_MAPPING,
        "default": 0,
        "description": "Accident method/manner"
    },
    "PNE_KVISH": {
        "type": "categorical",
        "mapping": ROAD_SURFACE_MAPPING,
        "default": 0,
        "description": "Road surface condition"
    },
}


# ============================================================================
# CORE CONVERSION FUNCTIONS
# ============================================================================

def map_value_to_integer(
    value: Any,
    mapping_dict: Dict[Any, int],
    feature_name: str = "Unknown",
    default: int = 0
) -> int:
    """
    Convert a user input (string/value) to an integer code using the provided mapping.
    
    Args:
        value: The input value to map (typically a string from the frontend)
        mapping_dict: Dictionary mapping input values to integer codes
        feature_name: Name of the feature (for logging/debugging)
        default: Default integer code if value not found
    
    Returns:
        Integer code, or default if not found
    
    Examples:
        >>> map_value_to_integer("יבש", ROAD_SURFACE_MAPPING, "PNE_KVISH")
        1
        >>> map_value_to_integer("invalid", ROAD_SURFACE_MAPPING, "PNE_KVISH", default=0)
        0
    """
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return default
    
    # Try case-insensitive string matching if value is a string
    if isinstance(value, str):
        value = value.strip()
        if value in mapping_dict:
            return mapping_dict[value]
        
        # Try case-insensitive match (if applicable)
        for key, code in mapping_dict.items():
            if isinstance(key, str) and key.lower() == value.lower():
                return code
    
    # If value is already an integer and within valid range
    if isinstance(value, (int, np.integer)):
        if value in mapping_dict.values():
            return int(value)
    
    # Default to unknown code
    return default


def engineer_road_structure(
    df: pd.DataFrame,
    had_maslul_col: str = "HAD_MASLUL",
    rav_maslul_col: str = "RAV_MASLUL"
) -> pd.Series:
    """
    Engineer ROAD_STRUCTURE feature from HAD_MASLUL (single-lane) and RAV_MASLUL (multi-lane).
    
    Logic:
    - 0 (unknown/missing): → 0 (unknown)
    - Single lane (HAD_MASLUL = 1): → 1 (single lane)
    - Two-way (default): → 2 (two-way)
    - Multi-lane one-way: → 3 (multi-lane one-way)
    - Multi-lane two-way: → 4 (multi-lane two-way)
    
    Args:
        df: DataFrame containing HAD_MASLUL and RAV_MASLUL columns
        had_maslul_col: Column name for single-lane indicator
        rav_maslul_col: Column name for multi-lane indicator
    
    Returns:
        pd.Series with engineered ROAD_STRUCTURE codes
    """
    road_structure = pd.Series(2, index=df.index, dtype=int)  # Default: two-way
    
    if had_maslul_col in df.columns:
        single_lane = (df[had_maslul_col] == 1)
        road_structure[single_lane] = 1
    
    if rav_maslul_col in df.columns:
        multi_lane = (df[rav_maslul_col] == 1)
        # Determine if multi-lane is one-way or two-way
        if had_maslul_col in df.columns:
            multi_lane_one_way = multi_lane & (df[had_maslul_col] == 1)
            road_structure[multi_lane_one_way] = 3
            road_structure[multi_lane & ~(df[had_maslul_col] == 1)] = 4
        else:
            road_structure[multi_lane] = 4
    
    # Mark truly missing values as unknown
    road_structure[df[[had_maslul_col, rav_maslul_col]].isna().all(axis=1)] = 0
    
    return road_structure


def prepare_model_input(
    ui_input: Dict[str, Any],
    feature_order: List[str] = None
) -> Dict[str, int]:
    """
    Convert UI input dictionary (Hebrew strings) to model input dictionary (integer codes).
    
    This function maps frontend form values to backend model-ready integer codes,
    handling edge cases and missing values automatically.
    
    Args:
        ui_input: Dictionary with feature names as keys and user input as values
                 Example: {
                     "SHAA": "14:00",
                     "HODESH_TEUNA": "1",
                     "SUG_DEREH": "עירוני בצומת",
                     "MEHIRUT_MUTERET": "עד 80 קמ״ש",
                     "PNE_KVISH": "יבש",
                     ...
                 }
        feature_order: List of feature names in desired order (default: 16-feature order)
    
    Returns:
        Dictionary with integer-coded values ready for the model
    
    Raises:
        ValueError: If required features are missing
    
    Examples:
        >>> ui_input = {
        ...     "SHAA": "08:00",
        ...     "HODESH_TEUNA": "5",
        ...     "SUG_DEREH": "עירוני בצומת",
        ...     "MEHIRUT_MUTERET": "עד 80 קמ״ש",
        ...     "PNE_KVISH": "יבש"
        ... }
        >>> model_input = prepare_model_input(ui_input)
    """
    if feature_order is None:
        feature_order = [
            'SHAA', 'HODESH_TEUNA', 'YOM_BASHAVUA', 'SUG_TEUNA',
            'ROAD_STRUCTURE', 'ROHAV', 'NAFA', 'ZURAT_ISHUV',
            'MEHIRUT_MUTERET', 'TEURA', 'SUG_DEREH', 'SIMUN_TIMRUR',
            'MEKOM_HAZIYA', 'TKINUT', 'OFEN_HAZIYA', 'PNE_KVISH'
        ]
    
    model_input = {}
    
    for feature in feature_order:
        if feature not in FEATURE_CONFIG:
            raise ValueError(f"Unknown feature: {feature}")
        
        config = FEATURE_CONFIG[feature]
        value = ui_input.get(feature)
        mapping = config["mapping"]
        default = config["default"]
        
        # Convert value to integer code
        model_input[feature] = map_value_to_integer(
            value,
            mapping,
            feature_name=feature,
            default=default
        )
    
    return model_input


def prepare_model_array(
    ui_input: Dict[str, Any],
    feature_order: List[str] = None
) -> np.ndarray:
    """
    Convert UI input dictionary to a numpy array for direct model prediction.
    
    Args:
        ui_input: Dictionary with feature names and user input values
        feature_order: Desired feature order (default: 16-feature model order)
    
    Returns:
        1D numpy array of integer codes in the specified feature order
    
    Examples:
        >>> ui_input = {"SHAA": "08:00", "HODESH_TEUNA": "5", ...}
        >>> prediction_array = prepare_model_array(ui_input)
        >>> # Use with your model: model.predict_proba(prediction_array.reshape(1, -1))
    """
    model_input_dict = prepare_model_input(ui_input, feature_order)
    
    if feature_order is None:
        feature_order = list(model_input_dict.keys())
    
    return np.array([model_input_dict[feat] for feat in feature_order], dtype=int)


def validate_ui_input(ui_input: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate UI input and provide warnings/errors for invalid values.
    
    Returns a validation report with any issues found.
    
    Args:
        ui_input: Dictionary of user input values
    
    Returns:
        Dictionary with validation results: {
            "valid": bool,
            "errors": List[str],
            "warnings": List[str],
            "missing_features": List[str]
        }
    """
    report = {
        "valid": True,
        "errors": [],
        "warnings": [],
        "missing_features": []
    }
    
    required_features = [
        'SHAA', 'HODESH_TEUNA', 'YOM_BASHAVUA', 'SUG_TEUNA',
        'ROAD_STRUCTURE', 'ROHAV', 'NAFA', 'ZURAT_ISHUV',
        'MEHIRUT_MUTERET', 'TEURA', 'SUG_DEREH', 'SIMUN_TIMRUR',
        'MEKOM_HAZIYA', 'TKINUT', 'OFEN_HAZIYA', 'PNE_KVISH'
    ]
    
    for feature in required_features:
        if feature not in ui_input or ui_input[feature] is None:
            report["missing_features"].append(feature)
            report["valid"] = False
    
    for feature, value in ui_input.items():
        if feature not in FEATURE_CONFIG:
            report["warnings"].append(f"Unknown feature: {feature}")
            continue
        
        config = FEATURE_CONFIG[feature]
        mapping = config["mapping"]
        
        if not isinstance(value, (str, int, float)) and value is not None:
            report["errors"].append(
                f"{feature}: Invalid value type {type(value).__name__}. Expected string or integer."
            )
            report["valid"] = False
        elif isinstance(value, str) and value not in mapping:
            report["warnings"].append(
                f"{feature}: Value '{value}' not in mapping. Will use default."
            )
    
    return report


# ============================================================================
# DATASET PREPROCESSING
# ============================================================================

def preprocess_dataset(
    df: pd.DataFrame,
    selected_features: List[str] = None,
    target_column: str = "NIKVIYUT_TEUNA"
) -> pd.DataFrame:
    """
    Preprocess raw accidents dataset for model training.
    
    Steps:
    1. Select only the required 16 features
    2. Engineer ROAD_STRUCTURE from HAD_MASLUL & RAV_MASLUL
    3. Handle missing values
    4. Remove rows with insufficient data
    
    Args:
        df: Raw dataset DataFrame
        selected_features: List of features to use (default: 16-feature model)
        target_column: Name of the target column
    
    Returns:
        Preprocessed DataFrame with only selected features and valid rows
    """
    if selected_features is None:
        selected_features = [
            'SHAA', 'HODESH_TEUNA', 'YOM_BASHAVUA', 'SUG_TEUNA',
            'ROAD_STRUCTURE', 'ROHAV', 'NAFA', 'ZURAT_ISHUV',
            'MEHIRUT_MUTERET', 'TEURA', 'SUG_DEREH', 'SIMUN_TIMRUR',
            'MEKOM_HAZIYA', 'TKINUT', 'OFEN_HAZIYA', 'PNE_KVISH'
        ]
    
    # Create a copy to avoid modifying original
    df_processed = df.copy()
    
    # Engineer ROAD_STRUCTURE if not present
    if 'ROAD_STRUCTURE' in selected_features and 'ROAD_STRUCTURE' not in df_processed.columns:
        if 'HAD_MASLUL' in df_processed.columns or 'RAV_MASLUL' in df_processed.columns:
            df_processed['ROAD_STRUCTURE'] = engineer_road_structure(df_processed)
        else:
            df_processed['ROAD_STRUCTURE'] = 0  # Default unknown
    
    # Select only required features
    available_features = [f for f in selected_features if f in df_processed.columns]
    if target_column in df_processed.columns:
        available_features.append(target_column)
    
    df_processed = df_processed[available_features]
    
    # Fill missing values with 0 (unknown)
    df_processed = df_processed.fillna(0)
    
    # Ensure all values are integers
    for col in selected_features:
        if col in df_processed.columns:
            df_processed[col] = df_processed[col].astype(int)
    
    # Remove rows with all zero values (completely missing)
    df_processed = df_processed[~(df_processed[selected_features] == 0).all(axis=1)]
    
    return df_processed


if __name__ == "__main__":
    # Example usage
    print("=" * 80)
    print("Data Mapper & Preprocessing Module")
    print("=" * 80)
    
    # Example 1: Map single value
    print("\n[Example 1] Mapping single values:")
    print(f"  'יבש' → {map_value_to_integer('יבש', ROAD_SURFACE_MAPPING, 'PNE_KVISH')}")
    print(f"  'עירוני בצומת' → {map_value_to_integer('עירוני בצומת', ROAD_TYPE_MAPPING, 'SUG_DEREH')}")
    
    # Example 2: Prepare model input from UI data
    print("\n[Example 2] Convert UI input to model input:")
    ui_data = {
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
    
    model_input = prepare_model_input(ui_data)
    print("  Input Dictionary:")
    for k, v in list(model_input.items())[:5]:
        print(f"    {k}: {v}")
    print("  ...")
    
    # Example 3: Create numpy array for model
    print("\n[Example 3] Create prediction array:")
    model_array = prepare_model_array(ui_data)
    print(f"  Shape: {model_array.shape}")
    print(f"  Values: {model_array[:5]}...")
    
    # Example 4: Validate UI input
    print("\n[Example 4] Validate user input:")
    validation = validate_ui_input(ui_data)
    print(f"  Valid: {validation['valid']}")
    print(f"  Errors: {len(validation['errors'])}")
    print(f"  Warnings: {len(validation['warnings'])}")
    
    print("\n" + "=" * 80)
