# Deduction

# The Deduction Object ### Description The `Deduction` object is used to represent an array of the wages withheld from total earnings for the purpose of paying taxes.  ### Usage Example Fetch from the `LIST Deductions` endpoint and filter by `ID` to show all deductions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**employee_payroll_run** | **str, none_type** |  | [optional] 
**name** | **str, none_type** | The deduction&#39;s name. | [optional] 
**employee_deduction** | **float, none_type** | The amount of money that is withheld from an employee&#39;s gross pay by the employee. | [optional] 
**company_deduction** | **float, none_type** | The amount of money that is withheld on behalf of an employee by the company. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


