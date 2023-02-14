# Location

# The Location Object ### Description The `Location` object is used to represent an address that can be associated with an employee.  ### Usage Example Fetch from the `LIST Locations` endpoint and filter by `ID` to show all office locations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The location&#39;s name. | [optional] 
**phone_number** | **str, none_type** | The location&#39;s phone number. | [optional] 
**street_1** | **str, none_type** | Line 1 of the location&#39;s street address. | [optional] 
**street_2** | **str, none_type** | Line 2 of the location&#39;s street address. | [optional] 
**city** | **str, none_type** | The location&#39;s city. | [optional] 
**state** | **str, none_type** | The location&#39;s state. Represents a region if outside of the US. | [optional] 
**zip_code** | **str, none_type** | The location&#39;s zip code or postal code. | [optional] 
**country** | **object, none_type** | The location&#39;s country. | [optional] 
**location_type** | **object, none_type** | The location&#39;s type. Can be either WORK or HOME | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


