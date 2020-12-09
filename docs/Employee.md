# Employee

# The Employee Object ### Description The `Employee` object is used to represent an Employee for a company. ### Usage Example Fetch from the `LIST Employee` endpoint and filter by `ID` to show all employees.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**remote_id** | **str** | The third-party API ID of the matching object. | [optional] 
**company** | **str** | The ID of the Employee&#39;s company. | [optional] 
**first_name** | **str** | The employee&#39;s first name. | [optional] 
**last_name** | **str** | The employee&#39;s last name. | [optional] 
**display_full_name** | **str** | The employee&#39;s full name, to use for display purposes. | [optional] 
**work_email** | **str** | The employee&#39;s work email. | [optional] 
**personal_email** | **str** | The employee&#39;s personal email. | [optional] 
**mobile_phone_number** | **str** | The employee&#39;s mobile phone number. | [optional] 
**employments** | **list[str]** |  | [readonly] 
**home_location** | **str** | The employee&#39;s home address. | [optional] 
**work_location** | **str** | The employee&#39;s work address. | [optional] 
**manager** | **str** | The employeee ID of the employee&#39;s manager. | [optional] 
**team** | **str** | The employee&#39;s team. | [optional] 
**ssn** | **str** | The employee&#39;s social security number. | [optional] 
**gender** | [**OneOfGenderEnumBlankEnumNullEnum**](OneOfGenderEnumBlankEnumNullEnum.md) | The employee&#39;s gender. | [optional] 
**ethnicity** | [**OneOfEthnicityEnumBlankEnumNullEnum**](OneOfEthnicityEnumBlankEnumNullEnum.md) | The employee&#39;s ethnicity. | [optional] 
**marital_status** | [**OneOfMaritalStatusEnumBlankEnumNullEnum**](OneOfMaritalStatusEnumBlankEnumNullEnum.md) | The employee&#39;s marital status. | [optional] 
**date_of_birth** | **datetime** | The employee&#39;s date of birth. | [optional] 
**hire_dates** | [**list[HireDate]**](HireDate.md) |  | [readonly] 
**employment_status** | [**OneOfEmploymentStatusEnumBlankEnumNullEnum**](OneOfEmploymentStatusEnumBlankEnumNullEnum.md) | The employment status of the employee. | [optional] 
**termination_dates** | [**list[TerminationDate]**](TerminationDate.md) |  | [readonly] 
**avatar** | **str** | The URL of the employee&#39;s avatar image. | [optional] 
**about** | **str** | A description of the employee. | [optional] 
**documents** | **list[str]** |  | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


