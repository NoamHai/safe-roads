# Model Handoff Guide — For Mor (ML Partner)

This guide provides instructions for delivering and integrating the trained ML model into the Safe Roads backend. Follow these steps to ensure seamless integration without backend code changes.

## 1. Model File Placement

- **File Name**: `model.pkl`
- **Location**: Place the file in the project root directory (same level as `backend/`, `frontend/`, `docs/`).
- **Format**: Joblib-serialized scikit-learn model (or compatible) with `predict_proba` method.
- **Example Path**: `c:\path\to\final_project\model.pkl` (adjust for your environment).

**Note**: Do not modify the filename or location; the backend expects `model.pkl` in the root.

## 2. Expected Input Feature Order and Types

The model must accept input as a list of 6 categorical string features in this exact order:

1. `road_type` (str): e.g., "urban", "highway"
2. `weather` (str): e.g., "clear", "rain", "fog"
3. `time_of_day` (str): e.g., "day", "night"
4. `lighting` (str): e.g., "daylight", "dark_with_streetlights", "dark_no_streetlights"
5. `junction` (str): e.g., "no_junction", "junction"
6. `road_surface` (str): e.g., "dry", "wet", "unknown"

- **Input Format**: List of lists, e.g., `[["urban", "clear", "day", "daylight", "no_junction", "dry"]]`
- **Encoding**: The model handles any necessary encoding (e.g., LabelEncoder, OneHotEncoder) internally.
- **Validation**: Backend does not preprocess; ensure model is robust to these string inputs.

## 3. How the Backend Loads and Uses the Model

- **Loading**: At runtime, `backend/services/model_service.py` checks for `model.pkl` existence. If found, loads via `joblib.load(model.pkl)`.
- **Usage**: For each prediction, calls `model.predict_proba([features])`, which returns `[prob_no_accident, prob_accident]`.
- **Output Extraction**: Backend uses `prob_accident` (index 1) as the accident probability, clamped to [0.0, 0.95].
- **Fallback**: If model loading/prediction fails, logs error and falls back to rule-based prediction.
- **Caching**: Model is loaded once per process; no reloading on each request.
- **Explainability**: `breakdown` remains rule-based (not ML-derived) for user explanations.

**Code Reference**: See `backend/services/model_service.py` for implementation details.

## 4. Testing Integration After Model Delivery

1. **Place Model**: Copy `model.pkl` to project root.
2. **Start Backend**: Run `uvicorn backend.app:app --reload --port 8000`.
3. **Test API Call**: Use curl, Postman, or frontend to POST to `http://127.0.0.1:8000/predict` with sample JSON:
   ```json
   {
     "road_type": "urban",
     "weather": "clear",
     "time_of_day": "day",
     "lighting": "daylight",
     "junction": "no_junction",
     "road_surface": "dry"
   }
   ```
4. **Verify Response**: Check for valid `probability`, `risk_percent`, `breakdown`. Probability should differ from rule-based (e.g., not exactly 0.14 for the above input).
5. **Check Logs**: Backend logs should show no "ML model prediction failed" messages. If using ML, no fallback logs.
6. **Edge Cases**: Test with invalid inputs (e.g., unknown strings) — should fallback gracefully.
7. **Performance**: Ensure prediction is fast (<1s); monitor for memory issues.
8. **Remove Model**: Temporarily rename `model.pkl` to verify fallback works.

**Success Criteria**: API returns predictions using ML (different from rule-based), no errors in logs, frontend displays results correctly.

If issues arise, check model compatibility or contact for backend adjustments. This ensures clean handoff and integration.