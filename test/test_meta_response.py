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
from MergeHRISClient.model.linked_account_status import LinkedAccountStatus
globals()['LinkedAccountStatus'] = LinkedAccountStatus
from MergeHRISClient.model.meta_response import MetaResponse
from MergeHRISClient.api_client import ApiClient


class TestMetaResponse(unittest.TestCase):
    """MetaResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetaResponse(self):
        """Test MetaResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetaResponse()  # noqa: E501

        """
        No test json responses were defined for MetaResponse
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (MetaResponse,), False)

        assert deserialized is not None

        assert deserialized.request_schema is not None
        assert deserialized.has_conditional_params is not None
        assert deserialized.has_required_linked_account_params is not None


if __name__ == '__main__':
    unittest.main()
