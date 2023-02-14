# ConditionSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the condition schema. This ID is used when updating selective syncs for a linked account. | 
**native_name** | **str, none_type** | User-facing *native condition* name. e.g. \&quot;Skip Manager\&quot;. | 
**field_name** | **str, none_type** | The name of the field on the common model that this condition corresponds to, if they conceptually match. e.g. \&quot;location_type\&quot;. | 
**condition_type** | [**ConditionTypeEnum**](ConditionTypeEnum.md) |  | 
**operators** | [**[OperatorSchema]**](OperatorSchema.md) | The schemas for the operators that can be used on a condition. | 
**common_model** | **str** | The common model for which a condition schema is defined. | [optional] [readonly] 
**is_unique** | **bool** | Whether this condition can only be applied once. If false, the condition can be AND&#39;d together multiple times. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


