"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from MergeHRISClient.api_client import ApiClient, Endpoint
from MergeHRISClient.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from MergeHRISClient.model.employee import Employee
from MergeHRISClient.model.paginated_employee_list import PaginatedEmployeeList


class EmployeesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __employees_create(
            self,
            x_account_token,
            **kwargs
        ):
            """employees_create  # noqa: E501

            Creates an `Employee` object with the given values.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.employees_create(x_account_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.

            Keyword Args:
                run_async (bool): Whether or not third-party updates should be run asynchronously.. [optional]
                employee (Employee): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Employee
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_account_token'] = \
                x_account_token
            return self.call_with_http_info(**kwargs)

        self.employees_create = Endpoint(
            settings={
                'response_type': (Employee,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/employees',
                'operation_id': 'employees_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'run_async',
                    'employee',
                ],
                'required': [
                    'x_account_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'run_async':
                        (bool,),
                    'employee':
                        (Employee,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'run_async': 'run_async',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'run_async': 'query',
                    'employee': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__employees_create
        )

        def __employees_list(
            self,
            x_account_token,
            **kwargs
        ):
            """employees_list  # noqa: E501

            Returns a list of `Employee` objects.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.employees_list(x_account_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.

            Keyword Args:
                company_id (str): If provided, will only return employees for this company.. [optional]
                created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
                created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
                cursor (str): The pagination cursor value.. [optional]
                expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional]
                manager_id (str): If provided, will only return employees for this manager.. [optional]
                modified_after (datetime): If provided, will only return objects modified after this datetime.. [optional]
                modified_before (datetime): If provided, will only return objects modified before this datetime.. [optional]
                page_size (int): Number of results to return per page.. [optional]
                remote_id (str, none_type): The API provider's ID for the given object.. [optional]
                team_id (str): If provided, will only return employees for this team.. [optional]
                work_location_id (str): If provided, will only return employees for this location.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaginatedEmployeeList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_account_token'] = \
                x_account_token
            return self.call_with_http_info(**kwargs)

        self.employees_list = Endpoint(
            settings={
                'response_type': (PaginatedEmployeeList,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/employees',
                'operation_id': 'employees_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'company_id',
                    'created_after',
                    'created_before',
                    'cursor',
                    'expand',
                    'manager_id',
                    'modified_after',
                    'modified_before',
                    'page_size',
                    'remote_id',
                    'team_id',
                    'work_location_id',
                ],
                'required': [
                    'x_account_token',
                ],
                'nullable': [
                    'remote_id',
                ],
                'enum': [
                    'expand',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "COMPANY": "company",
                        "EMPLOYMENTS": "employments",
                        "EMPLOYMENTS,COMPANY": "employments,company",
                        "EMPLOYMENTS,HOME_LOCATION": "employments,home_location",
                        "EMPLOYMENTS,HOME_LOCATION,COMPANY": "employments,home_location,company",
                        "EMPLOYMENTS,HOME_LOCATION,MANAGER": "employments,home_location,manager",
                        "EMPLOYMENTS,HOME_LOCATION,MANAGER,COMPANY": "employments,home_location,manager,company",
                        "EMPLOYMENTS,HOME_LOCATION,MANAGER,TEAM": "employments,home_location,manager,team",
                        "EMPLOYMENTS,HOME_LOCATION,MANAGER,TEAM,COMPANY": "employments,home_location,manager,team,company",
                        "EMPLOYMENTS,HOME_LOCATION,TEAM": "employments,home_location,team",
                        "EMPLOYMENTS,HOME_LOCATION,TEAM,COMPANY": "employments,home_location,team,company",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION": "employments,home_location,work_location",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,COMPANY": "employments,home_location,work_location,company",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,MANAGER": "employments,home_location,work_location,manager",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,MANAGER,COMPANY": "employments,home_location,work_location,manager,company",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,MANAGER,TEAM": "employments,home_location,work_location,manager,team",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,MANAGER,TEAM,COMPANY": "employments,home_location,work_location,manager,team,company",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,TEAM": "employments,home_location,work_location,team",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,TEAM,COMPANY": "employments,home_location,work_location,team,company",
                        "EMPLOYMENTS,MANAGER": "employments,manager",
                        "EMPLOYMENTS,MANAGER,COMPANY": "employments,manager,company",
                        "EMPLOYMENTS,MANAGER,TEAM": "employments,manager,team",
                        "EMPLOYMENTS,MANAGER,TEAM,COMPANY": "employments,manager,team,company",
                        "EMPLOYMENTS,TEAM": "employments,team",
                        "EMPLOYMENTS,TEAM,COMPANY": "employments,team,company",
                        "EMPLOYMENTS,WORK_LOCATION": "employments,work_location",
                        "EMPLOYMENTS,WORK_LOCATION,COMPANY": "employments,work_location,company",
                        "EMPLOYMENTS,WORK_LOCATION,MANAGER": "employments,work_location,manager",
                        "EMPLOYMENTS,WORK_LOCATION,MANAGER,COMPANY": "employments,work_location,manager,company",
                        "EMPLOYMENTS,WORK_LOCATION,MANAGER,TEAM": "employments,work_location,manager,team",
                        "EMPLOYMENTS,WORK_LOCATION,MANAGER,TEAM,COMPANY": "employments,work_location,manager,team,company",
                        "EMPLOYMENTS,WORK_LOCATION,TEAM": "employments,work_location,team",
                        "EMPLOYMENTS,WORK_LOCATION,TEAM,COMPANY": "employments,work_location,team,company",
                        "HOME_LOCATION": "home_location",
                        "HOME_LOCATION,COMPANY": "home_location,company",
                        "HOME_LOCATION,MANAGER": "home_location,manager",
                        "HOME_LOCATION,MANAGER,COMPANY": "home_location,manager,company",
                        "HOME_LOCATION,MANAGER,TEAM": "home_location,manager,team",
                        "HOME_LOCATION,MANAGER,TEAM,COMPANY": "home_location,manager,team,company",
                        "HOME_LOCATION,TEAM": "home_location,team",
                        "HOME_LOCATION,TEAM,COMPANY": "home_location,team,company",
                        "HOME_LOCATION,WORK_LOCATION": "home_location,work_location",
                        "HOME_LOCATION,WORK_LOCATION,COMPANY": "home_location,work_location,company",
                        "HOME_LOCATION,WORK_LOCATION,MANAGER": "home_location,work_location,manager",
                        "HOME_LOCATION,WORK_LOCATION,MANAGER,COMPANY": "home_location,work_location,manager,company",
                        "HOME_LOCATION,WORK_LOCATION,MANAGER,TEAM": "home_location,work_location,manager,team",
                        "HOME_LOCATION,WORK_LOCATION,MANAGER,TEAM,COMPANY": "home_location,work_location,manager,team,company",
                        "HOME_LOCATION,WORK_LOCATION,TEAM": "home_location,work_location,team",
                        "HOME_LOCATION,WORK_LOCATION,TEAM,COMPANY": "home_location,work_location,team,company",
                        "MANAGER": "manager",
                        "MANAGER,COMPANY": "manager,company",
                        "MANAGER,TEAM": "manager,team",
                        "MANAGER,TEAM,COMPANY": "manager,team,company",
                        "TEAM": "team",
                        "TEAM,COMPANY": "team,company",
                        "WORK_LOCATION": "work_location",
                        "WORK_LOCATION,COMPANY": "work_location,company",
                        "WORK_LOCATION,MANAGER": "work_location,manager",
                        "WORK_LOCATION,MANAGER,COMPANY": "work_location,manager,company",
                        "WORK_LOCATION,MANAGER,TEAM": "work_location,manager,team",
                        "WORK_LOCATION,MANAGER,TEAM,COMPANY": "work_location,manager,team,company",
                        "WORK_LOCATION,TEAM": "work_location,team",
                        "WORK_LOCATION,TEAM,COMPANY": "work_location,team,company"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'company_id':
                        (str,),
                    'created_after':
                        (datetime,),
                    'created_before':
                        (datetime,),
                    'cursor':
                        (str,),
                    'expand':
                        (str,),
                    'manager_id':
                        (str,),
                    'modified_after':
                        (datetime,),
                    'modified_before':
                        (datetime,),
                    'page_size':
                        (int,),
                    'remote_id':
                        (str, none_type,),
                    'team_id':
                        (str,),
                    'work_location_id':
                        (str,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'company_id': 'company_id',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'expand': 'expand',
                    'manager_id': 'manager_id',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'page_size': 'page_size',
                    'remote_id': 'remote_id',
                    'team_id': 'team_id',
                    'work_location_id': 'work_location_id',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'company_id': 'query',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'expand': 'query',
                    'manager_id': 'query',
                    'modified_after': 'query',
                    'modified_before': 'query',
                    'page_size': 'query',
                    'remote_id': 'query',
                    'team_id': 'query',
                    'work_location_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__employees_list
        )

        def __employees_retrieve(
            self,
            x_account_token,
            id,
            **kwargs
        ):
            """employees_retrieve  # noqa: E501

            Returns an `Employee` object with the given `id`.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.employees_retrieve(x_account_token, id, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.
                id (str):

            Keyword Args:
                expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Employee
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_account_token'] = \
                x_account_token
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.employees_retrieve = Endpoint(
            settings={
                'response_type': (Employee,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/employees/{id}',
                'operation_id': 'employees_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'id',
                    'expand',
                ],
                'required': [
                    'x_account_token',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                    'expand',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "COMPANY": "company",
                        "EMPLOYMENTS": "employments",
                        "EMPLOYMENTS,COMPANY": "employments,company",
                        "EMPLOYMENTS,HOME_LOCATION": "employments,home_location",
                        "EMPLOYMENTS,HOME_LOCATION,COMPANY": "employments,home_location,company",
                        "EMPLOYMENTS,HOME_LOCATION,MANAGER": "employments,home_location,manager",
                        "EMPLOYMENTS,HOME_LOCATION,MANAGER,COMPANY": "employments,home_location,manager,company",
                        "EMPLOYMENTS,HOME_LOCATION,MANAGER,TEAM": "employments,home_location,manager,team",
                        "EMPLOYMENTS,HOME_LOCATION,MANAGER,TEAM,COMPANY": "employments,home_location,manager,team,company",
                        "EMPLOYMENTS,HOME_LOCATION,TEAM": "employments,home_location,team",
                        "EMPLOYMENTS,HOME_LOCATION,TEAM,COMPANY": "employments,home_location,team,company",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION": "employments,home_location,work_location",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,COMPANY": "employments,home_location,work_location,company",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,MANAGER": "employments,home_location,work_location,manager",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,MANAGER,COMPANY": "employments,home_location,work_location,manager,company",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,MANAGER,TEAM": "employments,home_location,work_location,manager,team",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,MANAGER,TEAM,COMPANY": "employments,home_location,work_location,manager,team,company",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,TEAM": "employments,home_location,work_location,team",
                        "EMPLOYMENTS,HOME_LOCATION,WORK_LOCATION,TEAM,COMPANY": "employments,home_location,work_location,team,company",
                        "EMPLOYMENTS,MANAGER": "employments,manager",
                        "EMPLOYMENTS,MANAGER,COMPANY": "employments,manager,company",
                        "EMPLOYMENTS,MANAGER,TEAM": "employments,manager,team",
                        "EMPLOYMENTS,MANAGER,TEAM,COMPANY": "employments,manager,team,company",
                        "EMPLOYMENTS,TEAM": "employments,team",
                        "EMPLOYMENTS,TEAM,COMPANY": "employments,team,company",
                        "EMPLOYMENTS,WORK_LOCATION": "employments,work_location",
                        "EMPLOYMENTS,WORK_LOCATION,COMPANY": "employments,work_location,company",
                        "EMPLOYMENTS,WORK_LOCATION,MANAGER": "employments,work_location,manager",
                        "EMPLOYMENTS,WORK_LOCATION,MANAGER,COMPANY": "employments,work_location,manager,company",
                        "EMPLOYMENTS,WORK_LOCATION,MANAGER,TEAM": "employments,work_location,manager,team",
                        "EMPLOYMENTS,WORK_LOCATION,MANAGER,TEAM,COMPANY": "employments,work_location,manager,team,company",
                        "EMPLOYMENTS,WORK_LOCATION,TEAM": "employments,work_location,team",
                        "EMPLOYMENTS,WORK_LOCATION,TEAM,COMPANY": "employments,work_location,team,company",
                        "HOME_LOCATION": "home_location",
                        "HOME_LOCATION,COMPANY": "home_location,company",
                        "HOME_LOCATION,MANAGER": "home_location,manager",
                        "HOME_LOCATION,MANAGER,COMPANY": "home_location,manager,company",
                        "HOME_LOCATION,MANAGER,TEAM": "home_location,manager,team",
                        "HOME_LOCATION,MANAGER,TEAM,COMPANY": "home_location,manager,team,company",
                        "HOME_LOCATION,TEAM": "home_location,team",
                        "HOME_LOCATION,TEAM,COMPANY": "home_location,team,company",
                        "HOME_LOCATION,WORK_LOCATION": "home_location,work_location",
                        "HOME_LOCATION,WORK_LOCATION,COMPANY": "home_location,work_location,company",
                        "HOME_LOCATION,WORK_LOCATION,MANAGER": "home_location,work_location,manager",
                        "HOME_LOCATION,WORK_LOCATION,MANAGER,COMPANY": "home_location,work_location,manager,company",
                        "HOME_LOCATION,WORK_LOCATION,MANAGER,TEAM": "home_location,work_location,manager,team",
                        "HOME_LOCATION,WORK_LOCATION,MANAGER,TEAM,COMPANY": "home_location,work_location,manager,team,company",
                        "HOME_LOCATION,WORK_LOCATION,TEAM": "home_location,work_location,team",
                        "HOME_LOCATION,WORK_LOCATION,TEAM,COMPANY": "home_location,work_location,team,company",
                        "MANAGER": "manager",
                        "MANAGER,COMPANY": "manager,company",
                        "MANAGER,TEAM": "manager,team",
                        "MANAGER,TEAM,COMPANY": "manager,team,company",
                        "TEAM": "team",
                        "TEAM,COMPANY": "team,company",
                        "WORK_LOCATION": "work_location",
                        "WORK_LOCATION,COMPANY": "work_location,company",
                        "WORK_LOCATION,MANAGER": "work_location,manager",
                        "WORK_LOCATION,MANAGER,COMPANY": "work_location,manager,company",
                        "WORK_LOCATION,MANAGER,TEAM": "work_location,manager,team",
                        "WORK_LOCATION,MANAGER,TEAM,COMPANY": "work_location,manager,team,company",
                        "WORK_LOCATION,TEAM": "work_location,team",
                        "WORK_LOCATION,TEAM,COMPANY": "work_location,team,company"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'id':
                        (str,),
                    'expand':
                        (str,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'id': 'id',
                    'expand': 'expand',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'id': 'path',
                    'expand': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__employees_retrieve
        )
