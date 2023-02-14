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
from MergeHRISClient.model.linked_account_condition_request import LinkedAccountConditionRequest
from MergeHRISClient.api_client import ApiClient


class TestLinkedAccountConditionRequest(unittest.TestCase):
    """LinkedAccountConditionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLinkedAccountConditionRequest(self):
        """Test LinkedAccountConditionRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LinkedAccountConditionRequest()  # noqa: E501

        """
        No test json responses were defined for LinkedAccountConditionRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (LinkedAccountConditionRequest,), False)

        assert deserialized is not None

        assert deserialized.condition_schema_id is not None
        assert deserialized.operator is not None
        assert deserialized.value is not None


if __name__ == '__main__':
    unittest.main()
