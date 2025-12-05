from app.core.constants import *


def calculate_gnc_calc(tier: str, user_usage: dict):
    """
    Calculates:
    - Total credits used within tier limits
    - Spill-over usage per feature
    - Spill-over credits
    - Remaining tier credits
    - ✅ Total additional credits required (if usage exceeds tier)
    """

    if tier not in TIERS_FEATURE_LIMITS:
        raise ValueError("Invalid tier")

    tier_credits = TIERS_FEATURE_LIMITS[tier]["credits"]
    tier_limits = TIERS_FEATURE_LIMITS[tier]["feature_limits"]

    total_included_credits_used = 0
    total_spillover_credits = 0

    breakdown = {}

    for feature, usage in user_usage.items():

        if feature not in CREDITS_PER_FEATURES:
            raise ValueError(f"Invalid feature: {feature}")

        credit_per_unit = CREDITS_PER_FEATURES[feature]
        max_limit = tier_limits.get(feature, float("inf"))

        # ✅ Usage split
        included_usage = min(usage, max_limit)
        spillover_usage = max(usage - max_limit, 0)

        # ✅ Credit calculations
        included_credits = included_usage * credit_per_unit
        spillover_credits = spillover_usage * credit_per_unit

        total_included_credits_used += included_credits
        total_spillover_credits += spillover_credits

        breakdown[feature] = {
            "usage": usage,
            "tier_limit": max_limit,
            "included_usage": included_usage,
            "spillover_usage": spillover_usage,
            "credit_per_unit": credit_per_unit,
            "included_credits": included_credits,
            "spillover_credits": spillover_credits
        }

    # ✅ Remaining credits after INCLUDED usage
    remaining_tier_credits = tier_credits - total_included_credits_used

    # ✅ Total actual credits needed (included + spillover)
    total_actual_credits_required = total_included_credits_used + total_spillover_credits

    # ✅ EXTRA credits user must buy
    additional_credits_required = max(
        total_actual_credits_required - tier_credits,
        0
    )

    return {
        "tier": tier,
        "tier_total_credits": tier_credits,
        "total_included_credits_used": total_included_credits_used,
        "total_spillover_credits": total_spillover_credits,
        "total_actual_credits_required": total_actual_credits_required,  # ✅ NEW
        "remaining_tier_credits": remaining_tier_credits if remaining_tier_credits > 0 else 0,
        "additional_credits_required": additional_credits_required,      # ✅ NEW
        "breakdown": breakdown
    }
