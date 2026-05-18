# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VehicleUpdateParams"]


class VehicleUpdateParams(TypedDict, total=False):
    dealer_id: Required[str]

    alloy_wheel_size: Optional[int]

    certified_km: Optional[int]

    color: Optional[str]

    description: Optional[str]

    extended_warranty_enabled: Optional[bool]

    extended_warranty_months: Optional[int]

    is_for_sale: Optional[bool]

    is_visible: Optional[bool]

    notes: Optional[str]

    registration_month: Optional[int]

    sale_price_eur: Optional[float]

    vat_displayed: Optional[bool]

    vehicle_damaged: Optional[bool]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
