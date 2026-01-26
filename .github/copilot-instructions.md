# Copilot instructions for Safe Roads project

Summary
- Purpose: small demo web app (frontend + FastAPI backend) that predicts accident risk using a generic ML inference service in `backend/services/model_service.py` (loads trained model from `model.pkl` in project root if available, else rule-based fallback).
- Top-level components: `frontend/` (static UI), `backend/` (FastAPI API), `tools/` (data analysis utilities), `data/` (CSV master dataset).

Quick start (developer):
- Run backend (default port 8000):

```bash
pip install fastapi uvicorn pydantic
# then
uvicorn backend.app:app --reload --port 8000
```

- Serve frontend files (Live Server or simple static server) on port 5500 so CORS in `backend/app.py` works as-is. Example using VS Code Live Server or `python -m http.server 5500` from `frontend/`.

- Frontend is served automatically at root (/) by FastAPI StaticFiles mount - no separate server needed. Access at `http://127.0.0.1:8000`

API & contracts (critical)
- Endpoint: POST `http://127.0.0.1:8000/predict` (see `frontend/index.html` hint).
- Request schema: `backend.app.PredictRequest` — fields: `road_type`, `weather`, `time_of_day`, `lighting`, `junction`, `road_surface`. These are Enum values and must match the `<option value="...">` strings in `frontend/index.html`.
- Response schema: `ModelResult` contains `probability` (float 0..1), `risk_percent` (int 0..100), and `breakdown` (list of {factor, value, delta, note}). `frontend/script.js` depends on these keys.

Architecture notes & important patterns
- The backend uses a generic ML inference infrastructure in `backend/services/model_service.py`. It loads a trained model from `model.pkl` in the project root if available; otherwise falls back to rule-based logic. The model is cached in memory for the process lifetime.
- When swapping to an ML model, ensure the model is trained on the 6 string features (road_type, weather, time_of_day, lighting, junction, road_surface) and implements `predict_proba` returning probabilities for accident/no-accident (use p1 as accident probability).
- Preserve the response keys: `probability` (clamped 0..0.95), `risk_percent`, and `breakdown` (rule-based for explainability).
- `backend/routes/predict.py` uses `pydantic` Enums and `req.model_dump(mode="json")` to convert Enums -> strings before handing to `predict_probability`.
- CORS is intentionally restrictive: allowed origins are `http://127.0.0.1:5500` and `http://localhost:5500`. If you host frontend elsewhere, update `origins` in `backend/config.py`.

- CORS middleware is imported in `backend/app.py` but not configured (origins in `backend/config.py` are set to 127.0.0.1:8000/localhost:8000, but since frontend is served from same origin, CORS isn't needed).

Data & tools
- `tools/accidents_analysis.py` is an analysis utility using `pandas`. It expects a CSV and (optionally) an XLSX data dictionary. The example in that file builds paths relative to `tools/` — note your actual CSV is at `data/accidents_raw_master.csv`. Either run the analyzer with the correct path or update the example constants.
- Key function to reuse: `AccidentsAnalyzer.analyze_column(...)` returns a distribution DataFrame and optional unknowns dataframe — useful when building features or validating input value sets.

Testing & verification
- Run tests with `pytest` (configured in `pytest.ini` with verbose output and short traceback).
- `verify_final.py` provides end-to-end verification of imports and basic prediction functionality.
- Tests in `tests/test_predict.py` validate output structure, types, and sanity checks for various risk scenarios.

Conventions and gotchas
- Keep frontend `<option value>` strings and backend Enum values in sync — mismatches will produce silent logic errors in predictions.
- `model_service.predict_probability` returns a capped probability (0..0.95). Tests or UI logic may assume this cap; preserve semantics when swapping implementations.
- No requirements file or tests are present. Add `requirements.txt` when adding packages and run the app in a virtualenv.

- Requirements are specified in `requirements.txt` (core) and `requirements-dev.txt` (with pandas, pytest, httpx).
- Virtual environment recommended: `python -m venv venv; venv\Scripts\activate` then `pip install -r requirements-dev.txt`

Suggested dev commands

```bash
# install common deps
pip install fastapi uvicorn pydantic pandas

# run backend
uvicorn backend.app:app --reload --port 8000

# serve frontend (from frontend/)
cd frontend
python -m http.server 5500
```

```bash
# install deps
pip install -r requirements-dev.txt

# run backend
uvicorn backend.app:app --reload --port 8000

# run tests
pytest

# verify functionality
python verify_final.py
```

If something is unclear or you want the guide expanded (run workflows, CI, or examples of replacing the rule-based model), tell me which sections to expand or correct.
