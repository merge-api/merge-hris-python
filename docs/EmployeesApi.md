# MergeHRISClient.EmployeesApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employees_list**](EmployeesApi.md#employees_list) | **GET** /employees | 
[**employees_retrieve**](EmployeesApi.md#employees_retrieve) | **GET** /employees/{id} | 


# **employees_list**
> PaginatedEmployeeList employees_list(x_account_token, company_id=company_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, manager_id=manager_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, team_id=team_id, work_location_id=work_location_id)



Returns a list of `Employee` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import MergeHRISClient
from MergeHRISClient.rest import ApiException
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
configuration = MergeHRISClient.Configuration(
    host = "https://api.merge.dev/api/hris/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeesApi(api_client)
    x_account_token = 'x_account_token_example' # str | Token identifying the end user.
company_id = 'company_id_example' # str | If provided, will only return employees for this company. (optional)
created_after = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects created after this datetime. (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects created before this datetime. (optional)
cursor = 'cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw' # str | The pagination cursor value. (optional)
expand = 'employments,documents,home_location,work_location,manager,team,company' # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
manager_id = 'manager_id_example' # str | If provided, will only return employees for this manager. (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects modified after this datetime. (optional)
modified_before = '2013-10-20T19:20:30+01:00' # datetime | If provided, will only return objects modified before this datetime. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
remote_id = 'remote_id_example' # str | The API provider's ID for the given object. (optional)
team_id = 'team_id_example' # str | If provided, will only return employees for this team. (optional)
work_location_id = 'work_location_id_example' # str | If provided, will only return employees for this location. (optional)

    try:
        api_response = api_instance.employees_list(x_account_token, company_id=company_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, manager_id=manager_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, team_id=team_id, work_location_id=work_location_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->employees_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. | 
 **company_id** | [**str**](.md)| If provided, will only return employees for this company. | [optional] 
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional] 
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional] 
 **cursor** | **str**| The pagination cursor value. | [optional] 
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] 
 **manager_id** | [**str**](.md)| If provided, will only return employees for this manager. | [optional] 
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional] 
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **remote_id** | **str**| The API provider&#39;s ID for the given object. | [optional] 
 **team_id** | [**str**](.md)| If provided, will only return employees for this team. | [optional] 
 **work_location_id** | [**str**](.md)| If provided, will only return employees for this location. | [optional] 

### Return type

[**PaginatedEmployeeList**](PaginatedEmployeeList.md)

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

# **employees_retrieve**
> Employee employees_retrieve(x_account_token, id, expand=expand)



Returns an `Employee` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import MergeHRISClient
from MergeHRISClient.rest import ApiException
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
configuration = MergeHRISClient.Configuration(
    host = "https://api.merge.dev/api/hris/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeesApi(api_client)
    x_account_token = 'x_account_token_example' # str | Token identifying the end user.
id = 'id_example' # str | 
expand = 'employments,documents,home_location,work_location,manager,team,company' # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)

    try:
        api_response = api_instance.employees_retrieve(x_account_token, id, expand=expand)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->employees_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. | 
 **id** | [**str**](.md)|  | 
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] 

### Return type

[**Employee**](Employee.md)

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

