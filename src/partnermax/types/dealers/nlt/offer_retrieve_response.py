# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .nlt_offer_summary import NltOfferSummary

__all__ = [
    "OfferRetrieveResponse",
    "OfferRetrieveResponseQuotation",
    "OfferRetrieveResponseSpecs",
    "OfferRetrieveResponseDealerCard",
    "OfferRetrieveResponseOptionalAccessory",
]


class OfferRetrieveResponseQuotation(BaseModel):
    down_payment_eur: int
    """Down-payment amount in EUR for this tier (from the dealer's NLT settings)."""

    down_payment_tier: Literal["low", "medium", "high"]

    duration_months: Literal[24, 36, 48]

    km_per_year: Literal[10000, 15000, 20000, 25000, 30000, 40000]

    monthly_canon_eur: float
    """Displayed monthly canon (includes dealer markup + VAT treatment)."""


class OfferRetrieveResponseSpecs(BaseModel):
    co2_g_per_km: Optional[int] = None

    engine_displacement_cc: Optional[int] = None

    height_mm: Optional[int] = None

    length_mm: Optional[int] = None

    power_kw: Optional[float] = None

    transmission: Optional[str] = None

    trunk_litres: Optional[int] = None

    width_mm: Optional[int] = None


class OfferRetrieveResponseDealerCard(BaseModel):
    business_name: Optional[str] = None

    city: Optional[str] = None

    phone: Optional[str] = None

    primary_domain: Optional[str] = None

    province_code: Optional[str] = None


class OfferRetrieveResponseOptionalAccessory(BaseModel):
    label: str

    monthly_canon_delta_eur: float


class OfferRetrieveResponse(NltOfferSummary):
    included_services: List[
        Literal["full_insurance", "maintenance", "road_tax", "tires", "replacement_vehicle", "roadside_assistance"]
    ]

    quotations: List[OfferRetrieveResponseQuotation]
    """All 54 displayed price points (18 base quotations × 3 down-payment tiers)."""

    specs: OfferRetrieveResponseSpecs

    dealer_card: Optional[OfferRetrieveResponseDealerCard] = None

    image_gallery: Optional[List[str]] = None

    optional_accessories: Optional[List[OfferRetrieveResponseOptionalAccessory]] = None
