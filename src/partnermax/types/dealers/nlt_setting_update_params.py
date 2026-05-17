# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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

    image_mode: Required[Literal["branded", "scenario_locked", "scenario_seasonal"]]

    currency: Literal["EUR"]

    image_scenario_locked: Optional[Literal["mediterraneo", "cortina", "milano", "showroom"]]
    """Required when `image_mode='scenario_locked'`; must be null otherwise."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
