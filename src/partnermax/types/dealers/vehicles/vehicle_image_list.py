# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .vehicle_image import VehicleImage

__all__ = ["VehicleImageList"]


class VehicleImageList(BaseModel):
    """All photos attached to a single vehicle, ordered by ``position``.

    No pagination — a vehicle is capped at
    ``VEHICLE_IMAGE_MAX_PER_VEHICLE`` photos by contract, so the full list
    always fits in one response.
    """

    data: List[VehicleImage]
