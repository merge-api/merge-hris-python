# MergeHRISClient.EmployeePayrollRunsApi

All URIs are relative to *https://app.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employee_payroll_runs_create**](EmployeePayrollRunsApi.md#employee_payroll_runs_create) | **POST** /employee-payroll-runs | 
[**employee_payroll_runs_destroy**](EmployeePayrollRunsApi.md#employee_payroll_runs_destroy) | **DELETE** /employee-payroll-runs/{id} | 
[**employee_payroll_runs_list**](EmployeePayrollRunsApi.md#employee_payroll_runs_list) | **GET** /employee-payroll-runs | 
[**employee_payroll_runs_partial_update**](EmployeePayrollRunsApi.md#employee_payroll_runs_partial_update) | **PATCH** /employee-payroll-runs/{id} | 
[**employee_payroll_runs_retrieve**](EmployeePayrollRunsApi.md#employee_payroll_runs_retrieve) | **GET** /employee-payroll-runs/{id} | 
[**employee_payroll_runs_update**](EmployeePayrollRunsApi.md#employee_payroll_runs_update) | **PUT** /employee-payroll-runs/{id} | 


# **employee_payroll_runs_create**
> EmployeePayrollRun employee_payroll_runs_create(x_link_token=x_link_token, run_async=run_async, employee_payroll_run=employee_payroll_run)



Creates an `EmployeePayrollRun` object with the given values.

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
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    x_link_token = 'x_link_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
employee_payroll_run = MergeHRISClient.EmployeePayrollRun() # EmployeePayrollRun |  (optional)

    try:
        api_response = api_instance.employee_payroll_runs_create(x_link_token=x_link_token, run_async=run_async, employee_payroll_run=employee_payroll_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_link_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 
 **employee_payroll_run** | [**EmployeePayrollRun**](EmployeePayrollRun.md)|  | [optional] 

### Return type

[**EmployeePayrollRun**](EmployeePayrollRun.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_payroll_runs_destroy**
> AsyncTaskExecution employee_payroll_runs_destroy(id, x_link_token=x_link_token, run_async=run_async)



Deletes an `EmployeePayrollRun` object with the given `id`.

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
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 
x_link_token = 'x_link_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    try:
        api_response = api_instance.employee_payroll_runs_destroy(id, x_link_token=x_link_token, run_async=run_async)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_link_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 

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
**204** |  |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_payroll_runs_list**
> PaginatedEmployeePayrollRunList employee_payroll_runs_list(x_link_token=x_link_token, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, linked_account_id=linked_account_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)



Returns a list of `EmployeePayrollRun` objects.

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
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    x_link_token = 'x_link_token_example' # str | Token identifying the end user. (optional)
created_after = 'created_after_example' # str | If provided, will only return objects created after this datetime. (optional)
created_before = 'created_before_example' # str | If provided, will only return objects created before this datetime. (optional)
cursor = 56 # int | The pagination cursor value. (optional)
expand = 'expand_example' # str | Which relations should be returned in expanded form. (optional)
linked_account_id = 'linked_account_id_example' # str | If provided, will only return objects associated with the given `linked_account_id`. (optional)
modified_after = 'modified_after_example' # str | If provided, will only return objects modified after this datetime. (optional)
modified_before = 'modified_before_example' # str | If provided, will only return objects modified before this datetime. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
remote_id = 'remote_id_example' # str | The API provider's ID for the given object. (optional)

    try:
        api_response = api_instance.employee_payroll_runs_list(x_link_token=x_link_token, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, linked_account_id=linked_account_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_link_token** | **str**| Token identifying the end user. | [optional] 
 **created_after** | **str**| If provided, will only return objects created after this datetime. | [optional] 
 **created_before** | **str**| If provided, will only return objects created before this datetime. | [optional] 
 **cursor** | **int**| The pagination cursor value. | [optional] 
 **expand** | **str**| Which relations should be returned in expanded form. | [optional] 
 **linked_account_id** | **str**| If provided, will only return objects associated with the given &#x60;linked_account_id&#x60;. | [optional] 
 **modified_after** | **str**| If provided, will only return objects modified after this datetime. | [optional] 
 **modified_before** | **str**| If provided, will only return objects modified before this datetime. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **remote_id** | **str**| The API provider&#39;s ID for the given object. | [optional] 

### Return type

[**PaginatedEmployeePayrollRunList**](PaginatedEmployeePayrollRunList.md)

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

# **employee_payroll_runs_partial_update**
> EmployeePayrollRun employee_payroll_runs_partial_update(id, x_link_token=x_link_token, run_async=run_async, patched_employee_payroll_run=patched_employee_payroll_run)



Updates an `EmployeePayrollRun` object with the given `id`.

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
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 
x_link_token = 'x_link_token_example' # str | Token identifying the end user. (optional)
run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
patched_employee_payroll_run = MergeHRISClient.PatchedEmployeePayrollRun() # PatchedEmployeePayrollRun |  (optional)

    try:
        api_response = api_instance.employee_payroll_runs_partial_update(id, x_link_token=x_link_token, run_async=run_async, patched_employee_payroll_run=patched_employee_payroll_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_link_token** | **str**| Token identifying the end user. | [optional] 
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional] 
 **patched_employee_payroll_run** | [**PatchedEmployeePayrollRun**](PatchedEmployeePayrollRun.md)|  | [optional] 

### Return type

[**EmployeePayrollRun**](EmployeePayrollRun.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_payroll_runs_retrieve**
> EmployeePayrollRun employee_payroll_runs_retrieve(id, x_link_token=x_link_token, expand=expand)



Returns an `EmployeePayrollRun` object with the given `id`.

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
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 
x_link_token = 'x_link_token_example' # str | Token identifying the end user. (optional)
expand = 'expand_example' # str | Which relations should be returned in expanded form. (optional)

    try:
        api_response = api_instance.employee_payroll_runs_retrieve(id, x_link_token=x_link_token, expand=expand)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **x_link_token** | **str**| Token identifying the end user. | [optional] 
 **expand** | **str**| Which relations should be returned in expanded form. | [optional] 

### Return type

[**EmployeePayrollRun**](EmployeePayrollRun.md)

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

# **employee_payroll_runs_update**
> EmployeePayrollRun employee_payroll_runs_update(id, employee_payroll_run=employee_payroll_run)



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
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 
employee_payroll_run = MergeHRISClient.EmployeePayrollRun() # EmployeePayrollRun |  (optional)

    try:
        api_response = api_instance.employee_payroll_runs_update(id, employee_payroll_run=employee_payroll_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **employee_payroll_run** | [**EmployeePayrollRun**](EmployeePayrollRun.md)|  | [optional] 

### Return type

[**EmployeePayrollRun**](EmployeePayrollRun.md)

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

