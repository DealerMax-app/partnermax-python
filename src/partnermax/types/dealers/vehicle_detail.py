# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime

from ..._models import BaseModel

__all__ = ["VehicleDetail"]


class VehicleDetail(BaseModel):
    """Full vehicle resource.

    Returned by `GET /v1/dealers/{id}/vehicles/{id}`,
    `POST /v1/dealers/{id}/vehicles`, and `PATCH /v1/dealers/{id}/vehicles/{id}`.

    `technical_details` carries the flat Motornet specs dict (Italian column
    names as keys: `cilindrata`, `kw`, `hp`, `lunghezza`, `consumo_medio`,
    `emissioni_co2`, etc.). Same shape conventions as `NltOfferDetail`
    (`feedback_partnermax_field_naming_us_english`: field names are
    English snake_case, raw catalogue values stay verbatim).
    """

    certified_km: int

    cost_price_eur: float

    created_at: datetime

    dealer_id: str

    description: str

    extended_warranty_enabled: bool

    is_for_sale: bool

    is_visible: bool

    last_modified_at: datetime

    motornet_code: str

    partner_id: str

    plate: str

    registration_year: int

    sale_price_eur: float

    vat_displayed: bool

    vehicle_damaged: bool

    vehicle_id: str

    alloy_wheel_size: Optional[int] = None

    brand: Optional[str] = None

    color: Optional[str] = None

    extended_warranty_months: Optional[int] = None

    fuel_type: Optional[str] = None

    image_urls: Optional[List[str]] = None
    """Vehicle photos. Empty in v1 (media upload ships in v1.2)."""

    inspection_expiry_date: Optional[date] = None

    last_service_date: Optional[date] = None

    last_service_km: Optional[int] = None

    last_service_notes: Optional[str] = None

    model: Optional[str] = None

    notes: Optional[str] = None

    previous_owner_count: Optional[int] = None

    previous_ownership_transfer_date: Optional[date] = None

    registration_month: Optional[int] = None

    road_tax_expiry_date: Optional[date] = None

    technical_details: Optional[Dict[str, object]] = None
    """
    Flat dict of every non-null `mnet_dettagli_usato` column for this
    `motornet_code`. Keys stay in Italian because they are raw SQL column names;
    native units preserved (mm, kg, kW, CV, g/km, etc.).
    """

    trim: Optional[str] = None

    vin: Optional[str] = None
