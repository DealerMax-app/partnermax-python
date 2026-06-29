# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["AccessoryUpdateParams"]


class AccessoryUpdateParams(TypedDict, total=False):
    dealer_id: Required[str]

    alloy_wheel_size: Optional[int]

    equipment_ids: SequenceNotStr[str]

    optional_ids: SequenceNotStr[str]

    package_ids: SequenceNotStr[str]
