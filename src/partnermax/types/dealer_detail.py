# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DealerDetail", "IndexedInSurfaces"]


class IndexedInSurfaces(BaseModel):
    """Per-surface AI indexing state.

    All values may be ``false`` immediately
    after provisioning; reconciliation by ``azurenet-engine`` flips them within
    five minutes.
    """

    custom_gpt: Optional[bool] = None

    llms_txt: Optional[bool] = None

    mcp: Optional[bool] = None

    nlweb: Optional[bool] = None


class DealerDetail(BaseModel):
    """Full dealer payload used by single-resource and write endpoints."""

    address: str

    business_name: str

    city: str

    contact_email: str

    created_at: datetime

    dealer_id: str

    nlt_enabled: bool

    partner_id: str

    postal_code: str

    primary_domain: str

    province_code: str

    status: Literal["active", "inactive", "deleted"]

    vat_number: str

    contact_phone: Optional[str] = None

    indexed_in_surfaces: Optional[IndexedInSurfaces] = None
    """Per-surface AI indexing state.

    All values may be `false` immediately after provisioning; reconciliation by
    `azurenet-engine` flips them within five minutes.
    """

    last_active_at: Optional[datetime] = None

    metadata: Optional[Dict[str, str]] = None

    nlt_settings: Optional[Dict[str, object]] = None
