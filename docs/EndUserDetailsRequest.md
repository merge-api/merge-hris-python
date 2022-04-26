# EndUserDetailsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_user_email_address** | **str** |  | 
**end_user_organization_name** | **str** |  | 
**end_user_origin_id** | **str** |  | 
**categories** | [**[CategoriesEnum]**](CategoriesEnum.md) |  | 
**integration** | **str, none_type** | The slug of a specific pre-selected integration for this linking flow token, for examples of slugs see https://www.merge.dev/docs/basics/integration-metadata | [optional] 
**link_expiry_mins** | **int** | An integer number of minutes between [30, 720] for how long this token is valid. Defaults to 30 | [optional]  if omitted the server will use the default value of 30

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


