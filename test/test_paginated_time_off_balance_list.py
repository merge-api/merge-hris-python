"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergeHRISClient
from MergeHRISClient.model.time_off_balance import TimeOffBalance
globals()['TimeOffBalance'] = TimeOffBalance
from MergeHRISClient.model.paginated_time_off_balance_list import PaginatedTimeOffBalanceList
from MergeHRISClient.api_client import ApiClient


class TestPaginatedTimeOffBalanceList(unittest.TestCase):
    """PaginatedTimeOffBalanceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedTimeOffBalanceList(self):
        """Test PaginatedTimeOffBalanceList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedTimeOffBalanceList()  # noqa: E501

        """
        No test json responses were defined for PaginatedTimeOffBalanceList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedTimeOffBalanceList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
