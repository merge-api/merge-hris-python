# PatchedEEOC

# The EEOC Object ### Description The `EEOC` object is used to represent the Equal Employment Opportunity Commission information for a candidate.  ### Usage Example Fetch from the `LIST EEOCs` endpoint and filter by `candidate` to show all EEOC information for a candidate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**candidate** | **str, none_type** | The candidate being represented. | [optional] 
**submitted_at** | **datetime, none_type** | When the information was submitted. | [optional] 
**race** | **str, none_type** | The candidate&#39;s race. | [optional] 
**gender** | **str, none_type** | The candidate&#39;s gender. | [optional] 
**veteran_status** | **str, none_type** | The candidate&#39;s veteran status. | [optional] 
**disability_status** | **str, none_type** | The candidate&#39;s disability status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


