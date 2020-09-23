# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest
import warnings

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
global_api = None

class TestCellsChartAreaApi(unittest.TestCase):
    """ CellsChartAreaApi unit test stubs """

    def setUp(self):
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_chart_area_get_chart_area(self):
        """
        Test case for cells_chart_area_get_chart_area

        Get chart area info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_chart_area_get_chart_area(name, sheet_name,chartIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_chart_area_get_chart_area_border(self):
        """
        Test case for cells_chart_area_get_chart_area_border

        Get chart area border info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_chart_area_get_chart_area_border(name, sheet_name,chartIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_chart_area_get_chart_area_fill_format(self):
        """
        Test case for cells_chart_area_get_chart_area_fill_format

        Get chart area fill format info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_chart_area_get_chart_area_fill_format(name, sheet_name,chartIndex, folder = folder)
        self.assertEqual(result.code,200)
        pass


if __name__ == '__main__':
    unittest.main()
