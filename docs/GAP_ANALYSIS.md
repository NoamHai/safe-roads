# Gap Analysis — Safe Roads Project

This analysis compares the current codebase implementation against the requirements in `docs/REQUIREMENTS_CHECKLIST.md`. Status has been updated based on scanning `backend/app.py`, `backend/services/model_service.py`, `frontend/index.html`, `frontend/script.js`, and `frontend/style.css`.

| Requirement | Updated Status | Implementation Plan for Partial/Missing |
|-------------|-----------------|-----------------------------------------|
| Build a small demo web application demonstrating accident risk predictor pipeline | Done | N/A |
| Static frontend (`frontend/`): HTML, CSS, and JavaScript files that collect user inputs and display results | Done | N/A |
| FastAPI backend (`backend/`): Handles API requests, validates inputs using Pydantic models, and serves predictions | Done | N/A |
| Model service (`backend/services/model_service.py`): Implements a rule-based probability calculation based on input factors | Done | N/A |
| Data tools (`tools/`): Includes analysis utilities for processing accident data CSV files | Done | N/A |
| API Endpoint: POST `/predict` accepting JSON with specified fields | Done | N/A |
| API Response: JSON with `probability`, `risk_percent`, and `breakdown` | Done | N/A |
| Preserve exact response keys and types for frontend compatibility | Done | N/A |
| Ability to run backend with `uvicorn backend.app:app --reload --port 8000` | Done | N/A |
| Serve frontend locally, either separately or integrated with the backend | Partial | Already supports separate serving; to integrate, mount StaticFiles in FastAPI app and update frontend API URL to relative path. |
| Stabilize local development by serving frontend from FastAPI to eliminate CORS issues | Missing | Add StaticFiles mount to `backend/app.py` for `/` route serving `frontend/` directory; update CORS to allow same-origin or remove if not needed. |
| Improve backend error handling and logging (use `logging` instead of `print`, sanitize error responses) | Missing | Import `logging` in `backend/app.py`; replace `print` and `traceback.format_exc()` with `logger.exception()`; change HTTPException to return generic error message without exposing internals. |
| Harden frontend request handling (validate responses, handle errors gracefully) | Missing | In `frontend/script.js`, add validation for `data.probability` (check finite number 0-1); guard JSON parsing with content-type check; render `breakdown` defensively to avoid NaN; use relative API URL if served from backend. |
| Add reproducible environment files (`requirements.txt`, `README.md`) | Missing | Create `requirements.txt` with `fastapi`, `uvicorn`, `pydantic`, `pandas`; create `README.md` with installation, run commands, and brief description. |
| Add unit tests for core functions (`predict_probability`, `analyze_column`) | Missing | Create `tests/` directory; add `pytest` tests for `predict_probability` with sample inputs asserting output keys/types; add tests for `analyze_column` using a small CSV fixture. |
| Keep `predict_probability` synchronous and returning a plain dict | Done | N/A |
| Maintain compatibility when swapping to an ML model | Done | N/A |
| Ensure changes are minimal and reversible | N/A | N/A |
| Add GitHub Actions CI workflow (optional) | Missing | Create `.github/workflows/ci.yml` with steps to install dependencies, run tests, and check linting. |
| Additional documentation (UML diagrams, etc.) (optional) | Missing | Add sequence diagram for API flow and component diagram in `docs/`. |
| Complete `frontend/`, `backend/`, `tools/`, and `data/` directories with improvements | Partial | Directories exist; apply above plans to update files. |
| `docs/requirements.md`: Detailed understanding of the codebase | Done | N/A |
| `docs/plan.md`: Implementation plan and design notes | Done | N/A |
| `docs/REQUIREMENTS_SUMMARY.md`: This summary file | Done | N/A |
| `README.md`: Quick start guide with run commands | Missing | Create as part of environment files plan. |
| `.github/copilot-instructions.md`: AI guidance for the codebase | Done | N/A |
| `requirements.txt`: List of Python dependencies | Missing | Create as part of environment files plan. |
| Unit tests (e.g., in `tests/` directory) for core functions, passing with `pytest` | Missing | Create as part of tests plan. |
| Optional CI: GitHub Actions workflow file | Missing | Create as part of CI plan. |
| Submission format: Entire project repository running locally | Partial | Repository exists; ensure all plans implemented for full compliance. |