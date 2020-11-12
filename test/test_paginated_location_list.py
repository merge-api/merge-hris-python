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
from MergeHRISClient.models.paginated_location_list import PaginatedLocationList  # noqa: E501
from MergeHRISClient.rest import ApiException

class TestPaginatedLocationList(unittest.TestCase):
    """PaginatedLocationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedLocationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MergeHRISClient.models.paginated_location_list.PaginatedLocationList()  # noqa: E501
        if include_optional :
            return PaginatedLocationList(
                next = '0', 
                previous = '0', 
                results = [
                    MergeHRISClient.models.location.Location(
                        id = '0', 
                        origin_id = '93018402', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        phone_number = '4153922938', 
                        street_1 = '211 Valencia St', 
                        street_2 = 'Apt 95', 
                        city = 'San Francisco', 
                        state = CA, 
                        zip_code = '94103', 
                        country = USA, 
                        linked_account_id = '0', )
                    ]
            )
        else :
            return PaginatedLocationList(
        )

    def testPaginatedLocationList(self):
        """Test PaginatedLocationList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
