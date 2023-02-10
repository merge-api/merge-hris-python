# AccountDetailsAndActions

# The LinkedAccount Object ### Description The `LinkedAccount` object is used to represent an end user's link with a specific integration.  ### Usage Example View a list of your organization's `LinkedAccount` objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **object** |  | 
**end_user_organization_name** | **str** |  | 
**end_user_email_address** | **str** |  | 
**webhook_listener_url** | **str** |  | 
**category** | **object** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**end_user_origin_id** | **str** |  | [optional] 
**is_duplicate** | **bool, none_type** | Whether a Production Linked Account&#39;s credentials match another existing Production Linked Account. This field is &#x60;null&#x60; for Test Linked Accounts, incomplete Production Linked Accounts, and ignored duplicate Production Linked Account sets. | [optional] 
**integration** | [**AccountDetailsAndActionsIntegration**](AccountDetailsAndActionsIntegration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


