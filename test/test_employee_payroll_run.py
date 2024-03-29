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
from MergeHRISClient.model.deduction import Deduction
from MergeHRISClient.model.earning import Earning
from MergeHRISClient.model.remote_data import RemoteData
from MergeHRISClient.model.tax import Tax
globals()['Deduction'] = Deduction
globals()['Earning'] = Earning
globals()['RemoteData'] = RemoteData
globals()['Tax'] = Tax
from MergeHRISClient.model.employee_payroll_run import EmployeePayrollRun
from MergeHRISClient.api_client import ApiClient


class TestEmployeePayrollRun(unittest.TestCase):
    """EmployeePayrollRun unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployeePayrollRun(self):
        """Test EmployeePayrollRun"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EmployeePayrollRun()  # noqa: E501

        """
        No test json responses were defined for EmployeePayrollRun
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (EmployeePayrollRun,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
