from app.utils.calculator import calculate_gnc_calc


def process_pricing(data):
    result = calculate_gnc_calc(
        tier=data.tier,
        user_usage=data.features
    )
    return result
