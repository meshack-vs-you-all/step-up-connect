# Youth Growth Ecosystem Platform

A static-first, scalable platform for youth growth, connecting users to jobs, skills, side hustles, mentorship, and an AI digest.

## Features
- **Frontend**: Hugo (Blowfish Theme) with Multilingual support.
- **Backend**: FastAPI with JWT Authentication & Role-based Access.
- **AI**: Integrated abstract connector for OpenAI & Gemini.
- **Payments**: Flutterwave integration (Test Mode).
- **Deployment**: Full Docker support (App, DB, Redis, Frontend).

## Quick Start (Docker)

The easiest way to run the platform is via Docker.

1.  **Environment Setup**:
    Create a `.env` file in the root directory:
    ```env
    OPENAI_API_KEY=your_key_here
    GEMINI_API_KEY=your_key_here
    FLUTTERWAVE_SECRET_KEY=FLWSECK_TEST-SANDBOX
    ```

    **Frontend Config**:
    Update `frontend/config.toml` if your backend URL changes:
    ```toml
    [params]
      apiBaseURL = "http://localhost:8000"
    ```


2.  **Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```

3.  **Access**:
    -   **Frontend**: http://localhost:1313
    -   **Backend API**: http://localhost:8000
    -   **API Docs**: http://localhost:8000/docs

## Development Setup (Local)

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
hugo server -D
```

## AI & Data
-   **AI**: Endpoints at `/api/generate/job` and `/api/generate/skill`.
-   **Data**: Seed data located in `data/` is served via API.

## Contributions
See `docs/CONTRIBUTING.md`.
