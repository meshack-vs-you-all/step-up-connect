# StepUp Connect | Youth Growth Ecosystem

A static-first, scalable platform for youth empowerment in Kenya, connecting users to jobs, skills, side hustles, mentorship, and AI-driven career digests.

## 🚀 Live Frontend
View the project live: [https://meshack-vs-you-all.github.io/step-up-connect/](https://meshack-vs-you-all.github.io/step-up-connect/)

## 🤝 Technical Partner
Developed and managed by **[Crafted Edge Solutions](https://meshack-vs-you-all.github.io/crafted-edge-solutions-hg/)**.

## 🏗️ Backend Architecture (FastAPI)

This project features a production-grade backend designed for scalability and performance.

### 🔐 Authentication & Authorization
- **JWT Authentication**: Secure token-based authentication for user sessions.
- **RBAC (Role-Based Access Control)**: Different permission levels for Users, Mentors, and Administrators.
- **Secure Password Hashing**: Using `passlib` with `bcrypt`.

### 📊 Database & Data Modeling (SQLAlchemy + PostgreSQL)
- **Relational Design**: 
  - `User`: Core user data and profile.
  - `Job`: Job listings with relationships to categories and locations.
  - `Skill`: Skill descriptions and levels.
  - `Relationship`: Many-to-Many relationships between Users and Skills (tracking progress).
- **Migrations**: Database schema versioning with **Alembic** (in development).

### ✅ Validation & Security
- **Pydantic Schemas**: Strict data validation for all API request bodies and response models.
- **CORS Middleware**: Configured for secure cross-origin resource sharing.
- **Input Sanitization**: Built-in protections against common web vulnerabilities.

### 🤖 AI Integration
- **Unified Interface**: An abstract connector that seamlessly switches between **OpenAI (GPT-4o)** and **Google Gemini Pro**.
- **Features**: 
  - `/api/generate/job`: Automatically generates detailed job descriptions from keywords.
  - `/api/generate/skill`: Curates skill learning paths based on user interests.

### 💳 Payments
- **Flutterwave**: Integration for handling service payments and subscriptions (Test Mode).

## 🚀 Features
- **Frontend**: Hugo (Blowfish Theme) with Multilingual support.
- **Backend**: FastAPI with JWT Authentication & Role-based Access.
- **AI**: Integrated abstract connector for OpenAI & Gemini.
- **Deployment**: Full Docker support (App, DB, Redis, Frontend).

## 🛠️ Quick Start (Docker)

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
