# Group

# The Group Object ### Description The `Group` object is used to represent any subset of employees, such as `PayGroup` or `Team`. Employees can be in multiple Groups.  ### Usage Example Fetch from the `LIST Employee` endpoint and expand groups to view an employee's groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**parent_group** | **str, none_type** | The parent group for this group. | [optional] 
**name** | **str, none_type** | The group name. | [optional] 
**type** | **object, none_type** | The group type | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


