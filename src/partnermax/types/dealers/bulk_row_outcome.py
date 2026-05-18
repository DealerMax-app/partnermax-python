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

    `technical_details` carries the flat Motornet specs dict (Italian column names
    as keys: `cilindrata`, `kw`, `hp`, `lunghezza`, `consumo_medio`,
    `emissioni_co2`, etc.). Same shape conventions as `NltOfferDetail`
    (`feedback_partnermax_field_naming_us_english`: field names are English
    snake_case, raw catalogue values stay verbatim).
    """
