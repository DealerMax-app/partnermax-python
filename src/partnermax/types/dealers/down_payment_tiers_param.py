# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DownPaymentTiersParam", "High", "Low", "Medium"]


class High(TypedDict, total=False):
    """
    One down-payment tier — `final_eur = listino_imponibile * (percent_of_list / 100) + fixed_eur`. Persisted in apimax shape `{"pct": <0..1>, "eur": <int>}` on `dealer_public.nlt_anticipi_config`.
    """

    fixed_eur: Required[int]
    """Flat EUR component added on top of the percentage (e.g.

    promo `0% + 500€ fissi`). Whole euros only.
    """

    percent_of_list: Required[float]
    """Percent of the IVA-excluded list price applied as down payment for this tier.

    Range 0–100. Typical defaults: 0 (low), 12.5 (medium), 25 (high).
    """


class Low(TypedDict, total=False):
    """
    One down-payment tier — `final_eur = listino_imponibile * (percent_of_list / 100) + fixed_eur`. Persisted in apimax shape `{"pct": <0..1>, "eur": <int>}` on `dealer_public.nlt_anticipi_config`.
    """

    fixed_eur: Required[int]
    """Flat EUR component added on top of the percentage (e.g.

    promo `0% + 500€ fissi`). Whole euros only.
    """

    percent_of_list: Required[float]
    """Percent of the IVA-excluded list price applied as down payment for this tier.

    Range 0–100. Typical defaults: 0 (low), 12.5 (medium), 25 (high).
    """


class Medium(TypedDict, total=False):
    """
    One down-payment tier — `final_eur = listino_imponibile * (percent_of_list / 100) + fixed_eur`. Persisted in apimax shape `{"pct": <0..1>, "eur": <int>}` on `dealer_public.nlt_anticipi_config`.
    """

    fixed_eur: Required[int]
    """Flat EUR component added on top of the percentage (e.g.

    promo `0% + 500€ fissi`). Whole euros only.
    """

    percent_of_list: Required[float]
    """Percent of the IVA-excluded list price applied as down payment for this tier.

    Range 0–100. Typical defaults: 0 (low), 12.5 (medium), 25 (high).
    """


class DownPaymentTiersParam(TypedDict, total=False):
    """Three down-payment scenarios (basso / medio / alto).

    Each tier carries `{percent_of_list (0–100), fixed_eur (≥0)}`. No strict-ascending check — the final EUR per tier is offer-dependent (`listino_imponibile * pct + eur`).
    """

    high: Required[High]
    """
    One down-payment tier —
    `final_eur = listino_imponibile * (percent_of_list / 100) + fixed_eur`.
    Persisted in apimax shape `{"pct": <0..1>, "eur": <int>}` on
    `dealer_public.nlt_anticipi_config`.
    """

    low: Required[Low]
    """
    One down-payment tier —
    `final_eur = listino_imponibile * (percent_of_list / 100) + fixed_eur`.
    Persisted in apimax shape `{"pct": <0..1>, "eur": <int>}` on
    `dealer_public.nlt_anticipi_config`.
    """

    medium: Required[Medium]
    """
    One down-payment tier —
    `final_eur = listino_imponibile * (percent_of_list / 100) + fixed_eur`.
    Persisted in apimax shape `{"pct": <0..1>, "eur": <int>}` on
    `dealer_public.nlt_anticipi_config`.
    """
