# TimeOffRequest

# The TimeOff Object ### Description The `TimeOff` object is used to represent a Time Off Request filed by an employee.  ### Usage Example Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee** | **str, none_type** |  | [optional] 
**approver** | **str, none_type** |  | [optional] 
**status** | **object, none_type** | The status of this time off request. | [optional] 
**employee_note** | **str, none_type** | The employee note for this time off request. | [optional] 
**units** | **object, none_type** | The unit of time requested. | [optional] 
**amount** | **float, none_type** | The number of time off units requested. | [optional] 
**request_type** | **object, none_type** | The type of time off request. | [optional] 
**start_time** | **datetime, none_type** | The day and time of the start of the time requested off. | [optional] 
**end_time** | **datetime, none_type** | The day and time of the end of the time requested off. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


