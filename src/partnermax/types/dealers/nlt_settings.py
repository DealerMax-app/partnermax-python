# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .down_payment_tiers import DownPaymentTiers

__all__ = ["NltSettings"]


class NltSettings(BaseModel):
    """Dealer-level NLT economics.

    VAT treatment is NOT a dealer-level field — it is a property of the offer (see `NltOfferSummary.vat_treatment`).
    """

    agency_markup_percent: float
    """Markup applied on top of the network base canon, in percent. Hard cap at 10%."""

    currency: Literal["EUR"]
    """Only EUR supported in v1."""

    dealer_id: str

    down_payment_tiers: DownPaymentTiers
    """
    Three down-payment scenarios shown to consumers, in strictly ascending order
    (low < medium < high).
    """

    effective_from: datetime
