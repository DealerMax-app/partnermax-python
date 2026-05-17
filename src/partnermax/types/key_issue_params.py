# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["KeyIssueParams"]


class KeyIssueParams(TypedDict, total=False):
    label: Required[str]
    """Human-readable identifier for this key, used for safe logging."""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional expiry timestamp. Null = never expires until revoked."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
