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
    "Faq",
    "Gallery",
    "IncludedAccessory",
    "IncludedService",
    "NetworkOffer",
    "Quotation",
    "Tag",
]


class AvailableAddonsReplacementVehicle(BaseModel):
    """Replacement-vehicle add-on lookup.

    Always category B (utilitaria) per founder decision — the spoken
    "average customer" segment.
    """

    category_description: str

    default_category: str

    monthly_cost_eur: float


class AvailableAddonsTires(BaseModel):
    """Tyre-replacement add-on lookup.

    Populated when the catalogue carries a parseable tyre diameter and a
    DealerMAX-managed tyre package exists for that diameter. Null otherwise.
    Replacement rule: 1 set of 4 tyres every 30 000 km, rounded up.
    """

    diameter_in: int

    replacement_rule: str

    set_cost_eur: float


class AvailableAddons(BaseModel):
    """Container for optional add-ons."""

    replacement_vehicle: Optional[AvailableAddonsReplacementVehicle] = None
    """Replacement-vehicle add-on lookup.

    Always category B (utilitaria) per founder decision — the spoken "average
    customer" segment.
    """

    tires: Optional[AvailableAddonsTires] = None
    """Tyre-replacement add-on lookup.

    Populated when the catalogue carries a parseable tyre diameter and a
    DealerMAX-managed tyre package exists for that diameter. Null otherwise.
    Replacement rule: 1 set of 4 tyres every 30 000 km, rounded up.
    """


class DownPaymentScenariosEur(BaseModel):
    """Three down-payment scenarios in EUR (whole amounts).

    Keys use American-English snake_case for the partnermax SDK:
    `zero`, `medium`, `standard`.
    """

    medium: int

    standard: int

    zero: int


class DownPaymentScenariosLabels(BaseModel):
    """Italian labels paired 1:1 with `NltDownPaymentScenariosEur`.

    Values stay in Italian raw ("Senza anticipo" / "Anticipo 12,5%" /
    "Anticipo 25%") so partner UIs match DealerMAX consumer-facing copy.
    """

    medium: str

    standard: str

    zero: str


class Faq(BaseModel):
    """One Italian Q&A entry derived per-offer.

    Generated from the same grounded offer payload used by DealerMAX
    consumer-facing surfaces: dimensions, fuel, transmission, CO2, monthly
    canon, available durations, VAT inclusion, down-payment tiers, etc.
    """

    answer: str

    question: str


class Gallery(BaseModel):
    """One image in the offer gallery."""

    is_cover: bool

    url: str


class IncludedAccessory(BaseModel):
    """One accessory bundled with the offer."""

    code: str

    description: str

    extra_price_eur: float


class IncludedService(BaseModel):
    """One NLT service normally included in the canone.

    Same set of services across the network (Assicurazione RCA / Kasco /
    Incendio-Furto, Manutenzione, Assistenza Stradale, Bollo,
    Pneumatici, Veicolo in anticipo, Vettura sostitutiva). Not per-offer.
    """

    name: str

    description: Optional[str] = None


class NetworkOffer(BaseModel):
    """One network dealer's quote for this offer.

    Sorted by `min_monthly_canon_eur ASC`. In PartnerMAX this list is scoped
    to the calling partner's `partner_dealers` rows and returns the
    partner-owned `external_dealer_id`. Legacy `dlr_<id>` values remain only
    for compatibility callers.
    """

    dealer_id: str

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

    Reflects the dealer-aware pricing formula applied to each
    (duration, yearly-km) combination. Cells with implausible canons are
    filtered upstream, so the list may contain fewer than 18 rows.
    """

    duration_months: int

    km_per_year: int

    monthly_canon_eur: float


class Tag(BaseModel):
    """Category tag for an offer.

    Examples in production: "Promo", "Stock pronto", "GreenChoice".
    """

    name: str

    color: Optional[str] = None

    icon: Optional[str] = None


class OfferRetrieveResponse(BaseModel):
    """Full offer detail.

    Field names use American-English snake_case for the partner SDK contract.
    Values stay Italian raw where the underlying automotive catalogue uses
    Italian labels. The dict `technical_details` keeps Italian domain keys.
    """

    found: bool

    network_dealer_count: int

    offer_id: str

    slug: str

    title: str

    vat_included: bool

    available_addons: Optional[AvailableAddons] = None
    """Container for optional add-ons."""

    brand: Optional[str] = None

    description_full: Optional[str] = None

    description_short: Optional[str] = None

    down_payment_scenarios_eur: Optional[DownPaymentScenariosEur] = None
    """Three down-payment scenarios in EUR (whole amounts).

    Keys use American-English snake_case for the partnermax SDK: `zero`, `medium`,
    `standard`.
    """

    down_payment_scenarios_labels: Optional[DownPaymentScenariosLabels] = None
    """Italian labels paired 1:1 with `NltDownPaymentScenariosEur`.

    Values stay in Italian raw ("Senza anticipo" / "Anticipo 12,5%" / "Anticipo
    25%") so partner UIs match DealerMAX consumer-facing copy.
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

    schema_org: Optional[Dict[str, object]] = None

    segment: Optional[str] = None

    standard_equipment: Optional[List[str]] = None

    tags: Optional[List[Tag]] = None

    technical_details: Optional[Dict[str, object]] = None

    total_price_eur: Optional[float] = None

    transmission: Optional[str] = None

    trim: Optional[str] = None

    vehicle_type: Optional[Literal["auto", "vcom"]] = None
