# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["KeyListResponse", "Data"]


class Data(BaseModel):
    """Metadata-only representation of an API key. Safe to return on list calls."""

    created_at: datetime

    expires_at: Optional[datetime] = None

    is_active: bool

    key_id: str

    key_prefix: str

    label: str

    last_used_at: Optional[datetime] = None


class KeyListResponse(BaseModel):
    """Response envelope for ``GET /v1/keys``."""

    data: List[Data]
