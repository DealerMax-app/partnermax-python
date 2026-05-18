# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = [
    "OfferRetrieveResponse",
    "AvailableAddons",
    "AvailableAddonsReplacementVehicle",
    "AvailableAddonsTires",
    "DownPaymentScenariosEur",
    "DownPaymentScenariosLabels",
    "Faq",
    "Gallery",
    "IncludedAccessory",
    "IncludedService",
    "NetworkOffer",
    "Quotation",
    "Tag",
]


class AvailableAddonsReplacementVehicle(BaseModel):
    """
    Replacement-vehicle add-on lookup (apimax: `addons_disponibili.auto_sostitutiva`).

    Always category B (utilitaria) per founder decision — the spoken
    "average customer" segment.
    """

    category_description: str

    default_category: str

    monthly_cost_eur: float


class AvailableAddonsTires(BaseModel):
    """Tyre-replacement add-on lookup (apimax: `addons_disponibili.pneumatici`).

    Populated when `mnet_dettagli.pneumatici_anteriori` matches `R\\dd+` and
    a row exists in `nlt_pneumatici` for that diameter. Null otherwise.
    Replacement rule (founder decision 2026-05-12): 1 set of 4 tyres
    every 30 000 km, rounded up.
    """

    diameter_in: int

    replacement_rule: str

    set_cost_eur: float


class AvailableAddons(BaseModel):
    """Container for optional add-ons (apimax: `addons_disponibili`)."""

    replacement_vehicle: Optional[AvailableAddonsReplacementVehicle] = None
    """
    Replacement-vehicle add-on lookup (apimax:
    `addons_disponibili.auto_sostitutiva`).

    Always category B (utilitaria) per founder decision — the spoken "average
    customer" segment.
    """

    tires: Optional[AvailableAddonsTires] = None
    """Tyre-replacement add-on lookup (apimax: `addons_disponibili.pneumatici`).

    Populated when `mnet_dettagli.pneumatici_anteriori` matches `R\\dd+` and a row
    exists in `nlt_pneumatici` for that diameter. Null otherwise. Replacement rule
    (founder decision 2026-05-12): 1 set of 4 tyres every 30 000 km, rounded up.
    """


class DownPaymentScenariosEur(BaseModel):
    """Three down-payment scenarios in EUR (whole amounts).

    apimax: `anticipo_scenari_eur` (keys remapped to American English
    snake_case for partnermax SDK: `zero/medium/standard`).
    """

    medium: int

    standard: int

    zero: int


class DownPaymentScenariosLabels(BaseModel):
    """Italian labels paired 1:1 with `NltDownPaymentScenariosEur`.

    apimax: `anticipo_scenari_labels` — used by Custom GPT to render the
    three options in conversation. Values stay in Italian raw
    ("Senza anticipo" / "Anticipo 12,5%" / "Anticipo 25%").
    """

    medium: str

    standard: str

    zero: str


class Faq(BaseModel):
    """One Italian Q&A entry derived per-offer.

    apimax: `build_offer_faqs` in `seo_engine/nlt_faq_builder.py` —
    generates up to ~11 Q&A pairs (dimensions, fuel, transmission, CO2,
    monthly canon at preset combo, available durations, VAT inclusion,
    down-payment tiers, etc.). Partnermax surfaces them all, 1:1.
    """

    answer: str

    question: str


class Gallery(BaseModel):
    """One image in the offer gallery (apimax: `gallery[]`)."""

    is_cover: bool

    url: str


class IncludedAccessory(BaseModel):
    """One accessory bundled with the offer (apimax: `accessori_inclusi[]`)."""

    code: str

    description: str

    extra_price_eur: float


class IncludedService(BaseModel):
    """One NLT service normally included in the canone.

    apimax: `_get_services_included` (`nlt_resolver.py:719`). Source is
    the global `nlt_services` table (active rows only). Same set of
    services across the network (Assicurazione RCA / Kasco /
    Incendio-Furto, Manutenzione, Assistenza Stradale, Bollo,
    Pneumatici, Veicolo in anticipo, Vettura sostitutiva). Not per-offer.
    """

    name: str

    description: Optional[str] = None


class NetworkOffer(BaseModel):
    """One network dealer's quote for this offer (apimax: `network_offers[]`).

    Sorted by `min_monthly_canon_eur ASC`. In partnermax this list is
    scoped to dealers owned by the calling partner
    (`utenti.parent_id = partner.user_id`) — same shape as the apimax
    cross-network list, partner-scoped to avoid data leakage.
    """

    dealer_id: int

    dealer_name: str

    min_monthly_canon_eur: float

    city: Optional[str] = None

    contact_url: Optional[str] = None

    google_maps_url: Optional[str] = None

    phone: Optional[str] = None

    province: Optional[str] = None

    rating_value: Optional[float] = None

    review_count: Optional[int] = None


class Quotation(BaseModel):
    """One priced cell of the 18-combination matrix.

    apimax: `quotazioni[]` entry — `_compute_quotazioni_dealer_aware`
    (mcp_server.py:180). Reflects the dealer's vetrina formula applied to
    each (durata, km) combo; cells with implausible canon (<€50) are
    dropped upstream, so the list may contain fewer than 18 rows.
    """

    duration_months: int

    km_per_year: int

    monthly_canon_eur: float


class Tag(BaseModel):
    """Category tag for an offer (apimax: `tags[]`).

    Populated from `nlt_offerta_tag` ⋈ `nlt_offerte_tag`. Examples in
    production: "Promo", "Stock pronto", "GreenChoice".
    """

    name: str

    color: Optional[str] = None

    icon: Optional[str] = None


class OfferRetrieveResponse(BaseModel):
    """Full offer detail.

    Shape mirrors `_tool_get_nlt_offer_details` (apimax MCP) with all
    field names translated to American English snake_case for the
    partner SDK contract. VALUES stay Italian raw (apimax-aligned).
    The dict `technical_details` keeps Italian KEYS because they are
    `mnet_dettagli` column names (raw DB).
    """

    found: bool

    network_dealer_count: int

    offer_id: str

    slug: str

    title: str

    vat_included: bool

    available_addons: Optional[AvailableAddons] = None
    """Container for optional add-ons (apimax: `addons_disponibili`)."""

    brand: Optional[str] = None

    description_full: Optional[str] = None

    description_short: Optional[str] = None

    down_payment_scenarios_eur: Optional[DownPaymentScenariosEur] = None
    """Three down-payment scenarios in EUR (whole amounts).

    apimax: `anticipo_scenari_eur` (keys remapped to American English snake_case for
    partnermax SDK: `zero/medium/standard`).
    """

    down_payment_scenarios_labels: Optional[DownPaymentScenariosLabels] = None
    """Italian labels paired 1:1 with `NltDownPaymentScenariosEur`.

    apimax: `anticipo_scenari_labels` — used by Custom GPT to render the three
    options in conversation. Values stay in Italian raw ("Senza anticipo" /
    "Anticipo 12,5%" / "Anticipo 25%").
    """

    faqs: Optional[List[Faq]] = None

    fuel_type: Optional[str] = None

    gallery: Optional[List[Gallery]] = None

    image_url: Optional[str] = None

    included_accessories: Optional[List[IncludedAccessory]] = None

    included_services: Optional[List[IncludedService]] = None

    last_modified: Optional[datetime] = None

    min_monthly_canon_eur: Optional[float] = None

    model: Optional[str] = None

    network_offers: Optional[List[NetworkOffer]] = None

    primary_dealer_city: Optional[str] = None

    primary_dealer_name: Optional[str] = None

    primary_dealer_province: Optional[str] = None

    private_only: Optional[bool] = None

    quotations: Optional[List[Quotation]] = None

    segment: Optional[str] = None

    standard_equipment: Optional[List[str]] = None

    tags: Optional[List[Tag]] = None

    technical_details: Optional[Dict[str, object]] = None

    total_price_eur: Optional[float] = None

    transmission: Optional[str] = None

    trim: Optional[str] = None
