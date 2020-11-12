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
from MergeHRISClient.api.companies_api import CompaniesApi  # noqa: E501
from MergeHRISClient.rest import ApiException


class TestCompaniesApi(unittest.TestCase):
    """CompaniesApi unit test stubs"""

    def setUp(self):
        self.api = MergeHRISClient.api.companies_api.CompaniesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_create(self):
        """Test case for companies_create

        """
        pass

    def test_companies_destroy(self):
        """Test case for companies_destroy

        """
        pass

    def test_companies_list(self):
        """Test case for companies_list

        """
        pass

    def test_companies_partial_update(self):
        """Test case for companies_partial_update

        """
        pass

    def test_companies_retrieve(self):
        """Test case for companies_retrieve

        """
        pass

    def test_companies_update(self):
        """Test case for companies_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
