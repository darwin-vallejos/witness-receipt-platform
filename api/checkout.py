import os
import stripe
from fastapi import APIRouter

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

router = APIRouter()

@router.post("/checkout")
def checkout():
    session = stripe.checkout.Session.create(
        mode="payment",
        line_items=[
            {
                "price": os.environ["STRIPE_PRICE_ID"],
                "quantity": 1,
            }
        ],
        success_url="http://localhost:8000/success",
        cancel_url="http://localhost:8000/cancel",
    )
    return {"checkout_url": session.url}
