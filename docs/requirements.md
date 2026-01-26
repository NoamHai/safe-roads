## Requirements & Codebase Understanding — Safe Roads (final_project)

Summary

- Small demo web app: static frontend + FastAPI backend + simple rule-based model.
- Purpose: demonstrate an accident risk predictor pipeline (UI → API → model service → JSON response).

Top-level components

- `frontend/`: static UI assets (`index.html`, `script.js`, `style.css`). The UI posts JSON to the backend and expects a response with `probability`, `risk_percent`, and `breakdown`.
- `backend/`: FastAPI app (`app.py`) and rule-based model stub (`services/model_service.py`). `app.py` defines `PredictRequest` (Pydantic) and `ModelResult` (response model).
- `tools/`: data utilities, notably `tools/accidents_analysis.py` which analyzes a CSV master dataset and can parse an XLSX data dictionary.
- `data/`: contains `accidents_raw_master.csv` used by analysis tools.

API contract (critical)

- POST `/predict` (see `backend/app.py`) with JSON matching `PredictRequest` fields:
  - `road_type` (`urban` | `highway`)
  - `weather` (`clear` | `rain` | `fog`)
  - `time_of_day` (`day` | `night`)
  - `lighting` (`daylight` | `dark_with_streetlights` | `dark_no_streetlights`)
  - `junction` (`no_junction` | `junction`)
  - `road_surface` (`dry` | `wet` | `unknown`)
- Response (`ModelResult`) must include:
  - `probability`: float (0..1) — currently clamped to 0..0.95 in `services/model_service.py`
  - `risk_percent`: int (0..100)
  - `breakdown`: list of objects `{ factor, value, delta, note }` where `delta` is numeric (fractional change used by UI)

Important implementation details & gotchas

- Frontend `frontend/script.js` expects the response keys above exactly; changing key names or types will break the UI.
- `backend/app.py` converts Pydantic Enums to strings via `req.model_dump(mode="json")` before calling `predict_probability`.
- CORS: `backend/app.py` currently allows only origins `http://127.0.0.1:5500` and `http://localhost:5500` — this matches running a separate static server (e.g., `python -m http.server 5500` or Live Server). The frontend currently uses an absolute API URL `http://127.0.0.1:8000/predict`.
- `backend/services/model_service.py` is a rule-based stub. It starts from a base `score = 0.10`, adds deltas for each factor, records a `breakdown`, then clamps probability to 0..0.95. Preserve the output shape when replacing the model.
- `tools/accidents_analysis.py` expects CSV/XLSX paths; the example at the bottom uses paths relative to the `tools/` file and may need adjusting to `data/accidents_raw_master.csv` when run from repo root.

Developer workflows (what works now)

- Run backend only: `uvicorn backend.app:app --reload --port 8000`
- Serve frontend locally (if not served by backend): from `frontend/` run `python -m http.server 5500` and open `http://127.0.0.1:5500`.

Recommended constraints for future changes

- When swapping the rule-based model for an ML model, keep `predict_probability` synchronous and returning a plain dict with the response keys above (so `app.py` and `frontend/script.js` remain compatible).
- If you change the CORS or hosting strategy, update `frontend/script.js` to use a configurable API base (or prefer relative paths if serving frontend from backend).

Files to inspect for details

- `backend/app.py` — request/response models, CORS, route wiring.
- `backend/services/model_service.py` — rule-based scoring logic and output format.
- `frontend/index.html` and `frontend/script.js` — input `<option>` values, API call, and UI expectations.
- `tools/accidents_analysis.py` — data dictionary parsing and `AccidentsAnalyzer.analyze_column`.

If anything above is incomplete or you want a different level of detail (e.g., UML sequence diagram, dataflow diagram, or explicit list of production-incompatible patterns), tell me which format to produce next.
