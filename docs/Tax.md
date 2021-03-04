# Tax

# The Tax Object ### Description The `Tax` object is used to represent a tax for a given employee's payroll run. One run could include several taxes.  ### Usage Example Fetch from the `LIST Taxes` endpoint and filter by `ID` to show all taxes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**employee_payroll_run** | **str, none_type** | The tax&#39;s employee payroll run. | [optional] 
**name** | **str, none_type** | The tax&#39;s name. | [optional] 
**amount** | **float, none_type** | The tax amount. | [optional] 
**employer_tax** | **bool, none_type** | Whether or not the employer is responsible for paying the tax. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


