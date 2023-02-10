# Employment

# The Employment Object ### Description The `Employment` object is used to represent a job position at a company.  Please note: When there is a change in pay or title, integrations with historical data will create new Employment objects while integrations without historical data will update existing ones.  ### Usage Example Fetch from the `LIST Employments` endpoint and filter by `ID` to show all employees.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee** | **str, none_type** | The employee holding this position. | [optional] 
**job_title** | **str, none_type** | The position&#39;s title. | [optional] 
**pay_rate** | **float, none_type** | The position&#39;s pay rate in dollars. | [optional] 
**pay_period** | **object, none_type** | The time period this pay rate encompasses. | [optional] 
**pay_frequency** | **object, none_type** | The position&#39;s pay frequency. | [optional] 
**pay_currency** | **object, none_type** | The position&#39;s currency code. | [optional] 
**pay_group** | **str, none_type** | The employment&#39;s pay group | [optional] 
**flsa_status** | **object, none_type** | The position&#39;s FLSA status. | [optional] 
**effective_date** | **datetime, none_type** | The position&#39;s effective date. | [optional] 
**employment_type** | **object, none_type** | The position&#39;s type of employment. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


