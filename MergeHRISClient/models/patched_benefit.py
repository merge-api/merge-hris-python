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


class PatchedBenefit(object):
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
        'origin_id': 'str',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'employee': 'str',
        'provider_name': 'str',
        'benefit_plan_type': 'OneOfBenefitPlanTypeEnumBlankEnumNullEnum',
        'employee_contribution': 'float',
        'company_contribution': 'float'
    }

    attribute_map = {
        'id': 'id',
        'origin_id': 'origin_id',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'employee': 'employee',
        'provider_name': 'provider_name',
        'benefit_plan_type': 'benefit_plan_type',
        'employee_contribution': 'employee_contribution',
        'company_contribution': 'company_contribution'
    }

    def __init__(self, id=None, origin_id=None, created_at=None, modified_at=None, employee=None, provider_name=None, benefit_plan_type=None, employee_contribution=None, company_contribution=None, local_vars_configuration=None):  # noqa: E501
        """PatchedBenefit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._origin_id = None
        self._created_at = None
        self._modified_at = None
        self._employee = None
        self._provider_name = None
        self._benefit_plan_type = None
        self._employee_contribution = None
        self._company_contribution = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.origin_id = origin_id
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        self.employee = employee
        self.provider_name = provider_name
        self.benefit_plan_type = benefit_plan_type
        self.employee_contribution = employee_contribution
        self.company_contribution = company_contribution

    @property
    def id(self):
        """Gets the id of this PatchedBenefit.  # noqa: E501


        :return: The id of this PatchedBenefit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PatchedBenefit.


        :param id: The id of this PatchedBenefit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def origin_id(self):
        """Gets the origin_id of this PatchedBenefit.  # noqa: E501

        The third-party API ID of the matching object.  # noqa: E501

        :return: The origin_id of this PatchedBenefit.  # noqa: E501
        :rtype: str
        """
        return self._origin_id

    @origin_id.setter
    def origin_id(self, origin_id):
        """Sets the origin_id of this PatchedBenefit.

        The third-party API ID of the matching object.  # noqa: E501

        :param origin_id: The origin_id of this PatchedBenefit.  # noqa: E501
        :type: str
        """

        self._origin_id = origin_id

    @property
    def created_at(self):
        """Gets the created_at of this PatchedBenefit.  # noqa: E501


        :return: The created_at of this PatchedBenefit.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PatchedBenefit.


        :param created_at: The created_at of this PatchedBenefit.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this PatchedBenefit.  # noqa: E501


        :return: The modified_at of this PatchedBenefit.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this PatchedBenefit.


        :param modified_at: The modified_at of this PatchedBenefit.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def employee(self):
        """Gets the employee of this PatchedBenefit.  # noqa: E501

        The employee on the plan.  # noqa: E501

        :return: The employee of this PatchedBenefit.  # noqa: E501
        :rtype: str
        """
        return self._employee

    @employee.setter
    def employee(self, employee):
        """Sets the employee of this PatchedBenefit.

        The employee on the plan.  # noqa: E501

        :param employee: The employee of this PatchedBenefit.  # noqa: E501
        :type: str
        """

        self._employee = employee

    @property
    def provider_name(self):
        """Gets the provider_name of this PatchedBenefit.  # noqa: E501

        The name of the benfit's provider.  # noqa: E501

        :return: The provider_name of this PatchedBenefit.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this PatchedBenefit.

        The name of the benfit's provider.  # noqa: E501

        :param provider_name: The provider_name of this PatchedBenefit.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def benefit_plan_type(self):
        """Gets the benefit_plan_type of this PatchedBenefit.  # noqa: E501

        The type of benefit plan  # noqa: E501

        :return: The benefit_plan_type of this PatchedBenefit.  # noqa: E501
        :rtype: OneOfBenefitPlanTypeEnumBlankEnumNullEnum
        """
        return self._benefit_plan_type

    @benefit_plan_type.setter
    def benefit_plan_type(self, benefit_plan_type):
        """Sets the benefit_plan_type of this PatchedBenefit.

        The type of benefit plan  # noqa: E501

        :param benefit_plan_type: The benefit_plan_type of this PatchedBenefit.  # noqa: E501
        :type: OneOfBenefitPlanTypeEnumBlankEnumNullEnum
        """

        self._benefit_plan_type = benefit_plan_type

    @property
    def employee_contribution(self):
        """Gets the employee_contribution of this PatchedBenefit.  # noqa: E501

        The employee's contribution.  # noqa: E501

        :return: The employee_contribution of this PatchedBenefit.  # noqa: E501
        :rtype: float
        """
        return self._employee_contribution

    @employee_contribution.setter
    def employee_contribution(self, employee_contribution):
        """Sets the employee_contribution of this PatchedBenefit.

        The employee's contribution.  # noqa: E501

        :param employee_contribution: The employee_contribution of this PatchedBenefit.  # noqa: E501
        :type: float
        """

        self._employee_contribution = employee_contribution

    @property
    def company_contribution(self):
        """Gets the company_contribution of this PatchedBenefit.  # noqa: E501

        The company's contribution.  # noqa: E501

        :return: The company_contribution of this PatchedBenefit.  # noqa: E501
        :rtype: float
        """
        return self._company_contribution

    @company_contribution.setter
    def company_contribution(self, company_contribution):
        """Sets the company_contribution of this PatchedBenefit.

        The company's contribution.  # noqa: E501

        :param company_contribution: The company_contribution of this PatchedBenefit.  # noqa: E501
        :type: float
        """

        self._company_contribution = company_contribution

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
        if not isinstance(other, PatchedBenefit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedBenefit):
            return True

        return self.to_dict() != other.to_dict()
