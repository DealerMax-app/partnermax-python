# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .dealer_summary import DealerSummary

__all__ = ["DealerListResponse"]


class DealerListResponse(BaseModel):
    data: List[DealerSummary]

    has_more: bool

    next_cursor: Optional[str] = None
    """Pass as `cursor` to retrieve next page; null when no more pages."""
