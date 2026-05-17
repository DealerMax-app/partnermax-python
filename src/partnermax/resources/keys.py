# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import key_issue_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.key_list_response import KeyListResponse
from ..types.key_issue_response import KeyIssueResponse

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    """API key lifecycle management — issue, list, revoke.

    The partner authenticates every request with `X-Api-Key` (preferred) or `Authorization: Bearer <key>`; the server identifies the partner from the key and scopes all reads/writes to dealers owned by that partner.
    """

    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return KeysResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyListResponse:
        """Returns metadata for all active keys belonging to the calling partner.

        Key
        material is never returned — only the prefix (first 8 characters) for safe
        logging and identification.
        """
        return self._get(
            "/v1/keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyListResponse,
        )

    def issue(
        self,
        *,
        label: str,
        expires_at: Union[str, datetime] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyIssueResponse:
        """Creates a new API key for the calling partner.

        The key material is returned in
        plaintext in the response and is never retrievable again — store it securely on
        first receipt. Must be called with an existing API key that has the
        `can_issue_keys` capability (the initial key issued by DealerMAX support has
        this capability by default; rotated keys inherit it unless explicitly scoped
        down).

        Args:
          label: Human-readable identifier for this key, used for safe logging.

          expires_at: Optional expiry timestamp. Null = never expires until revoked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/v1/keys/issue",
            body=maybe_transform(
                {
                    "label": label,
                    "expires_at": expires_at,
                },
                key_issue_params.KeyIssueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyIssueResponse,
        )

    def revoke(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Immediately invalidates the specified key.

        Any in-flight requests using this key
        will continue until completion; subsequent requests will receive 401
        invalid_api_key. Revocation is logged in the audit trail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/keys/{key_id}", key_id=key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncKeysResource(AsyncAPIResource):
    """API key lifecycle management — issue, list, revoke.

    The partner authenticates every request with `X-Api-Key` (preferred) or `Authorization: Bearer <key>`; the server identifies the partner from the key and scopes all reads/writes to dealers owned by that partner.
    """

    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return AsyncKeysResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyListResponse:
        """Returns metadata for all active keys belonging to the calling partner.

        Key
        material is never returned — only the prefix (first 8 characters) for safe
        logging and identification.
        """
        return await self._get(
            "/v1/keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyListResponse,
        )

    async def issue(
        self,
        *,
        label: str,
        expires_at: Union[str, datetime] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyIssueResponse:
        """Creates a new API key for the calling partner.

        The key material is returned in
        plaintext in the response and is never retrievable again — store it securely on
        first receipt. Must be called with an existing API key that has the
        `can_issue_keys` capability (the initial key issued by DealerMAX support has
        this capability by default; rotated keys inherit it unless explicitly scoped
        down).

        Args:
          label: Human-readable identifier for this key, used for safe logging.

          expires_at: Optional expiry timestamp. Null = never expires until revoked.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/v1/keys/issue",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "expires_at": expires_at,
                },
                key_issue_params.KeyIssueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeyIssueResponse,
        )

    async def revoke(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Immediately invalidates the specified key.

        Any in-flight requests using this key
        will continue until completion; subsequent requests will receive 401
        invalid_api_key. Revocation is logged in the audit trail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/keys/{key_id}", key_id=key_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.list = to_raw_response_wrapper(
            keys.list,
        )
        self.issue = to_raw_response_wrapper(
            keys.issue,
        )
        self.revoke = to_raw_response_wrapper(
            keys.revoke,
        )


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.list = async_to_raw_response_wrapper(
            keys.list,
        )
        self.issue = async_to_raw_response_wrapper(
            keys.issue,
        )
        self.revoke = async_to_raw_response_wrapper(
            keys.revoke,
        )


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.list = to_streamed_response_wrapper(
            keys.list,
        )
        self.issue = to_streamed_response_wrapper(
            keys.issue,
        )
        self.revoke = to_streamed_response_wrapper(
            keys.revoke,
        )


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
        self.issue = async_to_streamed_response_wrapper(
            keys.issue,
        )
        self.revoke = async_to_streamed_response_wrapper(
            keys.revoke,
        )
