# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .bulk_row_outcome import BulkRowOutcome

__all__ = ["BulkCreateVehiclesResponse"]


class BulkCreateVehiclesResponse(BaseModel):
    """Response of ``POST /v1/dealers/{dealer_id}/vehicles/bulk``.

    HTTP status is ``207 Multi-Status`` (rather than 201) to make
    partial success explicit at the protocol level. The aggregate
    counters at the top let a partner short-circuit when every row
    succeeded; the ``results`` array carries per-row detail when not.
    """

    failed: int

    results: List[BulkRowOutcome]

    succeeded: int

    total: int
    """Number of rows in the request body."""
