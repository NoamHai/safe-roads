from typing import Any, Dict, List
import os
import joblib
import logging

logger = logging.getLogger(__name__)

# Cache the loaded model in memory (load once per process)
_cached_model = None
_model_loaded = False


def _load_model():
    """Load and cache the ML model if available."""
    global _cached_model, _model_loaded
    if _model_loaded:
        return _cached_model is not None

    model_path = os.path.join(os.path.dirname(__file__), "..", "..", "model.pkl")
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


def predict_probability(user_input: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generic ML inference infrastructure.
    Loads trained model if available; falls back to rule-based stub.
    Returns:
      {
        "probability": float (0..1),
        "risk_percent": int (0..100),
        "breakdown": [ {factor, value, delta, note}, ... ]  # Rule-based for explainability
      }
    """

    # Prepare input features (strings as per API)
    features = [
        user_input.get("road_type", "urban"),
        user_input.get("weather", "clear"),
        user_input.get("time_of_day", "day"),
        user_input.get("lighting", "daylight"),
        user_input.get("junction", "no_junction"),
        user_input.get("road_surface", "dry")
    ]

    # Try to use cached ML model
    probability = None
    if _load_model() and _cached_model is not None:
        try:
            # Assume model.predict_proba returns [prob_no_accident, prob_accident]
            probas = _cached_model.predict_proba([features])[0]
            probability = float(probas[1])  # Probability of accident
            probability = _clamp(probability, 0.0, 0.95)
            logger.info("ML model prediction successful")
        except Exception as e:
            logger.warning(f"ML model prediction failed: {e}. Falling back to rule-based.")

    # Fall back to rule-based if no model or error
    if probability is None:
        probability = _rule_based_probability(user_input)
        logger.info("Using rule-based prediction")

    risk_percent = int(round(probability * 100))
    breakdown = _rule_based_breakdown(user_input)  # Keep explainable breakdown

    return {
        "probability": round(probability, 3),
        "risk_percent": risk_percent,
        "breakdown": breakdown
    }


def _rule_based_probability(user_input: Dict[str, Any]) -> float:
    """Rule-based probability calculation (fallback)."""
    score = 0.10

    road_type = str(user_input.get("road_type", "urban"))
    weather = str(user_input.get("weather", "clear"))
    time_of_day = str(user_input.get("time_of_day", "day"))
    lighting = str(user_input.get("lighting", "daylight"))
    junction = str(user_input.get("junction", "no_junction"))
    road_surface = str(user_input.get("road_surface", "dry"))

    if road_type == "highway":
        score += 0.12
    else:
        score += 0.04

    if weather == "rain":
        score += 0.18
    elif weather == "fog":
        score += 0.22

    if time_of_day == "night":
        score += 0.12

    if lighting == "dark_no_streetlights":
        score += 0.22
    elif lighting == "dark_with_streetlights":
        score += 0.12

    if junction == "junction":
        score += 0.10

    if road_surface == "wet":
        score += 0.16
    elif road_surface == "unknown":
        score += 0.06

    return _clamp(score, 0.0, 0.95)


def _rule_based_breakdown(user_input: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Generate explainable breakdown using rule-based logic."""
    breakdown: List[Dict[str, Any]] = []

    def add(factor: str, value: str, delta: float, note: str):
        breakdown.append({
            "factor": factor,
            "value": value,
            "delta": round(delta, 3),
            "note": note
        })

    road_type = str(user_input.get("road_type", "urban"))
    weather = str(user_input.get("weather", "clear"))
    time_of_day = str(user_input.get("time_of_day", "day"))
    lighting = str(user_input.get("lighting", "daylight"))
    junction = str(user_input.get("junction", "no_junction"))
    road_surface = str(user_input.get("road_surface", "dry"))

    # Road type
    if road_type == "highway":
        add("road_type", road_type, 0.12, "Higher speed environment")
    else:
        add("road_type", road_type, 0.04, "Urban driving has many interactions")

    # Weather
    if weather == "rain":
        add("weather", weather, 0.18, "Reduced friction + visibility")
    elif weather == "fog":
        add("weather", weather, 0.22, "Significant visibility reduction")
    else:
        add("weather", weather, 0.00, "Good conditions")

    # Time of day
    if time_of_day == "night":
        add("time_of_day", time_of_day, 0.12, "Lower visibility + fatigue risk")
    else:
        add("time_of_day", time_of_day, 0.00, "Daytime")

    # Lighting
    if lighting == "dark_no_streetlights":
        add("lighting", lighting, 0.22, "Very low visibility")
    elif lighting == "dark_with_streetlights":
        add("lighting", lighting, 0.12, "Some visibility limitations")
    else:
        add("lighting", lighting, 0.00, "Good lighting")

    # Junction
    if junction == "junction":
        add("junction", junction, 0.10, "More conflict points")
    else:
        add("junction", junction, 0.00, "No junction")

    # Road surface
    if road_surface == "wet":
        add("road_surface", road_surface, 0.16, "Lower grip")
    elif road_surface == "unknown":
        add("road_surface", road_surface, 0.06, "Uncertain condition")
    else:
        add("road_surface", road_surface, 0.00, "Dry surface")

    return breakdown