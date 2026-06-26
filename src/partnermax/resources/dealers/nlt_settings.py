# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.dealers import nlt_setting_update_params
from ...types.dealers.nlt_settings import NltSettings
from ...types.dealers.down_payment_tiers_param import DownPaymentTiersParam

__all__ = ["NltSettingsResource", "AsyncNltSettingsResource"]


class NltSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NltSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return NltSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NltSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return NltSettingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        dealer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NltSettings:
        """
        Return current NLT economics for the dealer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return self._get(
            path_template("/v1/dealers/{dealer_id}/nlt-settings", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NltSettings,
        )

    def update(
        self,
        dealer_id: str,
        *,
        agency_markup_percent: float,
        down_payment_tiers: DownPaymentTiersParam,
        currency: Literal["EUR"] | Omit = omit,
        image_mode: Literal["branded", "scenario_locked", "scenario_seasonal"] | Omit = omit,
        image_scenario_locked: Optional[Literal["mediterraneo", "cortina", "milano", "showroom", "building"]]
        | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NltSettings:
        """
        Set markup percent (0-10) and three down-payment tiers (strictly ascending).

        Validation:

        - `agency_markup_percent` ∈ [0, 10] (Pydantic).
        - `down_payment_tiers.{low,medium,high}` each
          `{percent_of_list (0–100), fixed_eur (≥0)}`. No strict-ascending check — the
          final EUR per tier is offer-dependent (`listino_imponibile * pct + eur`).

        Persistence:

        - `agency_markup_percent` → `dealer_public.nlt_agency_percent` (rounded to int;
          live column is `Integer NOT NULL DEFAULT 2`).
        - `down_payment_tiers` → `dealer_public.nlt_anticipi_config` JSONB, stored in
          apimax shape `[{"pct": <0..1>, "eur": <int>}, ...]`. The partner-facing
          `percent_of_list` (0–100) is divided by 100 to keep the column byte-compatible
          with the DealerMAX UI calculator that reads the same JSONB.

        There is NO `vat_treatment` field: VAT is per-offer (`nlt_offerte.solo_privati`)
        in the canonical DataMax pricing model, not per-dealer. The offer detail
        endpoint surfaces it per row instead.

        `Idempotency-Key` replay uses the shared endpoint helper; a re-applied identical
        PATCH is also a row-level no-op by construction.

        Args:
          down_payment_tiers: Three down-payment scenarios (basso / medio / alto).

              No strict-ascending validation: the final EUR amount depends on the offer's list
              price (`tier.percent_of_list / 100 * listino_imponibile + tier.fixed_eur`), so a
              tier that looks larger by % can produce a smaller EUR on cheap vehicles. Label
              semantics (low/medium/high) are advisory — apimax/DealerMAX UI treats the 3
              positions as opaque slots ordered by intent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._patch(
            path_template("/v1/dealers/{dealer_id}/nlt-settings", dealer_id=dealer_id),
            body=maybe_transform(
                {
                    "agency_markup_percent": agency_markup_percent,
                    "down_payment_tiers": down_payment_tiers,
                    "currency": currency,
                    "image_mode": image_mode,
                    "image_scenario_locked": image_scenario_locked,
                },
                nlt_setting_update_params.NltSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NltSettings,
        )


class AsyncNltSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNltSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNltSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNltSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return AsyncNltSettingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        dealer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NltSettings:
        """
        Return current NLT economics for the dealer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return await self._get(
            path_template("/v1/dealers/{dealer_id}/nlt-settings", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NltSettings,
        )

    async def update(
        self,
        dealer_id: str,
        *,
        agency_markup_percent: float,
        down_payment_tiers: DownPaymentTiersParam,
        currency: Literal["EUR"] | Omit = omit,
        image_mode: Literal["branded", "scenario_locked", "scenario_seasonal"] | Omit = omit,
        image_scenario_locked: Optional[Literal["mediterraneo", "cortina", "milano", "showroom", "building"]]
        | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NltSettings:
        """
        Set markup percent (0-10) and three down-payment tiers (strictly ascending).

        Validation:

        - `agency_markup_percent` ∈ [0, 10] (Pydantic).
        - `down_payment_tiers.{low,medium,high}` each
          `{percent_of_list (0–100), fixed_eur (≥0)}`. No strict-ascending check — the
          final EUR per tier is offer-dependent (`listino_imponibile * pct + eur`).

        Persistence:

        - `agency_markup_percent` → `dealer_public.nlt_agency_percent` (rounded to int;
          live column is `Integer NOT NULL DEFAULT 2`).
        - `down_payment_tiers` → `dealer_public.nlt_anticipi_config` JSONB, stored in
          apimax shape `[{"pct": <0..1>, "eur": <int>}, ...]`. The partner-facing
          `percent_of_list` (0–100) is divided by 100 to keep the column byte-compatible
          with the DealerMAX UI calculator that reads the same JSONB.

        There is NO `vat_treatment` field: VAT is per-offer (`nlt_offerte.solo_privati`)
        in the canonical DataMax pricing model, not per-dealer. The offer detail
        endpoint surfaces it per row instead.

        `Idempotency-Key` replay uses the shared endpoint helper; a re-applied identical
        PATCH is also a row-level no-op by construction.

        Args:
          down_payment_tiers: Three down-payment scenarios (basso / medio / alto).

              No strict-ascending validation: the final EUR amount depends on the offer's list
              price (`tier.percent_of_list / 100 * listino_imponibile + tier.fixed_eur`), so a
              tier that looks larger by % can produce a smaller EUR on cheap vehicles. Label
              semantics (low/medium/high) are advisory — apimax/DealerMAX UI treats the 3
              positions as opaque slots ordered by intent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._patch(
            path_template("/v1/dealers/{dealer_id}/nlt-settings", dealer_id=dealer_id),
            body=await async_maybe_transform(
                {
                    "agency_markup_percent": agency_markup_percent,
                    "down_payment_tiers": down_payment_tiers,
                    "currency": currency,
                    "image_mode": image_mode,
                    "image_scenario_locked": image_scenario_locked,
                },
                nlt_setting_update_params.NltSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NltSettings,
        )


class NltSettingsResourceWithRawResponse:
    def __init__(self, nlt_settings: NltSettingsResource) -> None:
        self._nlt_settings = nlt_settings

        self.retrieve = to_raw_response_wrapper(
            nlt_settings.retrieve,
        )
        self.update = to_raw_response_wrapper(
            nlt_settings.update,
        )


class AsyncNltSettingsResourceWithRawResponse:
    def __init__(self, nlt_settings: AsyncNltSettingsResource) -> None:
        self._nlt_settings = nlt_settings

        self.retrieve = async_to_raw_response_wrapper(
            nlt_settings.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            nlt_settings.update,
        )


class NltSettingsResourceWithStreamingResponse:
    def __init__(self, nlt_settings: NltSettingsResource) -> None:
        self._nlt_settings = nlt_settings

        self.retrieve = to_streamed_response_wrapper(
            nlt_settings.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            nlt_settings.update,
        )


class AsyncNltSettingsResourceWithStreamingResponse:
    def __init__(self, nlt_settings: AsyncNltSettingsResource) -> None:
        self._nlt_settings = nlt_settings

        self.retrieve = async_to_streamed_response_wrapper(
            nlt_settings.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            nlt_settings.update,
        )
