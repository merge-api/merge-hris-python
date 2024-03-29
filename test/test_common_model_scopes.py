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
from MergeHRISClient.model.common_model_scope_data import CommonModelScopeData
globals()['CommonModelScopeData'] = CommonModelScopeData
from MergeHRISClient.model.common_model_scopes import CommonModelScopes
from MergeHRISClient.api_client import ApiClient


class TestCommonModelScopes(unittest.TestCase):
    """CommonModelScopes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommonModelScopes(self):
        """Test CommonModelScopes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CommonModelScopes()  # noqa: E501

        """
        No test json responses were defined for CommonModelScopes
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (CommonModelScopes,), False)

        assert deserialized is not None

        assert deserialized.scope_overrides is not None


if __name__ == '__main__':
    unittest.main()
