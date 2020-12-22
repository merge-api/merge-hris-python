# MergeHRISClient.TasksApi

All URIs are relative to *https://app.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_list**](TasksApi.md#tasks_list) | **GET** /tasks | 
[**tasks_retrieve**](TasksApi.md#tasks_retrieve) | **GET** /tasks/{task_id} | 


# **tasks_list**
> PaginatedAsyncTaskExecutionList tasks_list(x_link_token=x_link_token, created_after=created_after, created_before=created_before, cursor=cursor, linked_account_id=linked_account_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, status=status)



Returns all `AsyncTaskExecution` objects for the requester's organization.

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
    api_instance = MergeHRISClient.TasksApi(api_client)
    x_link_token = 'x_link_token_example' # str | Token identifying the end user. (optional)
created_after = 'created_after_example' # str | If provided, will only return objects created after this datetime. (optional)
created_before = 'created_before_example' # str | If provided, will only return objects created before this datetime. (optional)
cursor = 56 # int | The pagination cursor value. (optional)
linked_account_id = 'linked_account_id_example' # str | If provided, will only return objects associated with the given `linked_account_id`. (optional)
modified_after = 'modified_after_example' # str | If provided, will only return objects modified after this datetime. (optional)
modified_before = 'modified_before_example' # str | If provided, will only return objects modified before this datetime. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
remote_id = 'remote_id_example' # str | The API provider's ID for the given object. (optional)
status = 'status_example' # str | The status of the task. (optional)

    try:
        api_response = api_instance.tasks_list(x_link_token=x_link_token, created_after=created_after, created_before=created_before, cursor=cursor, linked_account_id=linked_account_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_link_token** | **str**| Token identifying the end user. | [optional] 
 **created_after** | **str**| If provided, will only return objects created after this datetime. | [optional] 
 **created_before** | **str**| If provided, will only return objects created before this datetime. | [optional] 
 **cursor** | **int**| The pagination cursor value. | [optional] 
 **linked_account_id** | **str**| If provided, will only return objects associated with the given &#x60;linked_account_id&#x60;. | [optional] 
 **modified_after** | **str**| If provided, will only return objects modified after this datetime. | [optional] 
 **modified_before** | **str**| If provided, will only return objects modified before this datetime. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **remote_id** | **str**| The API provider&#39;s ID for the given object. | [optional] 
 **status** | **str**| The status of the task. | [optional] 

### Return type

[**PaginatedAsyncTaskExecutionList**](PaginatedAsyncTaskExecutionList.md)

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

# **tasks_retrieve**
> AsyncTaskExecution tasks_retrieve(task_id, x_link_token=x_link_token)



Returns an `AsyncTaskExecution` object with the given `id`.

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
    api_instance = MergeHRISClient.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
x_link_token = 'x_link_token_example' # str | Token identifying the end user. (optional)

    try:
        api_response = api_instance.tasks_retrieve(task_id, x_link_token=x_link_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->tasks_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | [**str**](.md)|  | 
 **x_link_token** | **str**| Token identifying the end user. | [optional] 

### Return type

[**AsyncTaskExecution**](AsyncTaskExecution.md)

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

