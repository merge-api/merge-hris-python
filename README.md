# MergeHRISClient
The unified API for building rich integrations with multiple HR Information System platforms.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.merge.dev/](https://www.merge.dev/)

## Requirements.

Python 2.7 and 3.4+

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

# Configure API key authorization: tokenAuth
configuration = MergeHRISClient.Configuration(
    host = "https://app.merge.dev/api/hris/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with MergeHRISClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = MergeHRISClient.AccountTokenApi(api_client)
    production_key = 'production_key_example' # str | The requesting organization's production key.
public_token = 'public_token_example' # str | 

    try:
        api_response = api_instance.account_token_retrieve(production_key, public_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountTokenApi->account_token_retrieve: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://app.merge.dev/api/hris/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountTokenApi* | [**account_token_retrieve**](docs/AccountTokenApi.md#account_token_retrieve) | **GET** /account-token/{public_token} | 
*BenefitsApi* | [**benefits_create**](docs/BenefitsApi.md#benefits_create) | **POST** /benefits | 
*BenefitsApi* | [**benefits_destroy**](docs/BenefitsApi.md#benefits_destroy) | **DELETE** /benefits/{id} | 
*BenefitsApi* | [**benefits_list**](docs/BenefitsApi.md#benefits_list) | **GET** /benefits | 
*BenefitsApi* | [**benefits_partial_update**](docs/BenefitsApi.md#benefits_partial_update) | **PATCH** /benefits/{id} | 
*BenefitsApi* | [**benefits_retrieve**](docs/BenefitsApi.md#benefits_retrieve) | **GET** /benefits/{id} | 
*CompaniesApi* | [**companies_create**](docs/CompaniesApi.md#companies_create) | **POST** /companies | 
*CompaniesApi* | [**companies_destroy**](docs/CompaniesApi.md#companies_destroy) | **DELETE** /companies/{id} | 
*CompaniesApi* | [**companies_list**](docs/CompaniesApi.md#companies_list) | **GET** /companies | 
*CompaniesApi* | [**companies_partial_update**](docs/CompaniesApi.md#companies_partial_update) | **PATCH** /companies/{id} | 
*CompaniesApi* | [**companies_retrieve**](docs/CompaniesApi.md#companies_retrieve) | **GET** /companies/{id} | 
*DeductionsApi* | [**deductions_create**](docs/DeductionsApi.md#deductions_create) | **POST** /deductions | 
*DeductionsApi* | [**deductions_destroy**](docs/DeductionsApi.md#deductions_destroy) | **DELETE** /deductions/{id} | 
*DeductionsApi* | [**deductions_list**](docs/DeductionsApi.md#deductions_list) | **GET** /deductions | 
*DeductionsApi* | [**deductions_partial_update**](docs/DeductionsApi.md#deductions_partial_update) | **PATCH** /deductions/{id} | 
*DeductionsApi* | [**deductions_retrieve**](docs/DeductionsApi.md#deductions_retrieve) | **GET** /deductions/{id} | 
*DocumentsApi* | [**documents_create**](docs/DocumentsApi.md#documents_create) | **POST** /documents | 
*DocumentsApi* | [**documents_destroy**](docs/DocumentsApi.md#documents_destroy) | **DELETE** /documents/{id} | 
*DocumentsApi* | [**documents_list**](docs/DocumentsApi.md#documents_list) | **GET** /documents | 
*DocumentsApi* | [**documents_partial_update**](docs/DocumentsApi.md#documents_partial_update) | **PATCH** /documents/{id} | 
*DocumentsApi* | [**documents_retrieve**](docs/DocumentsApi.md#documents_retrieve) | **GET** /documents/{id} | 
*EarningsApi* | [**earnings_create**](docs/EarningsApi.md#earnings_create) | **POST** /earnings | 
*EarningsApi* | [**earnings_destroy**](docs/EarningsApi.md#earnings_destroy) | **DELETE** /earnings/{id} | 
*EarningsApi* | [**earnings_list**](docs/EarningsApi.md#earnings_list) | **GET** /earnings | 
*EarningsApi* | [**earnings_partial_update**](docs/EarningsApi.md#earnings_partial_update) | **PATCH** /earnings/{id} | 
*EarningsApi* | [**earnings_retrieve**](docs/EarningsApi.md#earnings_retrieve) | **GET** /earnings/{id} | 
*EmployeePayrollRunsApi* | [**employee_payroll_runs_create**](docs/EmployeePayrollRunsApi.md#employee_payroll_runs_create) | **POST** /employee-payroll-runs | 
*EmployeePayrollRunsApi* | [**employee_payroll_runs_destroy**](docs/EmployeePayrollRunsApi.md#employee_payroll_runs_destroy) | **DELETE** /employee-payroll-runs/{id} | 
*EmployeePayrollRunsApi* | [**employee_payroll_runs_list**](docs/EmployeePayrollRunsApi.md#employee_payroll_runs_list) | **GET** /employee-payroll-runs | 
*EmployeePayrollRunsApi* | [**employee_payroll_runs_partial_update**](docs/EmployeePayrollRunsApi.md#employee_payroll_runs_partial_update) | **PATCH** /employee-payroll-runs/{id} | 
*EmployeePayrollRunsApi* | [**employee_payroll_runs_retrieve**](docs/EmployeePayrollRunsApi.md#employee_payroll_runs_retrieve) | **GET** /employee-payroll-runs/{id} | 
*EmployeesApi* | [**employees_create**](docs/EmployeesApi.md#employees_create) | **POST** /employees | 
*EmployeesApi* | [**employees_destroy**](docs/EmployeesApi.md#employees_destroy) | **DELETE** /employees/{id} | 
*EmployeesApi* | [**employees_list**](docs/EmployeesApi.md#employees_list) | **GET** /employees | 
*EmployeesApi* | [**employees_partial_update**](docs/EmployeesApi.md#employees_partial_update) | **PATCH** /employees/{id} | 
*EmployeesApi* | [**employees_retrieve**](docs/EmployeesApi.md#employees_retrieve) | **GET** /employees/{id} | 
*EmploymentsApi* | [**employments_create**](docs/EmploymentsApi.md#employments_create) | **POST** /employments | 
*EmploymentsApi* | [**employments_destroy**](docs/EmploymentsApi.md#employments_destroy) | **DELETE** /employments/{id} | 
*EmploymentsApi* | [**employments_list**](docs/EmploymentsApi.md#employments_list) | **GET** /employments | 
*EmploymentsApi* | [**employments_partial_update**](docs/EmploymentsApi.md#employments_partial_update) | **PATCH** /employments/{id} | 
*EmploymentsApi* | [**employments_retrieve**](docs/EmploymentsApi.md#employments_retrieve) | **GET** /employments/{id} | 
*LinkTokenApi* | [**link_token_create**](docs/LinkTokenApi.md#link_token_create) | **POST** /link-token | 
*LocationsApi* | [**locations_create**](docs/LocationsApi.md#locations_create) | **POST** /locations | 
*LocationsApi* | [**locations_destroy**](docs/LocationsApi.md#locations_destroy) | **DELETE** /locations/{id} | 
*LocationsApi* | [**locations_list**](docs/LocationsApi.md#locations_list) | **GET** /locations | 
*LocationsApi* | [**locations_partial_update**](docs/LocationsApi.md#locations_partial_update) | **PATCH** /locations/{id} | 
*LocationsApi* | [**locations_retrieve**](docs/LocationsApi.md#locations_retrieve) | **GET** /locations/{id} | 
*PayrollRunsApi* | [**payroll_runs_create**](docs/PayrollRunsApi.md#payroll_runs_create) | **POST** /payroll-runs | 
*PayrollRunsApi* | [**payroll_runs_destroy**](docs/PayrollRunsApi.md#payroll_runs_destroy) | **DELETE** /payroll-runs/{id} | 
*PayrollRunsApi* | [**payroll_runs_list**](docs/PayrollRunsApi.md#payroll_runs_list) | **GET** /payroll-runs | 
*PayrollRunsApi* | [**payroll_runs_partial_update**](docs/PayrollRunsApi.md#payroll_runs_partial_update) | **PATCH** /payroll-runs/{id} | 
*PayrollRunsApi* | [**payroll_runs_retrieve**](docs/PayrollRunsApi.md#payroll_runs_retrieve) | **GET** /payroll-runs/{id} | 
*ReportsApi* | [**reports_create**](docs/ReportsApi.md#reports_create) | **POST** /reports | 
*ReportsApi* | [**reports_destroy**](docs/ReportsApi.md#reports_destroy) | **DELETE** /reports/{id} | 
*ReportsApi* | [**reports_list**](docs/ReportsApi.md#reports_list) | **GET** /reports | 
*ReportsApi* | [**reports_partial_update**](docs/ReportsApi.md#reports_partial_update) | **PATCH** /reports/{id} | 
*ReportsApi* | [**reports_retrieve**](docs/ReportsApi.md#reports_retrieve) | **GET** /reports/{id} | 
*TasksApi* | [**tasks_list**](docs/TasksApi.md#tasks_list) | **GET** /tasks | 
*TasksApi* | [**tasks_retrieve**](docs/TasksApi.md#tasks_retrieve) | **GET** /tasks/{common_model_id} | 
*TaxesApi* | [**taxes_create**](docs/TaxesApi.md#taxes_create) | **POST** /taxes | 
*TaxesApi* | [**taxes_destroy**](docs/TaxesApi.md#taxes_destroy) | **DELETE** /taxes/{id} | 
*TaxesApi* | [**taxes_list**](docs/TaxesApi.md#taxes_list) | **GET** /taxes | 
*TaxesApi* | [**taxes_partial_update**](docs/TaxesApi.md#taxes_partial_update) | **PATCH** /taxes/{id} | 
*TaxesApi* | [**taxes_retrieve**](docs/TaxesApi.md#taxes_retrieve) | **GET** /taxes/{id} | 
*TeamsApi* | [**teams_create**](docs/TeamsApi.md#teams_create) | **POST** /teams | 
*TeamsApi* | [**teams_destroy**](docs/TeamsApi.md#teams_destroy) | **DELETE** /teams/{id} | 
*TeamsApi* | [**teams_list**](docs/TeamsApi.md#teams_list) | **GET** /teams | 
*TeamsApi* | [**teams_partial_update**](docs/TeamsApi.md#teams_partial_update) | **PATCH** /teams/{id} | 
*TeamsApi* | [**teams_retrieve**](docs/TeamsApi.md#teams_retrieve) | **GET** /teams/{id} | 
*TimeOffApi* | [**time_off_create**](docs/TimeOffApi.md#time_off_create) | **POST** /time-off | 
*TimeOffApi* | [**time_off_destroy**](docs/TimeOffApi.md#time_off_destroy) | **DELETE** /time-off/{id} | 
*TimeOffApi* | [**time_off_list**](docs/TimeOffApi.md#time_off_list) | **GET** /time-off | 
*TimeOffApi* | [**time_off_partial_update**](docs/TimeOffApi.md#time_off_partial_update) | **PATCH** /time-off/{id} | 
*TimeOffApi* | [**time_off_retrieve**](docs/TimeOffApi.md#time_off_retrieve) | **GET** /time-off/{id} | 


## Documentation For Models

 - [AccountToken](docs/AccountToken.md)
 - [AsyncTaskExecution](docs/AsyncTaskExecution.md)
 - [AsyncTaskExecutionStatusEnum](docs/AsyncTaskExecutionStatusEnum.md)
 - [Benefit](docs/Benefit.md)
 - [BenefitPlanTypeEnum](docs/BenefitPlanTypeEnum.md)
 - [Company](docs/Company.md)
 - [CountryEnum](docs/CountryEnum.md)
 - [Deduction](docs/Deduction.md)
 - [Document](docs/Document.md)
 - [Earning](docs/Earning.md)
 - [Employee](docs/Employee.md)
 - [EmployeePayrollRun](docs/EmployeePayrollRun.md)
 - [Employment](docs/Employment.md)
 - [EmploymentStatusEnum](docs/EmploymentStatusEnum.md)
 - [EmploymentTypeEnum](docs/EmploymentTypeEnum.md)
 - [EndUserDetails](docs/EndUserDetails.md)
 - [EthnicityEnum](docs/EthnicityEnum.md)
 - [FlsaStatusEnum](docs/FlsaStatusEnum.md)
 - [GenderEnum](docs/GenderEnum.md)
 - [LinkToken](docs/LinkToken.md)
 - [Location](docs/Location.md)
 - [MaritalStatusEnum](docs/MaritalStatusEnum.md)
 - [PaginatedAsyncTaskExecutionList](docs/PaginatedAsyncTaskExecutionList.md)
 - [PaginatedBenefitList](docs/PaginatedBenefitList.md)
 - [PaginatedCompanyList](docs/PaginatedCompanyList.md)
 - [PaginatedDeductionList](docs/PaginatedDeductionList.md)
 - [PaginatedDocumentList](docs/PaginatedDocumentList.md)
 - [PaginatedEarningList](docs/PaginatedEarningList.md)
 - [PaginatedEmployeeList](docs/PaginatedEmployeeList.md)
 - [PaginatedEmployeePayrollRunList](docs/PaginatedEmployeePayrollRunList.md)
 - [PaginatedEmploymentList](docs/PaginatedEmploymentList.md)
 - [PaginatedLocationList](docs/PaginatedLocationList.md)
 - [PaginatedPayrollRunList](docs/PaginatedPayrollRunList.md)
 - [PaginatedReportList](docs/PaginatedReportList.md)
 - [PaginatedTaxList](docs/PaginatedTaxList.md)
 - [PaginatedTeamList](docs/PaginatedTeamList.md)
 - [PaginatedTimeOffList](docs/PaginatedTimeOffList.md)
 - [PatchedBenefit](docs/PatchedBenefit.md)
 - [PatchedCompany](docs/PatchedCompany.md)
 - [PatchedDeduction](docs/PatchedDeduction.md)
 - [PatchedDocument](docs/PatchedDocument.md)
 - [PatchedEarning](docs/PatchedEarning.md)
 - [PatchedEmployee](docs/PatchedEmployee.md)
 - [PatchedEmployeePayrollRun](docs/PatchedEmployeePayrollRun.md)
 - [PatchedEmployment](docs/PatchedEmployment.md)
 - [PatchedLocation](docs/PatchedLocation.md)
 - [PatchedPayrollRun](docs/PatchedPayrollRun.md)
 - [PatchedReport](docs/PatchedReport.md)
 - [PatchedTax](docs/PatchedTax.md)
 - [PatchedTeam](docs/PatchedTeam.md)
 - [PatchedTimeOff](docs/PatchedTimeOff.md)
 - [PayCurrencyEnum](docs/PayCurrencyEnum.md)
 - [PayFrequencyEnum](docs/PayFrequencyEnum.md)
 - [PayPeriodEnum](docs/PayPeriodEnum.md)
 - [PayrollRun](docs/PayrollRun.md)
 - [Report](docs/Report.md)
 - [RequestTypeEnum](docs/RequestTypeEnum.md)
 - [RunStateEnum](docs/RunStateEnum.md)
 - [RunTypeEnum](docs/RunTypeEnum.md)
 - [StateEnum](docs/StateEnum.md)
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


