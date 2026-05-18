# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VehicleUpdateParams"]


class VehicleUpdateParams(TypedDict, total=False):
    dealer_id: Required[str]

    alloy_wheel_size: Optional[int]

    certified_km: Optional[int]

    color: Optional[str]

    cost_price_eur: Optional[float]

    description: Optional[str]

    extended_warranty_enabled: Optional[bool]

    extended_warranty_months: Optional[int]

    inspection_expiry_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    is_for_sale: Optional[bool]

    is_visible: Optional[bool]

    last_service_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    last_service_km: Optional[int]

    last_service_notes: Optional[str]

    notes: Optional[str]

    previous_owner_count: Optional[int]

    previous_ownership_transfer_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    registration_month: Optional[int]

    road_tax_expiry_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    sale_price_eur: Optional[float]

    vat_displayed: Optional[bool]

    vehicle_damaged: Optional[bool]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
