# Employee

# The Employee Object ### Description The `Employee` object is used to represent an Employee for a company.  ### Usage Example Fetch from the `LIST Employee` endpoint and filter by `ID` to show all employees.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee_number** | **str, none_type** | The employee&#39;s number that appears in the remote UI. Note: This is distinct from the remote_id field, which is a unique identifier for the employee set by the remote API, and is not exposed to the user. This value can also change in many API providers. | [optional] 
**company** | **str, none_type** |  | [optional] 
**first_name** | **str, none_type** | The employee&#39;s first name. | [optional] 
**last_name** | **str, none_type** | The employee&#39;s last name. | [optional] 
**display_full_name** | **str, none_type** | The employee&#39;s full name, to use for display purposes. If a preferred first name is available, the full name will include the preferred first name. | [optional] 
**groups** | **[str, none_type]** |  | [optional] 
**work_email** | **str, none_type** | The employee&#39;s work email. | [optional] 
**personal_email** | **str, none_type** | The employee&#39;s personal email. | [optional] 
**mobile_phone_number** | **str, none_type** | The employee&#39;s mobile phone number. | [optional] 
**employments** | **[str, none_type]** | Array of &#x60;Employment&#x60; IDs for this Employee. | [optional] 
**home_location** | **str, none_type** |  | [optional] 
**work_location** | **str, none_type** |  | [optional] 
**manager** | **str, none_type** |  | [optional] 
**team** | **str, none_type** |  | [optional] 
**pay_group** | **str, none_type** |  | [optional] 
**ssn** | **str, none_type** | The employee&#39;s social security number. | [optional] 
**gender** | **object, none_type** | The employee&#39;s gender. | [optional] 
**ethnicity** | **object, none_type** | The employee&#39;s ethnicity. | [optional] 
**marital_status** | **object, none_type** | The employee&#39;s marital status. | [optional] 
**date_of_birth** | **datetime, none_type** | The employee&#39;s date of birth. | [optional] 
**hire_date** | **datetime, none_type** | The date that the employee was hired, usually the day that an offer letter is signed. If an employee has multiple hire dates from previous employments, this represents the most recent hire date. Note: If you&#39;re looking for the employee&#39;s start date, refer to the start_date field. | [optional] 
**start_date** | **datetime, none_type** | The date that the employee started working. If an employee has multiple start dates from previous employments, this represents the most recent start date. | [optional] 
**employment_status** | **object, none_type** | The employment status of the employee. | [optional] 
**termination_date** | **datetime, none_type** | The employee&#39;s termination date. | [optional] 
**avatar** | **str, none_type** | The URL of the employee&#39;s avatar image. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**custom_fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Custom fields configured for a given model. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


