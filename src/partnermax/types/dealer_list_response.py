# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .dealer_summary import DealerSummary

__all__ = ["DealerListResponse"]


class DealerListResponse(BaseModel):
    """Response envelope for ``GET /v1/dealers``."""

    data: List[DealerSummary]

    has_more: bool

    next_cursor: Optional[str] = None
