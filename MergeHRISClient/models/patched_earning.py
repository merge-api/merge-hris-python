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


class PatchedEarning(object):
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
        'employee_payroll_run': 'str',
        'amount': 'float',
        'type': 'OneOfTypeEnumBlankEnumNullEnum'
    }

    attribute_map = {
        'employee_payroll_run': 'employee_payroll_run',
        'amount': 'amount',
        'type': 'type'
    }

    def __init__(self, employee_payroll_run=None, amount=None, type=None, local_vars_configuration=None):  # noqa: E501
        """PatchedEarning - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._employee_payroll_run = None
        self._amount = None
        self._type = None
        self.discriminator = None

        self.employee_payroll_run = employee_payroll_run
        self.amount = amount
        self.type = type

    @property
    def employee_payroll_run(self):
        """Gets the employee_payroll_run of this PatchedEarning.  # noqa: E501

        The earning's employee payroll run.  # noqa: E501

        :return: The employee_payroll_run of this PatchedEarning.  # noqa: E501
        :rtype: str
        """
        return self._employee_payroll_run

    @employee_payroll_run.setter
    def employee_payroll_run(self, employee_payroll_run):
        """Sets the employee_payroll_run of this PatchedEarning.

        The earning's employee payroll run.  # noqa: E501

        :param employee_payroll_run: The employee_payroll_run of this PatchedEarning.  # noqa: E501
        :type: str
        """

        self._employee_payroll_run = employee_payroll_run

    @property
    def amount(self):
        """Gets the amount of this PatchedEarning.  # noqa: E501

        The amount earned.  # noqa: E501

        :return: The amount of this PatchedEarning.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PatchedEarning.

        The amount earned.  # noqa: E501

        :param amount: The amount of this PatchedEarning.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def type(self):
        """Gets the type of this PatchedEarning.  # noqa: E501

        The type of earning.  # noqa: E501

        :return: The type of this PatchedEarning.  # noqa: E501
        :rtype: OneOfTypeEnumBlankEnumNullEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PatchedEarning.

        The type of earning.  # noqa: E501

        :param type: The type of this PatchedEarning.  # noqa: E501
        :type: OneOfTypeEnumBlankEnumNullEnum
        """

        self._type = type

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
        if not isinstance(other, PatchedEarning):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedEarning):
            return True

        return self.to_dict() != other.to_dict()
