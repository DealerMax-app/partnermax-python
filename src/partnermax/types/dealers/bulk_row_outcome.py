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
    - **Catalogue-derived** — `technical_details` is a flat dictionary of
      Motornet-backed technical attributes using Italian domain labels such as
      `cilindrata`, `kw`, `hp`, `lunghezza`, `consumo_medio`, and `emissioni_co2`.
    - **AI-derived** — `ai_content` carries the editorial output the cross-network
      consumers display (descriptions, highlights, FAQ, SEO meta). `null` until the
      worker has processed the vehicle.

    Dealer-internal margin and operations data remains outside this SDK surface;
    partners receive only the inventory, commercial, catalogue, media, and
    AI-derived fields needed to publish the vehicle.
    """
