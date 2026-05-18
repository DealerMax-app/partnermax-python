# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...._files import deepcopy_with_paths
from ...._types import Body, Query, Headers, NoneType, NotGiven, FileTypes, not_given
from ...._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.dealers.vehicles import image_create_params
from ....types.dealers.vehicles.vehicle_image import VehicleImage
from ....types.dealers.vehicles.vehicle_image_list import VehicleImageList

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    """Used-vehicle stock management for partner-owned dealers.

    The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
    """

    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return ImagesResourceWithStreamingResponse(self)

    def create(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleImage:
        """
        Attach a photo to a used vehicle.

        The partner posts photos one at a time, in the desired display order. The first
        photo becomes the cover (`position=1`, `is_cover=true`) automatically;
        subsequent photos get the next `position`. There is intentionally no separate
        "set cover" endpoint — order is the contract. To re-order, DELETE and re-POST.

        Up to `20` photos per vehicle. Bigger payloads return `413`; unsupported formats
        return `415`; missing storage credentials return `503 storage_not_configured`.

        The uploaded photo is visible on every AI surface (MCP `search_vehicles`, Custom
        GPT `search-vehicles-network`, the dealer site SEO/JSON-LD, NLWeb `/ask`) within
        the next apimax cache TTL (≤ 5 min).

        Args:
          file: The photo file. JPEG, PNG, or WebP, up to 15 MB. WebP is converted to PNG
              server-side.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        body = deepcopy_with_paths({"file": file}, [["file"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/images", dealer_id=dealer_id, vehicle_id=vehicle_id
            ),
            body=maybe_transform(body, image_create_params.ImageCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleImage,
        )

    def list(
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
    ) -> VehicleImageList:
        """
        List every photo attached to a vehicle, ordered by `position`.

        No pagination — a vehicle is capped at 20 photos so the full list always fits in
        a single response. `position=1` is the cover; use `DELETE` and re-`POST` to
        re-order.

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
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/images", dealer_id=dealer_id, vehicle_id=vehicle_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleImageList,
        )

    def delete(
        self,
        image_id: str,
        *,
        dealer_id: str,
        vehicle_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a photo from a vehicle.

        If the deleted photo was the cover (`position=1`), the next photo in order is
        promoted to cover automatically — partnermax re-ranks every remaining photo to
        contiguous 1..N so the partner never has to reason about gaps in the ordinal
        sequence.

        Returns `404 vehicle_image_not_found` if the image id is unknown or belongs to a
        different vehicle (cross-partner enumeration is blocked by the dealer + vehicle
        ACL chain).

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
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/images/{image_id}",
                dealer_id=dealer_id,
                vehicle_id=vehicle_id,
                image_id=image_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncImagesResource(AsyncAPIResource):
    """Used-vehicle stock management for partner-owned dealers.

    The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
    """

    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return AsyncImagesResourceWithStreamingResponse(self)

    async def create(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleImage:
        """
        Attach a photo to a used vehicle.

        The partner posts photos one at a time, in the desired display order. The first
        photo becomes the cover (`position=1`, `is_cover=true`) automatically;
        subsequent photos get the next `position`. There is intentionally no separate
        "set cover" endpoint — order is the contract. To re-order, DELETE and re-POST.

        Up to `20` photos per vehicle. Bigger payloads return `413`; unsupported formats
        return `415`; missing storage credentials return `503 storage_not_configured`.

        The uploaded photo is visible on every AI surface (MCP `search_vehicles`, Custom
        GPT `search-vehicles-network`, the dealer site SEO/JSON-LD, NLWeb `/ask`) within
        the next apimax cache TTL (≤ 5 min).

        Args:
          file: The photo file. JPEG, PNG, or WebP, up to 15 MB. WebP is converted to PNG
              server-side.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        body = deepcopy_with_paths({"file": file}, [["file"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/images", dealer_id=dealer_id, vehicle_id=vehicle_id
            ),
            body=await async_maybe_transform(body, image_create_params.ImageCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleImage,
        )

    async def list(
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
    ) -> VehicleImageList:
        """
        List every photo attached to a vehicle, ordered by `position`.

        No pagination — a vehicle is capped at 20 photos so the full list always fits in
        a single response. `position=1` is the cover; use `DELETE` and re-`POST` to
        re-order.

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
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/images", dealer_id=dealer_id, vehicle_id=vehicle_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleImageList,
        )

    async def delete(
        self,
        image_id: str,
        *,
        dealer_id: str,
        vehicle_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a photo from a vehicle.

        If the deleted photo was the cover (`position=1`), the next photo in order is
        promoted to cover automatically — partnermax re-ranks every remaining photo to
        contiguous 1..N so the partner never has to reason about gaps in the ordinal
        sequence.

        Returns `404 vehicle_image_not_found` if the image id is unknown or belongs to a
        different vehicle (cross-partner enumeration is blocked by the dealer + vehicle
        ACL chain).

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
        if not image_id:
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/dealers/{dealer_id}/vehicles/{vehicle_id}/images/{image_id}",
                dealer_id=dealer_id,
                vehicle_id=vehicle_id,
                image_id=image_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.create = to_raw_response_wrapper(
            images.create,
        )
        self.list = to_raw_response_wrapper(
            images.list,
        )
        self.delete = to_raw_response_wrapper(
            images.delete,
        )


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.create = async_to_raw_response_wrapper(
            images.create,
        )
        self.list = async_to_raw_response_wrapper(
            images.list,
        )
        self.delete = async_to_raw_response_wrapper(
            images.delete,
        )


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.create = to_streamed_response_wrapper(
            images.create,
        )
        self.list = to_streamed_response_wrapper(
            images.list,
        )
        self.delete = to_streamed_response_wrapper(
            images.delete,
        )


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.create = async_to_streamed_response_wrapper(
            images.create,
        )
        self.list = async_to_streamed_response_wrapper(
            images.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            images.delete,
        )
