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


class PayrollRun(object):
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
        'run_state': 'OneOfRunStateEnumBlankEnumNullEnum',
        'run_type': 'OneOfRunTypeEnumBlankEnumNullEnum',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'check_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'remote_id': 'remote_id',
        'run_state': 'run_state',
        'run_type': 'run_type',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'check_date': 'check_date'
    }

    def __init__(self, id=None, remote_id=None, run_state=None, run_type=None, start_date=None, end_date=None, check_date=None, local_vars_configuration=None):  # noqa: E501
        """PayrollRun - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._remote_id = None
        self._run_state = None
        self._run_type = None
        self._start_date = None
        self._end_date = None
        self._check_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.remote_id = remote_id
        self.run_state = run_state
        self.run_type = run_type
        self.start_date = start_date
        self.end_date = end_date
        self.check_date = check_date

    @property
    def id(self):
        """Gets the id of this PayrollRun.  # noqa: E501


        :return: The id of this PayrollRun.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PayrollRun.


        :param id: The id of this PayrollRun.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def remote_id(self):
        """Gets the remote_id of this PayrollRun.  # noqa: E501

        The third-party API ID of the matching object.  # noqa: E501

        :return: The remote_id of this PayrollRun.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this PayrollRun.

        The third-party API ID of the matching object.  # noqa: E501

        :param remote_id: The remote_id of this PayrollRun.  # noqa: E501
        :type: str
        """

        self._remote_id = remote_id

    @property
    def run_state(self):
        """Gets the run_state of this PayrollRun.  # noqa: E501

        The state of the payroll run  # noqa: E501

        :return: The run_state of this PayrollRun.  # noqa: E501
        :rtype: OneOfRunStateEnumBlankEnumNullEnum
        """
        return self._run_state

    @run_state.setter
    def run_state(self, run_state):
        """Sets the run_state of this PayrollRun.

        The state of the payroll run  # noqa: E501

        :param run_state: The run_state of this PayrollRun.  # noqa: E501
        :type: OneOfRunStateEnumBlankEnumNullEnum
        """

        self._run_state = run_state

    @property
    def run_type(self):
        """Gets the run_type of this PayrollRun.  # noqa: E501

        The type of the payroll run  # noqa: E501

        :return: The run_type of this PayrollRun.  # noqa: E501
        :rtype: OneOfRunTypeEnumBlankEnumNullEnum
        """
        return self._run_type

    @run_type.setter
    def run_type(self, run_type):
        """Sets the run_type of this PayrollRun.

        The type of the payroll run  # noqa: E501

        :param run_type: The run_type of this PayrollRun.  # noqa: E501
        :type: OneOfRunTypeEnumBlankEnumNullEnum
        """

        self._run_type = run_type

    @property
    def start_date(self):
        """Gets the start_date of this PayrollRun.  # noqa: E501

        The day and time the payroll run started.  # noqa: E501

        :return: The start_date of this PayrollRun.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PayrollRun.

        The day and time the payroll run started.  # noqa: E501

        :param start_date: The start_date of this PayrollRun.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this PayrollRun.  # noqa: E501

        The day and time the payroll run ended.  # noqa: E501

        :return: The end_date of this PayrollRun.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this PayrollRun.

        The day and time the payroll run ended.  # noqa: E501

        :param end_date: The end_date of this PayrollRun.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def check_date(self):
        """Gets the check_date of this PayrollRun.  # noqa: E501

        The day and time the payroll run was checked.  # noqa: E501

        :return: The check_date of this PayrollRun.  # noqa: E501
        :rtype: datetime
        """
        return self._check_date

    @check_date.setter
    def check_date(self, check_date):
        """Sets the check_date of this PayrollRun.

        The day and time the payroll run was checked.  # noqa: E501

        :param check_date: The check_date of this PayrollRun.  # noqa: E501
        :type: datetime
        """

        self._check_date = check_date

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
        if not isinstance(other, PayrollRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PayrollRun):
            return True

        return self.to_dict() != other.to_dict()
