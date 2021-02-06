# Employment

# The Employment Object ### Description The `Employment` object is used to represent an employment position at a company. These are associated with the employee filling the role.  ### Usage Example Fetch from the `LIST Employments` endpoint and filter by `ID` to show all employees.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**job_title** | **str, none_type** | The position&#39;s title. | [optional] 
**pay_rate** | **float, none_type** | The position&#39;s pay rate in dollars. | [optional] 
**pay_period** | **str, none_type** | The time period this pay rate encompasses. | [optional] 
**pay_frequency** | **str, none_type** | The position&#39;s pay frequency. | [optional] 
**pay_currency** | **str, none_type** | The position&#39;s currency code. | [optional] 
**flsa_status** | **str, none_type** | The position&#39;s FLSA status. | [optional] 
**effective_date** | **datetime, none_type** | The position&#39;s effective date. | [optional] 
**employment_type** | **str, none_type** | The position&#39;s type of employment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


