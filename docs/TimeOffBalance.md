# TimeOffBalance

# The TimeOffBalance Object ### Description The `TimeOffBalance` object is used to represent a Time Off Balance for an employee.  ### Usage Example Fetch from the `LIST TimeOffBalances` endpoint and filter by `ID` to show all time off balances.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee** | **str, none_type** |  | [optional] 
**balance** | **float, none_type** | The current remaining PTO balance in terms of hours. This does not represent the starting PTO balance. If the API provider only provides PTO balance in terms of days, we estimate 8 hours per day. | [optional] 
**used** | **float, none_type** | The amount of PTO used in terms of hours. | [optional] 
**policy_type** | **object, none_type** | The policy type of this time off balance. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


