# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.dealers.vehicles import accessory_update_params
from ....types.dealers.vehicles.vehicle_accessories_catalog import VehicleAccessoriesCatalog

__all__ = ["AccessoriesResource", "AsyncAccessoriesResource"]


class AccessoriesResource(SyncAPIResource):
    """Used-vehicle stock management for dealers registered under a partner.

    Every vehicle request is scoped by dealer_id; the partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
    """

    @cached_property
    def with_raw_response(self) -> AccessoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AccessoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return AccessoriesResourceWithStreamingResponse(self)

    def update(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        alloy_wheel_size: Optional[int] | Omit = omit,
        equipment_ids: SequenceNotStr[str] | Omit = omit,
        optional_ids: SequenceNotStr[str] | Omit = omit,
        package_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleAccessoriesCatalog:
        """
        Set Vehicle Accessories

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        return self._put(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/accessories", dealer_id=dealer_id, vehicle_id=vehicle_id
            ),
            body=maybe_transform(
                {
                    "alloy_wheel_size": alloy_wheel_size,
                    "equipment_ids": equipment_ids,
                    "optional_ids": optional_ids,
                    "package_ids": package_ids,
                },
                accessory_update_params.AccessoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleAccessoriesCatalog,
        )

    def refresh_catalog(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleAccessoriesCatalog:
        """
        Refresh Vehicle Accessories Catalog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        return self._post(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/accessories/catalog/refresh",
                dealer_id=dealer_id,
                vehicle_id=vehicle_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleAccessoriesCatalog,
        )

    def retrieve_catalog(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleAccessoriesCatalog:
        """
        Get Vehicle Accessories Catalog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        return self._get(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/accessories/catalog",
                dealer_id=dealer_id,
                vehicle_id=vehicle_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleAccessoriesCatalog,
        )


class AsyncAccessoriesResource(AsyncAPIResource):
    """Used-vehicle stock management for dealers registered under a partner.

    Every vehicle request is scoped by dealer_id; the partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
    """

    @cached_property
    def with_raw_response(self) -> AsyncAccessoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return AsyncAccessoriesResourceWithStreamingResponse(self)

    async def update(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        alloy_wheel_size: Optional[int] | Omit = omit,
        equipment_ids: SequenceNotStr[str] | Omit = omit,
        optional_ids: SequenceNotStr[str] | Omit = omit,
        package_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleAccessoriesCatalog:
        """
        Set Vehicle Accessories

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        return await self._put(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/accessories", dealer_id=dealer_id, vehicle_id=vehicle_id
            ),
            body=await async_maybe_transform(
                {
                    "alloy_wheel_size": alloy_wheel_size,
                    "equipment_ids": equipment_ids,
                    "optional_ids": optional_ids,
                    "package_ids": package_ids,
                },
                accessory_update_params.AccessoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleAccessoriesCatalog,
        )

    async def refresh_catalog(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleAccessoriesCatalog:
        """
        Refresh Vehicle Accessories Catalog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        return await self._post(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/accessories/catalog/refresh",
                dealer_id=dealer_id,
                vehicle_id=vehicle_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleAccessoriesCatalog,
        )

    async def retrieve_catalog(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleAccessoriesCatalog:
        """
        Get Vehicle Accessories Catalog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        return await self._get(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/accessories/catalog",
                dealer_id=dealer_id,
                vehicle_id=vehicle_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleAccessoriesCatalog,
        )


class AccessoriesResourceWithRawResponse:
    def __init__(self, accessories: AccessoriesResource) -> None:
        self._accessories = accessories

        self.update = to_raw_response_wrapper(
            accessories.update,
        )
        self.refresh_catalog = to_raw_response_wrapper(
            accessories.refresh_catalog,
        )
        self.retrieve_catalog = to_raw_response_wrapper(
            accessories.retrieve_catalog,
        )


class AsyncAccessoriesResourceWithRawResponse:
    def __init__(self, accessories: AsyncAccessoriesResource) -> None:
        self._accessories = accessories

        self.update = async_to_raw_response_wrapper(
            accessories.update,
        )
        self.refresh_catalog = async_to_raw_response_wrapper(
            accessories.refresh_catalog,
        )
        self.retrieve_catalog = async_to_raw_response_wrapper(
            accessories.retrieve_catalog,
        )


class AccessoriesResourceWithStreamingResponse:
    def __init__(self, accessories: AccessoriesResource) -> None:
        self._accessories = accessories

        self.update = to_streamed_response_wrapper(
            accessories.update,
        )
        self.refresh_catalog = to_streamed_response_wrapper(
            accessories.refresh_catalog,
        )
        self.retrieve_catalog = to_streamed_response_wrapper(
            accessories.retrieve_catalog,
        )


class AsyncAccessoriesResourceWithStreamingResponse:
    def __init__(self, accessories: AsyncAccessoriesResource) -> None:
        self._accessories = accessories

        self.update = async_to_streamed_response_wrapper(
            accessories.update,
        )
        self.refresh_catalog = async_to_streamed_response_wrapper(
            accessories.refresh_catalog,
        )
        self.retrieve_catalog = async_to_streamed_response_wrapper(
            accessories.retrieve_catalog,
        )
