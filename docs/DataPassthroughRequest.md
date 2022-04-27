# DataPassthroughRequest

# The DataPassthrough Object ### Description The `DataPassthrough` object is used to send information to an otherwise-unsupported third-party endpoint.  ### Usage Example Create a `DataPassthrough` to get team hierarchies from your Rippling integration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **object** |  | 
**path** | **str** |  | 
**base_url_override** | **str, none_type** |  | [optional] 
**data** | **str, none_type** |  | [optional] 
**multipart_form_data** | [**[MultipartFormFieldRequest], none_type**](MultipartFormFieldRequest.md) | Pass an array of &#x60;MultipartFormField&#x60; objects in here instead of using the &#x60;data&#x60; param if &#x60;request_format&#x60; is set to &#x60;MULTIPART&#x60;. | [optional] 
**headers** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | The headers to use for the request (Merge will handle the account&#39;s authorization headers). &#x60;Content-Type&#x60; header is required for passthrough. Choose content type corresponding to expected format of receiving server. | [optional] 
**request_format** | **object, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


