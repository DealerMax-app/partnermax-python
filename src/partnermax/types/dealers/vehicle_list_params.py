# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VehicleListParams"]


class VehicleListParams(TypedDict, total=False):
    cursor: Optional[str]

    include_deleted: bool
    """If true, soft-deleted rows (`venduto_il` populated) are also returned.

    Default false — listings hide soft-deleted vehicles.
    """

    is_for_sale: Optional[bool]
    """Filter on the sale flag."""

    is_visible: Optional[bool]
    """Filter on the visibility flag."""

    limit: int
