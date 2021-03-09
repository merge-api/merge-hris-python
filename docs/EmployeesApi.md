# MergeHRISClient.EmployeesApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employees_create**](EmployeesApi.md#employees_create) | **POST** /employees | 
[**employees_list**](EmployeesApi.md#employees_list) | **GET** /employees | 
[**employees_retrieve**](EmployeesApi.md#employees_retrieve) | **GET** /employees/{id} | 


# **employees_create**
> Employee employees_create(x_account_token)



Creates an `Employee` object with the given values.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import employees_api
from MergeHRISClient.model.employee import Employee
from MergeHRISClient.model.create_employee import CreateEmployee
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
    api_instance = employees_api.EmployeesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)
    create_employee = CreateEmployee(
        company="8d9fd929-436c-4fd4-a48b-0c61f68d6178",
        first_name="Jane",
        last_name="Doe",
        display_full_name="Jane Doe",
        work_email="jane@merge.dev",
        personal_email="jane@gmail.com",
        mobile_phone_number="+1234567890",
        employments=["17a54124-287f-494d-965e-3c5b330c9a68"],
        home_location="d2f972d0-2526-434b-9409-4c3b468e08f0",
        work_location="9efbc633-3387-4306-aa55-e2c635e6bb4f",
        manager="0048ea5b-911e-4dff-9364-92070dea62ff",
        team="249c9faa-3045-4a31-953b-8f22d3613301",
        ssn="1234567890",
        gender=,
        ethnicity=,
        marital_status=,
        date_of_birth=dateutil_parser('1970-01-01T00:00:00.00Z'),
        hire_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        employment_status=,
        termination_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        avatar="http://alturl.com/h2h8m",
        code="code_example",
    ) # CreateEmployee |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.employees_create(x_account_token)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeesApi->employees_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.employees_create(x_account_token, run_async=run_async, create_employee=create_employee)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeesApi->employees_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]
 **create_employee** | [**CreateEmployee**](CreateEmployee.md)|  | [optional]

### Return type

[**Employee**](Employee.md)

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

# **employees_list**
> PaginatedEmployeeList employees_list(x_account_token)



Returns a list of `Employee` objects.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import employees_api
from MergeHRISClient.model.paginated_employee_list import PaginatedEmployeeList
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
    api_instance = employees_api.EmployeesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    company_id = "company_id_example" # str | If provided, will only return employees for this company. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "employments,home_location,work_location,manager,team,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    manager_id = "manager_id_example" # str | If provided, will only return employees for this manager. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    team_id = "team_id_example" # str | If provided, will only return employees for this team. (optional)
    work_location_id = "work_location_id_example" # str | If provided, will only return employees for this location. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.employees_list(x_account_token)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeesApi->employees_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.employees_list(x_account_token, company_id=company_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_remote_data=include_remote_data, manager_id=manager_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, team_id=team_id, work_location_id=work_location_id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeesApi->employees_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **company_id** | **str**| If provided, will only return employees for this company. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **manager_id** | **str**| If provided, will only return employees for this manager. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **team_id** | **str**| If provided, will only return employees for this team. | [optional]
 **work_location_id** | **str**| If provided, will only return employees for this location. | [optional]

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
> Employee employees_retrieve(x_account_token, id)



Returns an `Employee` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeHRISClient
from MergeHRISClient.api import employees_api
from MergeHRISClient.model.employee import Employee
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
    api_instance = employees_api.EmployeesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "employments,home_location,work_location,manager,team,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.employees_retrieve(x_account_token, id)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeesApi->employees_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.employees_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling EmployeesApi->employees_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

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

