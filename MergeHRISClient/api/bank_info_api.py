"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from MergeHRISClient.api_client import ApiClient, Endpoint as _Endpoint
from MergeHRISClient.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from MergeHRISClient.model.bank_info import BankInfo
from MergeHRISClient.model.paginated_bank_info_list import PaginatedBankInfoList


class BankInfoApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __bank_info_list(
            self,
            x_account_token,
            **kwargs
        ):
            """bank_info_list  # noqa: E501

            Returns a list of `BankInfo` objects.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.bank_info_list(x_account_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.

            Keyword Args:
                account_type (str, none_type): If provided, will only return BankInfo's with this account type. Options: ('SAVINGS', 'CHECKING'). [optional]
                bank_name (str, none_type): If provided, will only return BankInfo's with this bank name.. [optional]
                created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
                created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
                cursor (str): The pagination cursor value.. [optional]
                employee_id (str): If provided, will only return bank accounts for this employee.. [optional]
                expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "employee"
                include_deleted_data (bool): Whether to include data that was deleted in the third-party service.. [optional]
                include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
                modified_after (datetime): If provided, will only return objects modified after this datetime.. [optional]
                modified_before (datetime): If provided, will only return objects modified before this datetime.. [optional]
                order_by (str): Overrides the default ordering for this endpoint.. [optional]
                page_size (int): Number of results to return per page.. [optional]
                remote_id (str, none_type): The API provider's ID for the given object.. [optional]
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
                PaginatedBankInfoList
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

        self.bank_info_list = _Endpoint(
            settings={
                'response_type': (PaginatedBankInfoList,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/bank-info',
                'operation_id': 'bank_info_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'account_type',
                    'bank_name',
                    'created_after',
                    'created_before',
                    'cursor',
                    'employee_id',
                    'expand',
                    'include_deleted_data',
                    'include_remote_data',
                    'modified_after',
                    'modified_before',
                    'order_by',
                    'page_size',
                    'remote_id',
                ],
                'required': [
                    'x_account_token',
                ],
                'nullable': [
                    'account_type',
                    'bank_name',
                    'remote_id',
                ],
                'enum': [
                    'account_type',
                    'expand',
                    'order_by',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('account_type',): {
                        'None': None,
                        "CHECKING": "CHECKING",
                        "SAVINGS": "SAVINGS"
                    },
                    ('expand',): {

                        "EMPLOYEE": "employee"
                    },
                    ('order_by',): {

                        "-REMOTE_CREATED_AT": "-remote_created_at",
                        "REMOTE_CREATED_AT": "remote_created_at"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'account_type':
                        (str, none_type,),
                    'bank_name':
                        (str, none_type,),
                    'created_after':
                        (datetime,),
                    'created_before':
                        (datetime,),
                    'cursor':
                        (str,),
                    'employee_id':
                        (str,),
                    'expand':
                        (str,),
                    'include_deleted_data':
                        (bool,),
                    'include_remote_data':
                        (bool,),
                    'modified_after':
                        (datetime,),
                    'modified_before':
                        (datetime,),
                    'order_by':
                        (str,),
                    'page_size':
                        (int,),
                    'remote_id':
                        (str, none_type,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'account_type': 'account_type',
                    'bank_name': 'bank_name',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'employee_id': 'employee_id',
                    'expand': 'expand',
                    'include_deleted_data': 'include_deleted_data',
                    'include_remote_data': 'include_remote_data',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'order_by': 'order_by',
                    'page_size': 'page_size',
                    'remote_id': 'remote_id',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'account_type': 'query',
                    'bank_name': 'query',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'employee_id': 'query',
                    'expand': 'query',
                    'include_deleted_data': 'query',
                    'include_remote_data': 'query',
                    'modified_after': 'query',
                    'modified_before': 'query',
                    'order_by': 'query',
                    'page_size': 'query',
                    'remote_id': 'query',
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
            callable=__bank_info_list
        )

        def __bank_info_retrieve(
            self,
            x_account_token,
            id,
            **kwargs
        ):
            """bank_info_retrieve  # noqa: E501

            Returns a `BankInfo` object with the given `id`.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.bank_info_retrieve(x_account_token, id, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.
                id (str):

            Keyword Args:
                expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "employee"
                include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
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
                BankInfo
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

        self.bank_info_retrieve = _Endpoint(
            settings={
                'response_type': (BankInfo,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/bank-info/{id}',
                'operation_id': 'bank_info_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'id',
                    'expand',
                    'include_remote_data',
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

                        "EMPLOYEE": "employee"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'id':
                        (str,),
                    'expand':
                        (str,),
                    'include_remote_data':
                        (bool,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'id': 'id',
                    'expand': 'expand',
                    'include_remote_data': 'include_remote_data',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'id': 'path',
                    'expand': 'query',
                    'include_remote_data': 'query',
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
            callable=__bank_info_retrieve
        )
