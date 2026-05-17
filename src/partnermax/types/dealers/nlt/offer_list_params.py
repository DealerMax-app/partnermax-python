# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OfferListParams"]


class OfferListParams(TypedDict, total=False):
    brand: str
    """Filter by brand name, case-insensitive (e.g., `Fiat`)."""

    canone_max_eur: int
    """Upper bound on displayed monthly canon (EUR)."""

    cursor: str
    """Opaque pagination cursor."""

    duration_months: Literal[24, 36, 48]

    fuel_type: Literal["electric", "hybrid", "plugin_hybrid", "petrol", "diesel", "lpg", "methane"]

    km_per_year: Literal[10000, 15000, 20000, 25000, 30000, 40000]

    limit: int

    segment: Literal["A", "B", "C", "D", "E", "SUV", "VAN"]
