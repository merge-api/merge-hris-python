"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import MergeHRISClient
from MergeHRISClient.model.remote_data import RemoteData
globals()['RemoteData'] = RemoteData
from MergeHRISClient.model.bank_info import BankInfo


class TestBankInfo(unittest.TestCase):
    """BankInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBankInfo(self):
        """Test BankInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BankInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
