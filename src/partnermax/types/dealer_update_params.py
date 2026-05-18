# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DealerUpdateParams"]


class DealerUpdateParams(TypedDict, total=False):
    address: Optional[str]

    business_name: Optional[str]

    city: Optional[str]

    contact_email: Optional[str]

    contact_phone: Optional[str]

    metadata: Optional[Dict[str, str]]

    postal_code: Optional[str]

    province_code: Optional[str]

    status: Optional[Literal["active", "inactive"]]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
