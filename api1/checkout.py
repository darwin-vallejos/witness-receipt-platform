import os
import stripe
from fastapi import APIRouter, HTTPException
from uuid import uuid4

router = APIRouter()

# Stripe configuration
stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

PRICE_ID = os.environ["STRIPE_PRICE_ID"]
BASE_URL = os.environ.get("APP_BASE_URL", "http://localhost:8000")

@router.post("/checkout")
def create_checkout_session():
    """
    Creates a Stripe Checkout Session for PRO subscription.
    """
    try:
        user_id = str(uuid4())

        session = stripe.checkout.Session.create(
            mode="subscription",
            line_items=[
                {
                    "price": PRICE_ID,
                    "quantity": 1,
                }
            ],
            success_url=f"{BASE_URL}/success",
            cancel_url=f"{BASE_URL}/cancel",
            client_reference_id=user_id,
            metadata={
                "user_id": user_id,
            },
        )

        return {"checkout_url": session.url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
