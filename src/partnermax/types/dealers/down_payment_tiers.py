# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["DownPaymentTiers", "High", "Low", "Medium"]


class High(BaseModel):
    """One down-payment tier — percent of list price + flat EUR.

    Partnermax API exposes `percent_of_list` as a 0–100 number
    (UI-friendly: write `12.5`, not `0.125`). The final EUR applied to
    a deal is computed from the offer's IVA-excluded list price plus the
    flat component.
    """

    fixed_eur: int
    """Flat EUR component added on top of the percentage (e.g.

    promo `0% + 500 EUR fissi`). Whole euros only.
    """

    percent_of_list: float
    """Percentage of the IVA-excluded list price applied as down payment for this tier.

    Range 0–100. Typical defaults: 0 (low), 12.5 (medium), 25 (high).
    """


class Low(BaseModel):
    """One down-payment tier — percent of list price + flat EUR.

    Partnermax API exposes `percent_of_list` as a 0–100 number
    (UI-friendly: write `12.5`, not `0.125`). The final EUR applied to
    a deal is computed from the offer's IVA-excluded list price plus the
    flat component.
    """

    fixed_eur: int
    """Flat EUR component added on top of the percentage (e.g.

    promo `0% + 500 EUR fissi`). Whole euros only.
    """

    percent_of_list: float
    """Percentage of the IVA-excluded list price applied as down payment for this tier.

    Range 0–100. Typical defaults: 0 (low), 12.5 (medium), 25 (high).
    """


class Medium(BaseModel):
    """One down-payment tier — percent of list price + flat EUR.

    Partnermax API exposes `percent_of_list` as a 0–100 number
    (UI-friendly: write `12.5`, not `0.125`). The final EUR applied to
    a deal is computed from the offer's IVA-excluded list price plus the
    flat component.
    """

    fixed_eur: int
    """Flat EUR component added on top of the percentage (e.g.

    promo `0% + 500 EUR fissi`). Whole euros only.
    """

    percent_of_list: float
    """Percentage of the IVA-excluded list price applied as down payment for this tier.

    Range 0–100. Typical defaults: 0 (low), 12.5 (medium), 25 (high).
    """


class DownPaymentTiers(BaseModel):
    """Three down-payment scenarios (basso / medio / alto).

    No strict-ascending validation: the final EUR amount depends on
    the offer's list price (`tier.percent_of_list / 100 *
    listino_imponibile + tier.fixed_eur`), so a tier that looks
    larger by % can produce a smaller EUR on cheap vehicles. Label
    semantics (low/medium/high) are advisory — DealerMAX UI
    treats the 3 positions as opaque slots ordered by intent.
    """

    high: High
    """One down-payment tier — percent of list price + flat EUR.

    Partnermax API exposes `percent_of_list` as a 0–100 number (UI-friendly: write
    `12.5`, not `0.125`). The final EUR applied to a deal is computed from the
    offer's IVA-excluded list price plus the flat component.
    """

    low: Low
    """One down-payment tier — percent of list price + flat EUR.

    Partnermax API exposes `percent_of_list` as a 0–100 number (UI-friendly: write
    `12.5`, not `0.125`). The final EUR applied to a deal is computed from the
    offer's IVA-excluded list price plus the flat component.
    """

    medium: Medium
    """One down-payment tier — percent of list price + flat EUR.

    Partnermax API exposes `percent_of_list` as a 0–100 number (UI-friendly: write
    `12.5`, not `0.125`). The final EUR applied to a deal is computed from the
    offer's IVA-excluded list price plus the flat component.
    """
