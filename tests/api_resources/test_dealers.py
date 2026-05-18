# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from partnermax import Partnermax, AsyncPartnermax
from tests.utils import assert_matches_type
from partnermax.types import (
    DealerDetail,
    DealerListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDealers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Partnermax) -> None:
        dealer = client.dealers.create(
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            postal_code="21029",
            primary_domain="29-0.mi-57.16u-2d91-aha.o-l7c19m0.z.9zhin-8ja2-7.447----86.6.61--5-6.2.3-i2al.r.name",
            province_code="SE",
            vat_number="IT21029798095",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Partnermax) -> None:
        dealer = client.dealers.create(
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            postal_code="21029",
            primary_domain="29-0.mi-57.16u-2d91-aha.o-l7c19m0.z.9zhin-8ja2-7.447----86.6.61--5-6.2.3-i2al.r.name",
            province_code="SE",
            vat_number="IT21029798095",
            activate=True,
            metadata={"foo": "string"},
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Partnermax) -> None:
        response = client.dealers.with_raw_response.create(
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            postal_code="21029",
            primary_domain="29-0.mi-57.16u-2d91-aha.o-l7c19m0.z.9zhin-8ja2-7.447----86.6.61--5-6.2.3-i2al.r.name",
            province_code="SE",
            vat_number="IT21029798095",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = response.parse()
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Partnermax) -> None:
        with client.dealers.with_streaming_response.create(
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            postal_code="21029",
            primary_domain="29-0.mi-57.16u-2d91-aha.o-l7c19m0.z.9zhin-8ja2-7.447----86.6.61--5-6.2.3-i2al.r.name",
            province_code="SE",
            vat_number="IT21029798095",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = response.parse()
            assert_matches_type(DealerDetail, dealer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Partnermax) -> None:
        dealer = client.dealers.retrieve(
            "dealer_id",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Partnermax) -> None:
        response = client.dealers.with_raw_response.retrieve(
            "dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = response.parse()
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Partnermax) -> None:
        with client.dealers.with_streaming_response.retrieve(
            "dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = response.parse()
            assert_matches_type(DealerDetail, dealer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Partnermax) -> None:
        dealer = client.dealers.update(
            dealer_id="dealer_id",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Partnermax) -> None:
        dealer = client.dealers.update(
            dealer_id="dealer_id",
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            metadata={"foo": "string"},
            postal_code="21029",
            province_code="SE",
            status="active",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Partnermax) -> None:
        response = client.dealers.with_raw_response.update(
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = response.parse()
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Partnermax) -> None:
        with client.dealers.with_streaming_response.update(
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = response.parse()
            assert_matches_type(DealerDetail, dealer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.with_raw_response.update(
                dealer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Partnermax) -> None:
        dealer = client.dealers.list()
        assert_matches_type(DealerListResponse, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Partnermax) -> None:
        dealer = client.dealers.list(
            cursor="cursor",
            limit=1,
            status="active",
        )
        assert_matches_type(DealerListResponse, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Partnermax) -> None:
        response = client.dealers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = response.parse()
        assert_matches_type(DealerListResponse, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Partnermax) -> None:
        with client.dealers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = response.parse()
            assert_matches_type(DealerListResponse, dealer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Partnermax) -> None:
        dealer = client.dealers.delete(
            "dealer_id",
        )
        assert dealer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Partnermax) -> None:
        response = client.dealers.with_raw_response.delete(
            "dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = response.parse()
        assert dealer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Partnermax) -> None:
        with client.dealers.with_streaming_response.delete(
            "dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = response.parse()
            assert dealer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.with_raw_response.delete(
                "",
            )


class TestAsyncDealers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPartnermax) -> None:
        dealer = await async_client.dealers.create(
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            postal_code="21029",
            primary_domain="29-0.mi-57.16u-2d91-aha.o-l7c19m0.z.9zhin-8ja2-7.447----86.6.61--5-6.2.3-i2al.r.name",
            province_code="SE",
            vat_number="IT21029798095",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPartnermax) -> None:
        dealer = await async_client.dealers.create(
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            postal_code="21029",
            primary_domain="29-0.mi-57.16u-2d91-aha.o-l7c19m0.z.9zhin-8ja2-7.447----86.6.61--5-6.2.3-i2al.r.name",
            province_code="SE",
            vat_number="IT21029798095",
            activate=True,
            metadata={"foo": "string"},
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.with_raw_response.create(
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            postal_code="21029",
            primary_domain="29-0.mi-57.16u-2d91-aha.o-l7c19m0.z.9zhin-8ja2-7.447----86.6.61--5-6.2.3-i2al.r.name",
            province_code="SE",
            vat_number="IT21029798095",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = await response.parse()
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.with_streaming_response.create(
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            postal_code="21029",
            primary_domain="29-0.mi-57.16u-2d91-aha.o-l7c19m0.z.9zhin-8ja2-7.447----86.6.61--5-6.2.3-i2al.r.name",
            province_code="SE",
            vat_number="IT21029798095",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = await response.parse()
            assert_matches_type(DealerDetail, dealer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPartnermax) -> None:
        dealer = await async_client.dealers.retrieve(
            "dealer_id",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.with_raw_response.retrieve(
            "dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = await response.parse()
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.with_streaming_response.retrieve(
            "dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = await response.parse()
            assert_matches_type(DealerDetail, dealer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPartnermax) -> None:
        dealer = await async_client.dealers.update(
            dealer_id="dealer_id",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPartnermax) -> None:
        dealer = await async_client.dealers.update(
            dealer_id="dealer_id",
            address="xx",
            business_name="xx",
            city="xx",
            contact_email="dev@stainless.com",
            contact_phone="xxxxx",
            metadata={"foo": "string"},
            postal_code="21029",
            province_code="SE",
            status="active",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.with_raw_response.update(
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = await response.parse()
        assert_matches_type(DealerDetail, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.with_streaming_response.update(
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = await response.parse()
            assert_matches_type(DealerDetail, dealer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.with_raw_response.update(
                dealer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPartnermax) -> None:
        dealer = await async_client.dealers.list()
        assert_matches_type(DealerListResponse, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPartnermax) -> None:
        dealer = await async_client.dealers.list(
            cursor="cursor",
            limit=1,
            status="active",
        )
        assert_matches_type(DealerListResponse, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = await response.parse()
        assert_matches_type(DealerListResponse, dealer, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = await response.parse()
            assert_matches_type(DealerListResponse, dealer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPartnermax) -> None:
        dealer = await async_client.dealers.delete(
            "dealer_id",
        )
        assert dealer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.with_raw_response.delete(
            "dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dealer = await response.parse()
        assert dealer is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.with_streaming_response.delete(
            "dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dealer = await response.parse()
            assert dealer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.with_raw_response.delete(
                "",
            )
