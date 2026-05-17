# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.dealers.nlt import offer_list_params
from ....types.dealers.nlt.offer_list_response import OfferListResponse
from ....types.dealers.nlt.offer_retrieve_response import OfferRetrieveResponse

__all__ = ["OffersResource", "AsyncOffersResource"]


class OffersResource(SyncAPIResource):
    """
    Dealer-aware reads of the shared NLT catalog — pricing reflects the dealer's markup and down-payment tiers.
    """

    @cached_property
    def with_raw_response(self) -> OffersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return OffersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OffersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/partnermax-python#with_streaming_response
        """
        return OffersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        offer_id: str,
        *,
        dealer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferRetrieveResponse:
        """
        Returns the full detail of one NLT offer including the 18-quotation matrix (3
        durations × 6 km/year tiers) with prices computed for each of the dealer's three
        down-payment tiers — 54 displayed price points total — plus included services,
        optional accessories, image gallery, and the dealer business card.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not offer_id:
            raise ValueError(f"Expected a non-empty value for `offer_id` but received {offer_id!r}")
        return self._get(
            path_template("/v1/dealers/{dealer_id}/nlt/offers/{offer_id}", dealer_id=dealer_id, offer_id=offer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferRetrieveResponse,
        )

    def list(
        self,
        dealer_id: str,
        *,
        brand: str | Omit = omit,
        canone_max_eur: int | Omit = omit,
        cursor: str | Omit = omit,
        duration_months: Literal[24, 36, 48] | Omit = omit,
        fuel_type: Literal["electric", "hybrid", "plugin_hybrid", "petrol", "diesel", "lpg", "methane"] | Omit = omit,
        km_per_year: Literal[10000, 15000, 20000, 25000, 30000, 40000] | Omit = omit,
        limit: int | Omit = omit,
        segment: Literal["A", "B", "C", "D", "E", "SUV", "VAN"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferListResponse:
        """
        Returns a cursor-paginated list of NLT offers available to the specified dealer,
        with monthly canon already repriced using the dealer's markup and down-payment
        tiers.

        Args:
          brand: Filter by brand name, case-insensitive (e.g., `Fiat`).

          canone_max_eur: Upper bound on displayed monthly canon (EUR).

          cursor: Opaque pagination cursor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return self._get(
            path_template("/v1/dealers/{dealer_id}/nlt/offers", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "brand": brand,
                        "canone_max_eur": canone_max_eur,
                        "cursor": cursor,
                        "duration_months": duration_months,
                        "fuel_type": fuel_type,
                        "km_per_year": km_per_year,
                        "limit": limit,
                        "segment": segment,
                    },
                    offer_list_params.OfferListParams,
                ),
            ),
            cast_to=OfferListResponse,
        )


class AsyncOffersResource(AsyncAPIResource):
    """
    Dealer-aware reads of the shared NLT catalog — pricing reflects the dealer's markup and down-payment tiers.
    """

    @cached_property
    def with_raw_response(self) -> AsyncOffersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOffersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOffersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/partnermax-python#with_streaming_response
        """
        return AsyncOffersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        offer_id: str,
        *,
        dealer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferRetrieveResponse:
        """
        Returns the full detail of one NLT offer including the 18-quotation matrix (3
        durations × 6 km/year tiers) with prices computed for each of the dealer's three
        down-payment tiers — 54 displayed price points total — plus included services,
        optional accessories, image gallery, and the dealer business card.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not offer_id:
            raise ValueError(f"Expected a non-empty value for `offer_id` but received {offer_id!r}")
        return await self._get(
            path_template("/v1/dealers/{dealer_id}/nlt/offers/{offer_id}", dealer_id=dealer_id, offer_id=offer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OfferRetrieveResponse,
        )

    async def list(
        self,
        dealer_id: str,
        *,
        brand: str | Omit = omit,
        canone_max_eur: int | Omit = omit,
        cursor: str | Omit = omit,
        duration_months: Literal[24, 36, 48] | Omit = omit,
        fuel_type: Literal["electric", "hybrid", "plugin_hybrid", "petrol", "diesel", "lpg", "methane"] | Omit = omit,
        km_per_year: Literal[10000, 15000, 20000, 25000, 30000, 40000] | Omit = omit,
        limit: int | Omit = omit,
        segment: Literal["A", "B", "C", "D", "E", "SUV", "VAN"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OfferListResponse:
        """
        Returns a cursor-paginated list of NLT offers available to the specified dealer,
        with monthly canon already repriced using the dealer's markup and down-payment
        tiers.

        Args:
          brand: Filter by brand name, case-insensitive (e.g., `Fiat`).

          canone_max_eur: Upper bound on displayed monthly canon (EUR).

          cursor: Opaque pagination cursor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return await self._get(
            path_template("/v1/dealers/{dealer_id}/nlt/offers", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "brand": brand,
                        "canone_max_eur": canone_max_eur,
                        "cursor": cursor,
                        "duration_months": duration_months,
                        "fuel_type": fuel_type,
                        "km_per_year": km_per_year,
                        "limit": limit,
                        "segment": segment,
                    },
                    offer_list_params.OfferListParams,
                ),
            ),
            cast_to=OfferListResponse,
        )


class OffersResourceWithRawResponse:
    def __init__(self, offers: OffersResource) -> None:
        self._offers = offers

        self.retrieve = to_raw_response_wrapper(
            offers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            offers.list,
        )


class AsyncOffersResourceWithRawResponse:
    def __init__(self, offers: AsyncOffersResource) -> None:
        self._offers = offers

        self.retrieve = async_to_raw_response_wrapper(
            offers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            offers.list,
        )


class OffersResourceWithStreamingResponse:
    def __init__(self, offers: OffersResource) -> None:
        self._offers = offers

        self.retrieve = to_streamed_response_wrapper(
            offers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            offers.list,
        )


class AsyncOffersResourceWithStreamingResponse:
    def __init__(self, offers: AsyncOffersResource) -> None:
        self._offers = offers

        self.retrieve = async_to_streamed_response_wrapper(
            offers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            offers.list,
        )
