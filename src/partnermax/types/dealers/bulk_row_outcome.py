# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .vehicle_detail import VehicleDetail

__all__ = ["BulkRowOutcome"]


class BulkRowOutcome(BaseModel):
    """Per-row result inside ``BulkCreateVehiclesResponse``.

    On success ``vehicle`` is populated (full ``VehicleDetail``) and
    ``error_code``/``error_message`` are null. On failure ``vehicle`` is
    null and ``error_code``/``error_message`` carry the same code that
    the corresponding single-create POST would have raised
    (e.g. ``motornet_code_not_in_catalogue``, ``vehicle_plate_already_registered``,
    ``validation_error``).
    """

    row_index: int
    """Zero-based index of the row in the request `vehicles[]` array.

    Stable across retries — the partner can correlate failures back to its own batch
    by this index.
    """

    status: Literal["succeeded", "failed"]

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    vehicle: Optional[VehicleDetail] = None
    """Full vehicle resource.

    Returned by `GET /v1/dealers/{id}/vehicles/{id}`,
    `POST /v1/dealers/{id}/vehicles`, and `PATCH /v1/dealers/{id}/vehicles/{id}`.

    Carries three layers of information:

    - **Partner-supplied** — what the partner posted (`plate`, `description`,
      `sale_price_eur`, etc.).
    - **Catalogue-derived** — `technical_details` is the flat `mnet_dettagli_usato`
      dict (Italian column keys: `cilindrata`, `kw`, `hp`, `lunghezza`,
      `consumo_medio`, `emissioni_co2`, etc.). Same shape conventions as
      `NltOfferDetail` per `feedback_partnermax_field_naming_us_english`.
    - **AI-derived** — `ai_content` carries the editorial output the cross-network
      consumers display (descriptions, highlights, FAQ, SEO meta). `null` until the
      worker has processed the vehicle.

    Fields the partner does NOT see through this surface (because they are
    dealer-internal margin/operations data the partner does not own):
    `cost_price_eur`, `inspection_expiry_date`, `road_tax_expiry_date`,
    `previous_owner_count`, `previous_ownership_transfer_date`, `last_service_*`.
    These exist in the underlying DB tables for the DealerMAX dashboard but are
    intentionally not exposed via the SDK.
    """
