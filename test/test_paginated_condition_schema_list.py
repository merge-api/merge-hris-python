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
from MergeHRISClient.model.condition_schema import ConditionSchema
globals()['ConditionSchema'] = ConditionSchema
from MergeHRISClient.model.paginated_condition_schema_list import PaginatedConditionSchemaList
from MergeHRISClient.api_client import ApiClient


class TestPaginatedConditionSchemaList(unittest.TestCase):
    """PaginatedConditionSchemaList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedConditionSchemaList(self):
        """Test PaginatedConditionSchemaList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedConditionSchemaList()  # noqa: E501

        """
        No test json responses were defined for PaginatedConditionSchemaList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedConditionSchemaList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
