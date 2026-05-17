# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .dealer_summary import DealerSummary
from .dealers.nlt_settings import NltSettings

__all__ = ["DealerDetail", "DealerDetailIndexedInSurfaces"]


class DealerDetailIndexedInSurfaces(BaseModel):
    """Live indexing state for each cross-network AI surface.

    Values may be `false` immediately after provisioning; reaches `true` within five minutes.
    """

    custom_gpt: Optional[bool] = None

    llms_txt: Optional[bool] = None

    mcp: Optional[bool] = None

    nlweb: Optional[bool] = None


class DealerDetail(DealerSummary):
    contact_email: Optional[str] = None

    contact_phone: Optional[str] = None

    indexed_in_surfaces: Optional[DealerDetailIndexedInSurfaces] = None
    """Live indexing state for each cross-network AI surface.

    Values may be `false` immediately after provisioning; reaches `true` within five
    minutes.
    """

    metadata: Optional[Dict[str, str]] = None

    nlt_settings: Optional[NltSettings] = None

    partner_id: Optional[str] = None

    postal_code: Optional[str] = None

    vat_number: Optional[str] = None
