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

import MergeHRISClient
from MergeHRISClient.api.create_link_token_api import CreateLinkTokenApi  # noqa: E501
from MergeHRISClient.rest import ApiException


class TestCreateLinkTokenApi(unittest.TestCase):
    """CreateLinkTokenApi unit test stubs"""

    def setUp(self):
        self.api = MergeHRISClient.api.create_link_token_api.CreateLinkTokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_link_token_create(self):
        """Test case for create_link_token_create

        """
        pass


if __name__ == '__main__':
    unittest.main()