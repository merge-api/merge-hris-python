# MergeHRISClient.ScorecardsApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scorecards_list**](ScorecardsApi.md#scorecards_list) | **GET** /scorecards | 
[**scorecards_partial_update**](ScorecardsApi.md#scorecards_partial_update) | **PATCH** /scorecards/{id} | 
[**scorecards_retrieve**](ScorecardsApi.md#scorecards_retrieve) | **GET** /scorecards/{id} | 


# **scorecards_list**
> PaginatedScorecardList scorecards_list(x_account_token)



Returns a list of `Scorecard` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import scorecards_api
from MergeHRISClient.model.paginated_scorecard_list import PaginatedScorecardList
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
    api_instance = scorecards_api.ScorecardsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    application_id = "application_id_example" # str | If provided, will only return scorecards for this application. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "application,interview,interviewer" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    interview_id = "interview_id_example" # str | If provided, will only return scorecards for this interview. (optional)
    interviewer_id = "interviewer_id_example" # str | If provided, will only return scorecards for this interviewer. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.scorecards_list(x_account_token)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.scorecards_list(x_account_token, application_id=application_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, interview_id=interview_id, interviewer_id=interviewer_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **application_id** | **str**| If provided, will only return scorecards for this application. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **interview_id** | **str**| If provided, will only return scorecards for this interview. | [optional]
 **interviewer_id** | **str**| If provided, will only return scorecards for this interviewer. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedScorecardList**](PaginatedScorecardList.md)

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

# **scorecards_partial_update**
> Scorecard scorecards_partial_update(x_account_token, id)



Updates a `Scorecard` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import scorecards_api
from MergeHRISClient.model.scorecard import Scorecard
from MergeHRISClient.model.patched_scorecard import PatchedScorecard
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
    api_instance = scorecards_api.ScorecardsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
    patched_scorecard = PatchedScorecard(
        id="3eab2f17-eeb1-450d-97f0-029d8be1e06f",
        remote_id="22234",
        application="2872ba14-4084-492b-be96-e5eee6fc33ef",
        interview="52bf9b5e-0beb-4f6f-8a72-cd4dca7ca633",
        interviewer="bbb519a3-246e-4b95-b6b3-dba16107ba6b",
        remote_created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        submitted_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        overall_recommendation="overall_recommendation_example",
    ) # PatchedScorecard |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.scorecards_partial_update(x_account_token, id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.scorecards_partial_update(x_account_token, id, run_async=run_async, patched_scorecard=patched_scorecard)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]
 **patched_scorecard** | [**PatchedScorecard**](PatchedScorecard.md)|  | [optional]

### Return type

[**Scorecard**](Scorecard.md)

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

# **scorecards_retrieve**
> Scorecard scorecards_retrieve(x_account_token, id)



Returns a `Scorecard` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import scorecards_api
from MergeHRISClient.model.scorecard import Scorecard
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
    api_instance = scorecards_api.ScorecardsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "application,interview,interviewer" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.scorecards_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.scorecards_retrieve(x_account_token, id, expand=expand)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling ScorecardsApi->scorecards_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]

### Return type

[**Scorecard**](Scorecard.md)

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

