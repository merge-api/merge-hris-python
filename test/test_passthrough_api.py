"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergeHRISClient
from MergeHRISClient.api.passthrough_api import PassthroughApi  # noqa: E501


class TestPassthroughApi(unittest.TestCase):
    """PassthroughApi unit test stubs"""

    def setUp(self):
        self.api = PassthroughApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_passthrough_create(self):
        """Test case for passthrough_create

        """
        pass


if __name__ == '__main__':
    unittest.main()
