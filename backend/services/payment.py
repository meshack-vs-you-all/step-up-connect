import os
import httpx

FLUTTERWAVE_SECRET_KEY = os.getenv("FLUTTERWAVE_SECRET_KEY", "FLWSECK_TEST-SANDBOX")
BASE_URL = "https://api.flutterwave.com/v3"

async def initiate_payment(amount: float, email: str, user_id: int):
    headers = {
        "Authorization": f"Bearer {FLUTTERWAVE_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "tx_ref": f"txn_{user_id}_{os.urandom(4).hex()}",
        "amount": str(amount),
        "currency": "KES",
        "redirect_url": "http://localhost:1313/payment/callback", # Frontend callback
        "customer": {
            "email": email,
            "name": f"User {user_id}"
        },
        "customizations": {
            "title": "Growth Platform Premium"
        }
    }
    
    # In a real scenario, we would call the API.
    # async with httpx.AsyncClient() as client:
    #     response = await client.post(f"{BASE_URL}/payments", json=data, headers=headers)
    #     return response.json()

    # Mock response
    return {
        "status": "success",
        "message": "Payment initiation simulated",
        "data": {
            "link": "https://flutterwave.com/pay/mock_checkout_url"
        }
    }

async def verify_transaction(tx_ref: str):
    # Mock verification
    return {"status": "success", "tx_ref": tx_ref, "amount": 1000}
