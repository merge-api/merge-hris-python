# MergeHRISClient.TeamsApi

All URIs are relative to *https://app.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_create**](TeamsApi.md#teams_create) | **POST** /teams | 
[**teams_destroy**](TeamsApi.md#teams_destroy) | **DELETE** /teams/{id} | 
[**teams_list**](TeamsApi.md#teams_list) | **GET** /teams | 
[**teams_partial_update**](TeamsApi.md#teams_partial_update) | **PATCH** /teams/{id} | 
[**teams_retrieve**](TeamsApi.md#teams_retrieve) | **GET** /teams/{id} | 
[**teams_update**](TeamsApi.md#teams_update) | **PUT** /teams/{id} | 


# **teams_create**
> Team teams_create(team=team)



Creates a `Team` object with the given values.

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
    api_instance = MergeHRISClient.TeamsApi(api_client)
    team = MergeHRISClient.Team() # Team |  (optional)

    try:
        api_response = api_instance.teams_create(team=team)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | [**Team**](Team.md)|  | [optional] 

### Return type

[**Team**](Team.md)

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

# **teams_destroy**
> teams_destroy(id)



Deletes a `Team` object with the given `id`.

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
    api_instance = MergeHRISClient.TeamsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.teams_destroy(id)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_destroy: %s\n" % e)
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

# **teams_list**
> PaginatedTeamList teams_list(cursor=cursor, linked_account_id=linked_account_id, origin_id=origin_id)



Returns a list of `Team` objects.

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
    api_instance = MergeHRISClient.TeamsApi(api_client)
    cursor = 56 # int | The pagination cursor value. (optional)
linked_account_id = 'linked_account_id_example' # str | If provided, will only return objects associated with the given `linked_account_id`. (optional)
origin_id = 'origin_id_example' # str | The API provider's ID for the given object. (optional)

    try:
        api_response = api_instance.teams_list(cursor=cursor, linked_account_id=linked_account_id, origin_id=origin_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **int**| The pagination cursor value. | [optional] 
 **linked_account_id** | **str**| If provided, will only return objects associated with the given &#x60;linked_account_id&#x60;. | [optional] 
 **origin_id** | **str**| The API provider&#39;s ID for the given object. | [optional] 

### Return type

[**PaginatedTeamList**](PaginatedTeamList.md)

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

# **teams_partial_update**
> Team teams_partial_update(id, patched_team=patched_team)



Updates a `Team` object with the given `id`.

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
    api_instance = MergeHRISClient.TeamsApi(api_client)
    id = 'id_example' # str | 
patched_team = MergeHRISClient.PatchedTeam() # PatchedTeam |  (optional)

    try:
        api_response = api_instance.teams_partial_update(id, patched_team=patched_team)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **patched_team** | [**PatchedTeam**](PatchedTeam.md)|  | [optional] 

### Return type

[**Team**](Team.md)

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

# **teams_retrieve**
> Team teams_retrieve(id)



Returns a `Team` object with the given `id`.

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
    api_instance = MergeHRISClient.TeamsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.teams_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Team**](Team.md)

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

# **teams_update**
> Team teams_update(id, team=team)



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
    api_instance = MergeHRISClient.TeamsApi(api_client)
    id = 'id_example' # str | 
team = MergeHRISClient.Team() # Team |  (optional)

    try:
        api_response = api_instance.teams_update(id, team=team)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->teams_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **team** | [**Team**](Team.md)|  | [optional] 

### Return type

[**Team**](Team.md)

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

