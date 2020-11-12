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
> EmployeePayrollRun employee_payroll_runs_create(employee_payroll_run=employee_payroll_run)



Creates an `EmployeePayrollRun` object with the given values.

### Example

* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    employee_payroll_run = MergeHRISClient.EmployeePayrollRun() # EmployeePayrollRun |  (optional)

    try:
        api_response = api_instance.employee_payroll_runs_create(employee_payroll_run=employee_payroll_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_create: %s\n" % e)
```

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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    employee_payroll_run = MergeHRISClient.EmployeePayrollRun() # EmployeePayrollRun |  (optional)

    try:
        api_response = api_instance.employee_payroll_runs_create(employee_payroll_run=employee_payroll_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_payroll_run** | [**EmployeePayrollRun**](EmployeePayrollRun.md)|  | [optional] 

### Return type

[**EmployeePayrollRun**](EmployeePayrollRun.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_payroll_runs_destroy**
> employee_payroll_runs_destroy(id)



Deletes an `EmployeePayrollRun` object with the given `id`.

### Example

* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.employee_payroll_runs_destroy(id)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_destroy: %s\n" % e)
```

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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.employee_payroll_runs_destroy(id)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_payroll_runs_list**
> PaginatedEmployeePayrollRunList employee_payroll_runs_list(cursor=cursor, linked_account_id=linked_account_id, origin_id=origin_id)



Returns a list of `EmployeePayrollRun` objects.

### Example

* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    cursor = 56 # int | The pagination cursor value. (optional)
linked_account_id = 'linked_account_id_example' # str | If provided, will only return objects associated with the given `linked_account_id`. (optional)
origin_id = 'origin_id_example' # str | The API provider's ID for the given object. (optional)

    try:
        api_response = api_instance.employee_payroll_runs_list(cursor=cursor, linked_account_id=linked_account_id, origin_id=origin_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_list: %s\n" % e)
```

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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    cursor = 56 # int | The pagination cursor value. (optional)
linked_account_id = 'linked_account_id_example' # str | If provided, will only return objects associated with the given `linked_account_id`. (optional)
origin_id = 'origin_id_example' # str | The API provider's ID for the given object. (optional)

    try:
        api_response = api_instance.employee_payroll_runs_list(cursor=cursor, linked_account_id=linked_account_id, origin_id=origin_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **int**| The pagination cursor value. | [optional] 
 **linked_account_id** | **str**| If provided, will only return objects associated with the given &#x60;linked_account_id&#x60;. | [optional] 
 **origin_id** | **str**| The API provider&#39;s ID for the given object. | [optional] 

### Return type

[**PaginatedEmployeePayrollRunList**](PaginatedEmployeePayrollRunList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_payroll_runs_partial_update**
> EmployeePayrollRun employee_payroll_runs_partial_update(id, patched_employee_payroll_run=patched_employee_payroll_run)



Updates an `EmployeePayrollRun` object with the given `id`.

### Example

* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 
patched_employee_payroll_run = MergeHRISClient.PatchedEmployeePayrollRun() # PatchedEmployeePayrollRun |  (optional)

    try:
        api_response = api_instance.employee_payroll_runs_partial_update(id, patched_employee_payroll_run=patched_employee_payroll_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_partial_update: %s\n" % e)
```

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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 
patched_employee_payroll_run = MergeHRISClient.PatchedEmployeePayrollRun() # PatchedEmployeePayrollRun |  (optional)

    try:
        api_response = api_instance.employee_payroll_runs_partial_update(id, patched_employee_payroll_run=patched_employee_payroll_run)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **patched_employee_payroll_run** | [**PatchedEmployeePayrollRun**](PatchedEmployeePayrollRun.md)|  | [optional] 

### Return type

[**EmployeePayrollRun**](EmployeePayrollRun.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_payroll_runs_retrieve**
> EmployeePayrollRun employee_payroll_runs_retrieve(id)



Returns an `EmployeePayrollRun` object with the given `id`.

### Example

* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.employee_payroll_runs_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_retrieve: %s\n" % e)
```

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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

# Configure Bearer authorization (Token): tokenAuth
configuration = MergeHRISClient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.EmployeePayrollRunsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.employee_payroll_runs_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmployeePayrollRunsApi->employee_payroll_runs_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**EmployeePayrollRun**](EmployeePayrollRun.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

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

* Api Key Authentication (cookieAuth):
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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

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

# Configure API key authorization: cookieAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Session': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Session'] = 'Bearer'

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

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

