# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "OfferRetrieveResponse",
    "AvailableAddons",
    "AvailableAddonsReplacementVehicle",
    "AvailableAddonsTires",
    "DownPaymentScenariosEur",
    "DownPaymentScenariosLabels",
    "Gallery",
    "IncludedAccessory",
    "IncludedService",
    "NetworkOffer",
    "Quotation",
    "Tag",
]


class AvailableAddonsReplacementVehicle(BaseModel):
    category_description: str

    default_category: str
    """Replacement vehicle category (B fixed)."""

    monthly_cost_eur: float


class AvailableAddonsTires(BaseModel):
    diameter_in: int
    """Tyre diameter in inches."""

    replacement_rule: str
    """Replacement rule (e.g. one set every 30 000 km, rounded up)."""

    set_cost_eur: float
    """Cost of one set of 4 tyres, EUR."""


class AvailableAddons(BaseModel):
    replacement_vehicle: Optional[AvailableAddonsReplacementVehicle] = None

    tires: Optional[AvailableAddonsTires] = None


class DownPaymentScenariosEur(BaseModel):
    medium: int
    """12.5% down-payment scenario, whole EUR."""

    standard: int
    """25% down-payment scenario, whole EUR (matches vetrina canon)."""

    zero: int
    """Zero down-payment scenario, whole EUR."""


class DownPaymentScenariosLabels(BaseModel):
    medium: str

    standard: str

    zero: str


class Gallery(BaseModel):
    is_cover: bool

    url: str


class IncludedAccessory(BaseModel):
    code: str

    description: str

    extra_price_eur: float


class IncludedService(BaseModel):
    name: str
    """Service name (e.g. "Assicurazione RCA", "Manutenzione")."""

    description: Optional[str] = None
    """Short human description (e.g. "Responsabilità Civile Auto")."""


class NetworkOffer(BaseModel):
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
    duration_months: Literal[36, 48, 60]

    km_per_year: Literal[10000, 15000, 20000, 25000, 30000, 40000]

    monthly_canon_eur: float
    """Displayed monthly canon for this (duration, km) cell.

    Computed by `calcola_canone_vetrina` for the primary dealer of the partner
    network; VAT-inclusive when `private_only=true`.
    """


class Tag(BaseModel):
    name: str

    color: Optional[str] = None
    """Hex color for tag chip."""

    icon: Optional[str] = None
    """FontAwesome icon class."""


class OfferRetrieveResponse(BaseModel):
    """Full offer detail.

    Field names: American English snake_case (Stripe-style SDK contract). Values: raw Italian, apimax-aligned. Shape mirrors apimax MCP `get_nlt_offer_details` (`apimax/app/api/mcp_server.py::_tool_get_nlt_offer_details`).
    """

    found: bool

    network_dealer_count: int

    offer_id: str
    """Numeric `nlt_offerte.id_offerta` as string.

    Same value returned by the listing endpoint.
    """

    slug: str
    """
    Offer slug (stable identifier shared with apimax surfaces and used in canonical
    URLs).
    """

    title: str

    vat_included: bool
    """True when canon is VAT-inclusive (i.e. `private_only=true`)."""

    available_addons: Optional[AvailableAddons] = None

    brand: Optional[str] = None

    description_full: Optional[str] = None
    """AI-generated long-form description."""

    description_short: Optional[str] = None

    down_payment_scenarios_eur: Optional[DownPaymentScenariosEur] = None

    down_payment_scenarios_labels: Optional[DownPaymentScenariosLabels] = None

    fuel_type: Optional[str] = None
    """Raw Italian label from `nlt_offerte.alimentazione` (e.g.

    "Benzina", "Ibrido diesel").
    """

    gallery: Optional[List[Gallery]] = None

    image_url: Optional[str] = None

    included_accessories: Optional[List[IncludedAccessory]] = None

    included_services: Optional[List[IncludedService]] = None
    """Services normally included in the canone.

    apimax: `_get_services_included` (`nlt_resolver.py:719`) reads global
    `nlt_services` is_active table.
    """

    last_modified: Optional[datetime] = None

    min_monthly_canon_eur: Optional[float] = None
    """
    Lowest canon across the partner network for this offer (primary dealer's price).
    """

    model: Optional[str] = None

    network_offers: Optional[List[NetworkOffer]] = None
    """All the partner's dealers that can fulfil this offer, sorted by canon ASC."""

    primary_dealer_city: Optional[str] = None

    primary_dealer_name: Optional[str] = None

    primary_dealer_province: Optional[str] = None

    private_only: Optional[bool] = None
    """Per-offer VAT scope: true → consumer-facing (B2C, VAT-inclusive).

    false → business (B2B, VAT-exclusive). Sourced from `nlt_offerte.solo_privati`.
    """

    quotations: Optional[List[Quotation]] = None

    segment: Optional[str] = None
    """Raw Italian label from `nlt_offerte.segmento` (e.g.

    "SUV piccoli", "Superiori").
    """

    standard_equipment: Optional[List[str]] = None
    """Standard equipment list (one entry per item).

    Sourced from `mnet_dettagli.equipaggiamento` split on newlines/semicolons.
    Currently empty on every live offer (upstream column unpopulated); will
    auto-fill when the data flows in.
    """

    tags: Optional[List[Tag]] = None

    technical_details: Optional[Dict[str, object]] = None
    """
    Full Motornet technical sheet — apimax: `_get_dettagli_motornet`
    (`nlt_resolver.py:752`). Every non-null `mnet_dettagli` column for this
    `codice_motornet_uni` flattened into a plain dict (~30-40 keys typically
    populated out of 90 columns). KEYS stay Italian because they are raw SQL column
    names: cilindrata (cc), kw, hp, coppia, accelerazione (s), velocita (km/h),
    lunghezza/larghezza/altezza/passo (cm), peso (kg), bagagliaio (L, free-text),
    emissioni_co2 (g/km, free-text), pneumatici_anteriori ("205/55 R17"), trazione,
    alimentazione, cambio, euro, autonomia_media, capacita_nominale_batteria, etc.
    Native units preserved; values are int/float/bool/string (timestamps
    ISO-formatted).
    """

    total_price_eur: Optional[float] = None
    """List price IVA-inclusive (vehicle + accessories + MSS)."""

    transmission: Optional[str] = None
    """Raw Italian label from `nlt_offerte.cambio` (e.g. "Automatico sequenziale")."""

    trim: Optional[str] = None
