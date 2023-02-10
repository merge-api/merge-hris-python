# EmployeePayrollRun

# The EmployeePayrollRun Object ### Description The `EmployeePayrollRun` object is used to represent an employee's pay statement for a specific payroll run.  ### Usage Example Fetch from the `LIST EmployeePayrollRun` endpoint and filter by `ID` to show all employee payroll runs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee** | **str, none_type** | The employee whose payroll is being run. | [optional] 
**payroll_run** | **str, none_type** | The payroll being run. | [optional] 
**gross_pay** | **float, none_type** | The total earnings throughout a given period for an employee before any deductions are made. | [optional] 
**net_pay** | **float, none_type** | The take-home pay throughout a given period for an employee after deductions are made. | [optional] 
**start_date** | **datetime, none_type** | The day and time the payroll run started. | [optional] 
**end_date** | **datetime, none_type** | The day and time the payroll run ended. | [optional] 
**check_date** | **datetime, none_type** | The day and time the payroll run was checked. | [optional] 
**earnings** | [**[Earning]**](Earning.md) |  | [optional] [readonly] 
**deductions** | [**[Deduction]**](Deduction.md) |  | [optional] [readonly] 
**taxes** | [**[Tax]**](Tax.md) |  | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


