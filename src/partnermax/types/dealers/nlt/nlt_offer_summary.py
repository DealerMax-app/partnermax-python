# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["NltOfferSummary"]


class NltOfferSummary(BaseModel):
    brand: str

    dealer_id: str

    duration_months: Literal[24, 36, 48]
    """Duration corresponding to the `monthly_canon_from_eur` quote."""

    fuel_type: Literal["electric", "hybrid", "plugin_hybrid", "petrol", "diesel", "lpg", "methane"]

    km_per_year_at_quote: int
    """Km/year corresponding to the `monthly_canon_from_eur` quote."""

    model: str

    monthly_canon_from_eur: float
    """
    Lowest displayed monthly canon across all duration / km / down-payment
    combinations for this dealer.
    """

    offer_id: str

    segment: Literal["A", "B", "C", "D", "E", "SUV", "VAN"]

    canonical_url: Optional[str] = None
    """Consumer-facing URL on the dealer's public site."""

    has_promo: Optional[bool] = None

    image_url: Optional[str] = None

    trim: Optional[str] = None
