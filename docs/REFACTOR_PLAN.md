# Refactor Plan — Safe Roads Project

## Current Repository Inspection

### Structure
- `backend/`: Flat structure with `app.py` (FastAPI app, routes, models) and `services/model_service.py` (inference logic).
- `frontend/`: Static files (`index.html`, `script.js`, `style.css`) with hard-coded API URL and basic error handling.
- `tools/`: Data analysis script.
- `data/`: Raw CSV and XLSX.
- `docs/`: Comprehensive documentation.
- Missing: `requirements.txt`, `README.md`, tests, config, proper logging, environment variables.

### Code Quality Issues
- **Backend**: Monolithic `app.py` (routes + models + middleware); basic logging; no config; no tests; hardcoded paths.
- **Frontend**: No input validation; error handling shows raw messages; no config for API URL; static, no build process.
- **Overall**: No environment management; no CI; no Docker; docs are good but scattered.

### Strengths
- End-to-end flow works.
- API contract preserved.
- ML inference infrastructure implemented with fallback.
- Extensive docs.

## Proposed New Clean Structure

```
safe_roads/
├── src/
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── app.py              # FastAPI app factory
│   │   ├── config.py           # Settings (env vars, paths)
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── predict.py      # /predict endpoint
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── model_service.py # Inference logic
│   │   └── models/
│   │       ├── __init__.py
│   │       └── schemas.py      # Pydantic models
│   ├── frontend/               # Static files (serve via backend or separate)
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   └── shared/                 # If needed for common utils
├── tests/
│   ├── __init__.py
│   ├── test_model_service.py
│   └── test_routes.py
├── scripts/                    # Moved from tools/
│   └── accidents_analysis.py
├── data/                       # Keep as-is
├── docs/                       # Keep, add refactor notes
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── Dockerfile                  # Optional for containerization
```

### Key Improvements
- **Modular Backend**: Separate concerns (routes, services, config).
- **Config Management**: Use Pydantic settings for env vars (API port, model path, CORS origins).
- **Testing**: Pytest structure for unit tests.
- **Frontend Enhancements**: Configurable API URL, better validation, error handling.
- **Production Touches**: Logging with structlog or similar, health checks, graceful shutdown.
- **DevOps**: Requirements, README, .env, Dockerfile.

## Refactor Plan (Phased)

### Phase 1: Restructure Folders and Modularize Backend
- Move `backend/` to `src/backend/`, create modules.
- Extract schemas to `models/schemas.py`.
- Move routes to `routes/predict.py`.
- Update imports and paths.

### Phase 2: Add Configuration and Environment
- Create `config.py` with Pydantic BaseSettings for env vars.
- Add `.env.example` and load via python-dotenv.
- Update CORS, model path to use config.

### Phase 3: Improve Logging and Error Handling
- Use structlog for structured logging.
- Add middleware for request logging, error handling.
- Sanitize errors, add health endpoint.

### Phase 4: Enhance Frontend
- Add config object in `script.js` for API base URL.
- Improve input validation, error messages.
- Add loading states, retry logic.

### Phase 5: Add Tests and Requirements
- Create `requirements.txt` with all deps.
- Write unit tests for model_service and routes.
- Add pytest config.

### Phase 6: Documentation and Polish
- Update README with setup, run, test instructions.
- Add Dockerfile for containerized run.
- Ensure all docs are updated.

### Acceptance Criteria
- End-to-end flow works identically.
- API contract unchanged.
- ML inference loads model or falls back.
- Code is modular, tested, configurable.
- Easy to run locally and deploy.

### Risks and Mitigations
- **Breaking Changes**: Test after each phase; keep old code as backup.
- **Complexity**: Start small, refactor incrementally.
- **Dependencies**: Add only necessary (e.g., uvicorn, pydantic already used).

This plan transforms the project into a production-ready system while preserving functionality.