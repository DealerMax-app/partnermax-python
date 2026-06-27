# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from partnermax import Partnermax, AsyncPartnermax
from tests.utils import assert_matches_type
from partnermax.types.dealers.vehicles import VehicleImage, VehicleImageList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Partnermax) -> None:
        image = client.dealers.vehicles.images.create(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            file="file",
        )
        assert_matches_type(VehicleImage, image, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.images.with_raw_response.create(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            file="file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(VehicleImage, image, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Partnermax) -> None:
        with client.dealers.vehicles.images.with_streaming_response.create(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            file="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(VehicleImage, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.images.with_raw_response.create(
                vehicle_id="vehicle_id",
                dealer_id="",
                file="file",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.dealers.vehicles.images.with_raw_response.create(
                vehicle_id="",
                dealer_id="dealer_id",
                file="file",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Partnermax) -> None:
        image = client.dealers.vehicles.images.list(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleImageList, image, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.images.with_raw_response.list(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert_matches_type(VehicleImageList, image, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Partnermax) -> None:
        with client.dealers.vehicles.images.with_streaming_response.list(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert_matches_type(VehicleImageList, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.images.with_raw_response.list(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.dealers.vehicles.images.with_raw_response.list(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Partnermax) -> None:
        image = client.dealers.vehicles.images.delete(
            image_id="image_id",
            dealer_id="dealer_id",
            vehicle_id="vehicle_id",
        )
        assert image is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.images.with_raw_response.delete(
            image_id="image_id",
            dealer_id="dealer_id",
            vehicle_id="vehicle_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = response.parse()
        assert image is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Partnermax) -> None:
        with client.dealers.vehicles.images.with_streaming_response.delete(
            image_id="image_id",
            dealer_id="dealer_id",
            vehicle_id="vehicle_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = response.parse()
            assert image is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.images.with_raw_response.delete(
                image_id="image_id",
                dealer_id="",
                vehicle_id="vehicle_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.dealers.vehicles.images.with_raw_response.delete(
                image_id="image_id",
                dealer_id="dealer_id",
                vehicle_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.dealers.vehicles.images.with_raw_response.delete(
                image_id="",
                dealer_id="dealer_id",
                vehicle_id="vehicle_id",
            )


class TestAsyncImages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPartnermax) -> None:
        image = await async_client.dealers.vehicles.images.create(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            file="file",
        )
        assert_matches_type(VehicleImage, image, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.images.with_raw_response.create(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            file="file",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(VehicleImage, image, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.images.with_streaming_response.create(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            file="file",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(VehicleImage, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.images.with_raw_response.create(
                vehicle_id="vehicle_id",
                dealer_id="",
                file="file",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.dealers.vehicles.images.with_raw_response.create(
                vehicle_id="",
                dealer_id="dealer_id",
                file="file",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPartnermax) -> None:
        image = await async_client.dealers.vehicles.images.list(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleImageList, image, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.images.with_raw_response.list(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert_matches_type(VehicleImageList, image, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.images.with_streaming_response.list(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert_matches_type(VehicleImageList, image, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.images.with_raw_response.list(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.dealers.vehicles.images.with_raw_response.list(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPartnermax) -> None:
        image = await async_client.dealers.vehicles.images.delete(
            image_id="image_id",
            dealer_id="dealer_id",
            vehicle_id="vehicle_id",
        )
        assert image is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.images.with_raw_response.delete(
            image_id="image_id",
            dealer_id="dealer_id",
            vehicle_id="vehicle_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        image = await response.parse()
        assert image is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.images.with_streaming_response.delete(
            image_id="image_id",
            dealer_id="dealer_id",
            vehicle_id="vehicle_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            image = await response.parse()
            assert image is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.images.with_raw_response.delete(
                image_id="image_id",
                dealer_id="",
                vehicle_id="vehicle_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.dealers.vehicles.images.with_raw_response.delete(
                image_id="image_id",
                dealer_id="dealer_id",
                vehicle_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.dealers.vehicles.images.with_raw_response.delete(
                image_id="",
                dealer_id="dealer_id",
                vehicle_id="vehicle_id",
            )
