# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date

import httpx

from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.dealers import (
    vehicle_bulk_params,
    vehicle_list_params,
    vehicle_create_params,
    vehicle_update_params,
    vehicle_retrieve_params,
)
from ....types.dealers.vehicle_list import VehicleList
from ....types.dealers.vehicle_detail import VehicleDetail
from ....types.dealers.bulk_create_vehicles_response import BulkCreateVehiclesResponse

__all__ = ["VehiclesResource", "AsyncVehiclesResource"]


class VehiclesResource(SyncAPIResource):
    """Used-vehicle stock management for partner-owned dealers.

    The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
    """

    @cached_property
    def images(self) -> ImagesResource:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return ImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> VehiclesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return VehiclesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VehiclesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return VehiclesResourceWithStreamingResponse(self)

    def create(
        self,
        dealer_id: str,
        *,
        certified_km: int,
        cost_price_eur: float,
        motornet_code: str,
        plate: str,
        registration_year: int,
        sale_price_eur: float,
        alloy_wheel_size: Optional[int] | Omit = omit,
        color: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        extended_warranty_enabled: bool | Omit = omit,
        extended_warranty_months: Optional[int] | Omit = omit,
        inspection_expiry_date: Union[str, date, None] | Omit = omit,
        is_for_sale: bool | Omit = omit,
        is_visible: bool | Omit = omit,
        last_service_date: Union[str, date, None] | Omit = omit,
        last_service_km: Optional[int] | Omit = omit,
        last_service_notes: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        previous_owner_count: Optional[int] | Omit = omit,
        previous_ownership_transfer_date: Union[str, date, None] | Omit = omit,
        registration_month: Optional[int] | Omit = omit,
        road_tax_expiry_date: Union[str, date, None] | Omit = omit,
        vat_displayed: bool | Omit = omit,
        vehicle_damaged: bool | Omit = omit,
        vin: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleDetail:
        """
        Provision a new used vehicle in a dealer's stock.

        Writes are atomic across `azlease_usatoin` and `azlease_usatoauto` using a
        `SAVEPOINT` so a UNIQUE plate violation rolls back cleanly. On success the
        AI-content worker (:mod:`azurenet-engine.app.jobs.usato_ai_content_worker`)
        picks up the new row within 60 seconds and generates the SEO body + pgvector
        embedding — at which point the vehicle becomes discoverable on the cross-network
        MCP / Custom GPT / NLWeb surfaces. The response returns immediately (no
        synchronous wait on the worker).

        Args:
          certified_km: Certified odometer reading at intake, in kilometres.

          cost_price_eur: Cost basis to the dealer in EUR (partner/dealer internal). Not surfaced on
              consumer-facing AI surfaces; used by dealer reporting and margin analytics only.

          motornet_code: Motornet UNI code identifying the exact vehicle configuration. Must exist in
              `mnet_dettagli_usato` at submission time; otherwise the call returns 422
              `motornet_code_not_in_catalogue`. The partner is expected to source this from
              its own DMS; partnermax does not expose a plate→code lookup.

          plate: Italian licence plate. Uppercased server-side. UNIQUE across the network for
              active vehicles (`visibile=true AND venduto_il IS NULL`); reusable once the
              previous holder sells/hides the row.

          registration_year: Year of first registration. Upper bound is current year + 1.

          sale_price_eur: Public sale price in EUR. Surfaced on MCP / Custom GPT / NLWeb and on the
              dealer's site JSON-LD `Offer.price`.

          description: Partner-supplied long description. Surfaced on the dealer site detail page.

          is_for_sale: Maps to `azlease_usatoauto.is_vendita_enabled`. When false the row is in stock
              but not offered for sale.

          is_visible: Soft-publish flag. When false the row exists in stock but is excluded from
              consumer-facing AI surfaces. Maps to `azlease_usatoin.visibile`.

          notes: Free-form short notes; surfaced as `mnet_dettagli.precisazioni`-style.

          previous_ownership_transfer_date: Date of the most recent ownership transfer, if known.

          registration_month: Month of registration (1–12).

          vat_displayed: If true the public price is displayed VAT-exposed (B2B); otherwise VAT-inclusive
              (B2C).

          vin: ISO 3779 vehicle identification number. Optional but strongly recommended.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/dealers/{dealer_id}/vehicles", dealer_id=dealer_id),
            body=maybe_transform(
                {
                    "certified_km": certified_km,
                    "cost_price_eur": cost_price_eur,
                    "motornet_code": motornet_code,
                    "plate": plate,
                    "registration_year": registration_year,
                    "sale_price_eur": sale_price_eur,
                    "alloy_wheel_size": alloy_wheel_size,
                    "color": color,
                    "description": description,
                    "extended_warranty_enabled": extended_warranty_enabled,
                    "extended_warranty_months": extended_warranty_months,
                    "inspection_expiry_date": inspection_expiry_date,
                    "is_for_sale": is_for_sale,
                    "is_visible": is_visible,
                    "last_service_date": last_service_date,
                    "last_service_km": last_service_km,
                    "last_service_notes": last_service_notes,
                    "notes": notes,
                    "previous_owner_count": previous_owner_count,
                    "previous_ownership_transfer_date": previous_ownership_transfer_date,
                    "registration_month": registration_month,
                    "road_tax_expiry_date": road_tax_expiry_date,
                    "vat_displayed": vat_displayed,
                    "vehicle_damaged": vehicle_damaged,
                    "vin": vin,
                },
                vehicle_create_params.VehicleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleDetail,
        )

    def retrieve(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleDetail:
        """
        Get Vehicle

        Args:
          include_deleted: If true, the detail of a soft-deleted vehicle is returned. Default false —
              soft-deleted rows return 404 to keep behaviour consistent with the list
              endpoint.

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
            path_template("/v1/dealers/{dealer_id}/vehicles/{vehicle_id}", dealer_id=dealer_id, vehicle_id=vehicle_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_deleted": include_deleted}, vehicle_retrieve_params.VehicleRetrieveParams
                ),
            ),
            cast_to=VehicleDetail,
        )

    def update(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        alloy_wheel_size: Optional[int] | Omit = omit,
        certified_km: Optional[int] | Omit = omit,
        color: Optional[str] | Omit = omit,
        cost_price_eur: Optional[float] | Omit = omit,
        description: Optional[str] | Omit = omit,
        extended_warranty_enabled: Optional[bool] | Omit = omit,
        extended_warranty_months: Optional[int] | Omit = omit,
        inspection_expiry_date: Union[str, date, None] | Omit = omit,
        is_for_sale: Optional[bool] | Omit = omit,
        is_visible: Optional[bool] | Omit = omit,
        last_service_date: Union[str, date, None] | Omit = omit,
        last_service_km: Optional[int] | Omit = omit,
        last_service_notes: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        previous_owner_count: Optional[int] | Omit = omit,
        previous_ownership_transfer_date: Union[str, date, None] | Omit = omit,
        registration_month: Optional[int] | Omit = omit,
        road_tax_expiry_date: Union[str, date, None] | Omit = omit,
        sale_price_eur: Optional[float] | Omit = omit,
        vat_displayed: Optional[bool] | Omit = omit,
        vehicle_damaged: Optional[bool] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleDetail:
        """
        Partial update of a vehicle.

        Splits the inbound body across the two physical tables (`azlease_usatoauto` and
        `azlease_usatoin`) and emits at most one UPDATE per table inside a single
        transaction. Fields not present in the body are not touched.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._patch(
            path_template("/v1/dealers/{dealer_id}/vehicles/{vehicle_id}", dealer_id=dealer_id, vehicle_id=vehicle_id),
            body=maybe_transform(
                {
                    "alloy_wheel_size": alloy_wheel_size,
                    "certified_km": certified_km,
                    "color": color,
                    "cost_price_eur": cost_price_eur,
                    "description": description,
                    "extended_warranty_enabled": extended_warranty_enabled,
                    "extended_warranty_months": extended_warranty_months,
                    "inspection_expiry_date": inspection_expiry_date,
                    "is_for_sale": is_for_sale,
                    "is_visible": is_visible,
                    "last_service_date": last_service_date,
                    "last_service_km": last_service_km,
                    "last_service_notes": last_service_notes,
                    "notes": notes,
                    "previous_owner_count": previous_owner_count,
                    "previous_ownership_transfer_date": previous_ownership_transfer_date,
                    "registration_month": registration_month,
                    "road_tax_expiry_date": road_tax_expiry_date,
                    "sale_price_eur": sale_price_eur,
                    "vat_displayed": vat_displayed,
                    "vehicle_damaged": vehicle_damaged,
                },
                vehicle_update_params.VehicleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleDetail,
        )

    def list(
        self,
        dealer_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        include_deleted: bool | Omit = omit,
        is_for_sale: Optional[bool] | Omit = omit,
        is_visible: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleList:
        """
        List vehicles in a dealer's stock owned by the calling partner.

        Cursor pagination is opaque base64url over the last vehicle UUID. Default sort
        is `i.data_inserimento ASC` so freshly provisioned vehicles surface at the tail.
        Soft-deleted rows are excluded unless `include_deleted=true` is set explicitly —
        this preserves the soft-delete semantic across the API contract.

        Args:
          include_deleted: If true, soft-deleted rows (`venduto_il` populated) are also returned. Default
              false — listings hide soft-deleted vehicles.

          is_for_sale: Filter on the sale flag.

          is_visible: Filter on the visibility flag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return self._get(
            path_template("/v1/dealers/{dealer_id}/vehicles", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_deleted": include_deleted,
                        "is_for_sale": is_for_sale,
                        "is_visible": is_visible,
                        "limit": limit,
                    },
                    vehicle_list_params.VehicleListParams,
                ),
            ),
            cast_to=VehicleList,
        )

    def delete(
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
    ) -> None:
        """
        Withdraw a vehicle from sale without deleting the row.

        Sets `azlease_usatoin.visibile = FALSE` and stamps `venduto_il = now()`. The
        plate becomes reusable on the network the moment this returns (the
        active-uniqueness check excludes rows where `visibile = FALSE` OR
        `venduto_il IS NOT NULL`).

        Soft-delete is the canonical "remove this vehicle from sale" surface. The
        AI-citation consumers (MCP `_tool_search_vehicles`, Custom GPT
        `search_vehicles_network`, NLWeb `/ask`) each filter their own queries on
        `i.visibile = TRUE AND i.venduto_il IS NULL` — the shared `v_apimax_listing`
        view itself does not impose that filter, every consumer adds it. The result on
        the partner side is the same: a soft-deleted vehicle disappears from every AI
        surface within the next index cycle.

        Returns `409 vehicle_already_deleted` if the row is already soft- deleted — same
        idempotency pattern as the dealers DELETE endpoint.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/dealers/{dealer_id}/vehicles/{vehicle_id}", dealer_id=dealer_id, vehicle_id=vehicle_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def bulk(
        self,
        dealer_id: str,
        *,
        vehicles: Iterable[vehicle_bulk_params.Vehicle],
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkCreateVehiclesResponse:
        """
        Provision up to `BULK_MAX_ROWS` vehicles in a single synchronous call.

        Each row is processed inside its own `SAVEPOINT` so a failure on row N
        (validation, plate conflict, motornet not in catalogue, race) is isolated — the
        SAVEPOINT rolls back, the per-row outcome is collected with a structured error
        code, and the loop continues with row N+1.

        Successful rows accumulate in the outer transaction and are committed together
        at the end of the request. Failed rows leave no trace in the database.

        Returns `207 Multi-Status`. The response carries:

        - `total`, `succeeded`, `failed` — aggregate counters for quick branch logic on
          the partner side.
        - `results` — array of per-row outcomes, indexed by the position in the request
          `vehicles[]` array. Successful rows include the full `VehicleDetail`; failed
          rows include `error_code` + `error_message` keyed to the same codes as the
          single-POST surface so the partner reuses one error handler for both paths.

        For imports larger than `BULK_MAX_ROWS` (currently 100), the partner is expected
        to chunk the array client-side. A 5 000-vehicle initial migration is 50 calls;
        the partner controls concurrency.

        Args:
          vehicles: Array of vehicles to create. Between 1 and 100 rows per call. For larger
              imports, the partner is expected to chunk client-side (e.g. 50 calls of 100 rows
              each for a 5 000-vehicle migration).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/dealers/{dealer_id}/vehicles/bulk", dealer_id=dealer_id),
            body=maybe_transform({"vehicles": vehicles}, vehicle_bulk_params.VehicleBulkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreateVehiclesResponse,
        )


class AsyncVehiclesResource(AsyncAPIResource):
    """Used-vehicle stock management for partner-owned dealers.

    The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
    """

    @cached_property
    def images(self) -> AsyncImagesResource:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return AsyncImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVehiclesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVehiclesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVehiclesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DealerMax-app/partnermax-python#with_streaming_response
        """
        return AsyncVehiclesResourceWithStreamingResponse(self)

    async def create(
        self,
        dealer_id: str,
        *,
        certified_km: int,
        cost_price_eur: float,
        motornet_code: str,
        plate: str,
        registration_year: int,
        sale_price_eur: float,
        alloy_wheel_size: Optional[int] | Omit = omit,
        color: Optional[str] | Omit = omit,
        description: str | Omit = omit,
        extended_warranty_enabled: bool | Omit = omit,
        extended_warranty_months: Optional[int] | Omit = omit,
        inspection_expiry_date: Union[str, date, None] | Omit = omit,
        is_for_sale: bool | Omit = omit,
        is_visible: bool | Omit = omit,
        last_service_date: Union[str, date, None] | Omit = omit,
        last_service_km: Optional[int] | Omit = omit,
        last_service_notes: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        previous_owner_count: Optional[int] | Omit = omit,
        previous_ownership_transfer_date: Union[str, date, None] | Omit = omit,
        registration_month: Optional[int] | Omit = omit,
        road_tax_expiry_date: Union[str, date, None] | Omit = omit,
        vat_displayed: bool | Omit = omit,
        vehicle_damaged: bool | Omit = omit,
        vin: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleDetail:
        """
        Provision a new used vehicle in a dealer's stock.

        Writes are atomic across `azlease_usatoin` and `azlease_usatoauto` using a
        `SAVEPOINT` so a UNIQUE plate violation rolls back cleanly. On success the
        AI-content worker (:mod:`azurenet-engine.app.jobs.usato_ai_content_worker`)
        picks up the new row within 60 seconds and generates the SEO body + pgvector
        embedding — at which point the vehicle becomes discoverable on the cross-network
        MCP / Custom GPT / NLWeb surfaces. The response returns immediately (no
        synchronous wait on the worker).

        Args:
          certified_km: Certified odometer reading at intake, in kilometres.

          cost_price_eur: Cost basis to the dealer in EUR (partner/dealer internal). Not surfaced on
              consumer-facing AI surfaces; used by dealer reporting and margin analytics only.

          motornet_code: Motornet UNI code identifying the exact vehicle configuration. Must exist in
              `mnet_dettagli_usato` at submission time; otherwise the call returns 422
              `motornet_code_not_in_catalogue`. The partner is expected to source this from
              its own DMS; partnermax does not expose a plate→code lookup.

          plate: Italian licence plate. Uppercased server-side. UNIQUE across the network for
              active vehicles (`visibile=true AND venduto_il IS NULL`); reusable once the
              previous holder sells/hides the row.

          registration_year: Year of first registration. Upper bound is current year + 1.

          sale_price_eur: Public sale price in EUR. Surfaced on MCP / Custom GPT / NLWeb and on the
              dealer's site JSON-LD `Offer.price`.

          description: Partner-supplied long description. Surfaced on the dealer site detail page.

          is_for_sale: Maps to `azlease_usatoauto.is_vendita_enabled`. When false the row is in stock
              but not offered for sale.

          is_visible: Soft-publish flag. When false the row exists in stock but is excluded from
              consumer-facing AI surfaces. Maps to `azlease_usatoin.visibile`.

          notes: Free-form short notes; surfaced as `mnet_dettagli.precisazioni`-style.

          previous_ownership_transfer_date: Date of the most recent ownership transfer, if known.

          registration_month: Month of registration (1–12).

          vat_displayed: If true the public price is displayed VAT-exposed (B2B); otherwise VAT-inclusive
              (B2C).

          vin: ISO 3779 vehicle identification number. Optional but strongly recommended.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/dealers/{dealer_id}/vehicles", dealer_id=dealer_id),
            body=await async_maybe_transform(
                {
                    "certified_km": certified_km,
                    "cost_price_eur": cost_price_eur,
                    "motornet_code": motornet_code,
                    "plate": plate,
                    "registration_year": registration_year,
                    "sale_price_eur": sale_price_eur,
                    "alloy_wheel_size": alloy_wheel_size,
                    "color": color,
                    "description": description,
                    "extended_warranty_enabled": extended_warranty_enabled,
                    "extended_warranty_months": extended_warranty_months,
                    "inspection_expiry_date": inspection_expiry_date,
                    "is_for_sale": is_for_sale,
                    "is_visible": is_visible,
                    "last_service_date": last_service_date,
                    "last_service_km": last_service_km,
                    "last_service_notes": last_service_notes,
                    "notes": notes,
                    "previous_owner_count": previous_owner_count,
                    "previous_ownership_transfer_date": previous_ownership_transfer_date,
                    "registration_month": registration_month,
                    "road_tax_expiry_date": road_tax_expiry_date,
                    "vat_displayed": vat_displayed,
                    "vehicle_damaged": vehicle_damaged,
                    "vin": vin,
                },
                vehicle_create_params.VehicleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleDetail,
        )

    async def retrieve(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleDetail:
        """
        Get Vehicle

        Args:
          include_deleted: If true, the detail of a soft-deleted vehicle is returned. Default false —
              soft-deleted rows return 404 to keep behaviour consistent with the list
              endpoint.

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
            path_template("/v1/dealers/{dealer_id}/vehicles/{vehicle_id}", dealer_id=dealer_id, vehicle_id=vehicle_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_deleted": include_deleted}, vehicle_retrieve_params.VehicleRetrieveParams
                ),
            ),
            cast_to=VehicleDetail,
        )

    async def update(
        self,
        vehicle_id: str,
        *,
        dealer_id: str,
        alloy_wheel_size: Optional[int] | Omit = omit,
        certified_km: Optional[int] | Omit = omit,
        color: Optional[str] | Omit = omit,
        cost_price_eur: Optional[float] | Omit = omit,
        description: Optional[str] | Omit = omit,
        extended_warranty_enabled: Optional[bool] | Omit = omit,
        extended_warranty_months: Optional[int] | Omit = omit,
        inspection_expiry_date: Union[str, date, None] | Omit = omit,
        is_for_sale: Optional[bool] | Omit = omit,
        is_visible: Optional[bool] | Omit = omit,
        last_service_date: Union[str, date, None] | Omit = omit,
        last_service_km: Optional[int] | Omit = omit,
        last_service_notes: Optional[str] | Omit = omit,
        notes: Optional[str] | Omit = omit,
        previous_owner_count: Optional[int] | Omit = omit,
        previous_ownership_transfer_date: Union[str, date, None] | Omit = omit,
        registration_month: Optional[int] | Omit = omit,
        road_tax_expiry_date: Union[str, date, None] | Omit = omit,
        sale_price_eur: Optional[float] | Omit = omit,
        vat_displayed: Optional[bool] | Omit = omit,
        vehicle_damaged: Optional[bool] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleDetail:
        """
        Partial update of a vehicle.

        Splits the inbound body across the two physical tables (`azlease_usatoauto` and
        `azlease_usatoin`) and emits at most one UPDATE per table inside a single
        transaction. Fields not present in the body are not touched.

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
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._patch(
            path_template("/v1/dealers/{dealer_id}/vehicles/{vehicle_id}", dealer_id=dealer_id, vehicle_id=vehicle_id),
            body=await async_maybe_transform(
                {
                    "alloy_wheel_size": alloy_wheel_size,
                    "certified_km": certified_km,
                    "color": color,
                    "cost_price_eur": cost_price_eur,
                    "description": description,
                    "extended_warranty_enabled": extended_warranty_enabled,
                    "extended_warranty_months": extended_warranty_months,
                    "inspection_expiry_date": inspection_expiry_date,
                    "is_for_sale": is_for_sale,
                    "is_visible": is_visible,
                    "last_service_date": last_service_date,
                    "last_service_km": last_service_km,
                    "last_service_notes": last_service_notes,
                    "notes": notes,
                    "previous_owner_count": previous_owner_count,
                    "previous_ownership_transfer_date": previous_ownership_transfer_date,
                    "registration_month": registration_month,
                    "road_tax_expiry_date": road_tax_expiry_date,
                    "sale_price_eur": sale_price_eur,
                    "vat_displayed": vat_displayed,
                    "vehicle_damaged": vehicle_damaged,
                },
                vehicle_update_params.VehicleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VehicleDetail,
        )

    async def list(
        self,
        dealer_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        include_deleted: bool | Omit = omit,
        is_for_sale: Optional[bool] | Omit = omit,
        is_visible: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VehicleList:
        """
        List vehicles in a dealer's stock owned by the calling partner.

        Cursor pagination is opaque base64url over the last vehicle UUID. Default sort
        is `i.data_inserimento ASC` so freshly provisioned vehicles surface at the tail.
        Soft-deleted rows are excluded unless `include_deleted=true` is set explicitly —
        this preserves the soft-delete semantic across the API contract.

        Args:
          include_deleted: If true, soft-deleted rows (`venduto_il` populated) are also returned. Default
              false — listings hide soft-deleted vehicles.

          is_for_sale: Filter on the sale flag.

          is_visible: Filter on the visibility flag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        return await self._get(
            path_template("/v1/dealers/{dealer_id}/vehicles", dealer_id=dealer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "include_deleted": include_deleted,
                        "is_for_sale": is_for_sale,
                        "is_visible": is_visible,
                        "limit": limit,
                    },
                    vehicle_list_params.VehicleListParams,
                ),
            ),
            cast_to=VehicleList,
        )

    async def delete(
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
    ) -> None:
        """
        Withdraw a vehicle from sale without deleting the row.

        Sets `azlease_usatoin.visibile = FALSE` and stamps `venduto_il = now()`. The
        plate becomes reusable on the network the moment this returns (the
        active-uniqueness check excludes rows where `visibile = FALSE` OR
        `venduto_il IS NOT NULL`).

        Soft-delete is the canonical "remove this vehicle from sale" surface. The
        AI-citation consumers (MCP `_tool_search_vehicles`, Custom GPT
        `search_vehicles_network`, NLWeb `/ask`) each filter their own queries on
        `i.visibile = TRUE AND i.venduto_il IS NULL` — the shared `v_apimax_listing`
        view itself does not impose that filter, every consumer adds it. The result on
        the partner side is the same: a soft-deleted vehicle disappears from every AI
        surface within the next index cycle.

        Returns `409 vehicle_already_deleted` if the row is already soft- deleted — same
        idempotency pattern as the dealers DELETE endpoint.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/dealers/{dealer_id}/vehicles/{vehicle_id}", dealer_id=dealer_id, vehicle_id=vehicle_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def bulk(
        self,
        dealer_id: str,
        *,
        vehicles: Iterable[vehicle_bulk_params.Vehicle],
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkCreateVehiclesResponse:
        """
        Provision up to `BULK_MAX_ROWS` vehicles in a single synchronous call.

        Each row is processed inside its own `SAVEPOINT` so a failure on row N
        (validation, plate conflict, motornet not in catalogue, race) is isolated — the
        SAVEPOINT rolls back, the per-row outcome is collected with a structured error
        code, and the loop continues with row N+1.

        Successful rows accumulate in the outer transaction and are committed together
        at the end of the request. Failed rows leave no trace in the database.

        Returns `207 Multi-Status`. The response carries:

        - `total`, `succeeded`, `failed` — aggregate counters for quick branch logic on
          the partner side.
        - `results` — array of per-row outcomes, indexed by the position in the request
          `vehicles[]` array. Successful rows include the full `VehicleDetail`; failed
          rows include `error_code` + `error_message` keyed to the same codes as the
          single-POST surface so the partner reuses one error handler for both paths.

        For imports larger than `BULK_MAX_ROWS` (currently 100), the partner is expected
        to chunk the array client-side. A 5 000-vehicle initial migration is 50 calls;
        the partner controls concurrency.

        Args:
          vehicles: Array of vehicles to create. Between 1 and 100 rows per call. For larger
              imports, the partner is expected to chunk client-side (e.g. 50 calls of 100 rows
              each for a 5 000-vehicle migration).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dealer_id:
            raise ValueError(f"Expected a non-empty value for `dealer_id` but received {dealer_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/dealers/{dealer_id}/vehicles/bulk", dealer_id=dealer_id),
            body=await async_maybe_transform({"vehicles": vehicles}, vehicle_bulk_params.VehicleBulkParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkCreateVehiclesResponse,
        )


class VehiclesResourceWithRawResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

        self.create = to_raw_response_wrapper(
            vehicles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vehicles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            vehicles.update,
        )
        self.list = to_raw_response_wrapper(
            vehicles.list,
        )
        self.delete = to_raw_response_wrapper(
            vehicles.delete,
        )
        self.bulk = to_raw_response_wrapper(
            vehicles.bulk,
        )

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return ImagesResourceWithRawResponse(self._vehicles.images)


class AsyncVehiclesResourceWithRawResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

        self.create = async_to_raw_response_wrapper(
            vehicles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            vehicles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            vehicles.update,
        )
        self.list = async_to_raw_response_wrapper(
            vehicles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vehicles.delete,
        )
        self.bulk = async_to_raw_response_wrapper(
            vehicles.bulk,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return AsyncImagesResourceWithRawResponse(self._vehicles.images)


class VehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: VehiclesResource) -> None:
        self._vehicles = vehicles

        self.create = to_streamed_response_wrapper(
            vehicles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            vehicles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            vehicles.update,
        )
        self.list = to_streamed_response_wrapper(
            vehicles.list,
        )
        self.delete = to_streamed_response_wrapper(
            vehicles.delete,
        )
        self.bulk = to_streamed_response_wrapper(
            vehicles.bulk,
        )

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return ImagesResourceWithStreamingResponse(self._vehicles.images)


class AsyncVehiclesResourceWithStreamingResponse:
    def __init__(self, vehicles: AsyncVehiclesResource) -> None:
        self._vehicles = vehicles

        self.create = async_to_streamed_response_wrapper(
            vehicles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            vehicles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            vehicles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            vehicles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vehicles.delete,
        )
        self.bulk = async_to_streamed_response_wrapper(
            vehicles.bulk,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        """Used-vehicle stock management for partner-owned dealers.

        The partner uploads each used vehicle by its canonical Motornet UNI code; DealerMAX joins the partner-provided pricing and stock metadata with the catalog master so the resulting listing is immediately indexed by the AI surfaces (MCP server, ChatGPT Custom GPT, NLWeb /ask, and the SEO/JSON-LD layer).
        """
        return AsyncImagesResourceWithStreamingResponse(self._vehicles.images)
