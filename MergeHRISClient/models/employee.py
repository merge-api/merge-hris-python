# coding: utf-8

"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from MergeHRISClient.configuration import Configuration


class Employee(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'remote_id': 'str',
        'company': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'display_full_name': 'str',
        'work_email': 'str',
        'personal_email': 'str',
        'mobile_phone_number': 'str',
        'employments': 'list[str]',
        'home_location': 'str',
        'work_location': 'str',
        'manager': 'str',
        'team': 'str',
        'ssn': 'str',
        'gender': 'OneOfGenderEnumBlankEnumNullEnum',
        'ethnicity': 'OneOfEthnicityEnumBlankEnumNullEnum',
        'marital_status': 'OneOfMaritalStatusEnumBlankEnumNullEnum',
        'date_of_birth': 'datetime',
        'hire_dates': 'list[HireDate]',
        'employment_status': 'OneOfEmploymentStatusEnumBlankEnumNullEnum',
        'termination_dates': 'list[TerminationDate]',
        'avatar': 'str',
        'about': 'str',
        'documents': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'remote_id': 'remote_id',
        'company': 'company',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'display_full_name': 'display_full_name',
        'work_email': 'work_email',
        'personal_email': 'personal_email',
        'mobile_phone_number': 'mobile_phone_number',
        'employments': 'employments',
        'home_location': 'home_location',
        'work_location': 'work_location',
        'manager': 'manager',
        'team': 'team',
        'ssn': 'ssn',
        'gender': 'gender',
        'ethnicity': 'ethnicity',
        'marital_status': 'marital_status',
        'date_of_birth': 'date_of_birth',
        'hire_dates': 'hire_dates',
        'employment_status': 'employment_status',
        'termination_dates': 'termination_dates',
        'avatar': 'avatar',
        'about': 'about',
        'documents': 'documents'
    }

    def __init__(self, id=None, remote_id=None, company=None, first_name=None, last_name=None, display_full_name=None, work_email=None, personal_email=None, mobile_phone_number=None, employments=None, home_location=None, work_location=None, manager=None, team=None, ssn=None, gender=None, ethnicity=None, marital_status=None, date_of_birth=None, hire_dates=None, employment_status=None, termination_dates=None, avatar=None, about=None, documents=None, local_vars_configuration=None):  # noqa: E501
        """Employee - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._remote_id = None
        self._company = None
        self._first_name = None
        self._last_name = None
        self._display_full_name = None
        self._work_email = None
        self._personal_email = None
        self._mobile_phone_number = None
        self._employments = None
        self._home_location = None
        self._work_location = None
        self._manager = None
        self._team = None
        self._ssn = None
        self._gender = None
        self._ethnicity = None
        self._marital_status = None
        self._date_of_birth = None
        self._hire_dates = None
        self._employment_status = None
        self._termination_dates = None
        self._avatar = None
        self._about = None
        self._documents = None
        self.discriminator = None

        self.id = id
        self.remote_id = remote_id
        self.company = company
        self.first_name = first_name
        self.last_name = last_name
        self.display_full_name = display_full_name
        self.work_email = work_email
        self.personal_email = personal_email
        self.mobile_phone_number = mobile_phone_number
        self.employments = employments
        self.home_location = home_location
        self.work_location = work_location
        self.manager = manager
        self.team = team
        self.ssn = ssn
        self.gender = gender
        self.ethnicity = ethnicity
        self.marital_status = marital_status
        self.date_of_birth = date_of_birth
        self.hire_dates = hire_dates
        self.employment_status = employment_status
        self.termination_dates = termination_dates
        self.avatar = avatar
        self.about = about
        self.documents = documents

    @property
    def id(self):
        """Gets the id of this Employee.  # noqa: E501


        :return: The id of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Employee.


        :param id: The id of this Employee.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def remote_id(self):
        """Gets the remote_id of this Employee.  # noqa: E501

        The third-party API ID of the matching object.  # noqa: E501

        :return: The remote_id of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this Employee.

        The third-party API ID of the matching object.  # noqa: E501

        :param remote_id: The remote_id of this Employee.  # noqa: E501
        :type: str
        """

        self._remote_id = remote_id

    @property
    def company(self):
        """Gets the company of this Employee.  # noqa: E501

        The ID of the Employee's company.  # noqa: E501

        :return: The company of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Employee.

        The ID of the Employee's company.  # noqa: E501

        :param company: The company of this Employee.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def first_name(self):
        """Gets the first_name of this Employee.  # noqa: E501

        The employee's first name.  # noqa: E501

        :return: The first_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Employee.

        The employee's first name.  # noqa: E501

        :param first_name: The first_name of this Employee.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Employee.  # noqa: E501

        The employee's last name.  # noqa: E501

        :return: The last_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Employee.

        The employee's last name.  # noqa: E501

        :param last_name: The last_name of this Employee.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def display_full_name(self):
        """Gets the display_full_name of this Employee.  # noqa: E501

        The employee's full name, to use for display purposes.  # noqa: E501

        :return: The display_full_name of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._display_full_name

    @display_full_name.setter
    def display_full_name(self, display_full_name):
        """Sets the display_full_name of this Employee.

        The employee's full name, to use for display purposes.  # noqa: E501

        :param display_full_name: The display_full_name of this Employee.  # noqa: E501
        :type: str
        """

        self._display_full_name = display_full_name

    @property
    def work_email(self):
        """Gets the work_email of this Employee.  # noqa: E501

        The employee's work email.  # noqa: E501

        :return: The work_email of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._work_email

    @work_email.setter
    def work_email(self, work_email):
        """Sets the work_email of this Employee.

        The employee's work email.  # noqa: E501

        :param work_email: The work_email of this Employee.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                work_email is not None and len(work_email) > 254):
            raise ValueError("Invalid value for `work_email`, length must be less than or equal to `254`")  # noqa: E501

        self._work_email = work_email

    @property
    def personal_email(self):
        """Gets the personal_email of this Employee.  # noqa: E501

        The employee's personal email.  # noqa: E501

        :return: The personal_email of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._personal_email

    @personal_email.setter
    def personal_email(self, personal_email):
        """Sets the personal_email of this Employee.

        The employee's personal email.  # noqa: E501

        :param personal_email: The personal_email of this Employee.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                personal_email is not None and len(personal_email) > 254):
            raise ValueError("Invalid value for `personal_email`, length must be less than or equal to `254`")  # noqa: E501

        self._personal_email = personal_email

    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this Employee.  # noqa: E501

        The employee's mobile phone number.  # noqa: E501

        :return: The mobile_phone_number of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this Employee.

        The employee's mobile phone number.  # noqa: E501

        :param mobile_phone_number: The mobile_phone_number of this Employee.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                mobile_phone_number is not None and len(mobile_phone_number) > 17):
            raise ValueError("Invalid value for `mobile_phone_number`, length must be less than or equal to `17`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mobile_phone_number is not None and not re.search(r'^\+?1?\d{9,15}$', mobile_phone_number)):  # noqa: E501
            raise ValueError(r"Invalid value for `mobile_phone_number`, must be a follow pattern or equal to `/^\+?1?\d{9,15}$/`")  # noqa: E501

        self._mobile_phone_number = mobile_phone_number

    @property
    def employments(self):
        """Gets the employments of this Employee.  # noqa: E501


        :return: The employments of this Employee.  # noqa: E501
        :rtype: list[str]
        """
        return self._employments

    @employments.setter
    def employments(self, employments):
        """Sets the employments of this Employee.


        :param employments: The employments of this Employee.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and employments is None:  # noqa: E501
            raise ValueError("Invalid value for `employments`, must not be `None`")  # noqa: E501

        self._employments = employments

    @property
    def home_location(self):
        """Gets the home_location of this Employee.  # noqa: E501

        The employee's home address.  # noqa: E501

        :return: The home_location of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._home_location

    @home_location.setter
    def home_location(self, home_location):
        """Sets the home_location of this Employee.

        The employee's home address.  # noqa: E501

        :param home_location: The home_location of this Employee.  # noqa: E501
        :type: str
        """

        self._home_location = home_location

    @property
    def work_location(self):
        """Gets the work_location of this Employee.  # noqa: E501

        The employee's work address.  # noqa: E501

        :return: The work_location of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._work_location

    @work_location.setter
    def work_location(self, work_location):
        """Sets the work_location of this Employee.

        The employee's work address.  # noqa: E501

        :param work_location: The work_location of this Employee.  # noqa: E501
        :type: str
        """

        self._work_location = work_location

    @property
    def manager(self):
        """Gets the manager of this Employee.  # noqa: E501

        The employeee ID of the employee's manager.  # noqa: E501

        :return: The manager of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this Employee.

        The employeee ID of the employee's manager.  # noqa: E501

        :param manager: The manager of this Employee.  # noqa: E501
        :type: str
        """

        self._manager = manager

    @property
    def team(self):
        """Gets the team of this Employee.  # noqa: E501

        The employee's team.  # noqa: E501

        :return: The team of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Employee.

        The employee's team.  # noqa: E501

        :param team: The team of this Employee.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def ssn(self):
        """Gets the ssn of this Employee.  # noqa: E501

        The employee's social security number.  # noqa: E501

        :return: The ssn of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn):
        """Sets the ssn of this Employee.

        The employee's social security number.  # noqa: E501

        :param ssn: The ssn of this Employee.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ssn is not None and len(ssn) > 9):
            raise ValueError("Invalid value for `ssn`, length must be less than or equal to `9`")  # noqa: E501

        self._ssn = ssn

    @property
    def gender(self):
        """Gets the gender of this Employee.  # noqa: E501

        The employee's gender.  # noqa: E501

        :return: The gender of this Employee.  # noqa: E501
        :rtype: OneOfGenderEnumBlankEnumNullEnum
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Employee.

        The employee's gender.  # noqa: E501

        :param gender: The gender of this Employee.  # noqa: E501
        :type: OneOfGenderEnumBlankEnumNullEnum
        """

        self._gender = gender

    @property
    def ethnicity(self):
        """Gets the ethnicity of this Employee.  # noqa: E501

        The employee's ethnicity.  # noqa: E501

        :return: The ethnicity of this Employee.  # noqa: E501
        :rtype: OneOfEthnicityEnumBlankEnumNullEnum
        """
        return self._ethnicity

    @ethnicity.setter
    def ethnicity(self, ethnicity):
        """Sets the ethnicity of this Employee.

        The employee's ethnicity.  # noqa: E501

        :param ethnicity: The ethnicity of this Employee.  # noqa: E501
        :type: OneOfEthnicityEnumBlankEnumNullEnum
        """

        self._ethnicity = ethnicity

    @property
    def marital_status(self):
        """Gets the marital_status of this Employee.  # noqa: E501

        The employee's marital status.  # noqa: E501

        :return: The marital_status of this Employee.  # noqa: E501
        :rtype: OneOfMaritalStatusEnumBlankEnumNullEnum
        """
        return self._marital_status

    @marital_status.setter
    def marital_status(self, marital_status):
        """Sets the marital_status of this Employee.

        The employee's marital status.  # noqa: E501

        :param marital_status: The marital_status of this Employee.  # noqa: E501
        :type: OneOfMaritalStatusEnumBlankEnumNullEnum
        """

        self._marital_status = marital_status

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this Employee.  # noqa: E501

        The employee's date of birth.  # noqa: E501

        :return: The date_of_birth of this Employee.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this Employee.

        The employee's date of birth.  # noqa: E501

        :param date_of_birth: The date_of_birth of this Employee.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def hire_dates(self):
        """Gets the hire_dates of this Employee.  # noqa: E501


        :return: The hire_dates of this Employee.  # noqa: E501
        :rtype: list[HireDate]
        """
        return self._hire_dates

    @hire_dates.setter
    def hire_dates(self, hire_dates):
        """Sets the hire_dates of this Employee.


        :param hire_dates: The hire_dates of this Employee.  # noqa: E501
        :type: list[HireDate]
        """
        if self.local_vars_configuration.client_side_validation and hire_dates is None:  # noqa: E501
            raise ValueError("Invalid value for `hire_dates`, must not be `None`")  # noqa: E501

        self._hire_dates = hire_dates

    @property
    def employment_status(self):
        """Gets the employment_status of this Employee.  # noqa: E501

        The employment status of the employee.  # noqa: E501

        :return: The employment_status of this Employee.  # noqa: E501
        :rtype: OneOfEmploymentStatusEnumBlankEnumNullEnum
        """
        return self._employment_status

    @employment_status.setter
    def employment_status(self, employment_status):
        """Sets the employment_status of this Employee.

        The employment status of the employee.  # noqa: E501

        :param employment_status: The employment_status of this Employee.  # noqa: E501
        :type: OneOfEmploymentStatusEnumBlankEnumNullEnum
        """

        self._employment_status = employment_status

    @property
    def termination_dates(self):
        """Gets the termination_dates of this Employee.  # noqa: E501


        :return: The termination_dates of this Employee.  # noqa: E501
        :rtype: list[TerminationDate]
        """
        return self._termination_dates

    @termination_dates.setter
    def termination_dates(self, termination_dates):
        """Sets the termination_dates of this Employee.


        :param termination_dates: The termination_dates of this Employee.  # noqa: E501
        :type: list[TerminationDate]
        """
        if self.local_vars_configuration.client_side_validation and termination_dates is None:  # noqa: E501
            raise ValueError("Invalid value for `termination_dates`, must not be `None`")  # noqa: E501

        self._termination_dates = termination_dates

    @property
    def avatar(self):
        """Gets the avatar of this Employee.  # noqa: E501

        The URL of the employee's avatar image.  # noqa: E501

        :return: The avatar of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this Employee.

        The URL of the employee's avatar image.  # noqa: E501

        :param avatar: The avatar of this Employee.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                avatar is not None and len(avatar) > 200):
            raise ValueError("Invalid value for `avatar`, length must be less than or equal to `200`")  # noqa: E501

        self._avatar = avatar

    @property
    def about(self):
        """Gets the about of this Employee.  # noqa: E501

        A description of the employee.  # noqa: E501

        :return: The about of this Employee.  # noqa: E501
        :rtype: str
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this Employee.

        A description of the employee.  # noqa: E501

        :param about: The about of this Employee.  # noqa: E501
        :type: str
        """

        self._about = about

    @property
    def documents(self):
        """Gets the documents of this Employee.  # noqa: E501


        :return: The documents of this Employee.  # noqa: E501
        :rtype: list[str]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Employee.


        :param documents: The documents of this Employee.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and documents is None:  # noqa: E501
            raise ValueError("Invalid value for `documents`, must not be `None`")  # noqa: E501

        self._documents = documents

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Employee):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Employee):
            return True

        return self.to_dict() != other.to_dict()
