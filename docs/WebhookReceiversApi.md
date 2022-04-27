# MergeHRISClient.WebhookReceiversApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_receivers_create**](WebhookReceiversApi.md#webhook_receivers_create) | **POST** /webhook-receivers | 
[**webhook_receivers_list**](WebhookReceiversApi.md#webhook_receivers_list) | **GET** /webhook-receivers | 


# **webhook_receivers_create**
> WebhookReceiver webhook_receivers_create(x_account_token, webhook_receiver_request)



Creates a `WebhookReceiver` object with the given values.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import webhook_receivers_api
from MergeHRISClient.model.webhook_receiver_request import WebhookReceiverRequest
from MergeHRISClient.model.webhook_receiver import WebhookReceiver
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeHRISClient.Configuration(
    host = "https://api.merge.dev/api/hris/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_receivers_api.WebhookReceiversApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    webhook_receiver_request = WebhookReceiverRequest(
        event="event_example",
        is_active=True,
        key="key_example",
    ) # WebhookReceiverRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.webhook_receivers_create(x_account_token, webhook_receiver_request)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling WebhookReceiversApi->webhook_receivers_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **webhook_receiver_request** | [**WebhookReceiverRequest**](WebhookReceiverRequest.md)|  |

### Return type

[**WebhookReceiver**](WebhookReceiver.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_receivers_list**
> [WebhookReceiver] webhook_receivers_list(x_account_token)



Returns a list of `WebhookReceiver` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import webhook_receivers_api
from MergeHRISClient.model.webhook_receiver import WebhookReceiver
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeHRISClient.Configuration(
    host = "https://api.merge.dev/api/hris/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webhook_receivers_api.WebhookReceiversApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.webhook_receivers_list(x_account_token)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling WebhookReceiversApi->webhook_receivers_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |

### Return type

[**[WebhookReceiver]**](WebhookReceiver.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

