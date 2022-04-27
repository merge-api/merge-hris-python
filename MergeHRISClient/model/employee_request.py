"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from MergeHRISClient.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class EmployeeRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('work_email',): {
            'max_length': 254,
        },
        ('personal_email',): {
            'max_length': 254,
        },
        ('ssn',): {
            'max_length': 100,
        },
        ('avatar',): {
            'max_length': 2000,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'remote_id': (str, none_type,),  # noqa: E501
            'employee_number': (str, none_type,),  # noqa: E501
            'company': (str, none_type,),  # noqa: E501
            'first_name': (str, none_type,),  # noqa: E501
            'last_name': (str, none_type,),  # noqa: E501
            'display_full_name': (str, none_type,),  # noqa: E501
            'groups': ([str, none_type],),  # noqa: E501
            'work_email': (str, none_type,),  # noqa: E501
            'personal_email': (str, none_type,),  # noqa: E501
            'mobile_phone_number': (str, none_type,),  # noqa: E501
            'employments': ([str, none_type],),  # noqa: E501
            'home_location': (str, none_type,),  # noqa: E501
            'work_location': (str, none_type,),  # noqa: E501
            'manager': (str, none_type,),  # noqa: E501
            'team': (str, none_type,),  # noqa: E501
            'pay_group': (str, none_type,),  # noqa: E501
            'ssn': (str, none_type,),  # noqa: E501
            'gender': (object, none_type,),  # noqa: E501
            'ethnicity': (object, none_type,),  # noqa: E501
            'marital_status': (object, none_type,),  # noqa: E501
            'date_of_birth': (datetime, none_type,),  # noqa: E501
            'hire_date': (datetime, none_type,),  # noqa: E501
            'start_date': (datetime, none_type,),  # noqa: E501
            'employment_status': (object, none_type,),  # noqa: E501
            'termination_date': (datetime, none_type,),  # noqa: E501
            'avatar': (str, none_type,),  # noqa: E501
            'custom_fields': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'remote_id': 'remote_id',  # noqa: E501
        'employee_number': 'employee_number',  # noqa: E501
        'company': 'company',  # noqa: E501
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'display_full_name': 'display_full_name',  # noqa: E501
        'groups': 'groups',  # noqa: E501
        'work_email': 'work_email',  # noqa: E501
        'personal_email': 'personal_email',  # noqa: E501
        'mobile_phone_number': 'mobile_phone_number',  # noqa: E501
        'employments': 'employments',  # noqa: E501
        'home_location': 'home_location',  # noqa: E501
        'work_location': 'work_location',  # noqa: E501
        'manager': 'manager',  # noqa: E501
        'team': 'team',  # noqa: E501
        'pay_group': 'pay_group',  # noqa: E501
        'ssn': 'ssn',  # noqa: E501
        'gender': 'gender',  # noqa: E501
        'ethnicity': 'ethnicity',  # noqa: E501
        'marital_status': 'marital_status',  # noqa: E501
        'date_of_birth': 'date_of_birth',  # noqa: E501
        'hire_date': 'hire_date',  # noqa: E501
        'start_date': 'start_date',  # noqa: E501
        'employment_status': 'employment_status',  # noqa: E501
        'termination_date': 'termination_date',  # noqa: E501
        'avatar': 'avatar',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """EmployeeRequest - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            employee_number (str, none_type): The employee's number that appears in the remote UI. Note: This is distinct from the remote_id field, which is a unique identifier for the employee set by the remote API, and is not exposed to the user. This value can also change in many API providers.. [optional]  # noqa: E501
            company (str, none_type): [optional]  # noqa: E501
            first_name (str, none_type): The employee's first name.. [optional]  # noqa: E501
            last_name (str, none_type): The employee's last name.. [optional]  # noqa: E501
            display_full_name (str, none_type): The employee's full name, to use for display purposes. If a preferred first name is available, the full name will include the preferred first name.. [optional]  # noqa: E501
            groups ([str, none_type]): [optional]  # noqa: E501
            work_email (str, none_type): The employee's work email.. [optional]  # noqa: E501
            personal_email (str, none_type): The employee's personal email.. [optional]  # noqa: E501
            mobile_phone_number (str, none_type): The employee's mobile phone number.. [optional]  # noqa: E501
            employments ([str, none_type]): Array of `Employment` IDs for this Employee.. [optional]  # noqa: E501
            home_location (str, none_type): [optional]  # noqa: E501
            work_location (str, none_type): [optional]  # noqa: E501
            manager (str, none_type): [optional]  # noqa: E501
            team (str, none_type): [optional]  # noqa: E501
            pay_group (str, none_type): [optional]  # noqa: E501
            ssn (str, none_type): The employee's social security number.. [optional]  # noqa: E501
            gender (object, none_type): The employee's gender.. [optional]  # noqa: E501
            ethnicity (object, none_type): The employee's ethnicity.. [optional]  # noqa: E501
            marital_status (object, none_type): The employee's marital status.. [optional]  # noqa: E501
            date_of_birth (datetime, none_type): The employee's date of birth.. [optional]  # noqa: E501
            hire_date (datetime, none_type): The date that the employee was hired, usually the day that an offer letter is signed. If an employee has multiple hire dates from previous employments, this represents the most recent hire date. Note: If you're looking for the employee's start date, refer to the start_date field.. [optional]  # noqa: E501
            start_date (datetime, none_type): The date that the employee started working. If an employee has multiple start dates from previous employments, this represents the most recent start date.. [optional]  # noqa: E501
            employment_status (object, none_type): The employment status of the employee.. [optional]  # noqa: E501
            termination_date (datetime, none_type): The employee's termination date.. [optional]  # noqa: E501
            avatar (str, none_type): The URL of the employee's avatar image.. [optional]  # noqa: E501
            custom_fields ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Custom fields configured for a given model.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
