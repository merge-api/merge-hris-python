# MergeHRISClient.EmployeePayrollRunsApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employee_payroll_runs_list**](EmployeePayrollRunsApi.md#employee_payroll_runs_list) | **GET** /employee-payroll-runs | 
[**employee_payroll_runs_retrieve**](EmployeePayrollRunsApi.md#employee_payroll_runs_retrieve) | **GET** /employee-payroll-runs/{id} | 


# **employee_payroll_runs_list**
> PaginatedEmployeePayrollRunList employee_payroll_runs_list(x_account_token)



Returns a list of `EmployeePayrollRun` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import employee_payroll_runs_api
from MergeHRISClient.model.paginated_employee_payroll_run_list import PaginatedEmployeePayrollRunList
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
    api_instance = employee_payroll_runs_api.EmployeePayrollRunsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    employee_id = "employee_id_example" # str | If provided, will only return employee payroll runs for this employee. (optional)
    ended_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return employee payroll runs ended after this datetime. (optional)
    ended_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return employee payroll runs ended before this datetime. (optional)
    expand = "employee,payroll_run" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    payroll_run_id = "payroll_run_id_example" # str | If provided, will only return employee payroll runs for this employee. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    started_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return employee payroll runs started after this datetime. (optional)
    started_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return employee payroll runs started before this datetime. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.employee_payroll_runs_list(x_account_token)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.employee_payroll_runs_list(x_account_token, created_after=created_after, created_before=created_before, cursor=cursor, employee_id=employee_id, ended_after=ended_after, ended_before=ended_before, expand=expand, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, payroll_run_id=payroll_run_id, remote_id=remote_id, started_after=started_after, started_before=started_before)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **employee_id** | **str**| If provided, will only return employee payroll runs for this employee. | [optional]
 **ended_after** | **datetime, none_type**| If provided, will only return employee payroll runs ended after this datetime. | [optional]
 **ended_before** | **datetime, none_type**| If provided, will only return employee payroll runs ended before this datetime. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **payroll_run_id** | **str**| If provided, will only return employee payroll runs for this employee. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **started_after** | **datetime, none_type**| If provided, will only return employee payroll runs started after this datetime. | [optional]
 **started_before** | **datetime, none_type**| If provided, will only return employee payroll runs started before this datetime. | [optional]

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

# **employee_payroll_runs_retrieve**
> EmployeePayrollRun employee_payroll_runs_retrieve(x_account_token, id)



Returns an `EmployeePayrollRun` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import employee_payroll_runs_api
from MergeHRISClient.model.employee_payroll_run import EmployeePayrollRun
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
    api_instance = employee_payroll_runs_api.EmployeePayrollRunsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "employee,payroll_run" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.employee_payroll_runs_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.employee_payroll_runs_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

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

