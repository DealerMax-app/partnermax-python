# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DownPaymentTiersParam"]


class DownPaymentTiersParam(TypedDict, total=False):
    """
    Three down-payment scenarios shown to consumers, in strictly ascending order (low < medium < high).
    """

    high_eur: Required[int]
    """Highest down-payment scenario."""

    low_eur: Required[int]
    """Lowest down-payment scenario, in whole EUR."""

    medium_eur: Required[int]
    """Middle down-payment scenario."""
