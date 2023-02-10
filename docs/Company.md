# Company

# The Company Object ### Description The `Company` object is used to represent a company within the HRIS / Payroll system.  ### Usage Example Fetch from the `LIST Companies` endpoint and filter by `ID` to show all companies.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**legal_name** | **str, none_type** | The company&#39;s legal name. | [optional] 
**display_name** | **str, none_type** | The company&#39;s display name. | [optional] 
**eins** | **[str, none_type], none_type** | The company&#39;s Employer Identification Numbers. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


