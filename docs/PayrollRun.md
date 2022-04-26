# PayrollRun

# The PayrollRun Object ### Description The `PayrollRun` object is used to represent a payroll run. This payroll run is not specific to an employee.  ### Usage Example Fetch from the `LIST PayrollRuns` endpoint and filter by `ID` to show all payroll runs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**run_state** | **object, none_type** | The state of the payroll run | [optional] 
**run_type** | **object, none_type** | The type of the payroll run | [optional] 
**start_date** | **datetime, none_type** | The day and time the payroll run started. | [optional] 
**end_date** | **datetime, none_type** | The day and time the payroll run ended. | [optional] 
**check_date** | **datetime, none_type** | The day and time the payroll run was checked. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


