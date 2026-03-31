# Requirements Checklist — Safe Roads Project

| Requirement | Source Document | Status | Verification Method |
|-------------|-----------------|--------|---------------------|
| Build a small demo web application demonstrating accident risk predictor pipeline | docs/REQUIREMENTS_SUMMARY.md | Done | Inspect `frontend/`, `backend/`, and `services/model_service.py` files; run the app and test prediction flow. |
| Static frontend (`frontend/`): HTML, CSS, and JavaScript files that collect user inputs and display results | docs/REQUIREMENTS_SUMMARY.md | Done | Check files in `frontend/` directory: `index.html`, `script.js`, `style.css`. |
| FastAPI backend (`backend/`): Handles API requests, validates inputs using Pydantic models, and serves predictions | docs/REQUIREMENTS_SUMMARY.md | Done | Inspect `backend/app.py` for FastAPI setup, Pydantic models, and route. |
| Model service (`backend/services/model_service.py`): Implements a rule-based probability calculation based on input factors | docs/REQUIREMENTS_SUMMARY.md | Done | Review `backend/services/model_service.py` for `predict_probability` function and rule-based logic. |
| Data tools (`tools/`): Includes analysis utilities for processing accident data CSV files | docs/REQUIREMENTS_SUMMARY.md | Done | Check `tools/accidents_analysis.py` and `data/accidents_raw_master.csv`. |
| API Endpoint: POST `/predict` accepting JSON with specified fields | docs/REQUIREMENTS_SUMMARY.md | Done | Inspect `backend/app.py` for route definition and Pydantic `PredictRequest`. |
| API Response: JSON with `probability`, `risk_percent`, and `breakdown` | docs/REQUIREMENTS_SUMMARY.md | Done | Check `backend/app.py` for `ModelResult` model and `services/model_service.py` output. |
| Preserve exact response keys and types for frontend compatibility | docs/REQUIREMENTS_SUMMARY.md | Done | Verify `frontend/script.js` expects the keys; test API response matches. |
| Ability to run backend with `uvicorn backend.app:app --reload --port 8000` | docs/REQUIREMENTS_SUMMARY.md | Done | Run the command and confirm server starts. |
| Serve frontend locally, either separately or integrated with the backend | docs/REQUIREMENTS_SUMMARY.md | Partial | Separate serving works; integration (serving from backend) not yet implemented. |
| Stabilize local development by serving frontend from FastAPI to eliminate CORS issues | docs/REQUIREMENTS_SUMMARY.md | Missing | Not implemented; CORS still restrictive. |
| Improve backend error handling and logging (use `logging` instead of `print`, sanitize error responses) | docs/REQUIREMENTS_SUMMARY.md | Missing | Current code uses `print` and returns raw tracebacks. |
| Harden frontend request handling (validate responses, handle errors gracefully) | docs/REQUIREMENTS_SUMMARY.md | Missing | `frontend/script.js` lacks robust validation and error handling. |
| Add reproducible environment files (`requirements.txt`, `README.md`) | docs/REQUIREMENTS_SUMMARY.md | Missing | No `requirements.txt`; `README.md` not present. |
| Add unit tests for core functions (`predict_probability`, `analyze_column`) | docs/REQUIREMENTS_SUMMARY.md | Missing | No test files or framework setup. |
| Keep `predict_probability` synchronous and returning a plain dict | docs/REQUIREMENTS_SUMMARY.md | Done | Inspect `services/model_service.py`; function is synchronous and returns dict. |
| Maintain compatibility when swapping to an ML model | docs/REQUIREMENTS_SUMMARY.md | Done | Current implementation preserves response shape. |
| Ensure changes are minimal and reversible | docs/REQUIREMENTS_SUMMARY.md | N/A | Applies to future changes; current code is baseline. |
| Add GitHub Actions CI workflow (optional) | docs/REQUIREMENTS_SUMMARY.md | Missing | No CI workflow file. |
| Additional documentation (UML diagrams, etc.) (optional) | docs/REQUIREMENTS_SUMMARY.md | Missing | No additional diagrams provided. |
| Complete `frontend/`, `backend/`, `tools/`, and `data/` directories with improvements | docs/REQUIREMENTS_SUMMARY.md | Partial | Directories exist; improvements not yet applied. |
| `docs/requirements.md`: Detailed understanding of the codebase | docs/REQUIREMENTS_SUMMARY.md | Done | File exists and contains details. |
| `docs/plan.md`: Implementation plan and design notes | docs/REQUIREMENTS_SUMMARY.md | Done | File exists with plan. |
| `docs/REQUIREMENTS_SUMMARY.md`: This summary file | docs/REQUIREMENTS_SUMMARY.md | Done | This file. |
| `README.md`: Quick start guide with run commands | docs/REQUIREMENTS_SUMMARY.md | Missing | No `README.md` file. |
| `.github/copilot-instructions.md`: AI guidance for the codebase | docs/REQUIREMENTS_SUMMARY.md | Done | File exists. |
| `requirements.txt`: List of Python dependencies | docs/REQUIREMENTS_SUMMARY.md | Missing | No file. |
| Unit tests (e.g., in `tests/` directory) for core functions, passing with `pytest` | docs/REQUIREMENTS_SUMMARY.md | Missing | No tests directory or tests. |
| Optional CI: GitHub Actions workflow file | docs/REQUIREMENTS_SUMMARY.md | Missing | No file. |
| Submission format: Entire project repository running locally | docs/REQUIREMENTS_SUMMARY.md | Partial | Repository exists; may not fully meet all after improvements. |