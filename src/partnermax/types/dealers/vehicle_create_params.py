# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VehicleCreateParams"]


class VehicleCreateParams(TypedDict, total=False):
    certified_km: Required[int]
    """Certified odometer reading at intake, in kilometres."""

    motornet_code: Required[str]
    """Motornet UNI code identifying the exact vehicle configuration.

    Must exist in the DealerMAX auto/VCOM catalogue at submission time; otherwise
    the call returns 422 `motornet_code_not_in_catalogue`. Partners may send a code
    from their own Motornet agreement or use the paid control-plane targa/VIN
    resolver before creating the vehicle.
    """

    plate: Required[str]
    """Italian licence plate.

    Uppercased server-side. UNIQUE across the network for active vehicles; reusable
    once the previous holder withdraws the vehicle from sale.
    """

    registration_year: Required[int]
    """Year of first registration. Upper bound is current year + 1."""

    alloy_wheel_size: Optional[int]

    base_color: Optional[str]

    co2_emissions_g_km_override: Optional[float]

    color: Optional[str]

    cost_price_eur: Optional[float]

    damage_repaired: Optional[bool]
    """Tri-state repaired-damage declaration: true=yes, false=no, null=unknown."""

    description: str
    """Partner-supplied long description. Surfaced on the dealer site detail page."""

    double_keys_available: bool

    enabled_channels: List[Literal["rewind", "nos"]]
    """Publication channels enabled for this vehicle. Default is ['rewind']."""

    extended_warranty_enabled: bool

    extended_warranty_months: Optional[int]

    fuel_type_override: Optional[str]

    inspection_due_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    is_visible: bool
    """Soft-publish flag.

    When false the row exists in stock but is excluded from consumer-facing AI
    surfaces.
    """

    last_inspection_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    last_inspection_km: Optional[int]

    last_service_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    last_service_km: Optional[int]

    last_service_notes: Optional[str]

    notes: Optional[str]
    """Free-form short notes for partner-facing vehicle detail views."""

    ownership_transfer_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    power_kw_override: Optional[int]

    previous_owner_count: Optional[int]

    property_tax_due_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    registration_month: Optional[int]
    """Month of registration (1–12)."""

    sale_price_eur: Optional[float]
    """Public REWIND sale price in EUR.

    Required when enabled_channels contains 'rewind'; optional/0 for NOS-only
    vehicles.
    """

    service_history_available: bool
    """Dealer-declared certified service-history availability."""

    trim_alias: Optional[str]

    vat_displayed: bool
    """
    If true the public price is displayed VAT-exposed (B2B); otherwise VAT-inclusive
    (B2C).
    """

    vehicle_damaged: Optional[bool]
    """Tri-state damage declaration: true=yes, false=no, null=unknown."""

    vin: Optional[str]
    """ISO 3779 vehicle identification number. Optional but strongly recommended."""

    wltp_consumption_combined_l_100km: Optional[float]

    wltp_consumption_extraurban_l_100km: Optional[float]

    wltp_consumption_urban_l_100km: Optional[float]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
