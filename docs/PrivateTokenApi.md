# MergeHRISClient.PrivateTokenApi

All URIs are relative to *https://app.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_token_retrieve**](PrivateTokenApi.md#private_token_retrieve) | **GET** /private-token/{public_token} | 


# **private_token_retrieve**
> PrivateToken private_token_retrieve(public_token, production_key=production_key)



Returns the private token for the end user with the provided public token.

### Example

* Bearer (Token) Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import MergeHRISClient
from MergeHRISClient.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.PrivateTokenApi(api_client)
    public_token = 'public_token_example' # str | 
production_key = 'production_key_example' # str | The requesting organization's production key. (optional)

    try:
        api_response = api_instance.private_token_retrieve(public_token, production_key=production_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrivateTokenApi->private_token_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_token** | **str**|  | 
 **production_key** | **str**| The requesting organization&#39;s production key. | [optional] 

### Return type

[**PrivateToken**](PrivateToken.md)

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

