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
from MergeHRISClient.model.debug_mode_log import DebugModeLog
from MergeHRISClient.model.employee import Employee
from MergeHRISClient.model.error_validation_problem import ErrorValidationProblem
from MergeHRISClient.model.warning_validation_problem import WarningValidationProblem
globals()['DebugModeLog'] = DebugModeLog
globals()['Employee'] = Employee
globals()['ErrorValidationProblem'] = ErrorValidationProblem
globals()['WarningValidationProblem'] = WarningValidationProblem
from MergeHRISClient.model.employee_response import EmployeeResponse
from MergeHRISClient.api_client import ApiClient


class TestEmployeeResponse(unittest.TestCase):
    """EmployeeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployeeResponse(self):
        """Test EmployeeResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EmployeeResponse()  # noqa: E501

        """
        No test json responses were defined for EmployeeResponse
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (EmployeeResponse,), False)

        assert deserialized is not None

        assert deserialized.model is not None
        assert deserialized.warnings is not None
        assert deserialized.errors is not None


if __name__ == '__main__':
    unittest.main()
