# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DealerCreateParams"]


class DealerCreateParams(TypedDict, total=False):
    external_dealer_id: Required[str]
    """Partner-owned opaque dealer id.

    This becomes the dealer_id used by vehicle and NLT SDK calls.
    """

    activate: bool
    """When true, the dealer can immediately receive vehicle/NLT operations.

    When false, create the registry row but keep it suspended until activated.
    """

    metadata: Dict[str, Union[str, float, bool, None]]
    """Optional scalar partner-side correlation metadata."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
