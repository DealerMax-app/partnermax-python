# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .down_payment_tiers_param import DownPaymentTiersParam

__all__ = ["NltSettingUpdateParams"]


class NltSettingUpdateParams(TypedDict, total=False):
    agency_markup_percent: Required[float]

    down_payment_tiers: Required[DownPaymentTiersParam]
    """
    Three down-payment scenarios shown to consumers, in strictly ascending order
    (low < medium < high).
    """

    vat_treatment: Required[Literal["private", "business"]]

    currency: Literal["EUR"]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
