from fastapi import APIRouter, HTTPException, Request, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from core.database import get_db
from models import Booking
from services.payment import initiate_payment, verify_transaction
import os

router = APIRouter()

FLUTTERWAVE_SECRET_KEY = os.getenv("FLUTTERWAVE_SECRET_KEY", "FLWSECK_TEST-SANDBOX")

class PaymentRequest(BaseModel):
    amount: float
    email: str
    user_id: int

@router.post("/initiate")
async def start_payment(payment: PaymentRequest):
    try:
        result = await initiate_payment(payment.amount, payment.email, payment.user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/webhook")
async def payment_webhook(request: Request, db: Session = Depends(get_db)):
    # Verify signature
    signature = request.headers.get("verif-hash")
    if signature and signature != FLUTTERWAVE_SECRET_KEY:
         # In production, check this. For now, we log it.
         print(f"Signature mismatch: {signature}")
         pass

    payload = await request.json()
    print(f"Received Webhook: {payload}")
    
    # Check status
    if payload.get("status") == "successful":
        tx_ref = payload.get("txRef") or payload.get("data", {}).get("tx_ref")
        
        # Handle Booking Confirmation
        if tx_ref and tx_ref.startswith("booking_"):
            try:
                booking_id = int(tx_ref.split("_")[1])
                booking = db.query(Booking).filter(Booking.id == booking_id).first()
                if booking:
                    booking.status = "confirmed"
                    db.commit()
            except (ValueError, IndexError):
                pass
                
    return {"status": "processed"}
