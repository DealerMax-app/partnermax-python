# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DealerListParams"]


class DealerListParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor from a previous response's `next_cursor`."""

    limit: int
    """Maximum number of items to return."""

    status: Literal["active", "inactive", "all"]
    """Filter by dealer status."""
