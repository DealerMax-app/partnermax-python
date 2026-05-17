# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .nlt_offer_summary import NltOfferSummary

__all__ = ["OfferListResponse"]


class OfferListResponse(BaseModel):
    data: List[NltOfferSummary]

    has_more: bool

    next_cursor: Optional[str] = None
