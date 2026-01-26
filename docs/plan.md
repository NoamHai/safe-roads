# Implementation Plan & Design — Safe Roads

Goal

- Make the project easier to develop, more robust, and ready for replacing the rule-based model with a real model.

Principles

- Preserve API contract (`probability`, `risk_percent`, `breakdown`).
- Keep changes minimal and reversible.
- Prefer small, reviewable commits.

Phased plan (ordered, with acceptance criteria)

1) Stabilize local dev flow (safe, quick)
- Task: Serve frontend from FastAPI to remove cross-origin dev friction.
- Files: `backend/app.py` change to mount `StaticFiles(directory="frontend", html=True)` and serve `/`.
- Acceptance: Running `uvicorn backend.app:app --reload` serves the UI at `http://127.0.0.1:8000/` and the UI can call `/predict` with a relative path.
- Rollback: Revert `app.mount` and restore strict CORS.

2) Improve backend logging and error handling (high impact)
- Task: Add `logging` usage, replace `print` with `logger.exception(...)`, and avoid returning raw tracebacks to clients.
- Files: `backend/app.py` and optionally create `backend/logging.py` helper.
- Acceptance: Server logs show stack traces; API responses return sanitized errors (e.g., `{"detail":"Internal server error"}`) while full details are only in logs.

3) Harden frontend request handling (medium)
- Task: Update `frontend/script.js` to:
  - Use a single `API_BASE` constant (default to `""` so relative paths work when served by backend).
  - Validate `data.probability` (finite number between 0 and 1) before using it.
  - Guard JSON parsing using `content-type` check and produce friendly UI error messages.
  - Render `breakdown` defensively so missing `delta` doesn't produce `NaN`.
- Acceptance: UI does not display `NaN` or raw tracebacks; works with both separate server (old flow) and backend-served UI (new flow).

4) Add reproducible dev environment files (medium)
- Task: Create `requirements.txt` with `fastapi`, `uvicorn`, `pydantic`, `pandas` and a short `README.md` run snippet.
- Acceptance: `pip install -r requirements.txt` installs necessary packages and the `README` shows the correct dev commands.

5) Add tests for core functions (medium)
- Task: Add unit tests using `pytest` for:
  - `backend/model_service.predict_probability` (assert output keys and types for a few input combinations).
  - `tools/accidents_analysis.AccidentsAnalyzer.analyze_column` basic behavior using a small synthetic CSV fixture.
- Acceptance: `pytest` passes locally.

6) Optional: CI workflow (low)
- Task: Add GitHub Actions workflow to install dependencies and run tests on push/PR.
- Acceptance: Workflow runs and reports test results.

Design notes & tradeoffs

- Serving frontend from FastAPI simplifies dev UX but slightly changes how static assets are deployed in production; ensure static mount aligns with final hosting strategy.
- Sanitizing errors in API responses improves security but reduces immediate debugging info in the UI; rely on logs for details.
- Tests should focus on contract stability (response shape) rather than exact numeric semantics of the current rule-based model.

Proposed commit plan (small commits)

- commit A: docs/* (requirements.md and plan.md) — reviewable
- commit B: `backend/app.py` — mount frontend static files + update CORS comment
- commit C: `backend/app.py` — add `logging` and sanitize exceptions
- commit D: `frontend/script.js` — add `API_BASE`, validation, defensive rendering
- commit E: `requirements.txt` + `README.md`
- commit F: tests/
- commit G: optional CI workflow

Next step

- Confirm you want me to implement the first code change: (A) mount static `frontend/` in `backend/app.py` and switch the frontend to use a relative `/predict` call, or choose a different first task from the plan.
