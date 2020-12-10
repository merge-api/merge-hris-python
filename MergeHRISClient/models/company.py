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


class Company(object):
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
        'legal_name': 'str',
        'display_name': 'str',
        'ei_ns': 'list[EIN]'
    }

    attribute_map = {
        'id': 'id',
        'remote_id': 'remote_id',
        'legal_name': 'legal_name',
        'display_name': 'display_name',
        'ei_ns': 'EINs'
    }

    def __init__(self, id=None, remote_id=None, legal_name=None, display_name=None, ei_ns=None, local_vars_configuration=None):  # noqa: E501
        """Company - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._remote_id = None
        self._legal_name = None
        self._display_name = None
        self._ei_ns = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.remote_id = remote_id
        self.legal_name = legal_name
        self.display_name = display_name
        if ei_ns is not None:
            self.ei_ns = ei_ns

    @property
    def id(self):
        """Gets the id of this Company.  # noqa: E501


        :return: The id of this Company.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Company.


        :param id: The id of this Company.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def remote_id(self):
        """Gets the remote_id of this Company.  # noqa: E501

        The third-party API ID of the matching object.  # noqa: E501

        :return: The remote_id of this Company.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this Company.

        The third-party API ID of the matching object.  # noqa: E501

        :param remote_id: The remote_id of this Company.  # noqa: E501
        :type: str
        """

        self._remote_id = remote_id

    @property
    def legal_name(self):
        """Gets the legal_name of this Company.  # noqa: E501

        The company's legal name.  # noqa: E501

        :return: The legal_name of this Company.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this Company.

        The company's legal name.  # noqa: E501

        :param legal_name: The legal_name of this Company.  # noqa: E501
        :type: str
        """

        self._legal_name = legal_name

    @property
    def display_name(self):
        """Gets the display_name of this Company.  # noqa: E501

        The company's display name.  # noqa: E501

        :return: The display_name of this Company.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Company.

        The company's display name.  # noqa: E501

        :param display_name: The display_name of this Company.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def ei_ns(self):
        """Gets the ei_ns of this Company.  # noqa: E501


        :return: The ei_ns of this Company.  # noqa: E501
        :rtype: list[EIN]
        """
        return self._ei_ns

    @ei_ns.setter
    def ei_ns(self, ei_ns):
        """Sets the ei_ns of this Company.


        :param ei_ns: The ei_ns of this Company.  # noqa: E501
        :type: list[EIN]
        """

        self._ei_ns = ei_ns

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
        if not isinstance(other, Company):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Company):
            return True

        return self.to_dict() != other.to_dict()
