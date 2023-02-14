# MergeHRISClient.CommonModelScopesApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**common_model_scopes_create**](CommonModelScopesApi.md#common_model_scopes_create) | **POST** /common-model-scopes | 
[**common_model_scopes_retrieve**](CommonModelScopesApi.md#common_model_scopes_retrieve) | **GET** /common-model-scopes | 


# **common_model_scopes_create**
> CommonModelScopes common_model_scopes_create(common_model_scopes_update_serializer)



Update the configuration of what data is saved by Merge when syncing. Common model scopes are set as a default across all linked accounts, but can be updated to have greater granularity per account.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import common_model_scopes_api
from MergeHRISClient.model.common_model_scopes import CommonModelScopes
from MergeHRISClient.model.common_model_scopes_update_serializer import CommonModelScopesUpdateSerializer
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
    api_instance = common_model_scopes_api.CommonModelScopesApi(api_client)
    common_model_scopes_update_serializer = CommonModelScopesUpdateSerializer(
        common_models=[
            CommonModelScopesPostInnerDeserializerRequest(
                model_id="hris.Employee",
                enabled_actions=[
                    EnabledActionsEnum("["READ","WRITE"]"),
                ],
                disabled_fields=[
                    "disabled_fields_example",
                ],
            ),
        ],
    ) # CommonModelScopesUpdateSerializer | 
    linked_account_id = "linked_account_id_example" # str | ID of specific linked account to fetch (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.common_model_scopes_create(common_model_scopes_update_serializer)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling CommonModelScopesApi->common_model_scopes_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.common_model_scopes_create(common_model_scopes_update_serializer, linked_account_id=linked_account_id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling CommonModelScopesApi->common_model_scopes_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_model_scopes_update_serializer** | [**CommonModelScopesUpdateSerializer**](CommonModelScopesUpdateSerializer.md)|  |
 **linked_account_id** | **str**| ID of specific linked account to fetch | [optional]

### Return type

[**CommonModelScopes**](CommonModelScopes.md)

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

# **common_model_scopes_retrieve**
> CommonModelScopes common_model_scopes_retrieve()



Fetch the configuration of what data is saved by Merge when syncing. Common model scopes are set as a default across all linked accounts, but can be updated to have greater granularity per account.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import common_model_scopes_api
from MergeHRISClient.model.common_model_scopes import CommonModelScopes
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
    api_instance = common_model_scopes_api.CommonModelScopesApi(api_client)
    linked_account_id = "linked_account_id_example" # str | ID of specific linked account to fetch (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.common_model_scopes_retrieve(linked_account_id=linked_account_id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling CommonModelScopesApi->common_model_scopes_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_account_id** | **str**| ID of specific linked account to fetch | [optional]

### Return type

[**CommonModelScopes**](CommonModelScopes.md)

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

