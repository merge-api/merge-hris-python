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
from MergeHRISClient.model.remote_data import RemoteData
globals()['RemoteData'] = RemoteData
from MergeHRISClient.model.group import Group
from MergeHRISClient.api_client import ApiClient


class TestGroup(unittest.TestCase):
    """Group unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGroup(self):
        """Test Group"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Group()  # noqa: E501

        """
        No test json responses were defined for Group
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Group,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
