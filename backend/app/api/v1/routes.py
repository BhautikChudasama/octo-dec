from fastapi import APIRouter
from app.api.v1.pricing import router as pricing_router

router = APIRouter()
router.include_router(pricing_router)
