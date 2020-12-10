# Location

# The Location Object ### Description The `Location` object is used to represent a Location for a company. This is shared across many models and is referenced whenever a location is stored.  ### Usage Example Fetch from the `LIST Locations` endpoint and filter by `ID` to show all office locations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**phone_number** | **str** | The location&#39;s phone number. | [optional] 
**street_1** | **str** | Line 1 of the location&#39;s street address. | [optional] 
**street_2** | **str** | Line 2 of the location&#39;s street address. | [optional] 
**city** | **str** | The location&#39;s city. | [optional] 
**state** | [**OneOfStateEnumBlankEnumNullEnum**](OneOfStateEnumBlankEnumNullEnum.md) | The location&#39;s state. | [optional] 
**zip_code** | **str** | The location&#39;s zip code. | [optional] 
**country** | [**OneOfCountryEnumBlankEnumNullEnum**](OneOfCountryEnumBlankEnumNullEnum.md) | The location&#39;s country. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


