from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from services.payment import initiate_payment, verify_transaction

router = APIRouter()

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
async def flutterwave_webhook(request: Request):
    # Validate secret hash (omitted for brevity)
    payload = await request.json()
    # Process payload (e.g., enable premium features for user)
    print(f"Received Webhook: {payload}")
    return {"status": "received"}
