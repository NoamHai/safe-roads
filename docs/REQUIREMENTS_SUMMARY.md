# Requirements Summary — Safe Roads Project

## 1. Project Goal

The project aims to build a small demo web application that demonstrates an accident risk predictor pipeline. The application consists of a static frontend user interface, a FastAPI backend API, and a rule-based model service. The primary purpose is to allow users to input driving conditions (e.g., road type, weather, lighting) and receive a predicted accident risk probability, along with a breakdown of contributing factors.

Additionally, the project includes improvements to make the codebase more robust, easier to develop, and prepared for future enhancements such as replacing the rule-based model with a machine learning model.

## 2. Mandatory Requirements

- **Architecture and Components**:
  - Static frontend (`frontend/`): HTML, CSS, and JavaScript files that collect user inputs and display results.
  - FastAPI backend (`backend/`): Handles API requests, validates inputs using Pydantic models, and serves predictions.
  - Model service (`backend/services/model_service.py`): Implements a rule-based probability calculation based on input factors.
  - Data tools (`tools/`): Includes analysis utilities for processing accident data CSV files.

- **API Contract**:
  - Endpoint: POST `/predict` accepting JSON with fields: `road_type`, `weather`, `time_of_day`, `lighting`, `junction`, `road_surface`.
  - Response: JSON with `probability` (float 0..1), `risk_percent` (int 0..100), and `breakdown` (list of {factor, value, delta, note}).
  - Preserve exact response keys and types to maintain frontend compatibility.

- **Developer Workflows**:
  - Ability to run the backend with `uvicorn backend.app:app --reload --port 8000`.
  - Serve frontend locally, either separately or integrated with the backend.

- **Implementation Improvements** (from plan):
  - Stabilize local development by serving frontend from FastAPI to eliminate CORS issues.
  - Improve backend error handling and logging (use `logging` instead of `print`, sanitize error responses).
  - Harden frontend request handling (validate responses, handle errors gracefully).
  - Add reproducible environment files (`requirements.txt`, `README.md`).
  - Add unit tests for core functions (`predict_probability`, `analyze_column`).

- **Constraints**:
  - Keep `predict_probability` synchronous and returning a plain dict.
  - Maintain compatibility when swapping to an ML model.
  - Ensure changes are minimal and reversible.

## 3. Optional / Bonus Requirements

- **CI Workflow**: Add GitHub Actions to automatically install dependencies and run tests on push/PR (optional, low priority).
- **Additional Documentation**: UML diagrams, dataflow diagrams, or expanded details on production deployment (if requested).

## 4. Required Deliverables for Submission

- **Source Code**:
  - Complete `frontend/`, `backend/`, `tools/`, and `data/` directories with all implemented improvements.
  - Updated files reflecting the phased plan (e.g., mounted static files, logging, validations).

- **Documentation**:
  - `docs/requirements.md`: Detailed understanding of the codebase.
  - `docs/plan.md`: Implementation plan and design notes.
  - `docs/REQUIREMENTS_SUMMARY.md`: This summary file.
  - `README.md`: Quick start guide with run commands.
  - `.github/copilot-instructions.md`: AI guidance for the codebase.

- **Environment and Tests**:
  - `requirements.txt`: List of Python dependencies.
  - Unit tests (e.g., in `tests/` directory) for core functions, passing with `pytest`.

- **Optional CI**: GitHub Actions workflow file if implemented.

- **Submission Format**: The entire project repository, ensuring it runs locally with the provided commands and meets all mandatory requirements.