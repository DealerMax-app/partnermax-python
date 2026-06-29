# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["VehicleAccessoryItem"]


class VehicleAccessoryItem(BaseModel):
    """Single accessory/equipment row available for a used vehicle."""

    id: str

    description: str

    category: Optional[str] = None

    code: Optional[str] = None

    group: Optional[str] = None

    price_eur: Optional[float] = None

    selected: Optional[bool] = None
