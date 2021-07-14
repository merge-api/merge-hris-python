# MergeHRISClient.IssuesApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issues_list**](IssuesApi.md#issues_list) | **GET** /issues | 
[**issues_retrieve**](IssuesApi.md#issues_retrieve) | **GET** /issues/{id} | 


# **issues_list**
> PaginatedIssueList issues_list()



Gets issues.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import issues_api
from MergeHRISClient.model.paginated_issue_list import PaginatedIssueList
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
    api_instance = issues_api.IssuesApi(api_client)
    account_token = "account_token_example" # str | account_token (optional)
    cursor = 1 # int | The pagination cursor value. (optional)
    end_date = "end_date_example" # str | If included, will only include issues whose most recent action occurred before this time (optional)
    end_user_organization_name = "end_user_organization_name_example" # str | end_user_organization_name (optional)
    include_muted = "include_muted_example" # str | If True, will include muted issues (optional)
    integration_name = "integration_name_example" # str | integration_name (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    start_date = "start_date_example" # str | If included, will only include issues whose most recent action occurred after this time (optional)
    status = "ONGOING" # str | status (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.issues_list(account_token=account_token, cursor=cursor, end_date=end_date, end_user_organization_name=end_user_organization_name, include_muted=include_muted, integration_name=integration_name, page_size=page_size, start_date=start_date, status=status)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling IssuesApi->issues_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_token** | **str**| account_token | [optional]
 **cursor** | **int**| The pagination cursor value. | [optional]
 **end_date** | **str**| If included, will only include issues whose most recent action occurred before this time | [optional]
 **end_user_organization_name** | **str**| end_user_organization_name | [optional]
 **include_muted** | **str**| If True, will include muted issues | [optional]
 **integration_name** | **str**| integration_name | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **start_date** | **str**| If included, will only include issues whose most recent action occurred after this time | [optional]
 **status** | **str**| status | [optional]

### Return type

[**PaginatedIssueList**](PaginatedIssueList.md)

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

# **issues_retrieve**
> Issue issues_retrieve(id)



Get a specific issue.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import issues_api
from MergeHRISClient.model.issue import Issue
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
    api_instance = issues_api.IssuesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.issues_retrieve(id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling IssuesApi->issues_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Issue**](Issue.md)

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

