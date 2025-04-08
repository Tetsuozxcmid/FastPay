from fastapi import APIRouter, Request, Depends, HTTPException

from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

import stripe

from core.config import Config


stripe.api_key = Config.get_stripe_secret_key()

router = APIRouter(tags=["PaymentRoutes"])
templates = Jinja2Templates(directory="templates")


async def get_stripe_customer_id(request: Request) -> str:
    return request.app.state.stripe_customer_id


@router.post("/create-order")
async def create_order(
    request: Request,
    stripe_customer_id: str = Depends(get_stripe_customer_id),
):
    data = await request.json()

    stripe_session = stripe.checkout.Session.create(
        customer=stripe_customer_id,
        success_url="http://localhost:8005/succes?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="http://localhost:8005/cancel",
        payment_method_types=["card"],
        mode="subscription",
        line_items=[
            {
                "price": data["priceId"],
                "quantity": 1,
            }
        ],
    )
    return {"session_id": stripe_session["id"]}


@router.post("/create-billing-portal")
async def create_portal(
    request: Request,
    stripe_customer_id: str = Depends(get_stripe_customer_id),
):
    session = stripe.billing_portal.Session.create(
        customer=stripe_customer_id,
        return_url="http://localhost:8005",
    )
    return {"url": session.url}


@router.get("/api/stripe-config")
async def get_stripe_config():
    try:
        stripe_public_key = Config.get_stripe_publish_key()
        premium_price_id = Config.get_premium_price_id()
        basic_price_id = Config.get_basic_price_id()

        if not stripe_public_key:
            raise ValueError("STRIPE_PUBLIC_KEY not found")
        if not premium_price_id:
            raise ValueError("PREMIUM_PRICE_ID not found")
        if not basic_price_id:
            raise ValueError("BASIC_PRICE_ID not found")

        return JSONResponse({
            "stripePublicKey": stripe_public_key,
            "premiumPriceId": premium_price_id,
            "basicPriceId": basic_price_id,
        })

    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
