from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from pydantic import BaseModel

from core.database import get_db
from models import Booking, User, Mentor
from api.deps import get_current_user

router = APIRouter()

# Pydantic Schemas
class BookingCreate(BaseModel):
    mentor_id: int
    date: datetime
    notes: str

class BookingOut(BaseModel):
    id: int
    mentor_id: int
    user_id: int
    date: datetime
    status: str
    notes: str
    
    class Config:
        orm_mode = True

@router.post("/", response_model=BookingOut)
async def create_booking(
    booking: BookingCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify mentor exists
    mentor = db.query(Mentor).filter(Mentor.id == booking.mentor_id).first()
    if not mentor:
         raise HTTPException(status_code=404, detail="Mentor not found")

    new_booking = Booking(
        user_id=current_user.id,
        mentor_id=booking.mentor_id,
        date=booking.date,
        notes=booking.notes,
        status="pending"
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

@router.get("/me", response_model=List[BookingOut])
async def get_my_bookings(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Booking).filter(Booking.user_id == current_user.id).all()
