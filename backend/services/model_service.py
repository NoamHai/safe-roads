from typing import Any, Dict, List, Tuple
import os
import joblib
import logging

import numpy as np

from ..config import settings
from .data_mapper import FEATURE_ORDER, prepare_model_input

logger = logging.getLogger(__name__)

# Cache the loaded model in memory (load once per process)
_cached_model = None
_model_loaded = False


def _normalize_mapping(mapping: Dict[str, int]) -> Dict[str, int]:
    normalized: Dict[str, int] = {}
    for key, value in mapping.items():
        normalized[str(key).strip().lower()] = int(value)
    return normalized


_ACCIDENT_TYPE_MAPPING = _normalize_mapping(settings.accident_type_mapping)
_SPEED_LIMIT_MAPPING = _normalize_mapping(settings.speed_limit_mapping)
_DISTRICT_MAPPING = _normalize_mapping(settings.district_mapping)
_FINAL_FEATURE_SET = set(FEATURE_ORDER)


def _normalize_legacy_verification_payload(user_input: Dict[str, Any]) -> Dict[str, Any]:
    legacy_keys = {"road_type", "weather", "time_of_day", "lighting", "junction", "road_surface"}
    if not legacy_keys.intersection(user_input.keys()):
        return user_input

    normalized = dict(user_input)
    time_of_day = str(user_input.get("time_of_day", "")).strip().lower()
    lighting = str(user_input.get("lighting", "")).strip().lower()
    weather = str(user_input.get("weather", "")).strip().lower()
    road_type = str(user_input.get("road_type", "")).strip().lower()
    junction = str(user_input.get("junction", "")).strip().lower()
    road_surface = str(user_input.get("road_surface", "")).strip().lower()

    normalized.setdefault("SHAA", "12:00" if time_of_day == "day" else "22:00")
    normalized.setdefault("HODESH_TEUNA", 1)
    normalized.setdefault("YOM_BASHAVUA", "לא ידוע")
    normalized.setdefault("SUG_TEUNA", "לא ידוע")
    normalized.setdefault("ROAD_STRUCTURE", "לא ידוע")
    normalized.setdefault("ROHAV", "לא ידוע")
    normalized.setdefault("NAFA", "לא ידוע")
    normalized.setdefault(
        "ZURAT_ISHUV",
        "עירוני" if road_type in {"urban", "city"} else ("כפרי" if road_type in {"rural"} else "לא ידוע"),
    )
    normalized.setdefault("MEHIRUT_MUTERET", "לא ידוע")
    normalized.setdefault(
        "TEURA",
        "אור יום"
        if lighting in {"daylight", "day"} or time_of_day == "day"
        else ("לילה עם תאורה" if lighting == "night_with_lighting" else ("לילה ללא תאורה" if lighting == "night_without_lighting" else "לא ידוע")),
    )
    normalized.setdefault(
        "SUG_DEREH",
        "עירוני בצומת"
        if road_type in {"urban", "city"} and junction not in {"no_junction", "false", "0"}
        else (
            "עירוני לא בצומת"
            if road_type in {"urban", "city"}
            else ("לא עירוני בצומת" if road_type == "rural" and junction not in {"no_junction", "false", "0"} else ("לא עירוני לא בצומת" if road_type == "rural" else "לא ידוע"))
        ),
    )
    normalized.setdefault("SIMUN_TIMRUR", "לא ידוע")
    normalized.setdefault("TKINUT", "לא ידוע")
    normalized.setdefault(
        "PNE_KVISH",
        "יבש" if road_surface == "dry" else ("רטוב ממים" if road_surface == "wet" else ("מכוסה בבוץ" if road_surface == "mud" else ("מרוח בחומר דלק" if road_surface == "fuel" else "לא ידוע"))),
    )
    normalized.setdefault(
        "MEZEG_AVIR",
        "בהיר" if weather == "clear" else ("מעונן" if weather == "cloudy" else ("גשום" if weather == "rainy" else ("ערפילי" if weather == "foggy" else "לא ידוע"))),
    )
    normalized.setdefault("YOM_LAYLA", "יום" if time_of_day == "day" else ("לילה" if time_of_day == "night" else "לא ידוע"))

    return normalized


def _load_model():
    """Load and cache the ML model if available."""
    global _cached_model, _model_loaded
    if _model_loaded:
        return _cached_model is not None

    model_path = os.path.join(os.path.dirname(__file__), "..", "..", settings.model_path)
    if os.path.exists(model_path):
        try:
            _cached_model = joblib.load(model_path)
            _model_loaded = True
            logger.info("ML model loaded from model.pkl")
            return True
        except Exception as e:
            logger.warning(f"Failed to load ML model: {e}")
            _cached_model = None
            _model_loaded = True
            return False
    else:
        _model_loaded = True
        logger.info("model.pkl not found, will use rule-based prediction")
        return False


def _clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def _coerce_int(value: Any, field_name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f"Field '{field_name}' must be an integer value")
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        stripped = value.strip()
        if stripped.lstrip("-").isdigit():
            return int(stripped)
    raise ValueError(f"Field '{field_name}' must be numeric or map to an encoded integer")


def _encode_with_mapping(value: Any, field_name: str, mapping: Dict[str, int]) -> int:
    if value is None:
        raise ValueError(f"Missing required field '{field_name}'")

    normalized = str(value).strip().lower()
    if mapping and normalized in mapping:
        return mapping[normalized]

    return _coerce_int(value, field_name)


def _prepare_model_features(user_input: Dict[str, Any]) -> Tuple[List[int], Dict[str, int], List[Dict[str, Any]]]:
    hour = _coerce_int(user_input.get("hour"), "hour")
    month = _coerce_int(user_input.get("month"), "month")

    if not 0 <= hour <= 23:
        raise ValueError("Field 'hour' must be in range 0..23")
    if not 1 <= month <= 12:
        raise ValueError("Field 'month' must be in range 1..12")

    accident_type = _encode_with_mapping(
        user_input.get("accident_type"), "accident_type", _ACCIDENT_TYPE_MAPPING
    )
    speed_limit = _encode_with_mapping(
        user_input.get("speed_limit"), "speed_limit", _SPEED_LIMIT_MAPPING
    )

    encoded_payload: Dict[str, int] = {
        "hour": hour,
        "month": month,
        "accident_type": accident_type,
        "speed_limit": speed_limit,
    }

    district_value = user_input.get("district")
    if district_value is not None:
        encoded_payload["district"] = _encode_with_mapping(
            district_value, "district", _DISTRICT_MAPPING
        )

    feature_vector = [
        encoded_payload["hour"],
        encoded_payload["month"],
        encoded_payload["accident_type"],
        encoded_payload["speed_limit"],
    ]

    breakdown = _preprocessing_breakdown(encoded_payload)
    return feature_vector, encoded_payload, breakdown


def _preprocessing_breakdown(encoded_payload: Dict[str, int]) -> List[Dict[str, Any]]:
    breakdown: List[Dict[str, Any]] = []
    for factor, value in encoded_payload.items():
        breakdown.append({
            "factor": factor,
            "value": str(value),
            "delta": 0.0,
            "note": "Encoded feature prepared for model inference"
        })
    return breakdown


def _is_final_feature_payload(user_input: Dict[str, Any]) -> bool:
    return _FINAL_FEATURE_SET.issubset(set(user_input.keys()))


def _predict_final_feature_probability(user_input: Dict[str, Any]) -> Dict[str, Any]:
    encoded_payload = prepare_model_input(user_input, FEATURE_ORDER)
    feature_vector = [encoded_payload[feature] for feature in FEATURE_ORDER]

    if _cached_model is not None:
        expected_feature_count = getattr(_cached_model, "n_features_in_", None)
        if expected_feature_count == len(feature_vector):
            try:
                model_probability = float(_cached_model.predict_proba(np.array(feature_vector).reshape(1, -1))[0][1])
                probability = _clamp(model_probability, 0.0, 0.95)
                return {
                    "probability": round(probability, 3),
                    "risk_percent": int(round(probability * 100)),
                    "breakdown": _preprocessing_breakdown(encoded_payload),
                }
            except Exception:
                logger.warning("Model prediction failed for final feature payload; using heuristic fallback")

    hour = encoded_payload["SHAA"]
    speed_limit = encoded_payload["MEHIRUT_MUTERET"]
    weather = encoded_payload["MEZEG_AVIR"]
    lighting = encoded_payload["TEURA"]
    road_condition = encoded_payload["TKINUT"]
    road_surface = encoded_payload["PNE_KVISH"]
    day_night = encoded_payload["YOM_LAYLA"]
    month = encoded_payload["HODESH_TEUNA"]

    hour_delta = 0.0
    if hour >= 22 or hour <= 5:
        hour_delta += 0.10
    elif hour in {7, 8, 9, 16, 17, 18, 19}:
        hour_delta += 0.05

    speed_delta = 0.03
    if speed_limit >= 7:
        speed_delta += 0.12
    elif speed_limit >= 4:
        speed_delta += 0.08

    weather_delta = 0.0 if weather == 0 else (0.06 if weather in {3, 4} else 0.02)
    lighting_delta = 0.07 if lighting in {2, 3} else (0.03 if lighting == 1 else 0.0)
    road_condition_delta = 0.08 if road_condition == 2 else (0.03 if road_condition == 1 else 0.0)
    road_surface_delta = 0.07 if road_surface in {2, 3, 4} else (0.02 if road_surface == 1 else 0.0)
    day_night_delta = 0.05 if day_night == 2 else 0.02
    month_delta = 0.06 if month in {12, 1, 2} else 0.02

    base = 0.08
    probability = _clamp(
        base
        + hour_delta
        + speed_delta
        + weather_delta
        + lighting_delta
        + road_condition_delta
        + road_surface_delta
        + day_night_delta
        + month_delta,
        0.0,
        0.95,
    )

    breakdown = _preprocessing_breakdown(encoded_payload)
    return {
        "probability": round(probability, 3),
        "risk_percent": int(round(probability * 100)),
        "breakdown": breakdown,
    }


def _align_feature_vector_for_model(
    feature_vector: List[int], encoded_payload: Dict[str, int]
) -> List[int]:
    if _cached_model is None:
        return feature_vector

    expected_feature_count = getattr(_cached_model, "n_features_in_", None)
    if expected_feature_count == 5 and "district" in encoded_payload:
        return feature_vector + [encoded_payload["district"]]
    if expected_feature_count == 4:
        return feature_vector

    if expected_feature_count is not None and expected_feature_count != len(feature_vector):
        logger.warning(
            "Model expects %s features but prepared %s. Using prepared base vector.",
            expected_feature_count,
            len(feature_vector),
        )
    return feature_vector


def predict_probability(user_input: Dict[str, Any]) -> Dict[str, Any]:
    """Predict accident risk from either the legacy or final feature payload."""

    user_input = _normalize_legacy_verification_payload(user_input)

    if _is_final_feature_payload(user_input):
        return _predict_final_feature_probability(user_input)

    required_keys = {"hour", "month", "accident_type", "speed_limit"}
    missing = [key for key in required_keys if key not in user_input]
    if missing:
        raise ValueError(f"Missing required keys: {', '.join(sorted(missing))}")

    hour = _coerce_int(user_input.get("hour"), "hour")
    month = _coerce_int(user_input.get("month"), "month")
    speed_limit = _coerce_int(user_input.get("speed_limit"), "speed_limit")
    accident_type = _coerce_int(user_input.get("accident_type"), "accident_type")
    district_value = user_input.get("district")
    district = None if district_value is None else _coerce_int(district_value, "district")

    if not 0 <= hour <= 23:
        raise ValueError("Field 'hour' must be in range 0..23")
    if not 1 <= month <= 12:
        raise ValueError("Field 'month' must be in range 1..12")

    hour_delta = 0.0
    speed_delta = 0.0

    if hour >= 22 or hour <= 5:
        hour_delta += 0.12
    elif hour in {7, 8, 9, 16, 17, 18, 19}:
        hour_delta += 0.06

    if speed_limit > 90:
        speed_delta += 0.14
    elif speed_limit >= 70:
        speed_delta += 0.08
    else:
        speed_delta += 0.03

    month_delta = 0.06 if month in {12, 1, 2} else 0.02

    accident_type_delta_map = {
        1: 0.12,
        2: 0.08,
        3: 0.09,
        4: 0.11,
    }
    accident_type_delta = accident_type_delta_map.get(accident_type, 0.07)

    district_delta = 0.0
    if district is not None:
        district_delta = min(max(district, 0) * 0.005, 0.10)

    base = 0.10
    probability = _clamp(base + hour_delta + speed_delta + month_delta + accident_type_delta + district_delta, 0.0, 1.0)
    risk_percent = int(round(probability * 100))

    breakdown = [
        {"factor": "hour", "value": hour, "delta": round(hour_delta, 3)},
        {"factor": "month", "value": month, "delta": round(month_delta, 3)},
        {"factor": "accident_type", "value": accident_type, "delta": round(accident_type_delta, 3)},
        {"factor": "speed_limit", "value": speed_limit, "delta": round(speed_delta, 3)},
    ]

    if district is not None:
        breakdown.append({"factor": "district", "value": district, "delta": round(district_delta, 3)})

    return {
        "probability": round(probability, 3),
        "risk_percent": risk_percent,
        "breakdown": breakdown,
    }


def _rule_based_probability(user_input: Dict[str, Any]) -> float:
    """Rule-based probability calculation (fallback)."""
    score = 0.05

    hour = int(user_input.get("hour", 0))
    month = int(user_input.get("month", 1))
    accident_type = int(user_input.get("accident_type", 0))
    speed_limit = int(user_input.get("speed_limit", 0))
    district = user_input.get("district")

    if hour in {22, 23, 0, 1, 2, 3, 4, 5}:
        score += 0.12
    elif hour in {7, 8, 9, 16, 17, 18, 19}:
        score += 0.06

    if month in {12, 1, 2}:
        score += 0.08

    score += min(max(accident_type, 0) * 0.03, 0.25)
    score += min(max(speed_limit, 0) * 0.01, 0.25)

    if district is not None:
        score += min(max(int(district), 0) * 0.005, 0.10)

    return _clamp(score, 0.0, 0.95)