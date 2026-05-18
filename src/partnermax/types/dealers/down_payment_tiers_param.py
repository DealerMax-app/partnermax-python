# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DownPaymentTiersParam", "High", "Low", "Medium"]


class High(TypedDict, total=False):
    """One down-payment tier — percent of list price + flat EUR.

    apimax: `dealer_public.nlt_anticipi_config` is a JSONB list of three
    `{"pct": <0..1>, "eur": <int>}` entries. The final EUR applied to
    a deal is `listino_imponibile * pct + eur` (see
    `apimax/app/services/nlt/calculator.py::calcola_anticipo_eur`).

    Partnermax API exposes `percent_of_list` as a 0–100 number
    (UI-friendly: write `12.5`, not `0.125`); the router persists
    `pct = percent_of_list / 100` to stay byte-compatible with the
    DealerMAX UI calculator.
    """

    fixed_eur: Required[int]
    """Flat EUR component added on top of the percentage (e.g.

    promo `0% + 500 EUR fissi`). Whole euros only.
    """

    percent_of_list: Required[float]
    """Percentage of the IVA-excluded list price applied as down payment for this tier.

    Range 0–100. Typical defaults: 0 (low), 12.5 (medium), 25 (high).
    """


class Low(TypedDict, total=False):
    """One down-payment tier — percent of list price + flat EUR.

    apimax: `dealer_public.nlt_anticipi_config` is a JSONB list of three
    `{"pct": <0..1>, "eur": <int>}` entries. The final EUR applied to
    a deal is `listino_imponibile * pct + eur` (see
    `apimax/app/services/nlt/calculator.py::calcola_anticipo_eur`).

    Partnermax API exposes `percent_of_list` as a 0–100 number
    (UI-friendly: write `12.5`, not `0.125`); the router persists
    `pct = percent_of_list / 100` to stay byte-compatible with the
    DealerMAX UI calculator.
    """

    fixed_eur: Required[int]
    """Flat EUR component added on top of the percentage (e.g.

    promo `0% + 500 EUR fissi`). Whole euros only.
    """

    percent_of_list: Required[float]
    """Percentage of the IVA-excluded list price applied as down payment for this tier.

    Range 0–100. Typical defaults: 0 (low), 12.5 (medium), 25 (high).
    """


class Medium(TypedDict, total=False):
    """One down-payment tier — percent of list price + flat EUR.

    apimax: `dealer_public.nlt_anticipi_config` is a JSONB list of three
    `{"pct": <0..1>, "eur": <int>}` entries. The final EUR applied to
    a deal is `listino_imponibile * pct + eur` (see
    `apimax/app/services/nlt/calculator.py::calcola_anticipo_eur`).

    Partnermax API exposes `percent_of_list` as a 0–100 number
    (UI-friendly: write `12.5`, not `0.125`); the router persists
    `pct = percent_of_list / 100` to stay byte-compatible with the
    DealerMAX UI calculator.
    """

    fixed_eur: Required[int]
    """Flat EUR component added on top of the percentage (e.g.

    promo `0% + 500 EUR fissi`). Whole euros only.
    """

    percent_of_list: Required[float]
    """Percentage of the IVA-excluded list price applied as down payment for this tier.

    Range 0–100. Typical defaults: 0 (low), 12.5 (medium), 25 (high).
    """


class DownPaymentTiersParam(TypedDict, total=False):
    """Three down-payment scenarios (basso / medio / alto).

    No strict-ascending validation: the final EUR amount depends on
    the offer's list price (`tier.percent_of_list / 100 *
    listino_imponibile + tier.fixed_eur`), so a tier that looks
    larger by % can produce a smaller EUR on cheap vehicles. Label
    semantics (low/medium/high) are advisory — apimax/DealerMAX UI
    treats the 3 positions as opaque slots ordered by intent.
    """

    high: Required[High]
    """One down-payment tier — percent of list price + flat EUR.

    apimax: `dealer_public.nlt_anticipi_config` is a JSONB list of three
    `{"pct": <0..1>, "eur": <int>}` entries. The final EUR applied to a deal is
    `listino_imponibile * pct + eur` (see
    `apimax/app/services/nlt/calculator.py::calcola_anticipo_eur`).

    Partnermax API exposes `percent_of_list` as a 0–100 number (UI-friendly: write
    `12.5`, not `0.125`); the router persists `pct = percent_of_list / 100` to stay
    byte-compatible with the DealerMAX UI calculator.
    """

    low: Required[Low]
    """One down-payment tier — percent of list price + flat EUR.

    apimax: `dealer_public.nlt_anticipi_config` is a JSONB list of three
    `{"pct": <0..1>, "eur": <int>}` entries. The final EUR applied to a deal is
    `listino_imponibile * pct + eur` (see
    `apimax/app/services/nlt/calculator.py::calcola_anticipo_eur`).

    Partnermax API exposes `percent_of_list` as a 0–100 number (UI-friendly: write
    `12.5`, not `0.125`); the router persists `pct = percent_of_list / 100` to stay
    byte-compatible with the DealerMAX UI calculator.
    """

    medium: Required[Medium]
    """One down-payment tier — percent of list price + flat EUR.

    apimax: `dealer_public.nlt_anticipi_config` is a JSONB list of three
    `{"pct": <0..1>, "eur": <int>}` entries. The final EUR applied to a deal is
    `listino_imponibile * pct + eur` (see
    `apimax/app/services/nlt/calculator.py::calcola_anticipo_eur`).

    Partnermax API exposes `percent_of_list` as a 0–100 number (UI-friendly: write
    `12.5`, not `0.125`); the router persists `pct = percent_of_list / 100` to stay
    byte-compatible with the DealerMAX UI calculator.
    """
