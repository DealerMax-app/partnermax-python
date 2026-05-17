# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DownPaymentTiers"]


class DownPaymentTiers(BaseModel):
    """
    Three down-payment scenarios shown to consumers, in strictly ascending order (low < medium < high).
    """

    high_eur: int
    """Highest down-payment scenario."""

    low_eur: int
    """Lowest down-payment scenario, in whole EUR."""

    medium_eur: int
    """Middle down-payment scenario."""
