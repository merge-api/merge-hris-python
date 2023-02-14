# Earning

# The Earning Object ### Description The `Earning` object is used to represent an array of different compensations that an employee receives within specific wage categories.  ### Usage Example Fetch from the `LIST Earnings` endpoint and filter by `ID` to show all earnings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**employee_payroll_run** | **str, none_type** |  | [optional] 
**amount** | **float, none_type** | The amount earned. | [optional] 
**type** | **object, none_type** | The type of earning. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


