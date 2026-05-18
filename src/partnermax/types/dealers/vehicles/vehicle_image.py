# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["VehicleImage"]


class VehicleImage(BaseModel):
    """A single photo attached to a used vehicle.

    Returned by ``POST .../images`` (single upload) and as elements of
    ``VehicleImageList.data`` (list endpoint). ``position == 1`` is the
    cover photo by convention; ``is_cover`` mirrors it for readability.

    The ``image_url`` is the raw Supabase public URL. The cross-network
    AI surfaces (MCP search_vehicles, Custom GPT, NLWeb) embed a CDN
    AVIF-transformed variant; partners that render this URL themselves
    can apply Supabase's render-service query parameters
    (`?format=avif&quality=70&resize=contain`) for the same treatment.
    """

    created_at: datetime

    image_id: str
    """Opaque image identifier in the form `img_<uuid>`.

    Use as the path parameter on `DELETE` to remove the photo.
    """

    image_url: str
    """Public Supabase Storage URL of the original upload.

    Stable for the lifetime of the photo.
    """

    is_cover: bool
    """True when `position == 1`.

    Surfaced as a separate field so partners can branch on cover handling without
    doing integer arithmetic on positions.
    """

    position: int
    """1-based ordinal among this vehicle's photos.

    `position=1` is the cover that appears on every AI surface; subsequent positions
    are gallery photos shown on the dealer site detail page.
    """
