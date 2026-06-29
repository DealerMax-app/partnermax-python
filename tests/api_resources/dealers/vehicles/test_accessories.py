# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from partnermax import Partnermax, AsyncPartnermax
from tests.utils import assert_matches_type
from partnermax.types.dealers.vehicles import VehicleAccessoriesCatalog

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Partnermax) -> None:
        accessory = client.dealers.vehicles.accessories.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Partnermax) -> None:
        accessory = client.dealers.vehicles.accessories.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            alloy_wheel_size=13,
            equipment_ids=["string"],
            optional_ids=["string"],
            package_ids=["string"],
        )
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.accessories.with_raw_response.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accessory = response.parse()
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Partnermax) -> None:
        with client.dealers.vehicles.accessories.with_streaming_response.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accessory = response.parse()
            assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.accessories.with_raw_response.update(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.dealers.vehicles.accessories.with_raw_response.update(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refresh_catalog(self, client: Partnermax) -> None:
        accessory = client.dealers.vehicles.accessories.refresh_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refresh_catalog(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.accessories.with_raw_response.refresh_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accessory = response.parse()
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refresh_catalog(self, client: Partnermax) -> None:
        with client.dealers.vehicles.accessories.with_streaming_response.refresh_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accessory = response.parse()
            assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_refresh_catalog(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.accessories.with_raw_response.refresh_catalog(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.dealers.vehicles.accessories.with_raw_response.refresh_catalog(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_catalog(self, client: Partnermax) -> None:
        accessory = client.dealers.vehicles.accessories.retrieve_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_catalog(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.accessories.with_raw_response.retrieve_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accessory = response.parse()
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_catalog(self, client: Partnermax) -> None:
        with client.dealers.vehicles.accessories.with_streaming_response.retrieve_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accessory = response.parse()
            assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_catalog(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.accessories.with_raw_response.retrieve_catalog(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.dealers.vehicles.accessories.with_raw_response.retrieve_catalog(
                vehicle_id="",
                dealer_id="dealer_id",
            )


class TestAsyncAccessories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPartnermax) -> None:
        accessory = await async_client.dealers.vehicles.accessories.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPartnermax) -> None:
        accessory = await async_client.dealers.vehicles.accessories.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            alloy_wheel_size=13,
            equipment_ids=["string"],
            optional_ids=["string"],
            package_ids=["string"],
        )
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.accessories.with_raw_response.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accessory = await response.parse()
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.accessories.with_streaming_response.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accessory = await response.parse()
            assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.accessories.with_raw_response.update(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.dealers.vehicles.accessories.with_raw_response.update(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refresh_catalog(self, async_client: AsyncPartnermax) -> None:
        accessory = await async_client.dealers.vehicles.accessories.refresh_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refresh_catalog(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.accessories.with_raw_response.refresh_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accessory = await response.parse()
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refresh_catalog(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.accessories.with_streaming_response.refresh_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accessory = await response.parse()
            assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_refresh_catalog(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.accessories.with_raw_response.refresh_catalog(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.dealers.vehicles.accessories.with_raw_response.refresh_catalog(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_catalog(self, async_client: AsyncPartnermax) -> None:
        accessory = await async_client.dealers.vehicles.accessories.retrieve_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_catalog(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.accessories.with_raw_response.retrieve_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        accessory = await response.parse()
        assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_catalog(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.accessories.with_streaming_response.retrieve_catalog(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            accessory = await response.parse()
            assert_matches_type(VehicleAccessoriesCatalog, accessory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_catalog(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.accessories.with_raw_response.retrieve_catalog(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.dealers.vehicles.accessories.with_raw_response.retrieve_catalog(
                vehicle_id="",
                dealer_id="dealer_id",
            )
