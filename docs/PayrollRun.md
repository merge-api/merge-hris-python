# PayrollRun

# The PayrollRun Object ### Description The `PayrollRun` object is used to represent a payroll run.  ### Usage Example Fetch from the `LIST PayrollRuns` endpoint and filter by `ID` to show all payroll runs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**run_state** | **str, none_type** | The state of the payroll run | [optional] 
**run_type** | **str, none_type** | The type of the payroll run | [optional] 
**start_date** | **datetime, none_type** | The day and time the payroll run started. | [optional] 
**end_date** | **datetime, none_type** | The day and time the payroll run ended. | [optional] 
**check_date** | **datetime, none_type** | The day and time the payroll run was checked. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


