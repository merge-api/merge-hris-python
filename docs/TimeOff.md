# TimeOff

# The TimeOff Object ### Description The `TimeOff` object is used to represent a Time Off Request filed by an employee.  ### Usage Example Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off requests.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**employee** | **str** | The employee requesting time off. | [optional] 
**approver** | **str** | The employee approving the time off request. | [optional] 
**status** | [**OneOfTimeOffStatusEnumBlankEnumNullEnum**](OneOfTimeOffStatusEnumBlankEnumNullEnum.md) | The status of this time off request. | [optional] 
**employee_note** | **str** | The status of this time off request. | [optional] 
**units** | [**OneOfUnitsEnumBlankEnumNullEnum**](OneOfUnitsEnumBlankEnumNullEnum.md) | The unit of time requested. | [optional] 
**amount** | **float** | The number of time off units requested. | [optional] 
**request_type** | [**OneOfRequestTypeEnumBlankEnumNullEnum**](OneOfRequestTypeEnumBlankEnumNullEnum.md) | The type of time off request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


