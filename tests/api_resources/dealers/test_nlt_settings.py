# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from partnermax import Partnermax, AsyncPartnermax
from tests.utils import assert_matches_type
from partnermax.types.dealers import NltSettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNltSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Partnermax) -> None:
        nlt_setting = client.dealers.nlt_settings.retrieve(
            "dealer_id",
        )
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Partnermax) -> None:
        response = client.dealers.nlt_settings.with_raw_response.retrieve(
            "dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nlt_setting = response.parse()
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Partnermax) -> None:
        with client.dealers.nlt_settings.with_streaming_response.retrieve(
            "dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nlt_setting = response.parse()
            assert_matches_type(NltSettings, nlt_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.nlt_settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Partnermax) -> None:
        nlt_setting = client.dealers.nlt_settings.update(
            dealer_id="dealer_id",
            agency_markup_percent=0,
            down_payment_tiers={
                "high": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "low": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "medium": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
            },
        )
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Partnermax) -> None:
        nlt_setting = client.dealers.nlt_settings.update(
            dealer_id="dealer_id",
            agency_markup_percent=0,
            down_payment_tiers={
                "high": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "low": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "medium": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
            },
            currency="EUR",
            image_mode="branded",
            image_scenario_locked="mediterraneo",
        )
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Partnermax) -> None:
        response = client.dealers.nlt_settings.with_raw_response.update(
            dealer_id="dealer_id",
            agency_markup_percent=0,
            down_payment_tiers={
                "high": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "low": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "medium": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nlt_setting = response.parse()
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Partnermax) -> None:
        with client.dealers.nlt_settings.with_streaming_response.update(
            dealer_id="dealer_id",
            agency_markup_percent=0,
            down_payment_tiers={
                "high": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "low": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "medium": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nlt_setting = response.parse()
            assert_matches_type(NltSettings, nlt_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.nlt_settings.with_raw_response.update(
                dealer_id="",
                agency_markup_percent=0,
                down_payment_tiers={
                    "high": {
                        "fixed_eur": 0,
                        "percent_of_list": 0,
                    },
                    "low": {
                        "fixed_eur": 0,
                        "percent_of_list": 0,
                    },
                    "medium": {
                        "fixed_eur": 0,
                        "percent_of_list": 0,
                    },
                },
            )


class TestAsyncNltSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPartnermax) -> None:
        nlt_setting = await async_client.dealers.nlt_settings.retrieve(
            "dealer_id",
        )
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.nlt_settings.with_raw_response.retrieve(
            "dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nlt_setting = await response.parse()
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.nlt_settings.with_streaming_response.retrieve(
            "dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nlt_setting = await response.parse()
            assert_matches_type(NltSettings, nlt_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.nlt_settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPartnermax) -> None:
        nlt_setting = await async_client.dealers.nlt_settings.update(
            dealer_id="dealer_id",
            agency_markup_percent=0,
            down_payment_tiers={
                "high": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "low": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "medium": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
            },
        )
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPartnermax) -> None:
        nlt_setting = await async_client.dealers.nlt_settings.update(
            dealer_id="dealer_id",
            agency_markup_percent=0,
            down_payment_tiers={
                "high": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "low": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "medium": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
            },
            currency="EUR",
            image_mode="branded",
            image_scenario_locked="mediterraneo",
        )
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.nlt_settings.with_raw_response.update(
            dealer_id="dealer_id",
            agency_markup_percent=0,
            down_payment_tiers={
                "high": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "low": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "medium": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nlt_setting = await response.parse()
        assert_matches_type(NltSettings, nlt_setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.nlt_settings.with_streaming_response.update(
            dealer_id="dealer_id",
            agency_markup_percent=0,
            down_payment_tiers={
                "high": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "low": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
                "medium": {
                    "fixed_eur": 0,
                    "percent_of_list": 0,
                },
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nlt_setting = await response.parse()
            assert_matches_type(NltSettings, nlt_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.nlt_settings.with_raw_response.update(
                dealer_id="",
                agency_markup_percent=0,
                down_payment_tiers={
                    "high": {
                        "fixed_eur": 0,
                        "percent_of_list": 0,
                    },
                    "low": {
                        "fixed_eur": 0,
                        "percent_of_list": 0,
                    },
                    "medium": {
                        "fixed_eur": 0,
                        "percent_of_list": 0,
                    },
                },
            )
