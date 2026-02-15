from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from core.database import get_db
from models import Skill

router = APIRouter()

# Pydantic Schema
class SkillOut(BaseModel):
    id: int
    name: str
    category: str
    level: str
    resources: List[str]

    class Config:
        orm_mode = True

@router.get("/", response_model=List[SkillOut])
async def get_skills(db: Session = Depends(get_db)):
    skills = db.query(Skill).all()
    return skills
