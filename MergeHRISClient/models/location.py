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


class Location(object):
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
        'phone_number': 'str',
        'street_1': 'str',
        'street_2': 'str',
        'city': 'str',
        'state': 'OneOfStateEnumBlankEnumNullEnum',
        'zip_code': 'str',
        'country': 'OneOfCountryEnumBlankEnumNullEnum'
    }

    attribute_map = {
        'id': 'id',
        'remote_id': 'remote_id',
        'phone_number': 'phone_number',
        'street_1': 'street_1',
        'street_2': 'street_2',
        'city': 'city',
        'state': 'state',
        'zip_code': 'zip_code',
        'country': 'country'
    }

    def __init__(self, id=None, remote_id=None, phone_number=None, street_1=None, street_2=None, city=None, state=None, zip_code=None, country=None, local_vars_configuration=None):  # noqa: E501
        """Location - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._remote_id = None
        self._phone_number = None
        self._street_1 = None
        self._street_2 = None
        self._city = None
        self._state = None
        self._zip_code = None
        self._country = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.remote_id = remote_id
        self.phone_number = phone_number
        self.street_1 = street_1
        self.street_2 = street_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    @property
    def id(self):
        """Gets the id of this Location.  # noqa: E501


        :return: The id of this Location.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Location.


        :param id: The id of this Location.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def remote_id(self):
        """Gets the remote_id of this Location.  # noqa: E501

        The third-party API ID of the matching object.  # noqa: E501

        :return: The remote_id of this Location.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this Location.

        The third-party API ID of the matching object.  # noqa: E501

        :param remote_id: The remote_id of this Location.  # noqa: E501
        :type: str
        """

        self._remote_id = remote_id

    @property
    def phone_number(self):
        """Gets the phone_number of this Location.  # noqa: E501

        The location's phone number.  # noqa: E501

        :return: The phone_number of this Location.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Location.

        The location's phone number.  # noqa: E501

        :param phone_number: The phone_number of this Location.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone_number is not None and len(phone_number) > 17):
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `17`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                phone_number is not None and not re.search(r'^\+?1?\d{9,15}$', phone_number)):  # noqa: E501
            raise ValueError(r"Invalid value for `phone_number`, must be a follow pattern or equal to `/^\+?1?\d{9,15}$/`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def street_1(self):
        """Gets the street_1 of this Location.  # noqa: E501

        Line 1 of the location's street address.  # noqa: E501

        :return: The street_1 of this Location.  # noqa: E501
        :rtype: str
        """
        return self._street_1

    @street_1.setter
    def street_1(self, street_1):
        """Sets the street_1 of this Location.

        Line 1 of the location's street address.  # noqa: E501

        :param street_1: The street_1 of this Location.  # noqa: E501
        :type: str
        """

        self._street_1 = street_1

    @property
    def street_2(self):
        """Gets the street_2 of this Location.  # noqa: E501

        Line 2 of the location's street address.  # noqa: E501

        :return: The street_2 of this Location.  # noqa: E501
        :rtype: str
        """
        return self._street_2

    @street_2.setter
    def street_2(self, street_2):
        """Sets the street_2 of this Location.

        Line 2 of the location's street address.  # noqa: E501

        :param street_2: The street_2 of this Location.  # noqa: E501
        :type: str
        """

        self._street_2 = street_2

    @property
    def city(self):
        """Gets the city of this Location.  # noqa: E501

        The location's city.  # noqa: E501

        :return: The city of this Location.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Location.

        The location's city.  # noqa: E501

        :param city: The city of this Location.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Location.  # noqa: E501

        The location's state.  # noqa: E501

        :return: The state of this Location.  # noqa: E501
        :rtype: OneOfStateEnumBlankEnumNullEnum
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Location.

        The location's state.  # noqa: E501

        :param state: The state of this Location.  # noqa: E501
        :type: OneOfStateEnumBlankEnumNullEnum
        """

        self._state = state

    @property
    def zip_code(self):
        """Gets the zip_code of this Location.  # noqa: E501

        The location's zip code.  # noqa: E501

        :return: The zip_code of this Location.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Location.

        The location's zip code.  # noqa: E501

        :param zip_code: The zip_code of this Location.  # noqa: E501
        :type: str
        """

        self._zip_code = zip_code

    @property
    def country(self):
        """Gets the country of this Location.  # noqa: E501

        The location's country.  # noqa: E501

        :return: The country of this Location.  # noqa: E501
        :rtype: OneOfCountryEnumBlankEnumNullEnum
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Location.

        The location's country.  # noqa: E501

        :param country: The country of this Location.  # noqa: E501
        :type: OneOfCountryEnumBlankEnumNullEnum
        """

        self._country = country

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
        if not isinstance(other, Location):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Location):
            return True

        return self.to_dict() != other.to_dict()
