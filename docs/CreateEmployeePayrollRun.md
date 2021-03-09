# CreateEmployeePayrollRun

# The EmployeePayrollRun Object ### Description The `EmployeePayrollRun` object is used to represent a payroll run for a specific employee.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee** | **str, none_type** | The employee who&#39;s payroll is being run. | [optional] 
**payroll_run** | **str, none_type** | The payroll being run. | [optional] 
**gross_pay** | **float, none_type** | The gross pay from the run. | [optional] 
**net_pay** | **float, none_type** | The net pay from the run. | [optional] 
**start_date** | **datetime, none_type** | The day and time the payroll run started. | [optional] 
**end_date** | **datetime, none_type** | The day and time the payroll run ended. | [optional] 
**check_date** | **datetime, none_type** | The day and time the payroll run was checked. | [optional] 
**earnings** | [**[Earning]**](Earning.md) |  | [optional] [readonly] 
**deductions** | [**[Deduction]**](Deduction.md) |  | [optional] [readonly] 
**taxes** | [**[Tax]**](Tax.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


