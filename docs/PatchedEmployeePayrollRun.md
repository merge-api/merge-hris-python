# PatchedEmployeePayrollRun

# The EmployeePayrollRun Object ### Description The `EmployeePayrollRun` object is used to represent a payroll run for a specific employee.  ### Usage Example Fetch from the `LIST EmployeePayrollRun` endpoint and filter by `ID` to show all employee payroll runs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**origin_id** | **str** | The third-party API ID of the matching object. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**modified_at** | **datetime** |  | [optional] [readonly] 
**employee** | **str** | The employee who&#39;s payroll is being run. | [optional] 
**payroll_run** | **str** | The payroll being run. | [optional] 
**gross_pay** | **float** | The gross pay from the run | [optional] 
**net_pay** | **float** | The net pay from the run | [optional] 
**start_date** | **datetime** | The day and time the payroll run started. | [optional] 
**end_date** | **datetime** | The day and time the payroll run ended. | [optional] 
**check_date** | **datetime** | The day and time the payroll run was checked. | [optional] 
**earnings** | [**list[Earning]**](Earning.md) |  | [optional] [readonly] 
**deductions** | [**list[Deduction]**](Deduction.md) |  | [optional] [readonly] 
**taxes** | [**list[Tax]**](Tax.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


