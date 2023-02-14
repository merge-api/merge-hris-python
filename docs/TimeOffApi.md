# MergeHRISClient.TimeOffApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**time_off_create**](TimeOffApi.md#time_off_create) | **POST** /time-off | 
[**time_off_list**](TimeOffApi.md#time_off_list) | **GET** /time-off | 
[**time_off_meta_post_retrieve**](TimeOffApi.md#time_off_meta_post_retrieve) | **GET** /time-off/meta/post | 
[**time_off_retrieve**](TimeOffApi.md#time_off_retrieve) | **GET** /time-off/{id} | 


# **time_off_create**
> TimeOffResponse time_off_create(x_account_token, time_off_endpoint_request)



Creates a `TimeOff` object with the given values.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import time_off_api
from MergeHRISClient.model.time_off_response import TimeOffResponse
from MergeHRISClient.model.time_off_endpoint_request import TimeOffEndpointRequest
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
    api_instance = time_off_api.TimeOffApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    time_off_endpoint_request = TimeOffEndpointRequest(
        model=TimeOffRequest(
            employee="d2f972d0-2526-434b-9409-4c3b468e08f0",
            approver="9efbc633-3387-4306-aa55-e2c635e6bb4f",
            status=,
            employee_note="Moving into the new apartment Kendall Roy gave me!",
            units=,
            amount=3,
            request_type=,
            start_time=dateutil_parser('2020-11-10T00:00:00Z'),
            end_time=dateutil_parser('2020-11-17T00:00:00Z'),
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # TimeOffEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.time_off_create(x_account_token, time_off_endpoint_request)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling TimeOffApi->time_off_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.time_off_create(x_account_token, time_off_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling TimeOffApi->time_off_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **time_off_endpoint_request** | [**TimeOffEndpointRequest**](TimeOffEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**TimeOffResponse**](TimeOffResponse.md)

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

# **time_off_list**
> PaginatedTimeOffList time_off_list(x_account_token)



Returns a list of `TimeOff` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import time_off_api
from MergeHRISClient.model.paginated_time_off_list import PaginatedTimeOffList
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
    api_instance = time_off_api.TimeOffApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    approver_id = "approver_id_example" # str | If provided, will only return time off for this approver. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    employee_id = "employee_id_example" # str | If provided, will only return time off for this employee. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_fields = "request_type,status,units" # str | Deprecated. Use show_enum_origins. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    request_type = "BEREAVEMENT" # str, none_type | If provided, will only return TimeOff with this request type. Options: ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT') (optional)
    show_enum_origins = "request_type,status,units" # str | Which fields should be returned in non-normalized form. (optional)
    status = "APPROVED" # str, none_type | If provided, will only return TimeOff with this status. Options: ('REQUESTED', 'APPROVED', 'DECLINED', 'CANCELLED', 'DELETED') (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.time_off_list(x_account_token)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling TimeOffApi->time_off_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.time_off_list(x_account_token, approver_id=approver_id, created_after=created_after, created_before=created_before, cursor=cursor, employee_id=employee_id, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_fields=remote_fields, remote_id=remote_id, request_type=request_type, show_enum_origins=show_enum_origins, status=status)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling TimeOffApi->time_off_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **approver_id** | **str**| If provided, will only return time off for this approver. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **employee_id** | **str**| If provided, will only return time off for this employee. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **request_type** | **str, none_type**| If provided, will only return TimeOff with this request type. Options: (&#39;VACATION&#39;, &#39;SICK&#39;, &#39;PERSONAL&#39;, &#39;JURY_DUTY&#39;, &#39;VOLUNTEER&#39;, &#39;BEREAVEMENT&#39;) | [optional]
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional]
 **status** | **str, none_type**| If provided, will only return TimeOff with this status. Options: (&#39;REQUESTED&#39;, &#39;APPROVED&#39;, &#39;DECLINED&#39;, &#39;CANCELLED&#39;, &#39;DELETED&#39;) | [optional]

### Return type

[**PaginatedTimeOffList**](PaginatedTimeOffList.md)

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

# **time_off_meta_post_retrieve**
> MetaResponse time_off_meta_post_retrieve(x_account_token)



Returns metadata for `TimeOff` POSTs.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import time_off_api
from MergeHRISClient.model.meta_response import MetaResponse
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
    api_instance = time_off_api.TimeOffApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.time_off_meta_post_retrieve(x_account_token)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling TimeOffApi->time_off_meta_post_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |

### Return type

[**MetaResponse**](MetaResponse.md)

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

# **time_off_retrieve**
> TimeOff time_off_retrieve(x_account_token, id)



Returns a `TimeOff` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import time_off_api
from MergeHRISClient.model.time_off import TimeOff
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
    api_instance = time_off_api.TimeOffApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "request_type,status,units" # str | Deprecated. Use show_enum_origins. (optional)
    show_enum_origins = "request_type,status,units" # str | Which fields should be returned in non-normalized form. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.time_off_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling TimeOffApi->time_off_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.time_off_retrieve(x_account_token, id, include_remote_data=include_remote_data, remote_fields=remote_fields, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling TimeOffApi->time_off_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional]
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional]

### Return type

[**TimeOff**](TimeOff.md)

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

