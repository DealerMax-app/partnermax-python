# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ...types import dealer_list_params, dealer_create_params, dealer_update_params
from .nlt.nlt import (
    NltResource,
    AsyncNltResource,
    NltResourceWithRawResponse,
    AsyncNltResourceWithRawResponse,
    NltResourceWithStreamingResponse,
    AsyncNltResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .nlt_settings import (
    NltSettingsResource,
    AsyncNltSettingsResource,
    NltSettingsResourceWithRawResponse,
    AsyncNltSettingsResourceWithRawResponse,
    NltSettingsResourceWithStreamingResponse,
    AsyncNltSettingsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .vehicles.vehicles import (
    VehiclesResource,
    AsyncVehiclesResource,
    VehiclesResourceWithRawResponse,
    AsyncVehiclesResourceWithRawResponse,
    VehiclesResourceWithStreamingResponse,
    AsyncVehiclesResourceWithStreamingResponse,
)
from ...types.dealer_detail import DealerDetail
from ...types.dealer_list_response import DealerListResponse

__all__ = ["DealersResource", "AsyncDealersResource"]


class DealersResource(SyncAPIResource):
    """Provision, update, deactivate, and list dealers owned by the calling partner."""

    @cached_property
    def nlt_settings(self) -> NltSettingsResource:
        return NltSettingsResource(self._client)

    @cached_property
    def nlt(self) -> NltResource:
        return NltResource(self._client)

    @cached_property
    def vehicles(self) -> VehiclesResource:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return VehiclesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DealersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return DealersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DealersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return DealersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address: str,
        business_name: str,
        city: str,
        contact_email: str,
        contact_phone: str,
        postal_code: str,
        primary_domain: str,
        province_code: str,
        vat_number: str,
        activate: bool | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerDetail:
        """
        Provision a new dealer as child of the calling partner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/v1/dealers",
            body=maybe_transform(
                {
                    "address": address,
                    "business_name": business_name,
                    "city": city,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone,
                    "postal_code": postal_code,
                    "primary_domain": primary_domain,
                    "province_code": province_code,
                    "vat_number": vat_number,
                    "activate": activate,
                    "metadata": metadata,
                },
                dealer_create_params.DealerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealerDetail,
        )

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
    ) -> DealerDetail:
        """Fetch a dealer's full detail.

        ACL-protected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return self._get(
            path_template("/v1/dealers/{dealer_id}", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealerDetail,
        )

    def update(
        self,
        dealer_id: str,
        *,
        address: Optional[str] | Omit = omit,
        business_name: Optional[str] | Omit = omit,
        city: Optional[str] | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        contact_phone: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        postal_code: Optional[str] | Omit = omit,
        province_code: Optional[str] | Omit = omit,
        status: Optional[Literal["active", "inactive"]] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerDetail:
        """Update or toggle status.

        Inactive dealers drop from AI surfaces within 5 min.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._patch(
            path_template("/v1/dealers/{dealer_id}", dealer_id=dealer_id),
            body=maybe_transform(
                {
                    "address": address,
                    "business_name": business_name,
                    "city": city,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone,
                    "metadata": metadata,
                    "postal_code": postal_code,
                    "province_code": province_code,
                    "status": status,
                },
                dealer_update_params.DealerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealerDetail,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["active", "inactive", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerListResponse:
        """List dealers owned by the calling partner.

        Cursor-paginated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/dealers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    dealer_list_params.DealerListParams,
                ),
            ),
            cast_to=DealerListResponse,
        )

    def delete(
        self,
        dealer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete.

        Audit trail retained; reactivation requires DealerMAX support.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/dealers/{dealer_id}", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDealersResource(AsyncAPIResource):
    """Provision, update, deactivate, and list dealers owned by the calling partner."""

    @cached_property
    def nlt_settings(self) -> AsyncNltSettingsResource:
        return AsyncNltSettingsResource(self._client)

    @cached_property
    def nlt(self) -> AsyncNltResource:
        return AsyncNltResource(self._client)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResource:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return AsyncVehiclesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDealersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDealersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDealersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return AsyncDealersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address: str,
        business_name: str,
        city: str,
        contact_email: str,
        contact_phone: str,
        postal_code: str,
        primary_domain: str,
        province_code: str,
        vat_number: str,
        activate: bool | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerDetail:
        """
        Provision a new dealer as child of the calling partner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/v1/dealers",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "business_name": business_name,
                    "city": city,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone,
                    "postal_code": postal_code,
                    "primary_domain": primary_domain,
                    "province_code": province_code,
                    "vat_number": vat_number,
                    "activate": activate,
                    "metadata": metadata,
                },
                dealer_create_params.DealerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealerDetail,
        )

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
    ) -> DealerDetail:
        """Fetch a dealer's full detail.

        ACL-protected.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return await self._get(
            path_template("/v1/dealers/{dealer_id}", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealerDetail,
        )

    async def update(
        self,
        dealer_id: str,
        *,
        address: Optional[str] | Omit = omit,
        business_name: Optional[str] | Omit = omit,
        city: Optional[str] | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        contact_phone: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        postal_code: Optional[str] | Omit = omit,
        province_code: Optional[str] | Omit = omit,
        status: Optional[Literal["active", "inactive"]] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerDetail:
        """Update or toggle status.

        Inactive dealers drop from AI surfaces within 5 min.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._patch(
            path_template("/v1/dealers/{dealer_id}", dealer_id=dealer_id),
            body=await async_maybe_transform(
                {
                    "address": address,
                    "business_name": business_name,
                    "city": city,
                    "contact_email": contact_email,
                    "contact_phone": contact_phone,
                    "metadata": metadata,
                    "postal_code": postal_code,
                    "province_code": province_code,
                    "status": status,
                },
                dealer_update_params.DealerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DealerDetail,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["active", "inactive", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerListResponse:
        """List dealers owned by the calling partner.

        Cursor-paginated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/dealers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    dealer_list_params.DealerListParams,
                ),
            ),
            cast_to=DealerListResponse,
        )

    async def delete(
        self,
        dealer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete.

        Audit trail retained; reactivation requires DealerMAX support.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/dealers/{dealer_id}", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DealersResourceWithRawResponse:
    def __init__(self, dealers: DealersResource) -> None:
        self._dealers = dealers

        self.create = to_raw_response_wrapper(
            dealers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            dealers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            dealers.update,
        )
        self.list = to_raw_response_wrapper(
            dealers.list,
        )
        self.delete = to_raw_response_wrapper(
            dealers.delete,
        )

    @cached_property
    def nlt_settings(self) -> NltSettingsResourceWithRawResponse:
        return NltSettingsResourceWithRawResponse(self._dealers.nlt_settings)

    @cached_property
    def nlt(self) -> NltResourceWithRawResponse:
        return NltResourceWithRawResponse(self._dealers.nlt)

    @cached_property
    def vehicles(self) -> VehiclesResourceWithRawResponse:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return VehiclesResourceWithRawResponse(self._dealers.vehicles)


class AsyncDealersResourceWithRawResponse:
    def __init__(self, dealers: AsyncDealersResource) -> None:
        self._dealers = dealers

        self.create = async_to_raw_response_wrapper(
            dealers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            dealers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            dealers.update,
        )
        self.list = async_to_raw_response_wrapper(
            dealers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dealers.delete,
        )

    @cached_property
    def nlt_settings(self) -> AsyncNltSettingsResourceWithRawResponse:
        return AsyncNltSettingsResourceWithRawResponse(self._dealers.nlt_settings)

    @cached_property
    def nlt(self) -> AsyncNltResourceWithRawResponse:
        return AsyncNltResourceWithRawResponse(self._dealers.nlt)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResourceWithRawResponse:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return AsyncVehiclesResourceWithRawResponse(self._dealers.vehicles)


class DealersResourceWithStreamingResponse:
    def __init__(self, dealers: DealersResource) -> None:
        self._dealers = dealers

        self.create = to_streamed_response_wrapper(
            dealers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dealers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dealers.update,
        )
        self.list = to_streamed_response_wrapper(
            dealers.list,
        )
        self.delete = to_streamed_response_wrapper(
            dealers.delete,
        )

    @cached_property
    def nlt_settings(self) -> NltSettingsResourceWithStreamingResponse:
        return NltSettingsResourceWithStreamingResponse(self._dealers.nlt_settings)

    @cached_property
    def nlt(self) -> NltResourceWithStreamingResponse:
        return NltResourceWithStreamingResponse(self._dealers.nlt)

    @cached_property
    def vehicles(self) -> VehiclesResourceWithStreamingResponse:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return VehiclesResourceWithStreamingResponse(self._dealers.vehicles)


class AsyncDealersResourceWithStreamingResponse:
    def __init__(self, dealers: AsyncDealersResource) -> None:
        self._dealers = dealers

        self.create = async_to_streamed_response_wrapper(
            dealers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dealers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dealers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dealers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dealers.delete,
        )

    @cached_property
    def nlt_settings(self) -> AsyncNltSettingsResourceWithStreamingResponse:
        return AsyncNltSettingsResourceWithStreamingResponse(self._dealers.nlt_settings)

    @cached_property
    def nlt(self) -> AsyncNltResourceWithStreamingResponse:
        return AsyncNltResourceWithStreamingResponse(self._dealers.nlt)

    @cached_property
    def vehicles(self) -> AsyncVehiclesResourceWithStreamingResponse:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return AsyncVehiclesResourceWithStreamingResponse(self._dealers.vehicles)
