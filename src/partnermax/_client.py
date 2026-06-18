# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import keys, dealers
    from .resources.keys import KeysResource, AsyncKeysResource
    from .resources.dealers.dealers import DealersResource, AsyncDealersResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Partnermax",
    "AsyncPartnermax",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://developers.dealermax.app",
    "sandbox": "https://sandbox.developers.dealermax.app",
}


class Partnermax(SyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Partnermax client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `PARTNERMAX_API_KEY`
        - `bearer_token` from `PARTNERMAX_BEARER_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("PARTNERMAX_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("PARTNERMAX_BEARER_TOKEN")
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("PARTNERMAX_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PARTNERMAX_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("PARTNERMAX_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def keys(self) -> KeysResource:
        """API key lifecycle management — issue, list, revoke.

        The partner authenticates every request with `X-Api-Key` (preferred) or `Authorization: Bearer <key>`; the server identifies the partner from the key and scopes all reads/writes to dealers owned by that partner.
        """
        from .resources.keys import KeysResource

        return KeysResource(self)

    @cached_property
    def dealers(self) -> DealersResource:
        """Provision, update, deactivate, and list dealers owned by the calling partner."""
        from .resources.dealers import DealersResource

        return DealersResource(self)

    @cached_property
    def with_raw_response(self) -> PartnermaxWithRawResponse:
        return PartnermaxWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartnermaxWithStreamedResponse:
        return PartnermaxWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("api_key_auth", False):
            for key, value in self._api_key_auth.items():
                headers.setdefault(key, value)
        if security.get("bearer_auth", False):
            for key, value in self._bearer_auth.items():
                headers.setdefault(key, value)
        return headers

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Api-Key": api_key}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("X-Api-Key") or isinstance(custom_headers.get("X-Api-Key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or bearer_token to be set. Or for one of the `X-Api-Key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPartnermax(AsyncAPIClient):
    # client options
    api_key: str | None
    bearer_token: str | None

    _environment: Literal["production", "sandbox"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "sandbox"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncPartnermax client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `PARTNERMAX_API_KEY`
        - `bearer_token` from `PARTNERMAX_BEARER_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("PARTNERMAX_API_KEY")
        self.api_key = api_key

        if bearer_token is None:
            bearer_token = os.environ.get("PARTNERMAX_BEARER_TOKEN")
        self.bearer_token = bearer_token

        self._environment = environment

        base_url_env = os.environ.get("PARTNERMAX_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PARTNERMAX_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        custom_headers_env = os.environ.get("PARTNERMAX_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def keys(self) -> AsyncKeysResource:
        """API key lifecycle management — issue, list, revoke.

        The partner authenticates every request with `X-Api-Key` (preferred) or `Authorization: Bearer <key>`; the server identifies the partner from the key and scopes all reads/writes to dealers owned by that partner.
        """
        from .resources.keys import AsyncKeysResource

        return AsyncKeysResource(self)

    @cached_property
    def dealers(self) -> AsyncDealersResource:
        """Provision, update, deactivate, and list dealers owned by the calling partner."""
        from .resources.dealers import AsyncDealersResource

        return AsyncDealersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPartnermaxWithRawResponse:
        return AsyncPartnermaxWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartnermaxWithStreamedResponse:
        return AsyncPartnermaxWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("api_key_auth", False):
            for key, value in self._api_key_auth.items():
                headers.setdefault(key, value)
        if security.get("bearer_auth", False):
            for key, value in self._bearer_auth.items():
                headers.setdefault(key, value)
        return headers

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"X-Api-Key": api_key}

    @property
    def _bearer_auth(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("X-Api-Key") or isinstance(custom_headers.get("X-Api-Key"), Omit):
            return

        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or bearer_token to be set. Or for one of the `X-Api-Key` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PartnermaxWithRawResponse:
    _client: Partnermax

    def __init__(self, client: Partnermax) -> None:
        self._client = client

    @cached_property
    def keys(self) -> keys.KeysResourceWithRawResponse:
        """API key lifecycle management — issue, list, revoke.

        The partner authenticates every request with `X-Api-Key` (preferred) or `Authorization: Bearer <key>`; the server identifies the partner from the key and scopes all reads/writes to dealers owned by that partner.
        """
        from .resources.keys import KeysResourceWithRawResponse

        return KeysResourceWithRawResponse(self._client.keys)

    @cached_property
    def dealers(self) -> dealers.DealersResourceWithRawResponse:
        """Provision, update, deactivate, and list dealers owned by the calling partner."""
        from .resources.dealers import DealersResourceWithRawResponse

        return DealersResourceWithRawResponse(self._client.dealers)


class AsyncPartnermaxWithRawResponse:
    _client: AsyncPartnermax

    def __init__(self, client: AsyncPartnermax) -> None:
        self._client = client

    @cached_property
    def keys(self) -> keys.AsyncKeysResourceWithRawResponse:
        """API key lifecycle management — issue, list, revoke.

        The partner authenticates every request with `X-Api-Key` (preferred) or `Authorization: Bearer <key>`; the server identifies the partner from the key and scopes all reads/writes to dealers owned by that partner.
        """
        from .resources.keys import AsyncKeysResourceWithRawResponse

        return AsyncKeysResourceWithRawResponse(self._client.keys)

    @cached_property
    def dealers(self) -> dealers.AsyncDealersResourceWithRawResponse:
        """Provision, update, deactivate, and list dealers owned by the calling partner."""
        from .resources.dealers import AsyncDealersResourceWithRawResponse

        return AsyncDealersResourceWithRawResponse(self._client.dealers)


class PartnermaxWithStreamedResponse:
    _client: Partnermax

    def __init__(self, client: Partnermax) -> None:
        self._client = client

    @cached_property
    def keys(self) -> keys.KeysResourceWithStreamingResponse:
        """API key lifecycle management — issue, list, revoke.

        The partner authenticates every request with `X-Api-Key` (preferred) or `Authorization: Bearer <key>`; the server identifies the partner from the key and scopes all reads/writes to dealers owned by that partner.
        """
        from .resources.keys import KeysResourceWithStreamingResponse

        return KeysResourceWithStreamingResponse(self._client.keys)

    @cached_property
    def dealers(self) -> dealers.DealersResourceWithStreamingResponse:
        """Provision, update, deactivate, and list dealers owned by the calling partner."""
        from .resources.dealers import DealersResourceWithStreamingResponse

        return DealersResourceWithStreamingResponse(self._client.dealers)


class AsyncPartnermaxWithStreamedResponse:
    _client: AsyncPartnermax

    def __init__(self, client: AsyncPartnermax) -> None:
        self._client = client

    @cached_property
    def keys(self) -> keys.AsyncKeysResourceWithStreamingResponse:
        """API key lifecycle management — issue, list, revoke.

        The partner authenticates every request with `X-Api-Key` (preferred) or `Authorization: Bearer <key>`; the server identifies the partner from the key and scopes all reads/writes to dealers owned by that partner.
        """
        from .resources.keys import AsyncKeysResourceWithStreamingResponse

        return AsyncKeysResourceWithStreamingResponse(self._client.keys)

    @cached_property
    def dealers(self) -> dealers.AsyncDealersResourceWithStreamingResponse:
        """Provision, update, deactivate, and list dealers owned by the calling partner."""
        from .resources.dealers import AsyncDealersResourceWithStreamingResponse

        return AsyncDealersResourceWithStreamingResponse(self._client.dealers)


Client = Partnermax

AsyncClient = AsyncPartnermax
