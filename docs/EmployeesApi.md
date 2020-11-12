# MergeHRISClient.EmployeesApi

All URIs are relative to *https://app.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employees_create**](EmployeesApi.md#employees_create) | **POST** /employees | 
[**employees_destroy**](EmployeesApi.md#employees_destroy) | **DELETE** /employees/{id} | 
[**employees_list**](EmployeesApi.md#employees_list) | **GET** /employees | 
[**employees_partial_update**](EmployeesApi.md#employees_partial_update) | **PATCH** /employees/{id} | 
[**employees_retrieve**](EmployeesApi.md#employees_retrieve) | **GET** /employees/{id} | 
[**employees_update**](EmployeesApi.md#employees_update) | **PUT** /employees/{id} | 


# **employees_create**
> Employee employees_create(employee=employee)



Creates an `Employee` object with the given values.

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
    api_instance = MergeHRISClient.EmployeesApi(api_client)
    employee = MergeHRISClient.Employee() # Employee |  (optional)

    try:
        api_response = api_instance.employees_create(employee=employee)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->employees_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee** | [**Employee**](Employee.md)|  | [optional] 

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

# **employees_destroy**
> employees_destroy(id)



Deletes an `Employee` object with the given `id`.

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
    api_instance = MergeHRISClient.EmployeesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.employees_destroy(id)
    except ApiException as e:
        print("Exception when calling EmployeesApi->employees_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_list**
> PaginatedEmployeeList employees_list(cursor=cursor, linked_account_id=linked_account_id, origin_id=origin_id)



Returns a list of `Employee` objects.

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
    api_instance = MergeHRISClient.EmployeesApi(api_client)
    cursor = 56 # int | The pagination cursor value. (optional)
linked_account_id = 'linked_account_id_example' # str | If provided, will only return objects associated with the given `linked_account_id`. (optional)
origin_id = 'origin_id_example' # str | The API provider's ID for the given object. (optional)

    try:
        api_response = api_instance.employees_list(cursor=cursor, linked_account_id=linked_account_id, origin_id=origin_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->employees_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **int**| The pagination cursor value. | [optional] 
 **linked_account_id** | **str**| If provided, will only return objects associated with the given &#x60;linked_account_id&#x60;. | [optional] 
 **origin_id** | **str**| The API provider&#39;s ID for the given object. | [optional] 

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

# **employees_partial_update**
> Employee employees_partial_update(id, patched_employee=patched_employee)



Updates an `Employee` object with the given `id`.

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
    api_instance = MergeHRISClient.EmployeesApi(api_client)
    id = 'id_example' # str | 
patched_employee = MergeHRISClient.PatchedEmployee() # PatchedEmployee |  (optional)

    try:
        api_response = api_instance.employees_partial_update(id, patched_employee=patched_employee)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->employees_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **patched_employee** | [**PatchedEmployee**](PatchedEmployee.md)|  | [optional] 

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

# **employees_retrieve**
> Employee employees_retrieve(id)



Returns an `Employee` object with the given `id`.

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
    api_instance = MergeHRISClient.EmployeesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.employees_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->employees_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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

# **employees_update**
> Employee employees_update(id, employee=employee)



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
    api_instance = MergeHRISClient.EmployeesApi(api_client)
    id = 'id_example' # str | 
employee = MergeHRISClient.Employee() # Employee |  (optional)

    try:
        api_response = api_instance.employees_update(id, employee=employee)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeesApi->employees_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **employee** | [**Employee**](Employee.md)|  | [optional] 

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

