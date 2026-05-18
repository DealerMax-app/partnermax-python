# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["KeyIssueResponse"]


class KeyIssueResponse(BaseModel):
    """One-time response for ``POST /v1/keys/issue``.

    The ``key`` field is plaintext and is never retrievable again. Callers
    must persist it immediately on receipt.
    """

    created_at: datetime

    expires_at: Optional[datetime] = None

    key: str
    """Plaintext key material. Returned ONCE — never retrievable again."""

    key_id: str

    key_prefix: str

    label: str
