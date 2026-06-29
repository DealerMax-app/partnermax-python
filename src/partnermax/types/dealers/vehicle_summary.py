# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VehicleSummary"]


class VehicleSummary(BaseModel):
    """Compact vehicle payload for list endpoints.

    Catalogue fields (`brand`, `model`, `trim`, `fuel_type`) are derived from
    DealerMAX's licensed Motornet-backed catalogue at read time. Italian raw
    labels are surfaced verbatim so partner clients see the same vocabulary as
    consumer-facing DealerMAX surfaces.
    """

    certified_km: int

    created_at: datetime

    dealer_id: str

    enabled_channels: List[Literal["rewind", "nos"]]

    is_visible: bool

    last_modified_at: datetime

    motornet_code: str

    plate: str

    registration_year: int

    sale_price_eur: float

    vat_displayed: bool

    vehicle_id: str

    ai_short: Optional[str] = None

    ai_tagline: Optional[str] = None

    brand: Optional[str] = None

    color: Optional[str] = None

    cost_price_eur: Optional[float] = None

    cover_image_url: Optional[str] = None

    damage_repaired: Optional[bool] = None

    deleted_at: Optional[datetime] = None

    fuel_type: Optional[str] = None

    image_count: Optional[int] = None

    model: Optional[str] = None

    registration_month: Optional[int] = None

    trim: Optional[str] = None

    trim_alias: Optional[str] = None

    vehicle_damaged: Optional[bool] = None
