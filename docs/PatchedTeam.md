# PatchedTeam

# The Team Object ### Description The `Team` object is used to represent a Team within a company. `Employee` objects are often grouped this way. Note that in the Merge HRIS API, company subdivisions are all represented with `Teams`, rather than `Teams` and `Departments`.  ### Usage Example If you're building a way to filter by `Team`, you'd hit the `GET Teams` endpoint to fetch the `Teams`, and then use the `ID` of the team your user selects to filter the `GET Employees` endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**origin_id** | **str** | The third-party API ID of the matching object. | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**modified_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | The team&#39;s name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


