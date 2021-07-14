# EmployeeRequest

# The Employee Object ### Description The `Employee` object is used to represent an Employee for a company.  ### Usage Example Fetch from the `LIST Employee` endpoint and filter by `ID` to show all employees.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee_number** | **str, none_type** | The employee&#39;s number that appears in the remote UI. Note: This is distinct from the remote_id field, which is a unique identifier for the employee set by the remote API, and is not exposed to the user. | [optional] 
**company** | **str, none_type** | The ID of the employee&#39;s company. | [optional] 
**first_name** | **str, none_type** | The employee&#39;s first name. | [optional] 
**last_name** | **str, none_type** | The employee&#39;s last name. | [optional] 
**display_full_name** | **str, none_type** | The employee&#39;s full name, to use for display purposes. | [optional] 
**work_email** | **str, none_type** | The employee&#39;s work email. | [optional] 
**personal_email** | **str, none_type** | The employee&#39;s personal email. | [optional] 
**mobile_phone_number** | **str, none_type** | The employee&#39;s mobile phone number. | [optional] 
**home_location** | **str, none_type** | The employee&#39;s home address. | [optional] 
**work_location** | **str, none_type** | The employee&#39;s work address. | [optional] 
**manager** | **str, none_type** | The employee ID of the employee&#39;s manager. | [optional] 
**team** | **str, none_type** | The employee&#39;s team. | [optional] 
**ssn** | **str, none_type** | The employee&#39;s social security number. | [optional] 
**gender** | **object, none_type** | The employee&#39;s gender. | [optional] 
**ethnicity** | **object, none_type** | The employee&#39;s ethnicity. | [optional] 
**marital_status** | **object, none_type** | The employee&#39;s marital status. | [optional] 
**date_of_birth** | **datetime, none_type** | The employee&#39;s date of birth. | [optional] 
**hire_date** | **datetime, none_type** | The employee&#39;s hire date. If an employee has multiple hire dates from previous employments, this represents the most recent hire date. | [optional] 
**start_date** | **datetime, none_type** | The employee&#39;s start date. | [optional] 
**employment_status** | **object, none_type** | The employment status of the employee. | [optional] 
**termination_date** | **datetime, none_type** | The employee&#39;s termination date. | [optional] 
**avatar** | **str, none_type** | The URL of the employee&#39;s avatar image. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


