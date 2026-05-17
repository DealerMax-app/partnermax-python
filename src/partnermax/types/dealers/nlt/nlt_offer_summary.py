# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["NltOfferSummary"]


class NltOfferSummary(BaseModel):
    brand: str

    dealer_id: str
    """Dealer id (prefixed `dlr_<n>`)."""

    duration_months: Literal[36, 48, 60]
    """Duration corresponding to the `monthly_canon_from_eur` quote."""

    km_per_year_at_quote: Literal[10000, 15000, 20000, 25000, 30000, 40000]
    """Km/year corresponding to the `monthly_canon_from_eur` quote."""

    model: str

    monthly_canon_from_eur: float
    """
    Lowest displayed monthly canon across all duration / km / down-payment
    combinations for this dealer.
    """

    offer_id: str
    """Numeric `nlt_offerte.id_offerta` as string.

    Use as the path parameter for the detail endpoint.
    """

    slug: str
    """Offer slug used in canonical URLs (`/noleggio-lungo-termine/{slug}`)."""

    vat_treatment: Literal["private", "business"]
    """VAT treatment of this offer (not the dealer).

    `private` → `monthly_canon_from_eur` is VAT-inclusive (×1.22). `business` →
    VAT-exclusive. Sourced from `nlt_offerte.solo_privati`.
    """

    canonical_url: Optional[str] = None
    """
    Consumer-facing URL on the dealer's public site:
    `https://{primary_domain}/noleggio-lungo-termine/{slug}`. Null when the dealer
    has no site row.
    """

    fuel_type: Optional[str] = None
    """Raw Italian label from `nlt_offerte.alimentazione` (e.g.

    "Benzina", "Ibrido diesel"). Apimax-aligned, no enum normalization.
    """

    has_promo: Optional[bool] = None

    image_url: Optional[str] = None

    segment: Optional[str] = None
    """Raw Italian label from `nlt_offerte.segmento` (e.g.

    "SUV piccoli", "Superiori"). Apimax-aligned, no enum normalization.
    """

    trim: Optional[str] = None
