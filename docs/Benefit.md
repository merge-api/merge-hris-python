# Benefit

# The Benefit Object ### Description The `Benefit` object is used to represent a Benefit for an employee.  ### Usage Example Fetch from the `LIST Benefits` endpoint and filter by `ID` to show all benefits.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**employee** | **str** | The employee on the plan. | [optional] 
**provider_name** | **str** | The name of the benefit provider. | [optional] 
**benefit_plan_type** | [**BenefitPlanTypeEnum**](BenefitPlanTypeEnum.md) | The type of benefit plan | [optional] 
**employee_contribution** | **float** | The employee&#39;s contribution. | [optional] 
**company_contribution** | **float** | The company&#39;s contribution. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


