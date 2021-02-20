# Benefit

# The Benefit Object ### Description The `Benefit` object is used to represent a Benefit for an employee.  ### Usage Example Fetch from the `LIST Benefits` endpoint and filter by `ID` to show all benefits.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee** | **str, none_type** | The employee on the plan. | [optional] 
**provider_name** | **str, none_type** | The name of the benefit provider. | [optional] 
**benefit_plan_type** | **str, none_type** | The type of benefit plan | [optional] 
**employee_contribution** | **float, none_type** | The employee&#39;s contribution. | [optional] 
**company_contribution** | **float, none_type** | The company&#39;s contribution. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


