# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DealerCreateParams"]


class DealerCreateParams(TypedDict, total=False):
    address: Required[str]

    business_name: Required[str]

    city: Required[str]

    contact_email: Required[str]

    contact_phone: Required[str]

    postal_code: Required[str]

    primary_domain: Required[str]

    province_code: Required[str]

    vat_number: Required[str]

    activate: bool

    metadata: Dict[str, str]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
