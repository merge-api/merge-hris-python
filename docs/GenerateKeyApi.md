# MergeHRISClient.GenerateKeyApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_key_create**](GenerateKeyApi.md#generate_key_create) | **POST** /generate-key | 


# **generate_key_create**
> RemoteKey generate_key_create(generate_remote_key_request)



Create a remote key.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import generate_key_api
from MergeHRISClient.model.generate_remote_key_request import GenerateRemoteKeyRequest
from MergeHRISClient.model.remote_key import RemoteKey
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
    api_instance = generate_key_api.GenerateKeyApi(api_client)
    generate_remote_key_request = GenerateRemoteKeyRequest(
        name="Remote Deployment Key 1",
    ) # GenerateRemoteKeyRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_key_create(generate_remote_key_request)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling GenerateKeyApi->generate_key_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_remote_key_request** | [**GenerateRemoteKeyRequest**](GenerateRemoteKeyRequest.md)|  |

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

