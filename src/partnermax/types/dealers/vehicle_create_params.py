# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VehicleCreateParams"]


class VehicleCreateParams(TypedDict, total=False):
    certified_km: Required[int]
    """Certified odometer reading at intake, in kilometres."""

    cost_price_eur: Required[float]
    """Cost basis to the dealer in EUR (partner/dealer internal).

    Not surfaced on consumer-facing AI surfaces; used by dealer reporting and margin
    analytics only.
    """

    motornet_code: Required[str]
    """Motornet UNI code identifying the exact vehicle configuration.

    Must exist in `mnet_dettagli_usato` at submission time; otherwise the call
    returns 422 `motornet_code_not_in_catalogue`. The partner is expected to source
    this from its own DMS; partnermax does not expose a plate→code lookup.
    """

    plate: Required[str]
    """Italian licence plate.

    Uppercased server-side. UNIQUE across the network for active vehicles
    (`visibile=true AND venduto_il IS NULL`); reusable once the previous holder
    sells/hides the row.
    """

    registration_year: Required[int]
    """Year of first registration. Upper bound is current year + 1."""

    sale_price_eur: Required[float]
    """Public sale price in EUR.

    Surfaced on MCP / Custom GPT / NLWeb and on the dealer's site JSON-LD
    `Offer.price`.
    """

    alloy_wheel_size: Optional[int]

    color: Optional[str]

    description: str
    """Partner-supplied long description. Surfaced on the dealer site detail page."""

    extended_warranty_enabled: bool

    extended_warranty_months: Optional[int]

    inspection_expiry_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    is_for_sale: bool
    """Maps to `azlease_usatoauto.is_vendita_enabled`.

    When false the row is in stock but not offered for sale.
    """

    is_visible: bool
    """Soft-publish flag.

    When false the row exists in stock but is excluded from consumer-facing AI
    surfaces. Maps to `azlease_usatoin.visibile`.
    """

    last_service_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    last_service_km: Optional[int]

    last_service_notes: Optional[str]

    notes: Optional[str]
    """Free-form short notes; surfaced as `mnet_dettagli.precisazioni`-style."""

    previous_owner_count: Optional[int]

    previous_ownership_transfer_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Date of the most recent ownership transfer, if known."""

    registration_month: Optional[int]
    """Month of registration (1–12)."""

    road_tax_expiry_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    vat_displayed: bool
    """
    If true the public price is displayed VAT-exposed (B2B); otherwise VAT-inclusive
    (B2C).
    """

    vehicle_damaged: bool

    vin: Optional[str]
    """ISO 3779 vehicle identification number. Optional but strongly recommended."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
