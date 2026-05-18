# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["NltOfferSummary"]


class NltOfferSummary(BaseModel):
    """Single row in the offers list. Pricing is dealer-aware.

    Field names: American English snake_case. Values: Italian raw,
    apimax-aligned (`fuel_type: "Benzina"`, `segment: "SUV piccoli"`).
    No enum normalization — apimax labels are surfaced verbatim, exactly
    as the detail endpoint does, so the partner client sees the same
    string in both listing and detail.
    """

    brand: str

    dealer_id: str

    duration_months: int

    km_per_year_at_quote: int

    model: str

    monthly_canon_from_eur: float

    offer_id: str

    slug: str

    vat_treatment: Literal["private", "business"]

    canonical_url: Optional[str] = None

    fuel_type: Optional[str] = None

    has_promo: Optional[bool] = None

    image_url: Optional[str] = None

    segment: Optional[str] = None

    trim: Optional[str] = None
