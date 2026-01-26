# TODO Plan — Safe Roads Project

This plan outlines step-by-step tasks to address the gaps identified in `docs/GAP_ANALYSIS.md`. Tasks are ordered for logical implementation, starting with core improvements and ending with optional enhancements.

## 1. Integrate Frontend Serving in Backend
**Task Name:** Mount StaticFiles in FastAPI to serve frontend and eliminate CORS issues.  
**Files Involved:** `backend/app.py`, `frontend/script.js`.  
**Acceptance Criteria:** Running `uvicorn backend.app:app --reload` serves the UI at `http://127.0.0.1:8000/`; frontend calls `/predict` with relative path; no CORS errors in dev.  
**Suggested Copilot Prompts:** "Add StaticFiles mount to FastAPI app in backend/app.py to serve frontend/ directory at root; update frontend/script.js to use relative API URL '/predict'."

## 2. Improve Backend Error Handling and Logging
**Task Name:** Replace print statements with logging and sanitize error responses.  
**Files Involved:** `backend/app.py`.  
**Acceptance Criteria:** Exceptions logged via `logging` without exposing tracebacks in API responses; HTTP 500 returns generic "Internal server error" message.  
**Suggested Copilot Prompts:** "Add logging import and setup in backend/app.py; replace print and traceback in predict route with logger.exception; update HTTPException to return sanitized detail."

## 3. Harden Frontend Request Handling
**Task Name:** Add validation, error handling, and defensive rendering in frontend.  
**Files Involved:** `frontend/script.js`.  
**Acceptance Criteria:** UI validates `probability` as finite 0-1 number; checks content-type for JSON; renders breakdown without NaN; handles non-JSON responses gracefully.  
**Suggested Copilot Prompts:** "In frontend/script.js, add validation for data.probability; guard await res.json() with content-type check; defensively format breakdown to handle missing delta; use relative '/predict' URL."

## 4. Add Reproducible Environment Files
**Task Name:** Create requirements.txt and README.md for easy setup.  
**Files Involved:** `requirements.txt` (new), `README.md` (new).  
**Acceptance Criteria:** `pip install -r requirements.txt` installs FastAPI, Uvicorn, Pydantic, Pandas; README.md includes installation, run commands, and project description.  
**Suggested Copilot Prompts:** "Create requirements.txt with fastapi, uvicorn, pydantic, pandas; create README.md with project overview, installation steps, and commands to run backend and frontend."

## 5. Add Unit Tests for Core Functions
**Task Name:** Implement pytest tests for predict_probability and analyze_column.  
**Files Involved:** `tests/` directory (new), `tests/test_model.py` (new), `tests/test_analysis.py` (new).  
**Acceptance Criteria:** `pytest` runs and passes tests asserting output keys/types for predict_probability; tests for analyze_column use a small CSV fixture.  
**Suggested Copilot Prompts:** "Create tests/ directory; add test_model.py with pytest tests for predict_probability using sample inputs; add test_analysis.py for AccidentsAnalyzer.analyze_column with a mock CSV."

## 6. Add GitHub Actions CI Workflow (Optional)
**Task Name:** Set up CI to run tests and linting on push/PR.  
**Files Involved:** `.github/workflows/ci.yml` (new).  
**Acceptance Criteria:** Workflow file exists; on push, installs deps, runs pytest, and reports results.  
**Suggested Copilot Prompts:** "Create .github/workflows/ci.yml with steps for checkout, install requirements.txt, run pytest, and optional linting."

## 7. Add Additional Documentation (Optional)
**Task Name:** Include diagrams for API flow and components.  
**Files Involved:** `docs/sequence_diagram.md` (new), `docs/component_diagram.md` (new).  
**Acceptance Criteria:** Markdown files with simple ASCII or Mermaid diagrams showing API sequence and component relationships.  
**Suggested Copilot Prompts:** "Create docs/sequence_diagram.md with Mermaid diagram for frontend-backend-model flow; create docs/component_diagram.md showing directories and interactions."

## 8. Ensure Submission Readiness
**Task Name:** Verify all mandatory requirements are met and repository is complete.  
**Files Involved:** All updated files.  
**Acceptance Criteria:** All mandatory items in gap analysis marked Done; repository runs locally with provided commands; docs updated.  
**Suggested Copilot Prompts:** "Review docs/GAP_ANALYSIS.md and verify each task; run full app test; update docs if needed."