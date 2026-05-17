# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["KeyListResponse", "Data"]


class Data(BaseModel):
    created_at: datetime

    is_active: bool

    key_id: str

    key_prefix: str

    label: str

    expires_at: Optional[datetime] = None

    last_used_at: Optional[datetime] = None


class KeyListResponse(BaseModel):
    data: List[Data]
