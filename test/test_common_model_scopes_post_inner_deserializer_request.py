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
from MergeHRISClient.model.enabled_actions_enum import EnabledActionsEnum
globals()['EnabledActionsEnum'] = EnabledActionsEnum
from MergeHRISClient.model.common_model_scopes_post_inner_deserializer_request import CommonModelScopesPostInnerDeserializerRequest
from MergeHRISClient.api_client import ApiClient


class TestCommonModelScopesPostInnerDeserializerRequest(unittest.TestCase):
    """CommonModelScopesPostInnerDeserializerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommonModelScopesPostInnerDeserializerRequest(self):
        """Test CommonModelScopesPostInnerDeserializerRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CommonModelScopesPostInnerDeserializerRequest()  # noqa: E501

        """
        No test json responses were defined for CommonModelScopesPostInnerDeserializerRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (CommonModelScopesPostInnerDeserializerRequest,), False)

        assert deserialized is not None

        assert deserialized.model_id is not None
        assert deserialized.enabled_actions is not None
        assert deserialized.disabled_fields is not None


if __name__ == '__main__':
    unittest.main()
