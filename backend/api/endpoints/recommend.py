from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from models import User, Gig, Job
from api.deps import get_current_user
from services.ai import AIService, get_ai_service

router = APIRouter()

@router.get("/gigs")
async def recommend_gigs(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    ai_service: AIService = Depends(get_ai_service)
):
    # Fetch all gigs (in a real app, we'd filter by vector similarity)
    all_gigs = db.query(Gig).all()
    
    # Simple rule-based filtering first
    # If user is youth, show all. If mentor, maybe show specific ones?
    # For now, let's just pick 3 random ones or use AI to rank them if possible.
    
    # AI Ranking Mockup
    # In Phase 2, we simulate this by returning a subset.
    # Ideally, we'd send user profile + gig list to LLM to rank.
    
    return all_gigs[:3] 

@router.get("/jobs")
async def recommend_jobs(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    all_jobs = db.query(Job).all()
    return all_jobs[:3]
