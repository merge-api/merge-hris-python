# Application

# The Application Object ### Description The `Application` object is used to represent an Application for a job position.  ### Usage Example Fetch from the `LIST Applications` endpoint and filter by `ID` to show all applications.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**candidate** | **str, none_type** | The candidate applying. | [optional] 
**job** | **str, none_type** | The job being applied for. | [optional] 
**is_prospect** | **bool, none_type** | Whether or not the application is a prospect. | [optional] 
**applied_at** | **datetime, none_type** | When the application was submitted. | [optional] 
**rejected_at** | **datetime, none_type** | When the application was rejected. | [optional] 
**source** | **str, none_type** | The application&#39;s source. | [optional] 
**credited_to** | **str, none_type** | The user credited for this application. | [optional] 
**current_stage** | **str, none_type** | The application&#39;s current stage. | [optional] 
**reject_reason** | **str, none_type** | The application&#39;s reason for rejection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


