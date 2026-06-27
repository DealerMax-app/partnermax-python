# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VehicleBulkParams", "Vehicle"]


class VehicleBulkParams(TypedDict, total=False):
    vehicles: Required[Iterable[Vehicle]]
    """Array of vehicles to create.

    Between 1 and 100 rows per call. For larger imports, the partner is expected to
    chunk client-side (e.g. 50 calls of 100 rows each for a 5 000-vehicle
    migration).
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Vehicle(TypedDict, total=False):
    """Request body for vehicle provisioning.

    The partner sends a small, vehicle-specific payload. All technical specs
    (brand, model, trim, fuel type, displacement, dimensions, CO2, etc.) are
    derived server-side from DealerMAX's licensed Motornet-backed catalogue —
    the partner never types them.

    Fields immutable after creation: `motornet_code`, `plate`, `vin`. Other
    fields may be updated via PATCH.
    """

    certified_km: Required[int]
    """Certified odometer reading at intake, in kilometres."""

    motornet_code: Required[str]
    """Motornet UNI code identifying the exact vehicle configuration.

    Must exist in the used-vehicle catalogue at submission time; otherwise the call
    returns 422 `motornet_code_not_in_catalogue`. Partners may send a code from
    their own Motornet agreement or use the paid control-plane targa/VIN resolver
    before creating the vehicle.
    """

    plate: Required[str]
    """Italian licence plate.

    Uppercased server-side. UNIQUE across the network for active vehicles; reusable
    once the previous holder withdraws the vehicle from sale.
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

    is_for_sale: bool
    """When false the vehicle remains in stock but is not offered for sale."""

    is_visible: bool
    """Soft-publish flag.

    When false the row exists in stock but is excluded from consumer-facing AI
    surfaces.
    """

    notes: Optional[str]
    """Free-form short notes for partner-facing vehicle detail views."""

    registration_month: Optional[int]
    """Month of registration (1–12)."""

    vat_displayed: bool
    """
    If true the public price is displayed VAT-exposed (B2B); otherwise VAT-inclusive
    (B2C).
    """

    vehicle_damaged: bool

    vin: Optional[str]
    """ISO 3779 vehicle identification number. Optional but strongly recommended."""
