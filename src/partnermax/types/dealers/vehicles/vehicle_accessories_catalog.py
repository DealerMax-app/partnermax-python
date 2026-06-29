# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .vehicle_accessory_item import VehicleAccessoryItem

__all__ = ["VehicleAccessoriesCatalog"]


class VehicleAccessoriesCatalog(BaseModel):
    """Per-vehicle accessories catalog plus current selections."""

    alloy_wheel_size: Optional[int] = None

    equipment: Optional[List[VehicleAccessoryItem]] = None

    optionals: Optional[List[VehicleAccessoryItem]] = None

    packages: Optional[List[VehicleAccessoryItem]] = None

    series: Optional[List[VehicleAccessoryItem]] = None
