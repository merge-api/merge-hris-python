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
from MergeHRISClient.model.group import Group
globals()['Group'] = Group
from MergeHRISClient.model.paginated_group_list import PaginatedGroupList
from MergeHRISClient.api_client import ApiClient


class TestPaginatedGroupList(unittest.TestCase):
    """PaginatedGroupList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedGroupList(self):
        """Test PaginatedGroupList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedGroupList()  # noqa: E501

        """
        No test json responses were defined for PaginatedGroupList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedGroupList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
