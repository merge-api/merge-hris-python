# Group

# The Group Object ### Description The `Group` object is used to represent Group information that employees belong to. This is often referenced with an Employee object.  Please note: The teams object will fulfill most use cases. The Groups object is for power-users that want all types of groups at a company and the optionality of pulling multiple groups for an employee.  ### Usage Example Fetch from the `LIST Employee` endpoint and expand groups to view an employee's groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**parent_group** | **str, none_type** | The parent group for this group. | [optional] 
**name** | **str, none_type** | The group name. | [optional] 
**type** | **object, none_type** | The group type | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


