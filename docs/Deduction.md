# Deduction

# The Deduction Object ### Description The `Deduction` object is used to represent a deduction for a given employee's payroll run. One run could include several deductions.  ### Usage Example Fetch from the `LIST Deductions` endpoint and filter by `ID` to show all deductions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**employee_payroll_run** | **str, none_type** | The deduction&#39;s employee payroll run. | [optional] 
**name** | **str, none_type** | The deduction&#39;s name. | [optional] 
**employee_deduction** | **float, none_type** | The amount the employee is deducting. | [optional] 
**company_deduction** | **float, none_type** | The amount the company is deducting. | [optional] 
**remote_data** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type], none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


