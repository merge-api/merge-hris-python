# coding: utf-8

"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import MergeHRISClient
from MergeHRISClient.models.paginated_time_off_list import PaginatedTimeOffList  # noqa: E501
from MergeHRISClient.rest import ApiException

class TestPaginatedTimeOffList(unittest.TestCase):
    """PaginatedTimeOffList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedTimeOffList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeHRISClient.models.paginated_time_off_list.PaginatedTimeOffList()  # noqa: E501
        if include_optional :
            return PaginatedTimeOffList(
                next = '0', 
                previous = '0', 
                results = [
                    MergeHRISClient.models.time_off.TimeOff(
                        id = '0', 
                        origin_id = '19202938', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        employee = 'd2f972d0-2526-434b-9409-4c3b468e08f0', 
                        approver = '9efbc633-3387-4306-aa55-e2c635e6bb4f', 
                        status = APPROVED, 
                        employee_note = 'Trip to Iowa', 
                        units = DAYS, 
                        amount = 13, 
                        request_type = VACATION, )
                    ]
            )
        else :
            return PaginatedTimeOffList(
        )

    def testPaginatedTimeOffList(self):
        """Test PaginatedTimeOffList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
