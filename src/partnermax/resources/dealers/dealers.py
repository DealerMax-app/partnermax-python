# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
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
from ...types.dealer_detail import DealerDetail
from ...types.dealer_list_response import DealerListResponse

__all__ = ["DealersResource", "AsyncDealersResource"]


class DealersResource(SyncAPIResource):
    """Provision, update, deactivate, and list dealers owned by the calling partner."""

    @cached_property
    def nlt_settings(self) -> NltSettingsResource:
        """Per-dealer NLT economics: agency markup percent and three down-payment tiers."""
        return NltSettingsResource(self._client)

    @cached_property
    def nlt(self) -> NltResource:
        return NltResource(self._client)

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
        business_name: str,
        contact_email: str,
        postal_code: str,
        primary_domain: str,
        province_code: str,
        vat_number: str,
        activate: bool | Omit = omit,
        contact_phone: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerDetail:
        """Creates a new dealer as a child of the calling partner account.

        The dealer is
        indexed in the cross-network AI-citation surfaces (MCP, Custom GPT, NLWeb,
        llms.txt) within five minutes. The partner is responsible for ensuring the
        business has consented to this provisioning and that the data provided is
        accurate.

        Idempotent on `Idempotency-Key` for 24 hours.

        Args:
          postal_code: Italian 5-digit postal code.

          primary_domain: Root domain of the dealer's public website.

          province_code: Italian two-letter province code, e.g., `MI`, `RM`, `TO`.

          vat_number: Italian VAT number, 11 digits prefixed with `IT`.

          activate: If false, dealer is created in inactive state and does not appear in AI surfaces
              until activated.

          contact_phone: E.164 format recommended.

          metadata: Free-form partner-supplied key-value pairs, max 16 keys, values max 500 chars.

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
                    "business_name": business_name,
                    "contact_email": contact_email,
                    "postal_code": postal_code,
                    "primary_domain": primary_domain,
                    "province_code": province_code,
                    "vat_number": vat_number,
                    "activate": activate,
                    "contact_phone": contact_phone,
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
        """
        Get a dealer's full detail

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
        business_name: str | Omit = omit,
        contact_email: str | Omit = omit,
        contact_phone: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        postal_code: str | Omit = omit,
        province_code: str | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerDetail:
        """Partial update of dealer fields.

        Only provided fields are modified. Setting
        `status: "inactive"` removes the dealer from the cross-network AI-citation
        surfaces within five minutes. Reactivation: send `status: "active"`.

        Args:
          status: Toggle activation. Inactive dealers are removed from AI surfaces within 5
              minutes.

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
                    "business_name": business_name,
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
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["active", "inactive", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerListResponse:
        """
        Returns a cursor-paginated list of dealers belonging to the calling partner.
        Default ordering: most recently created first.

        Args:
          cursor: Opaque pagination cursor from a previous response's `next_cursor`.

          limit: Maximum number of items to return.

          status: Filter by dealer status.

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
        """Marks the dealer as deleted while preserving the audit trail.

        Unlike
        deactivation (`PATCH status=inactive`), a deleted dealer cannot be reactivated
        by the partner — re-creation requires DealerMAX support. Use deactivation for
        reversible suspensions.

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
        """Per-dealer NLT economics: agency markup percent and three down-payment tiers."""
        return AsyncNltSettingsResource(self._client)

    @cached_property
    def nlt(self) -> AsyncNltResource:
        return AsyncNltResource(self._client)

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
        business_name: str,
        contact_email: str,
        postal_code: str,
        primary_domain: str,
        province_code: str,
        vat_number: str,
        activate: bool | Omit = omit,
        contact_phone: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerDetail:
        """Creates a new dealer as a child of the calling partner account.

        The dealer is
        indexed in the cross-network AI-citation surfaces (MCP, Custom GPT, NLWeb,
        llms.txt) within five minutes. The partner is responsible for ensuring the
        business has consented to this provisioning and that the data provided is
        accurate.

        Idempotent on `Idempotency-Key` for 24 hours.

        Args:
          postal_code: Italian 5-digit postal code.

          primary_domain: Root domain of the dealer's public website.

          province_code: Italian two-letter province code, e.g., `MI`, `RM`, `TO`.

          vat_number: Italian VAT number, 11 digits prefixed with `IT`.

          activate: If false, dealer is created in inactive state and does not appear in AI surfaces
              until activated.

          contact_phone: E.164 format recommended.

          metadata: Free-form partner-supplied key-value pairs, max 16 keys, values max 500 chars.

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
                    "business_name": business_name,
                    "contact_email": contact_email,
                    "postal_code": postal_code,
                    "primary_domain": primary_domain,
                    "province_code": province_code,
                    "vat_number": vat_number,
                    "activate": activate,
                    "contact_phone": contact_phone,
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
        """
        Get a dealer's full detail

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
        business_name: str | Omit = omit,
        contact_email: str | Omit = omit,
        contact_phone: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        postal_code: str | Omit = omit,
        province_code: str | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerDetail:
        """Partial update of dealer fields.

        Only provided fields are modified. Setting
        `status: "inactive"` removes the dealer from the cross-network AI-citation
        surfaces within five minutes. Reactivation: send `status: "active"`.

        Args:
          status: Toggle activation. Inactive dealers are removed from AI surfaces within 5
              minutes.

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
                    "business_name": business_name,
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
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["active", "inactive", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DealerListResponse:
        """
        Returns a cursor-paginated list of dealers belonging to the calling partner.
        Default ordering: most recently created first.

        Args:
          cursor: Opaque pagination cursor from a previous response's `next_cursor`.

          limit: Maximum number of items to return.

          status: Filter by dealer status.

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
        """Marks the dealer as deleted while preserving the audit trail.

        Unlike
        deactivation (`PATCH status=inactive`), a deleted dealer cannot be reactivated
        by the partner — re-creation requires DealerMAX support. Use deactivation for
        reversible suspensions.

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
        """Per-dealer NLT economics: agency markup percent and three down-payment tiers."""
        return NltSettingsResourceWithRawResponse(self._dealers.nlt_settings)

    @cached_property
    def nlt(self) -> NltResourceWithRawResponse:
        return NltResourceWithRawResponse(self._dealers.nlt)


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
        """Per-dealer NLT economics: agency markup percent and three down-payment tiers."""
        return AsyncNltSettingsResourceWithRawResponse(self._dealers.nlt_settings)

    @cached_property
    def nlt(self) -> AsyncNltResourceWithRawResponse:
        return AsyncNltResourceWithRawResponse(self._dealers.nlt)


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
        """Per-dealer NLT economics: agency markup percent and three down-payment tiers."""
        return NltSettingsResourceWithStreamingResponse(self._dealers.nlt_settings)

    @cached_property
    def nlt(self) -> NltResourceWithStreamingResponse:
        return NltResourceWithStreamingResponse(self._dealers.nlt)


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
        """Per-dealer NLT economics: agency markup percent and three down-payment tiers."""
        return AsyncNltSettingsResourceWithStreamingResponse(self._dealers.nlt_settings)

    @cached_property
    def nlt(self) -> AsyncNltResourceWithStreamingResponse:
        return AsyncNltResourceWithStreamingResponse(self._dealers.nlt)
