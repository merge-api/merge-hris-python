# Location

# The Location Object ### Description The `Location` object is used to represent a Location for a company. This is shared across many models and is referenced whenever a location is stored.  ### Usage Example Fetch from the `LIST Locations` endpoint and filter by `ID` to show all office locations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**phone_number** | **str, none_type** | The location&#39;s phone number. | [optional] 
**street_1** | **str, none_type** | Line 1 of the location&#39;s street address. | [optional] 
**street_2** | **str, none_type** | Line 2 of the location&#39;s street address. | [optional] 
**city** | **str, none_type** | The location&#39;s city. | [optional] 
**state** | **object, none_type** | The location&#39;s state. | [optional] 
**zip_code** | **str, none_type** | The location&#39;s zip code. | [optional] 
**country** | **object, none_type** | The location&#39;s country. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


