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
from MergeHRISClient.api.employments_api import EmploymentsApi  # noqa: E501
from MergeHRISClient.rest import ApiException


class TestEmploymentsApi(unittest.TestCase):
    """EmploymentsApi unit test stubs"""

    def setUp(self):
        self.api = MergeHRISClient.api.employments_api.EmploymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_employments_create(self):
        """Test case for employments_create

        """
        pass

    def test_employments_destroy(self):
        """Test case for employments_destroy

        """
        pass

    def test_employments_list(self):
        """Test case for employments_list

        """
        pass

    def test_employments_partial_update(self):
        """Test case for employments_partial_update

        """
        pass

    def test_employments_retrieve(self):
        """Test case for employments_retrieve

        """
        pass

    def test_employments_update(self):
        """Test case for employments_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
