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
from MergeHRISClient.model.location import Location
globals()['Location'] = Location
from MergeHRISClient.model.paginated_location_list import PaginatedLocationList
from MergeHRISClient.api_client import ApiClient


class TestPaginatedLocationList(unittest.TestCase):
    """PaginatedLocationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedLocationList(self):
        """Test PaginatedLocationList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedLocationList()  # noqa: E501

        """
        No test json responses were defined for PaginatedLocationList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedLocationList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
