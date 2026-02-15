from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from services.ai import get_ai_service, AIService
from api.endpoints import auth, payment, users, recommend
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
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(recommend.router, prefix="/api/recommend", tags=["recommend"])

from sqlalchemy.orm import Session
from core.database import get_db, Base, engine
from models import Job, Gig, Mentor

# Create tables on startup (simple migration)
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to the Growth Ecosystem API"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/jobs")
async def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()
    # Serialize if needed, or rely on FastAPI ORM serialization
    return jobs

@app.get("/api/skills")
async def get_skills():
    # Skills are still hardcoded/JSON for now as per audit
    return {"skills": [{"id": 1, "name": "Python", "level": "Intermediate"}]}

@app.get("/api/mentors")
async def get_mentors(db: Session = Depends(get_db)):
    mentors = db.query(Mentor).all()
    return mentors

@app.get("/api/gigs")
async def get_gigs(db: Session = Depends(get_db)):
    gigs = db.query(Gig).all()
    return gigs

@app.get("/api/generate/job")
async def ai_generate_job(title: str, ai_service: AIService = Depends(get_ai_service)):
    description = await ai_service.generate_job_description(title)
    return {"title": title, "description": description}

@app.get("/api/generate/skill")
async def ai_generate_skill(name: str, ai_service: AIService = Depends(get_ai_service)):
    summary = await ai_service.generate_skill_summary(name)
    return {"skill": name, "summary": summary}

@app.get("/api/generate/digest")
async def ai_generate_digest(topic: str = "AI Trends", ai_service: AIService = Depends(get_ai_service)):
    digest = await ai_service.generate_digest(topic)
    return {"topic": topic, "digest": digest}
