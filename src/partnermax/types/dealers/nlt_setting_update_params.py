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
    """Three down-payment scenarios (basso / medio / alto).

    No strict-ascending validation: the final EUR amount depends on the offer's list
    price (`tier.percent_of_list / 100 * listino_imponibile + tier.fixed_eur`), so a
    tier that looks larger by % can produce a smaller EUR on cheap vehicles. Label
    semantics (low/medium/high) are advisory — DealerMAX UI treats the 3 positions
    as opaque slots ordered by intent.
    """

    currency: Literal["EUR"]

    image_mode: Literal["branded", "scenario_locked", "scenario_seasonal"]

    image_scenario_locked: Optional[Literal["mediterraneo", "cortina", "milano", "showroom", "building"]]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
