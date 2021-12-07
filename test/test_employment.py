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
from MergeHRISClient.model.employment import Employment
from MergeHRISClient.api_client import ApiClient


class TestEmployment(unittest.TestCase):
    """Employment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployment(self):
        """Test Employment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Employment()  # noqa: E501

        """
        No test json responses were defined for Employment
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Employment,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
