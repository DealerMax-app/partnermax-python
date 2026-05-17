# Auth

Types:

```python
from partnermax.types import AuthLoginResponse
```

Methods:

- <code title="post /v1/auth/login">client.auth.<a href="./src/partnermax/resources/auth.py">login</a>(\*\*<a href="src/partnermax/types/auth_login_params.py">params</a>) -> <a href="./src/partnermax/types/auth_login_response.py">AuthLoginResponse</a></code>

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
