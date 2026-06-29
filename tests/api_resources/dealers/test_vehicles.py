# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from partnermax import Partnermax, AsyncPartnermax
from tests.utils import assert_matches_type
from partnermax._utils import parse_date
from partnermax.pagination import SyncCursorPage, AsyncCursorPage
from partnermax.types.dealers import (
    VehicleDetail,
    VehicleSummary,
    BulkCreateVehiclesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVehicles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.create(
            dealer_id="dealer_id",
            certified_km=0,
            motornet_code="xxxx",
            plate="26F1KLZN",
            registration_year=1960,
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.create(
            dealer_id="dealer_id",
            certified_km=0,
            motornet_code="xxxx",
            plate="26F1KLZN",
            registration_year=1960,
            alloy_wheel_size=13,
            base_color="base_color",
            co2_emissions_g_km_override=0,
            color="color",
            cost_price_eur=0,
            damage_repaired=True,
            description="description",
            double_keys_available=True,
            enabled_channels=["rewind"],
            extended_warranty_enabled=True,
            extended_warranty_months=1,
            fuel_type_override="fuel_type_override",
            inspection_due_date=parse_date("2019-12-27"),
            is_visible=True,
            last_inspection_date=parse_date("2019-12-27"),
            last_inspection_km=0,
            last_service_date=parse_date("2019-12-27"),
            last_service_km=0,
            last_service_notes="last_service_notes",
            notes="notes",
            ownership_transfer_date=parse_date("2019-12-27"),
            power_kw_override=1,
            previous_owner_count=0,
            property_tax_due_date=parse_date("2019-12-27"),
            registration_month=1,
            sale_price_eur=0,
            service_history_available=True,
            trim_alias="trim_alias",
            vat_displayed=True,
            vehicle_damaged=True,
            vin="PTNLCJPPNYGP316PJ",
            wltp_consumption_combined_l_100km=0,
            wltp_consumption_extraurban_l_100km=0,
            wltp_consumption_urban_l_100km=0,
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.with_raw_response.create(
            dealer_id="dealer_id",
            certified_km=0,
            motornet_code="xxxx",
            plate="26F1KLZN",
            registration_year=1960,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = response.parse()
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Partnermax) -> None:
        with client.dealers.vehicles.with_streaming_response.create(
            dealer_id="dealer_id",
            certified_km=0,
            motornet_code="xxxx",
            plate="26F1KLZN",
            registration_year=1960,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = response.parse()
            assert_matches_type(VehicleDetail, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.with_raw_response.create(
                dealer_id="",
                certified_km=0,
                motornet_code="xxxx",
                plate="26F1KLZN",
                registration_year=1960,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.retrieve(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.retrieve(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            include_deleted=True,
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.with_raw_response.retrieve(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = response.parse()
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Partnermax) -> None:
        with client.dealers.vehicles.with_streaming_response.retrieve(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = response.parse()
            assert_matches_type(VehicleDetail, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.with_raw_response.retrieve(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.dealers.vehicles.with_raw_response.retrieve(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            alloy_wheel_size=13,
            base_color="base_color",
            certified_km=0,
            co2_emissions_g_km_override=0,
            color="color",
            cost_price_eur=0,
            damage_repaired=True,
            description="description",
            double_keys_available=True,
            enabled_channels=["rewind"],
            extended_warranty_enabled=True,
            extended_warranty_months=1,
            fuel_type_override="fuel_type_override",
            inspection_due_date=parse_date("2019-12-27"),
            is_visible=True,
            last_inspection_date=parse_date("2019-12-27"),
            last_inspection_km=0,
            last_service_date=parse_date("2019-12-27"),
            last_service_km=0,
            last_service_notes="last_service_notes",
            notes="notes",
            ownership_transfer_date=parse_date("2019-12-27"),
            power_kw_override=1,
            previous_owner_count=0,
            property_tax_due_date=parse_date("2019-12-27"),
            registration_month=1,
            registration_year=1960,
            sale_price_eur=0,
            service_history_available=True,
            trim_alias="trim_alias",
            vat_displayed=True,
            vehicle_damaged=True,
            vin="PTNLCJPPNYGP316PJ",
            wltp_consumption_combined_l_100km=0,
            wltp_consumption_extraurban_l_100km=0,
            wltp_consumption_urban_l_100km=0,
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.with_raw_response.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = response.parse()
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Partnermax) -> None:
        with client.dealers.vehicles.with_streaming_response.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = response.parse()
            assert_matches_type(VehicleDetail, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.with_raw_response.update(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.dealers.vehicles.with_raw_response.update(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.list(
            dealer_id="dealer_id",
        )
        assert_matches_type(SyncCursorPage[VehicleSummary], vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.list(
            dealer_id="dealer_id",
            cursor="cursor",
            enabled_channel="rewind",
            include_deleted=True,
            is_visible=True,
            limit=1,
        )
        assert_matches_type(SyncCursorPage[VehicleSummary], vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.with_raw_response.list(
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = response.parse()
        assert_matches_type(SyncCursorPage[VehicleSummary], vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Partnermax) -> None:
        with client.dealers.vehicles.with_streaming_response.list(
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = response.parse()
            assert_matches_type(SyncCursorPage[VehicleSummary], vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.with_raw_response.list(
                dealer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.delete(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert vehicle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.with_raw_response.delete(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = response.parse()
        assert vehicle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Partnermax) -> None:
        with client.dealers.vehicles.with_streaming_response.delete(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = response.parse()
            assert vehicle is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.with_raw_response.delete(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.dealers.vehicles.with_raw_response.delete(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.bulk(
            dealer_id="dealer_id",
            vehicles=[
                {
                    "certified_km": 0,
                    "motornet_code": "xxxx",
                    "plate": "26F1KLZN",
                    "registration_year": 1960,
                }
            ],
        )
        assert_matches_type(BulkCreateVehiclesResponse, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_with_all_params(self, client: Partnermax) -> None:
        vehicle = client.dealers.vehicles.bulk(
            dealer_id="dealer_id",
            vehicles=[
                {
                    "certified_km": 0,
                    "motornet_code": "xxxx",
                    "plate": "26F1KLZN",
                    "registration_year": 1960,
                    "alloy_wheel_size": 13,
                    "base_color": "base_color",
                    "co2_emissions_g_km_override": 0,
                    "color": "color",
                    "cost_price_eur": 0,
                    "damage_repaired": True,
                    "description": "description",
                    "double_keys_available": True,
                    "enabled_channels": ["rewind"],
                    "extended_warranty_enabled": True,
                    "extended_warranty_months": 1,
                    "fuel_type_override": "fuel_type_override",
                    "inspection_due_date": parse_date("2019-12-27"),
                    "is_visible": True,
                    "last_inspection_date": parse_date("2019-12-27"),
                    "last_inspection_km": 0,
                    "last_service_date": parse_date("2019-12-27"),
                    "last_service_km": 0,
                    "last_service_notes": "last_service_notes",
                    "notes": "notes",
                    "ownership_transfer_date": parse_date("2019-12-27"),
                    "power_kw_override": 1,
                    "previous_owner_count": 0,
                    "property_tax_due_date": parse_date("2019-12-27"),
                    "registration_month": 1,
                    "sale_price_eur": 0,
                    "service_history_available": True,
                    "trim_alias": "trim_alias",
                    "vat_displayed": True,
                    "vehicle_damaged": True,
                    "vin": "PTNLCJPPNYGP316PJ",
                    "wltp_consumption_combined_l_100km": 0,
                    "wltp_consumption_extraurban_l_100km": 0,
                    "wltp_consumption_urban_l_100km": 0,
                }
            ],
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(BulkCreateVehiclesResponse, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk(self, client: Partnermax) -> None:
        response = client.dealers.vehicles.with_raw_response.bulk(
            dealer_id="dealer_id",
            vehicles=[
                {
                    "certified_km": 0,
                    "motornet_code": "xxxx",
                    "plate": "26F1KLZN",
                    "registration_year": 1960,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = response.parse()
        assert_matches_type(BulkCreateVehiclesResponse, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk(self, client: Partnermax) -> None:
        with client.dealers.vehicles.with_streaming_response.bulk(
            dealer_id="dealer_id",
            vehicles=[
                {
                    "certified_km": 0,
                    "motornet_code": "xxxx",
                    "plate": "26F1KLZN",
                    "registration_year": 1960,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = response.parse()
            assert_matches_type(BulkCreateVehiclesResponse, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_bulk(self, client: Partnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            client.dealers.vehicles.with_raw_response.bulk(
                dealer_id="",
                vehicles=[
                    {
                        "certified_km": 0,
                        "motornet_code": "xxxx",
                        "plate": "26F1KLZN",
                        "registration_year": 1960,
                    }
                ],
            )


class TestAsyncVehicles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.create(
            dealer_id="dealer_id",
            certified_km=0,
            motornet_code="xxxx",
            plate="26F1KLZN",
            registration_year=1960,
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.create(
            dealer_id="dealer_id",
            certified_km=0,
            motornet_code="xxxx",
            plate="26F1KLZN",
            registration_year=1960,
            alloy_wheel_size=13,
            base_color="base_color",
            co2_emissions_g_km_override=0,
            color="color",
            cost_price_eur=0,
            damage_repaired=True,
            description="description",
            double_keys_available=True,
            enabled_channels=["rewind"],
            extended_warranty_enabled=True,
            extended_warranty_months=1,
            fuel_type_override="fuel_type_override",
            inspection_due_date=parse_date("2019-12-27"),
            is_visible=True,
            last_inspection_date=parse_date("2019-12-27"),
            last_inspection_km=0,
            last_service_date=parse_date("2019-12-27"),
            last_service_km=0,
            last_service_notes="last_service_notes",
            notes="notes",
            ownership_transfer_date=parse_date("2019-12-27"),
            power_kw_override=1,
            previous_owner_count=0,
            property_tax_due_date=parse_date("2019-12-27"),
            registration_month=1,
            sale_price_eur=0,
            service_history_available=True,
            trim_alias="trim_alias",
            vat_displayed=True,
            vehicle_damaged=True,
            vin="PTNLCJPPNYGP316PJ",
            wltp_consumption_combined_l_100km=0,
            wltp_consumption_extraurban_l_100km=0,
            wltp_consumption_urban_l_100km=0,
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.with_raw_response.create(
            dealer_id="dealer_id",
            certified_km=0,
            motornet_code="xxxx",
            plate="26F1KLZN",
            registration_year=1960,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = await response.parse()
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.with_streaming_response.create(
            dealer_id="dealer_id",
            certified_km=0,
            motornet_code="xxxx",
            plate="26F1KLZN",
            registration_year=1960,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = await response.parse()
            assert_matches_type(VehicleDetail, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.with_raw_response.create(
                dealer_id="",
                certified_km=0,
                motornet_code="xxxx",
                plate="26F1KLZN",
                registration_year=1960,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.retrieve(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.retrieve(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            include_deleted=True,
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.with_raw_response.retrieve(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = await response.parse()
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.with_streaming_response.retrieve(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = await response.parse()
            assert_matches_type(VehicleDetail, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.with_raw_response.retrieve(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.dealers.vehicles.with_raw_response.retrieve(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
            alloy_wheel_size=13,
            base_color="base_color",
            certified_km=0,
            co2_emissions_g_km_override=0,
            color="color",
            cost_price_eur=0,
            damage_repaired=True,
            description="description",
            double_keys_available=True,
            enabled_channels=["rewind"],
            extended_warranty_enabled=True,
            extended_warranty_months=1,
            fuel_type_override="fuel_type_override",
            inspection_due_date=parse_date("2019-12-27"),
            is_visible=True,
            last_inspection_date=parse_date("2019-12-27"),
            last_inspection_km=0,
            last_service_date=parse_date("2019-12-27"),
            last_service_km=0,
            last_service_notes="last_service_notes",
            notes="notes",
            ownership_transfer_date=parse_date("2019-12-27"),
            power_kw_override=1,
            previous_owner_count=0,
            property_tax_due_date=parse_date("2019-12-27"),
            registration_month=1,
            registration_year=1960,
            sale_price_eur=0,
            service_history_available=True,
            trim_alias="trim_alias",
            vat_displayed=True,
            vehicle_damaged=True,
            vin="PTNLCJPPNYGP316PJ",
            wltp_consumption_combined_l_100km=0,
            wltp_consumption_extraurban_l_100km=0,
            wltp_consumption_urban_l_100km=0,
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.with_raw_response.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = await response.parse()
        assert_matches_type(VehicleDetail, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.with_streaming_response.update(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = await response.parse()
            assert_matches_type(VehicleDetail, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.with_raw_response.update(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.dealers.vehicles.with_raw_response.update(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.list(
            dealer_id="dealer_id",
        )
        assert_matches_type(AsyncCursorPage[VehicleSummary], vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.list(
            dealer_id="dealer_id",
            cursor="cursor",
            enabled_channel="rewind",
            include_deleted=True,
            is_visible=True,
            limit=1,
        )
        assert_matches_type(AsyncCursorPage[VehicleSummary], vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.with_raw_response.list(
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = await response.parse()
        assert_matches_type(AsyncCursorPage[VehicleSummary], vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.with_streaming_response.list(
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = await response.parse()
            assert_matches_type(AsyncCursorPage[VehicleSummary], vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.with_raw_response.list(
                dealer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.delete(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )
        assert vehicle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.with_raw_response.delete(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = await response.parse()
        assert vehicle is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.with_streaming_response.delete(
            vehicle_id="vehicle_id",
            dealer_id="dealer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = await response.parse()
            assert vehicle is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.with_raw_response.delete(
                vehicle_id="vehicle_id",
                dealer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.dealers.vehicles.with_raw_response.delete(
                vehicle_id="",
                dealer_id="dealer_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.bulk(
            dealer_id="dealer_id",
            vehicles=[
                {
                    "certified_km": 0,
                    "motornet_code": "xxxx",
                    "plate": "26F1KLZN",
                    "registration_year": 1960,
                }
            ],
        )
        assert_matches_type(BulkCreateVehiclesResponse, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_with_all_params(self, async_client: AsyncPartnermax) -> None:
        vehicle = await async_client.dealers.vehicles.bulk(
            dealer_id="dealer_id",
            vehicles=[
                {
                    "certified_km": 0,
                    "motornet_code": "xxxx",
                    "plate": "26F1KLZN",
                    "registration_year": 1960,
                    "alloy_wheel_size": 13,
                    "base_color": "base_color",
                    "co2_emissions_g_km_override": 0,
                    "color": "color",
                    "cost_price_eur": 0,
                    "damage_repaired": True,
                    "description": "description",
                    "double_keys_available": True,
                    "enabled_channels": ["rewind"],
                    "extended_warranty_enabled": True,
                    "extended_warranty_months": 1,
                    "fuel_type_override": "fuel_type_override",
                    "inspection_due_date": parse_date("2019-12-27"),
                    "is_visible": True,
                    "last_inspection_date": parse_date("2019-12-27"),
                    "last_inspection_km": 0,
                    "last_service_date": parse_date("2019-12-27"),
                    "last_service_km": 0,
                    "last_service_notes": "last_service_notes",
                    "notes": "notes",
                    "ownership_transfer_date": parse_date("2019-12-27"),
                    "power_kw_override": 1,
                    "previous_owner_count": 0,
                    "property_tax_due_date": parse_date("2019-12-27"),
                    "registration_month": 1,
                    "sale_price_eur": 0,
                    "service_history_available": True,
                    "trim_alias": "trim_alias",
                    "vat_displayed": True,
                    "vehicle_damaged": True,
                    "vin": "PTNLCJPPNYGP316PJ",
                    "wltp_consumption_combined_l_100km": 0,
                    "wltp_consumption_extraurban_l_100km": 0,
                    "wltp_consumption_urban_l_100km": 0,
                }
            ],
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(BulkCreateVehiclesResponse, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk(self, async_client: AsyncPartnermax) -> None:
        response = await async_client.dealers.vehicles.with_raw_response.bulk(
            dealer_id="dealer_id",
            vehicles=[
                {
                    "certified_km": 0,
                    "motornet_code": "xxxx",
                    "plate": "26F1KLZN",
                    "registration_year": 1960,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle = await response.parse()
        assert_matches_type(BulkCreateVehiclesResponse, vehicle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk(self, async_client: AsyncPartnermax) -> None:
        async with async_client.dealers.vehicles.with_streaming_response.bulk(
            dealer_id="dealer_id",
            vehicles=[
                {
                    "certified_km": 0,
                    "motornet_code": "xxxx",
                    "plate": "26F1KLZN",
                    "registration_year": 1960,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle = await response.parse()
            assert_matches_type(BulkCreateVehiclesResponse, vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_bulk(self, async_client: AsyncPartnermax) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dealer_id` but received ''"):
            await async_client.dealers.vehicles.with_raw_response.bulk(
                dealer_id="",
                vehicles=[
                    {
                        "certified_km": 0,
                        "motornet_code": "xxxx",
                        "plate": "26F1KLZN",
                        "registration_year": 1960,
                    }
                ],
            )
