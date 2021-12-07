# MergeHRISClient.AccountDetailsApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_details_retrieve**](AccountDetailsApi.md#account_details_retrieve) | **GET** /account-details | 


# **account_details_retrieve**
> AccountDetails account_details_retrieve()



Get details for a linked account.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import account_details_api
from MergeHRISClient.model.account_details import AccountDetails
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
    api_instance = account_details_api.AccountDetailsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.account_details_retrieve()
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling AccountDetailsApi->account_details_retrieve: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountDetails**](AccountDetails.md)

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

