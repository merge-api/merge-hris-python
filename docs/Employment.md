# Employment

# The Employment Object ### Description The `Employment` object is used to represent an employment position at a company. These are associated with the employee filling the role.  ### Usage Example Fetch from the `LIST Employments` endpoint and filter by `ID` to show all employees.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**job_title** | **str** | The position&#39;s title. | [optional] 
**pay_rate** | **float** | The position&#39;s pay rate in dollars. | [optional] 
**pay_period** | [**PayPeriodEnum**](PayPeriodEnum.md) | The time period this pay rate encompasses. | [optional] 
**pay_frequency** | [**PayFrequencyEnum**](PayFrequencyEnum.md) | The position&#39;s pay frequency. | [optional] 
**pay_currency** | [**PayCurrencyEnum**](PayCurrencyEnum.md) | The position&#39;s currency code. | [optional] 
**flsa_status** | [**FlsaStatusEnum**](FlsaStatusEnum.md) | The position&#39;s FLSA status. | [optional] 
**effective_date** | **datetime** | The position&#39;s effective date. | [optional] 
**employment_type** | [**EmploymentTypeEnum**](EmploymentTypeEnum.md) | The position&#39;s type of employment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


