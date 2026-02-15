from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from services.ai import get_ai_service, AIService
from api.endpoints import auth, payment
import json
import os

app = FastAPI(
    title="Growth Ecosystem API",
    description="API for Jobs, Skills, and AI Digest",
    version="0.1.0"
)

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:1313", # Hugo default port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(payment.router, prefix="/api/payment", tags=["payment"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Growth Ecosystem API"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

# Placeholder endpoints
@app.get("/api/jobs")
async def get_jobs():
    return {"jobs": [{"id": 1, "title": "Software Engineer", "location": "Remote"}]}

@app.get("/api/skills")
async def get_skills():
    return {"skills": [{"id": 1, "name": "Python", "level": "Intermediate"}]}

@app.get("/api/mentors")
async def get_mentors():
    # In real app, read from DB. Here read from seed.
    try:
         with open("../data/mentorship.json", "r") as f:
             return json.load(f)
    except FileNotFoundError:
        return []

@app.get("/api/gigs")
async def get_gigs():
    try:
         with open("../data/gigs.json", "r") as f:
             return json.load(f)
    except FileNotFoundError:
        return []

@app.get("/api/generate/job")
async def ai_generate_job(title: str, ai_service: AIService = Depends(get_ai_service)):
    description = await ai_service.generate_job_description(title)
    return {"title": title, "description": description}

@app.get("/api/generate/skill")
async def ai_generate_skill(name: str, ai_service: AIService = Depends(get_ai_service)):
    summary = await ai_service.generate_skill_summary(name)
    return {"skill": name, "summary": summary}
