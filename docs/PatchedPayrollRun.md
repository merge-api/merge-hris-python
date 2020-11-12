# PatchedPayrollRun

# The PayrollRun Object ### Description The `PayrollRun` object is used to represent a payroll run.  ### Usage Example Fetch from the `LIST PayrollRuns` endpoint and filter by `ID` to show all payroll runs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**origin_id** | **str** | The third-party API ID of the matching object. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**modified_at** | **datetime** |  | [optional] [readonly] 
**run_state** | [**OneOfRunStateEnumBlankEnumNullEnum**](OneOfRunStateEnumBlankEnumNullEnum.md) | The state of the payroll run | [optional] 
**run_type** | [**OneOfRunTypeEnumBlankEnumNullEnum**](OneOfRunTypeEnumBlankEnumNullEnum.md) | The type of the payroll run | [optional] 
**start_date** | **datetime** | The day and time the payroll run started. | [optional] 
**end_date** | **datetime** | he day and time the payroll run ended. | [optional] 
**check_date** | **datetime** | he day and time the payroll run was checked. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


