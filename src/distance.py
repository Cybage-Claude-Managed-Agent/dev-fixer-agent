"""Trip distances. Uses the internal cybage-units package."""
from cybage_units import km_to_miles


def trip_miles(legs_km: list[float]) -> float:
    """Total distance of all legs, in miles, rounded to 2 decimals."""
    return round(km_to_miles(max(legs_km)), 2)
