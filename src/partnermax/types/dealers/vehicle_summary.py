# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VehicleSummary"]


class VehicleSummary(BaseModel):
    """Compact vehicle payload for list endpoints.

    Catalogue fields (`brand`, `model`, `trim`, `fuel_type`) are derived from
    `mnet_dettagli` at read time. Italian raw labels are surfaced verbatim —
    same convention as NLT (`apimax`-aligned).
    """

    certified_km: int

    created_at: datetime

    dealer_id: str

    is_for_sale: bool

    is_visible: bool

    motornet_code: str

    plate: str

    registration_year: int

    sale_price_eur: float

    vehicle_id: str

    brand: Optional[str] = None

    color: Optional[str] = None

    fuel_type: Optional[str] = None

    model: Optional[str] = None

    trim: Optional[str] = None
