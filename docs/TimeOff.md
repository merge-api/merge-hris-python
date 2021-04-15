# TimeOff

# The TimeOff Object ### Description The `TimeOff` object is used to represent a Time Off Request filed by an employee.  ### Usage Example Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off requests.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee** | **str, none_type** | The employee requesting time off. | [optional] 
**approver** | **str, none_type** | The employee approving the time off request. | [optional] 
**status** | **object, none_type** | The status of this time off request. | [optional] 
**employee_note** | **str, none_type** | The employee note for this time off request. | [optional] 
**units** | **object, none_type** | The unit of time requested. | [optional] 
**amount** | **float, none_type** | The number of time off units requested. | [optional] 
**request_type** | **object, none_type** | The type of time off request. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


