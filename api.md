# Keys

Types:

```python
from partnermax.types import KeyListResponse, KeyIssueResponse
```

Methods:

- <code title="get /v1/keys">client.keys.<a href="./src/partnermax/resources/keys.py">list</a>() -> <a href="./src/partnermax/types/key_list_response.py">KeyListResponse</a></code>
- <code title="post /v1/keys/issue">client.keys.<a href="./src/partnermax/resources/keys.py">issue</a>(\*\*<a href="src/partnermax/types/key_issue_params.py">params</a>) -> <a href="./src/partnermax/types/key_issue_response.py">KeyIssueResponse</a></code>
- <code title="delete /v1/keys/{key_id}">client.keys.<a href="./src/partnermax/resources/keys.py">revoke</a>(key_id) -> None</code>

# Dealers

Types:

```python
from partnermax.types import DealerDetail, DealerSummary, DealerListResponse
```

Methods:

- <code title="post /v1/dealers">client.dealers.<a href="./src/partnermax/resources/dealers/dealers.py">create</a>(\*\*<a href="src/partnermax/types/dealer_create_params.py">params</a>) -> <a href="./src/partnermax/types/dealer_detail.py">DealerDetail</a></code>
- <code title="get /v1/dealers/{dealer_id}">client.dealers.<a href="./src/partnermax/resources/dealers/dealers.py">retrieve</a>(dealer_id) -> <a href="./src/partnermax/types/dealer_detail.py">DealerDetail</a></code>
- <code title="patch /v1/dealers/{dealer_id}">client.dealers.<a href="./src/partnermax/resources/dealers/dealers.py">update</a>(dealer_id, \*\*<a href="src/partnermax/types/dealer_update_params.py">params</a>) -> <a href="./src/partnermax/types/dealer_detail.py">DealerDetail</a></code>
- <code title="get /v1/dealers">client.dealers.<a href="./src/partnermax/resources/dealers/dealers.py">list</a>(\*\*<a href="src/partnermax/types/dealer_list_params.py">params</a>) -> <a href="./src/partnermax/types/dealer_list_response.py">DealerListResponse</a></code>
- <code title="delete /v1/dealers/{dealer_id}">client.dealers.<a href="./src/partnermax/resources/dealers/dealers.py">delete</a>(dealer_id) -> None</code>

## NltSettings

Types:

```python
from partnermax.types.dealers import DownPaymentTiers, NltSettings
```

Methods:

- <code title="get /v1/dealers/{dealer_id}/nlt-settings">client.dealers.nlt_settings.<a href="./src/partnermax/resources/dealers/nlt_settings.py">retrieve</a>(dealer_id) -> <a href="./src/partnermax/types/dealers/nlt_settings.py">NltSettings</a></code>
- <code title="patch /v1/dealers/{dealer_id}/nlt-settings">client.dealers.nlt_settings.<a href="./src/partnermax/resources/dealers/nlt_settings.py">update</a>(dealer_id, \*\*<a href="src/partnermax/types/dealers/nlt_setting_update_params.py">params</a>) -> <a href="./src/partnermax/types/dealers/nlt_settings.py">NltSettings</a></code>

## Nlt

### Offers

Types:

```python
from partnermax.types.dealers.nlt import NltOfferSummary, OfferRetrieveResponse, OfferListResponse
```

Methods:

- <code title="get /v1/dealers/{dealer_id}/nlt/offers/{offer_id}">client.dealers.nlt.offers.<a href="./src/partnermax/resources/dealers/nlt/offers.py">retrieve</a>(offer_id, \*, dealer_id) -> <a href="./src/partnermax/types/dealers/nlt/offer_retrieve_response.py">OfferRetrieveResponse</a></code>
- <code title="get /v1/dealers/{dealer_id}/nlt/offers">client.dealers.nlt.offers.<a href="./src/partnermax/resources/dealers/nlt/offers.py">list</a>(dealer_id, \*\*<a href="src/partnermax/types/dealers/nlt/offer_list_params.py">params</a>) -> <a href="./src/partnermax/types/dealers/nlt/offer_list_response.py">OfferListResponse</a></code>

## Vehicles

Types:

```python
from partnermax.types.dealers import (
    BulkCreateVehiclesResponse,
    BulkRowOutcome,
    VehicleDetail,
    VehicleList,
    VehicleSummary,
)
```

Methods:

- <code title="post /v1/dealers/{dealer_id}/vehicles">client.dealers.vehicles.<a href="./src/partnermax/resources/dealers/vehicles/vehicles.py">create</a>(dealer_id, \*\*<a href="src/partnermax/types/dealers/vehicle_create_params.py">params</a>) -> <a href="./src/partnermax/types/dealers/vehicle_detail.py">VehicleDetail</a></code>
- <code title="get /v1/dealers/{dealer_id}/vehicles/{vehicle_id}">client.dealers.vehicles.<a href="./src/partnermax/resources/dealers/vehicles/vehicles.py">retrieve</a>(vehicle_id, \*, dealer_id, \*\*<a href="src/partnermax/types/dealers/vehicle_retrieve_params.py">params</a>) -> <a href="./src/partnermax/types/dealers/vehicle_detail.py">VehicleDetail</a></code>
- <code title="patch /v1/dealers/{dealer_id}/vehicles/{vehicle_id}">client.dealers.vehicles.<a href="./src/partnermax/resources/dealers/vehicles/vehicles.py">update</a>(vehicle_id, \*, dealer_id, \*\*<a href="src/partnermax/types/dealers/vehicle_update_params.py">params</a>) -> <a href="./src/partnermax/types/dealers/vehicle_detail.py">VehicleDetail</a></code>
- <code title="get /v1/dealers/{dealer_id}/vehicles">client.dealers.vehicles.<a href="./src/partnermax/resources/dealers/vehicles/vehicles.py">list</a>(dealer_id, \*\*<a href="src/partnermax/types/dealers/vehicle_list_params.py">params</a>) -> <a href="./src/partnermax/types/dealers/vehicle_list.py">VehicleList</a></code>
- <code title="delete /v1/dealers/{dealer_id}/vehicles/{vehicle_id}">client.dealers.vehicles.<a href="./src/partnermax/resources/dealers/vehicles/vehicles.py">delete</a>(vehicle_id, \*, dealer_id) -> None</code>
- <code title="post /v1/dealers/{dealer_id}/vehicles/bulk">client.dealers.vehicles.<a href="./src/partnermax/resources/dealers/vehicles/vehicles.py">bulk</a>(dealer_id, \*\*<a href="src/partnermax/types/dealers/vehicle_bulk_params.py">params</a>) -> <a href="./src/partnermax/types/dealers/bulk_create_vehicles_response.py">BulkCreateVehiclesResponse</a></code>

### Images

Types:

```python
from partnermax.types.dealers.vehicles import VehicleImage, VehicleImageList
```

Methods:

- <code title="post /v1/dealers/{dealer_id}/vehicles/{vehicle_id}/images">client.dealers.vehicles.images.<a href="./src/partnermax/resources/dealers/vehicles/images.py">create</a>(vehicle_id, \*, dealer_id, \*\*<a href="src/partnermax/types/dealers/vehicles/image_create_params.py">params</a>) -> <a href="./src/partnermax/types/dealers/vehicles/vehicle_image.py">VehicleImage</a></code>
- <code title="get /v1/dealers/{dealer_id}/vehicles/{vehicle_id}/images">client.dealers.vehicles.images.<a href="./src/partnermax/resources/dealers/vehicles/images.py">list</a>(vehicle_id, \*, dealer_id) -> <a href="./src/partnermax/types/dealers/vehicles/vehicle_image_list.py">VehicleImageList</a></code>
- <code title="delete /v1/dealers/{dealer_id}/vehicles/{vehicle_id}/images/{image_id}">client.dealers.vehicles.images.<a href="./src/partnermax/resources/dealers/vehicles/images.py">delete</a>(image_id, \*, dealer_id, vehicle_id) -> None</code>
