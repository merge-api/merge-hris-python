# MergeHRISClient
The unified API for building rich integrations with multiple HR Information System platforms.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.merge.dev/](https://www.merge.dev/)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/merge-api/merge-hris-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/merge-api/merge-hris-python.git`)

Then import the package:
```python
import MergeHRISClient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import MergeHRISClient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import MergeHRISClient
from pprint import pprint
from MergeHRISClient.api import account_token_api
from MergeHRISClient.model.account_token import AccountToken
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
configuration.api_key_prefix['tokenAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_token_api.AccountTokenApi(api_client)
    public_token = "public_token_example" # str | 

    try:
        api_response = api_instance.account_token_retrieve(public_token)
        pprint(api_response)
    except MergeHRISClient.ApiException as e:
        print("Exception when calling AccountTokenApi->account_token_retrieve: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountTokenApi* | [**account_token_retrieve**](docs/AccountTokenApi.md#account_token_retrieve) | **GET** /account-token/{public_token} | 
*AvailableActionsApi* | [**available_actions_retrieve**](docs/AvailableActionsApi.md#available_actions_retrieve) | **GET** /available-actions | 
*BenefitsApi* | [**benefits_list**](docs/BenefitsApi.md#benefits_list) | **GET** /benefits | 
*BenefitsApi* | [**benefits_retrieve**](docs/BenefitsApi.md#benefits_retrieve) | **GET** /benefits/{id} | 
*CompaniesApi* | [**companies_list**](docs/CompaniesApi.md#companies_list) | **GET** /companies | 
*CompaniesApi* | [**companies_retrieve**](docs/CompaniesApi.md#companies_retrieve) | **GET** /companies/{id} | 
*EmployeePayrollRunsApi* | [**employee_payroll_runs_list**](docs/EmployeePayrollRunsApi.md#employee_payroll_runs_list) | **GET** /employee-payroll-runs | 
*EmployeePayrollRunsApi* | [**employee_payroll_runs_retrieve**](docs/EmployeePayrollRunsApi.md#employee_payroll_runs_retrieve) | **GET** /employee-payroll-runs/{id} | 
*EmployeesApi* | [**employees_list**](docs/EmployeesApi.md#employees_list) | **GET** /employees | 
*EmployeesApi* | [**employees_retrieve**](docs/EmployeesApi.md#employees_retrieve) | **GET** /employees/{id} | 
*EmploymentsApi* | [**employments_list**](docs/EmploymentsApi.md#employments_list) | **GET** /employments | 
*EmploymentsApi* | [**employments_retrieve**](docs/EmploymentsApi.md#employments_retrieve) | **GET** /employments/{id} | 
*GenerateKeyApi* | [**generate_key_create**](docs/GenerateKeyApi.md#generate_key_create) | **POST** /generate-key | 
*LinkTokenApi* | [**link_token_create**](docs/LinkTokenApi.md#link_token_create) | **POST** /link-token | 
*LocationsApi* | [**locations_list**](docs/LocationsApi.md#locations_list) | **GET** /locations | 
*LocationsApi* | [**locations_retrieve**](docs/LocationsApi.md#locations_retrieve) | **GET** /locations/{id} | 
*PassthroughApi* | [**passthrough_create**](docs/PassthroughApi.md#passthrough_create) | **POST** /passthrough | 
*PayrollRunsApi* | [**payroll_runs_list**](docs/PayrollRunsApi.md#payroll_runs_list) | **GET** /payroll-runs | 
*PayrollRunsApi* | [**payroll_runs_retrieve**](docs/PayrollRunsApi.md#payroll_runs_retrieve) | **GET** /payroll-runs/{id} | 
*RegenerateKeyApi* | [**regenerate_key_create**](docs/RegenerateKeyApi.md#regenerate_key_create) | **POST** /regenerate-key | 
*SyncStatusApi* | [**sync_status_retrieve**](docs/SyncStatusApi.md#sync_status_retrieve) | **GET** /sync-status | 
*TeamsApi* | [**teams_list**](docs/TeamsApi.md#teams_list) | **GET** /teams | 
*TeamsApi* | [**teams_retrieve**](docs/TeamsApi.md#teams_retrieve) | **GET** /teams/{id} | 
*TimeOffApi* | [**time_off_list**](docs/TimeOffApi.md#time_off_list) | **GET** /time-off | 
*TimeOffApi* | [**time_off_retrieve**](docs/TimeOffApi.md#time_off_retrieve) | **GET** /time-off/{id} | 


## Documentation For Models

 - [AccountIntegration](docs/AccountIntegration.md)
 - [AccountToken](docs/AccountToken.md)
 - [AvailableActions](docs/AvailableActions.md)
 - [Benefit](docs/Benefit.md)
 - [BenefitPlanTypeEnum](docs/BenefitPlanTypeEnum.md)
 - [Company](docs/Company.md)
 - [CountryEnum](docs/CountryEnum.md)
 - [DataPassthroughRequest](docs/DataPassthroughRequest.md)
 - [Deduction](docs/Deduction.md)
 - [Earning](docs/Earning.md)
 - [Employee](docs/Employee.md)
 - [EmployeePayrollRun](docs/EmployeePayrollRun.md)
 - [Employment](docs/Employment.md)
 - [EmploymentStatusEnum](docs/EmploymentStatusEnum.md)
 - [EmploymentTypeEnum](docs/EmploymentTypeEnum.md)
 - [EndUserDetailsRequest](docs/EndUserDetailsRequest.md)
 - [EthnicityEnum](docs/EthnicityEnum.md)
 - [FlsaStatusEnum](docs/FlsaStatusEnum.md)
 - [GenderEnum](docs/GenderEnum.md)
 - [GenerateRemoteKeyRequest](docs/GenerateRemoteKeyRequest.md)
 - [LinkToken](docs/LinkToken.md)
 - [Location](docs/Location.md)
 - [MaritalStatusEnum](docs/MaritalStatusEnum.md)
 - [MethodEnum](docs/MethodEnum.md)
 - [ModelOperation](docs/ModelOperation.md)
 - [PaginatedBenefitList](docs/PaginatedBenefitList.md)
 - [PaginatedCompanyList](docs/PaginatedCompanyList.md)
 - [PaginatedEmployeeList](docs/PaginatedEmployeeList.md)
 - [PaginatedEmployeePayrollRunList](docs/PaginatedEmployeePayrollRunList.md)
 - [PaginatedEmploymentList](docs/PaginatedEmploymentList.md)
 - [PaginatedLocationList](docs/PaginatedLocationList.md)
 - [PaginatedPayrollRunList](docs/PaginatedPayrollRunList.md)
 - [PaginatedTeamList](docs/PaginatedTeamList.md)
 - [PaginatedTimeOffList](docs/PaginatedTimeOffList.md)
 - [PayCurrencyEnum](docs/PayCurrencyEnum.md)
 - [PayFrequencyEnum](docs/PayFrequencyEnum.md)
 - [PayPeriodEnum](docs/PayPeriodEnum.md)
 - [PayrollRun](docs/PayrollRun.md)
 - [RemoteData](docs/RemoteData.md)
 - [RemoteKey](docs/RemoteKey.md)
 - [RemoteKeyForRegenerationRequest](docs/RemoteKeyForRegenerationRequest.md)
 - [RemoteResponse](docs/RemoteResponse.md)
 - [RequestTypeEnum](docs/RequestTypeEnum.md)
 - [RunStateEnum](docs/RunStateEnum.md)
 - [RunTypeEnum](docs/RunTypeEnum.md)
 - [StateEnum](docs/StateEnum.md)
 - [SyncStatus](docs/SyncStatus.md)
 - [Tax](docs/Tax.md)
 - [Team](docs/Team.md)
 - [TimeOff](docs/TimeOff.md)
 - [TimeOffStatusEnum](docs/TimeOffStatusEnum.md)
 - [TypeEnum](docs/TypeEnum.md)
 - [UnitsEnum](docs/UnitsEnum.md)


## Documentation For Authorization


## tokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

hello@merge.dev


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in MergeHRISClient.apis and MergeHRISClient.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from MergeHRISClient.api.default_api import DefaultApi`
- `from MergeHRISClient.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import MergeHRISClient
from MergeHRISClient.apis import *
from MergeHRISClient.models import *
```

