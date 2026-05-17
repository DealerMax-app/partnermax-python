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

    fuel_type: str
    """Raw Italian label (case-insensitive ILIKE match).

    Examples: "Benzina", "Diesel", "Ibrido benzina", "Ibrido diesel", "Elettrica",
    "GPL", "Metano".
    """

    km_per_year: Literal[10000, 15000, 20000, 25000, 30000, 40000]

    limit: int

    segment: str
    """Raw Italian label (case-insensitive ILIKE substring match).

    Examples: "SUV piccoli", "SUV medi", "Superiori", "Medie", "Utilitarie".
    """
