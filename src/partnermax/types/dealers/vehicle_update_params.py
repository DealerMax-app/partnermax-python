# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VehicleUpdateParams"]


class VehicleUpdateParams(TypedDict, total=False):
    dealer_id: Required[str]

    alloy_wheel_size: Optional[int]

    base_color: Optional[str]

    certified_km: Optional[int]

    co2_emissions_g_km_override: Optional[float]

    color: Optional[str]

    cost_price_eur: Optional[float]

    damage_repaired: Optional[bool]

    description: Optional[str]

    double_keys_available: Optional[bool]

    enabled_channels: Optional[List[Literal["rewind", "nos"]]]

    extended_warranty_enabled: Optional[bool]

    extended_warranty_months: Optional[int]

    fuel_type_override: Optional[str]

    inspection_due_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    is_visible: Optional[bool]

    last_inspection_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    last_inspection_km: Optional[int]

    last_service_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    last_service_km: Optional[int]

    last_service_notes: Optional[str]

    notes: Optional[str]

    ownership_transfer_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    power_kw_override: Optional[int]

    previous_owner_count: Optional[int]

    property_tax_due_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    registration_month: Optional[int]

    registration_year: Optional[int]

    sale_price_eur: Optional[float]

    service_history_available: Optional[bool]

    trim_alias: Optional[str]

    vat_displayed: Optional[bool]

    vehicle_damaged: Optional[bool]

    vin: Optional[str]

    wltp_consumption_combined_l_100km: Optional[float]

    wltp_consumption_extraurban_l_100km: Optional[float]

    wltp_consumption_urban_l_100km: Optional[float]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
