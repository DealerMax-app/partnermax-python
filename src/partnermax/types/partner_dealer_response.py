# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PartnerDealerResponse"]


class PartnerDealerResponse(BaseModel):
    """Partner dealer registry response.

    Use dealer_id as the path parameter for vehicle and NLT SDK calls.
    """

    created_at: datetime

    dealer_id: str
    """The partner-supplied external dealer id."""

    partner_id: str

    public_surfaces_enabled: bool

    status: Literal["active", "suspended", "revoked"]

    updated_at: datetime

    created: Optional[bool] = None
    """True only when this request inserted the registry row."""
