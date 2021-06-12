# MergeHRISClient.RegenerateKeyApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regenerate_key_create**](RegenerateKeyApi.md#regenerate_key_create) | **POST** /regenerate-key | 


# **regenerate_key_create**
> RemoteKey regenerate_key_create(remote_key_for_regeneration_request)



Exchange remote keys.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import regenerate_key_api
from MergeHRISClient.model.remote_key import RemoteKey
from MergeHRISClient.model.remote_key_for_regeneration_request import RemoteKeyForRegenerationRequest
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
    api_instance = regenerate_key_api.RegenerateKeyApi(api_client)
    remote_key_for_regeneration_request = RemoteKeyForRegenerationRequest(
        name="Remote Deployment Key 1",
    ) # RemoteKeyForRegenerationRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.regenerate_key_create(remote_key_for_regeneration_request)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling RegenerateKeyApi->regenerate_key_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_key_for_regeneration_request** | [**RemoteKeyForRegenerationRequest**](RemoteKeyForRegenerationRequest.md)|  |

### Return type

[**RemoteKey**](RemoteKey.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

