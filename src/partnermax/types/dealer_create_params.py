# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DealerCreateParams"]


class DealerCreateParams(TypedDict, total=False):
    business_name: Required[str]

    contact_email: Required[str]

    postal_code: Required[str]
    """Italian 5-digit postal code."""

    primary_domain: Required[str]
    """Root domain of the dealer's public website."""

    province_code: Required[str]
    """Italian two-letter province code, e.g., `MI`, `RM`, `TO`."""

    vat_number: Required[str]
    """Italian VAT number, 11 digits prefixed with `IT`."""

    activate: bool
    """
    If false, dealer is created in inactive state and does not appear in AI surfaces
    until activated.
    """

    contact_phone: str
    """E.164 format recommended."""

    metadata: Dict[str, str]
    """Free-form partner-supplied key-value pairs, max 16 keys, values max 500 chars."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
