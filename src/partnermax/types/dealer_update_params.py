# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DealerUpdateParams"]


class DealerUpdateParams(TypedDict, total=False):
    business_name: str

    contact_email: str

    contact_phone: str

    metadata: Dict[str, str]

    postal_code: str

    province_code: str

    status: Literal["active", "inactive"]
    """Toggle activation.

    Inactive dealers are removed from AI surfaces within 5 minutes.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
