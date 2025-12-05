from fastapi import APIRouter, HTTPException
from app.models.pricing import PricingRequest, PricingResponse
from app.services.pricing_service import process_pricing

router = APIRouter(prefix="/pricing", tags=["Pricing"])


@router.post("/calculate", response_model=PricingResponse)
def calculate_price(payload: PricingRequest):
    try:
        result = process_pricing(payload)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
