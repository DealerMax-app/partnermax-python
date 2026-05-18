# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .vehicle_summary import VehicleSummary

__all__ = ["VehicleList"]


class VehicleList(BaseModel):
    """Cursor-paginated list of vehicle summaries."""

    data: List[VehicleSummary]

    has_more: bool

    next_cursor: Optional[str] = None
