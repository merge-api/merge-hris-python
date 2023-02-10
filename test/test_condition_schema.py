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
from MergeHRISClient.model.condition_type_enum import ConditionTypeEnum
from MergeHRISClient.model.operator_schema import OperatorSchema
globals()['ConditionTypeEnum'] = ConditionTypeEnum
globals()['OperatorSchema'] = OperatorSchema
from MergeHRISClient.model.condition_schema import ConditionSchema
from MergeHRISClient.api_client import ApiClient


class TestConditionSchema(unittest.TestCase):
    """ConditionSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConditionSchema(self):
        """Test ConditionSchema"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConditionSchema()  # noqa: E501

        """
        No test json responses were defined for ConditionSchema
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (ConditionSchema,), False)

        assert deserialized is not None

        assert deserialized.id is not None
        assert deserialized.native_name is not None
        assert deserialized.field_name is not None
        assert deserialized.condition_type is not None
        assert deserialized.operators is not None


if __name__ == '__main__':
    unittest.main()
