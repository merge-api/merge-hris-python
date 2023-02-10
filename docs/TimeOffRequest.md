# TimeOffRequest

# The TimeOff Object ### Description The `TimeOff` object is used to represent all employees' Time Off entries.  ### Usage Example Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee** | **str, none_type** | The employee requesting time off. | [optional] 
**approver** | **str, none_type** | The Merge ID of the employee with the ability to approve the time off request. | [optional] 
**status** | **object, none_type** | The status of this time off request. | [optional] 
**employee_note** | **str, none_type** | The employee note for this time off request. | [optional] 
**units** | **object, none_type** | The measurement that the third-party integration uses to count time requested. | [optional] 
**amount** | **float, none_type** | The time off quantity measured by the prescribed “units”. | [optional] 
**request_type** | **object, none_type** | The type of time off request. | [optional] 
**start_time** | **datetime, none_type** | The day and time of the start of the time requested off. | [optional] 
**end_time** | **datetime, none_type** | The day and time of the end of the time requested off. | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


