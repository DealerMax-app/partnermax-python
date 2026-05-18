# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .offers import (
    OffersResource,
    AsyncOffersResource,
    OffersResourceWithRawResponse,
    AsyncOffersResourceWithRawResponse,
    OffersResourceWithStreamingResponse,
    AsyncOffersResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["NltResource", "AsyncNltResource"]


class NltResource(SyncAPIResource):
    @cached_property
    def offers(self) -> OffersResource:
        return OffersResource(self._client)

    @cached_property
    def with_raw_response(self) -> NltResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return NltResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NltResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return NltResourceWithStreamingResponse(self)


class AsyncNltResource(AsyncAPIResource):
    @cached_property
    def offers(self) -> AsyncOffersResource:
        return AsyncOffersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNltResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNltResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNltResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return AsyncNltResourceWithStreamingResponse(self)


class NltResourceWithRawResponse:
    def __init__(self, nlt: NltResource) -> None:
        self._nlt = nlt

    @cached_property
    def offers(self) -> OffersResourceWithRawResponse:
        return OffersResourceWithRawResponse(self._nlt.offers)


class AsyncNltResourceWithRawResponse:
    def __init__(self, nlt: AsyncNltResource) -> None:
        self._nlt = nlt

    @cached_property
    def offers(self) -> AsyncOffersResourceWithRawResponse:
        return AsyncOffersResourceWithRawResponse(self._nlt.offers)


class NltResourceWithStreamingResponse:
    def __init__(self, nlt: NltResource) -> None:
        self._nlt = nlt

    @cached_property
    def offers(self) -> OffersResourceWithStreamingResponse:
        return OffersResourceWithStreamingResponse(self._nlt.offers)


class AsyncNltResourceWithStreamingResponse:
    def __init__(self, nlt: AsyncNltResource) -> None:
        self._nlt = nlt

    @cached_property
    def offers(self) -> AsyncOffersResourceWithStreamingResponse:
        return AsyncOffersResourceWithStreamingResponse(self._nlt.offers)
