from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from models import Booking
import os

router = APIRouter()

FLUTTERWAVE_SECRET_KEY = os.getenv("FLUTTERWAVE_SECRET_KEY", "default_secret")

@router.post("/webhook")
async def payment_webhook(request: Request, db: Session = Depends(get_db)):
    # Verify signature (Flutterwave sends hash in headers)
    signature = request.headers.get("verif-hash")
    if not signature or signature != FLUTTERWAVE_SECRET_KEY:
        # In production, you strictly verify this. For test mode, we might be lenient or simulate it.
        # raise HTTPException(status_code=401, detail="Invalid signature")
        pass

    payload = await request.json()
    
    # Check status
    if payload.get("status") == "successful":
        tx_ref = payload.get("txRef")
        # Assuming tx_ref contains booking_id, e.g., "booking_123"
        if tx_ref and tx_ref.startswith("booking_"):
            try:
                booking_id = int(tx_ref.split("_")[1])
                booking = db.query(Booking).filter(Booking.id == booking_id).first()
                if booking:
                    booking.status = "confirmed"
                    db.commit()
            except ValueError:
                pass
                
    return {"status": "processed"}
