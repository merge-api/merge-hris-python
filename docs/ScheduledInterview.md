# ScheduledInterview

# The ScheduledInterview Object ### Description The `ScheduledInterview` object is used to represent an interview  ### Usage Example Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers` to show all office locations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**application** | **str, none_type** | The application being interviewed. | [optional] 
**job_interview_stage** | **str, none_type** | The stage of the interview. | [optional] 
**organizer** | **str, none_type** | The user organizing the interview. | [optional] 
**interviewers** | **[str]** |  | [optional] 
**location** | **str, none_type** | The interview&#39;s location. | [optional] 
**start_at** | **datetime, none_type** | When the interview was started. | [optional] 
**end_at** | **datetime, none_type** | When the interview was ended. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s interview was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s interview was updated. | [optional] 
**status** | **str, none_type** | The interview&#39;s status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


