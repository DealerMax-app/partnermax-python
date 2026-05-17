# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "OfferRetrieveResponse",
    "AccessoriInclusi",
    "AddonsDisponibili",
    "AddonsDisponibiliAutoSostitutiva",
    "AddonsDisponibiliPneumatici",
    "AnticipoScenariEur",
    "AnticipoScenariLabels",
    "Gallery",
    "NetworkOffer",
    "Quotazioni",
    "Tag",
]


class AccessoriInclusi(BaseModel):
    codice: str

    descrizione: str

    prezzo_extra_eur: float


class AddonsDisponibiliAutoSostitutiva(BaseModel):
    categoria_default: str
    """Replacement vehicle category (B fixed)."""

    categoria_descrizione: str

    costo_mensile_eur: float


class AddonsDisponibiliPneumatici(BaseModel):
    costo_treno_eur: float
    """Cost of one set of 4 tyres, EUR."""

    diametro_in: int
    """Tyre diameter in inches."""

    regola_cambio: str
    """Replacement rule (e.g. one set every 30 000 km, rounded up)."""


class AddonsDisponibili(BaseModel):
    auto_sostitutiva: Optional[AddonsDisponibiliAutoSostitutiva] = None

    pneumatici: Optional[AddonsDisponibiliPneumatici] = None


class AnticipoScenariEur(BaseModel):
    anticipo_medio: int
    """12.5% down-payment scenario, whole EUR."""

    anticipo_standard: int
    """25% down-payment scenario, whole EUR (matches vetrina canon)."""

    anticipo_zero: int
    """Zero down-payment scenario, whole EUR."""


class AnticipoScenariLabels(BaseModel):
    anticipo_medio: str

    anticipo_standard: str

    anticipo_zero: str


class Gallery(BaseModel):
    is_cover: bool

    url: str


class NetworkOffer(BaseModel):
    canone_mensile_min_eur: float

    dealer_id: int

    dealer_name: str

    city: Optional[str] = None

    contact_url: Optional[str] = None

    google_maps_url: Optional[str] = None

    phone: Optional[str] = None

    province: Optional[str] = None

    rating_value: Optional[float] = None

    review_count: Optional[int] = None


class Quotazioni(BaseModel):
    canone_mensile_eur: float
    """Displayed monthly canon for this (durata, km) cell.

    Computed by `calcola_canone_vetrina` for the primary dealer of the partner
    network; VAT-inclusive when `solo_privati=true`.
    """

    durata_mesi: Literal[36, 48, 60]

    km_inclusi_anno: Literal[10000, 15000, 20000, 25000, 30000, 40000]


class Tag(BaseModel):
    name: str

    color: Optional[str] = None
    """Hex color for tag chip."""

    icon: Optional[str] = None
    """FontAwesome icon class."""


class OfferRetrieveResponse(BaseModel):
    """Full offer detail.

    Shape mirrors apimax MCP `get_nlt_offer_details` (`apimax/app/api/mcp_server.py::_tool_get_nlt_offer_details`) bit-for-bit so partnermax SDK consumers stay aligned with the Custom GPT / MCP clients on the DealerMAX network.
    """

    found: bool

    iva_inclusa: bool
    """True when canon is VAT-inclusive (i.e. `solo_privati=true`)."""

    network_dealer_count: int

    slug: str
    """Offer slug (stable identifier shared with apimax surfaces)."""

    title: str

    accessori_inclusi: Optional[List[AccessoriInclusi]] = None

    addons_disponibili: Optional[AddonsDisponibili] = None

    anticipo_scenari_eur: Optional[AnticipoScenariEur] = None

    anticipo_scenari_labels: Optional[AnticipoScenariLabels] = None

    canone_mensile_min_eur: Optional[float] = None
    """
    Lowest canon across the partner network for this offer (primary dealer's price).
    """

    description_full: Optional[str] = None
    """AI-generated long-form description."""

    description_short: Optional[str] = None

    fuel_type: Optional[str] = None
    """Raw Italian label from `nlt_offerte.alimentazione` (e.g. "Benzina", "Ibrida")."""

    gallery: Optional[List[Gallery]] = None

    image_url: Optional[str] = None

    last_modified: Optional[datetime] = None

    marca: Optional[str] = None

    modello: Optional[str] = None

    network_offers: Optional[List[NetworkOffer]] = None
    """All the partner's dealers that can fulfil this offer, sorted by canon ASC."""

    prezzo_totale_eur: Optional[float] = None
    """List price IVA-inclusive (vehicle + accessories + MSS)."""

    primary_dealer_city: Optional[str] = None

    primary_dealer_name: Optional[str] = None

    primary_dealer_province: Optional[str] = None

    quotazioni: Optional[List[Quotazioni]] = None

    segmento: Optional[str] = None

    solo_privati: Optional[bool] = None
    """Per-offer VAT scope: true → consumer-facing (B2C, VAT-inclusive).

    false → business (B2B, VAT-exclusive).
    """

    tags: Optional[List[Tag]] = None

    transmission: Optional[str] = None
    """Raw Italian label from `nlt_offerte.cambio`."""

    versione: Optional[str] = None
