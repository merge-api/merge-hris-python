# Offer

# The Offer Object ### Description The `Offer` object is used to represent an offer for an application.  ### Usage Example Fetch from the `LIST Offers` endpoint and filter by `ID` to show all offers.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**application** | **str, none_type** | The application being for the offer. | [optional] 
**creator** | **str, none_type** | The user who created the offer. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s scorecard was created. | [optional] 
**closed_at** | **datetime, none_type** | When the offer was closed. | [optional] 
**sent_at** | **datetime, none_type** | When the offer was sent. | [optional] 
**start_date** | **datetime, none_type** | The offered start date. | [optional] 
**status** | **str, none_type** | The offer&#39;s status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


