# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["VehicleListParams"]


class VehicleListParams(TypedDict, total=False):
    cursor: Optional[str]

    enabled_channel: Optional[Literal["rewind", "nos"]]
    """Filter vehicles enabled on one publication channel: rewind or nos."""

    include_deleted: bool
    """If true, soft-deleted rows (`venduto_il` populated) are also returned.

    Default false — listings hide soft-deleted vehicles.
    """

    is_visible: Optional[bool]
    """Filter on the visibility flag."""

    limit: int
