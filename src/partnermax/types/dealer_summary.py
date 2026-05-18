# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DealerSummary"]


class DealerSummary(BaseModel):
    """Compact dealer payload used by list endpoints."""

    business_name: str

    created_at: datetime

    dealer_id: str

    nlt_enabled: bool

    primary_domain: str

    province_code: str

    status: Literal["active", "inactive", "deleted"]

    last_active_at: Optional[datetime] = None
