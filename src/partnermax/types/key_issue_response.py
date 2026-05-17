# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["KeyIssueResponse"]


class KeyIssueResponse(BaseModel):
    created_at: datetime

    expires_at: datetime

    key: str
    """Plaintext key material.

    Returned ONCE — never retrievable again. Store securely.
    """

    key_id: str

    key_prefix: str
    """First 8 characters of the key, safe for logging."""

    label: str
