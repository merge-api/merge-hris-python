# MergeHRISClient.InterviewsApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**interviews_list**](InterviewsApi.md#interviews_list) | **GET** /interviews | 
[**interviews_partial_update**](InterviewsApi.md#interviews_partial_update) | **PATCH** /interviews/{id} | 
[**interviews_retrieve**](InterviewsApi.md#interviews_retrieve) | **GET** /interviews/{id} | 


# **interviews_list**
> PaginatedScheduledInterviewList interviews_list(x_account_token)



Returns a list of `ScheduledInterview` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import interviews_api
from MergeHRISClient.model.paginated_scheduled_interview_list import PaginatedScheduledInterviewList
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeHRISClient.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
    api_instance = interviews_api.InterviewsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    application_id = "application_id_example" # str | If provided, will only return interviews for this application. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "interviewers,organizer,application,job_interview_stage" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    job_interview_stage_id = "job_interview_stage_id_example" # str | If provided, will only return interviews at this stage. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    organizer_id = "organizer_id_example" # str | If provided, will only return interviews organized by this user. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.interviews_list(x_account_token)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling InterviewsApi->interviews_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.interviews_list(x_account_token, application_id=application_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, job_interview_stage_id=job_interview_stage_id, modified_after=modified_after, modified_before=modified_before, organizer_id=organizer_id, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling InterviewsApi->interviews_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **application_id** | **str**| If provided, will only return interviews for this application. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **job_interview_stage_id** | **str**| If provided, will only return interviews at this stage. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **organizer_id** | **str**| If provided, will only return interviews organized by this user. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedScheduledInterviewList**](PaginatedScheduledInterviewList.md)

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

# **interviews_partial_update**
> ScheduledInterview interviews_partial_update(x_account_token, id)



Updates a `ScheduledInterview` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import interviews_api
from MergeHRISClient.model.patched_scheduled_interview import PatchedScheduledInterview
from MergeHRISClient.model.scheduled_interview import ScheduledInterview
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeHRISClient.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
    api_instance = interviews_api.InterviewsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
    patched_scheduled_interview = PatchedScheduledInterview(
        id="b8faf072-98b9-4445-8a9a-6b4950efca19",
        remote_id="3",
        application="92e8a369-fffe-430d-b93a-f7e8a16563f1",
        job_interview_stage="2f7adb59-3fe6-4b5b-aef6-563f72bd13dc",
        organizer="52bf9b5e-0beb-4f6f-8a72-cd4dca7ca633",
        interviewers=["f9813dd5-e70b-484c-91d8-00acd6065b07","89a86fcf-d540-4e6b-ac3d-ce07c4ec9b3c"],
        location="Embarcadero Center 2",
        start_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        end_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        remote_created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        remote_updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        status="status_example",
    ) # PatchedScheduledInterview |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.interviews_partial_update(x_account_token, id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling InterviewsApi->interviews_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.interviews_partial_update(x_account_token, id, run_async=run_async, patched_scheduled_interview=patched_scheduled_interview)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling InterviewsApi->interviews_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]
 **patched_scheduled_interview** | [**PatchedScheduledInterview**](PatchedScheduledInterview.md)|  | [optional]

### Return type

[**ScheduledInterview**](ScheduledInterview.md)

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

# **interviews_retrieve**
> ScheduledInterview interviews_retrieve(x_account_token, id)



Returns a `ScheduledInterview` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import interviews_api
from MergeHRISClient.model.scheduled_interview import ScheduledInterview
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeHRISClient.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
    api_instance = interviews_api.InterviewsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "interviewers,organizer,application,job_interview_stage" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.interviews_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling InterviewsApi->interviews_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.interviews_retrieve(x_account_token, id, expand=expand)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling InterviewsApi->interviews_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]

### Return type

[**ScheduledInterview**](ScheduledInterview.md)

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

