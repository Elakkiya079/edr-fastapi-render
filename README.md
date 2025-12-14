# Electronic Doctor Record (EDR) - FastAPI Microservice

## Overview
This project implements a simple Electronic Doctor Record (EDR) microservice using FastAPI and SQLite.
It supports registering doctors, retrieving by id, listing, updating, and soft-deleting.

## Structure
- `app/`
    - `main.py` - FastAPI app and endpoints
    - `database.py` - SQLAlchemy engine and session
    - `models.py` - SQLAlchemy models
    - `schemas.py` - Pydantic request/response models
    - `crud.py` - CRUD helper functions
- `requirements.txt` - Python dependencies
- `tests/` - Example pytest file (not executed here)
- `sample_expected_outputs.txt` - Example responses you can expect when running the server locally
- `run_instructions.txt` - How to run, test, and create screenshots + Word doc
- `LICENSE` - MIT

## Quick start (local)
1. Create a venv and activate:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate    # Windows (PowerShell)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
4. Open interactive docs:
   - Open http://127.0.0.1:8000/docs

## Notes on deployment
- This project uses SQLite for simplicity. For production, switch to PostgreSQL via SQLAlchemy and set DATABASE_URL env var.
- Popular simple deployment options: Railway.app, Render.com, Fly.io, or a container (Docker) pushed to AWS/Google Cloud.

## Deliverables included in this zip
- Complete working code (source files).
- `run_instructions.txt` with exact steps to run locally and capture screenshots.
- `sample_expected_outputs.txt` with example JSON payloads/responses to use when creating test screenshots and Word doc.
