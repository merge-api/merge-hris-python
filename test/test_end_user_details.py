# coding: utf-8

"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import MergeHRISClient
from MergeHRISClient.models.end_user_details import EndUserDetails  # noqa: E501
from MergeHRISClient.rest import ApiException

class TestEndUserDetails(unittest.TestCase):
    """EndUserDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EndUserDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeHRISClient.models.end_user_details.EndUserDetails()  # noqa: E501
        if include_optional :
            return EndUserDetails(
                end_user_email_address = '0', 
                end_user_organization_name = '0', 
                end_user_origin_id = '0', 
                categories = [
                    'hris'
                    ]
            )
        else :
            return EndUserDetails(
                end_user_email_address = '0',
                end_user_organization_name = '0',
                end_user_origin_id = '0',
                categories = [
                    'hris'
                    ],
        )

    def testEndUserDetails(self):
        """Test EndUserDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()