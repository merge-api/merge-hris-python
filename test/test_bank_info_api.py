"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeHRISClient
from MergeHRISClient.api.bank_info_api import BankInfoApi  # noqa: E501


class TestBankInfoApi(unittest.TestCase):
    """BankInfoApi unit test stubs"""

    def setUp(self):
        self.api = BankInfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bank_info_list(self):
        """Test case for bank_info_list

        """
        pass

    def test_bank_info_retrieve(self):
        """Test case for bank_info_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
