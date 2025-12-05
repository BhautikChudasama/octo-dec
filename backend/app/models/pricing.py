from pydantic import BaseModel
from typing import Dict


class PricingRequest(BaseModel):
    tier: str
    features: Dict[str, float]


class FeatureCostBreakdown(BaseModel):
    usage: float
    tier_limit: float
    included_usage: float
    spillover_usage: float
    credit_per_unit: float
    included_credits: float
    spillover_credits: float


class PricingResponse(BaseModel):
    tier: str
    tier_total_credits: float
    total_included_credits_used: float
    total_spillover_credits: float
    total_actual_credits_required: float
    remaining_tier_credits: float
    additional_credits_required: float
    breakdown: Dict[str, FeatureCostBreakdown]
