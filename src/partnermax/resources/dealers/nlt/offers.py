# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.dealers.nlt import offer_list_params
from ....types.dealers.nlt.nlt_offer_summary import NltOfferSummary
from ....types.dealers.nlt.offer_retrieve_response import OfferRetrieveResponse

__all__ = ["OffersResource", "AsyncOffersResource"]


class OffersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OffersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return OffersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OffersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
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
        """Full offer detail.

        Payload shape mirrors apimax MCP `get_nlt_offer_details`
        bit-for-bit (mcp_server.py:1546-1606).

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
        brand: Optional[str] | Omit = omit,
        canone_max_eur: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        duration_months: Optional[int] | Omit = omit,
        fuel_type: Optional[str] | Omit = omit,
        km_per_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        segment: Optional[str] | Omit = omit,
        vehicle_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[NltOfferSummary]:
        """
        Listing of NLT offers with monthly canon repriced for this dealer.

        The response is cursor-paginated and dealer-aware: filters are applied to the
        shared NLT catalogue, then each returned offer is repriced with the dealer's
        configured mark-up, down-payment tiers, duration, and yearly-km filters. The
        headline canon is the cheapest eligible priced cell.

        Args:
          vehicle_type: Macro discriminator: 'auto' (passenger vehicles) or 'vcom' (light commercial ≤35
              q.li: vans, panel trucks, multispace, pickups, minibuses). Omit to return the
              mixed catalog.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return self._get_api_list(
            path_template("/v1/dealers/{dealer_id}/nlt/offers", dealer_id=dealer_id),
            page=SyncCursorPage[NltOfferSummary],
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
                        "vehicle_type": vehicle_type,
                    },
                    offer_list_params.OfferListParams,
                ),
            ),
            model=NltOfferSummary,
        )


class AsyncOffersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOffersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOffersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOffersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
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
        """Full offer detail.

        Payload shape mirrors apimax MCP `get_nlt_offer_details`
        bit-for-bit (mcp_server.py:1546-1606).

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

    def list(
        self,
        dealer_id: str,
        *,
        brand: Optional[str] | Omit = omit,
        canone_max_eur: Optional[int] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        duration_months: Optional[int] | Omit = omit,
        fuel_type: Optional[str] | Omit = omit,
        km_per_year: Optional[int] | Omit = omit,
        limit: int | Omit = omit,
        segment: Optional[str] | Omit = omit,
        vehicle_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NltOfferSummary, AsyncCursorPage[NltOfferSummary]]:
        """
        Listing of NLT offers with monthly canon repriced for this dealer.

        The response is cursor-paginated and dealer-aware: filters are applied to the
        shared NLT catalogue, then each returned offer is repriced with the dealer's
        configured mark-up, down-payment tiers, duration, and yearly-km filters. The
        headline canon is the cheapest eligible priced cell.

        Args:
          vehicle_type: Macro discriminator: 'auto' (passenger vehicles) or 'vcom' (light commercial ≤35
              q.li: vans, panel trucks, multispace, pickups, minibuses). Omit to return the
              mixed catalog.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return self._get_api_list(
            path_template("/v1/dealers/{dealer_id}/nlt/offers", dealer_id=dealer_id),
            page=AsyncCursorPage[NltOfferSummary],
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
                        "vehicle_type": vehicle_type,
                    },
                    offer_list_params.OfferListParams,
                ),
            ),
            model=NltOfferSummary,
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
