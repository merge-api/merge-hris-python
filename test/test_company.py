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
from MergeHRISClient.models.company import Company  # noqa: E501
from MergeHRISClient.rest import ApiException

class TestCompany(unittest.TestCase):
    """Company unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Company
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeHRISClient.models.company.Company()  # noqa: E501
        if include_optional :
            return Company(
                id = '0', 
                origin_id = '19202938', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                legal_name = 'Merge API Inc.', 
                display_name = 'Merge', 
                ei_ns = [
                    '0'
                    ]
            )
        else :
            return Company(
                id = '0',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                ei_ns = [
                    '0'
                    ],
        )

    def testCompany(self):
        """Test Company"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
