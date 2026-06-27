# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .down_payment_tiers import DownPaymentTiers

__all__ = ["NltSettings"]


class NltSettings(BaseModel):
    """Response model for GET / PATCH /v1/dealers/{id}/nlt-settings.

    Note: there is no `vat_treatment` field — VAT is a property of the
    offer, not of the dealer. The offer detail returns the VAT treatment
    per row instead.
    """

    agency_markup_percent: float

    dealer_id: str

    down_payment_tiers: DownPaymentTiers
    """Three down-payment scenarios (basso / medio / alto).

    No strict-ascending validation: the final EUR amount depends on the offer's list
    price (`tier.percent_of_list / 100 * listino_imponibile + tier.fixed_eur`), so a
    tier that looks larger by % can produce a smaller EUR on cheap vehicles. Label
    semantics (low/medium/high) are advisory — DealerMAX UI treats the 3 positions
    as opaque slots ordered by intent.
    """

    effective_from: datetime

    currency: Optional[Literal["EUR"]] = None

    image_mode: Optional[Literal["branded", "scenario_locked", "scenario_seasonal"]] = None

    image_scenario_locked: Optional[Literal["mediterraneo", "cortina", "milano", "showroom", "building"]] = None
