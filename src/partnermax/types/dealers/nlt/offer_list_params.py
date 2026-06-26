# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["OfferListParams"]


class OfferListParams(TypedDict, total=False):
    brand: Optional[str]

    canone_max_eur: Optional[int]

    cursor: Optional[str]

    duration_months: Optional[int]

    fuel_type: Optional[str]

    km_per_year: Optional[int]

    limit: int

    segment: Optional[str]

    vehicle_type: Optional[str]
    """
    Macro discriminator: 'auto' (passenger vehicles) or 'vcom' (light commercial ≤35
    q.li: vans, panel trucks, multispace, pickups, minibuses). Omit to return the
    mixed catalog.
    """
