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
from asposecellscloud.models import Chart
from asposecellscloud.models import Legend
from asposecellscloud.models import Title
global_api = None
class TestCellsChartsApi(unittest.TestCase):
    """ CellsChartsApi unit test stubs """

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api


    def tearDown(self):
        pass

    def test_cells_charts_delete_worksheet_chart_legend(self):
        """
        Test case for cells_charts_delete_worksheet_chart_legend

        Hide legend in chart
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 1  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_delete_worksheet_chart_legend(name, sheet_name,chartIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_delete_worksheet_chart_title(self):
        """
        Test case for cells_charts_delete_worksheet_chart_title

        Hide title in chart
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 1  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_delete_worksheet_chart_title(name, sheet_name,chartIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_delete_worksheet_clear_charts(self):
        """
        Test case for cells_charts_delete_worksheet_clear_charts

        Clear the charts.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 1  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_delete_worksheet_clear_charts(name, sheet_name, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_delete_worksheet_delete_chart(self):
        """
        Test case for cells_charts_delete_worksheet_delete_chart

        Delete worksheet chart by index.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_delete_worksheet_delete_chart(name, sheet_name,chartIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_get_worksheet_chart(self):
        """
        Test case for cells_charts_get_worksheet_chart

        Get chart info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        format = 'png'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_get_worksheet_chart(name, sheet_name, chartIndex, format=format, folder=folder)
        # self.assertEqual(result.Code,200)
        pass

    def test_cells_charts_get_worksheet_chart_legend(self):
        """
        Test case for cells_charts_get_worksheet_chart_legend

        Get chart legend
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_get_worksheet_chart_legend(name, sheet_name,chartIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_get_worksheet_chart_title(self):
        """
        Test case for cells_charts_get_worksheet_chart_title

        Get chart title
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_get_worksheet_chart_title(name, sheet_name,chartIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_get_worksheet_charts(self):
        """
        Test case for cells_charts_get_worksheet_charts

        Get worksheet charts info.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_get_worksheet_charts(name, sheet_name, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_post_worksheet_chart(self):
        """
        Test case for cells_charts_post_worksheet_chart

        Update chart propreties
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        chart = Chart()
        chart.auto_scaling = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_post_worksheet_chart(name, sheet_name, chartIndex , chart=chart , folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_post_worksheet_chart_legend(self):
        """
        Test case for cells_charts_post_worksheet_chart_legend

        Update chart legend
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        legend = Legend()
        legend.width = 10
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_post_worksheet_chart_legend(name, sheet_name, chartIndex , legend=legend , folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_post_worksheet_chart_title(self):
        """
        Test case for cells_charts_post_worksheet_chart_title

        Update chart title
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        title = Title()
        title.text = "test"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_post_worksheet_chart_title(name, sheet_name, chartIndex , title = title, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_put_worksheet_add_chart(self):
        """
        Test case for cells_charts_put_worksheet_add_chart

        Add new chart to worksheet.
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartType = 'Pie'  
        upperLeftRow = 5  
        upperLeftColumn = 5 
        lowerRightRow = 10 
        lowerRightColumn = 10 
        area =  "C7:D11" 
        isVertical = True  
        categoryData = None  
        isAutoGetSerialName = 'False'  
        title = None  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_put_worksheet_add_chart(name, sheet_name, chartType , upper_left_row=upperLeftRow , upper_left_column=upperLeftColumn, lower_right_row=lowerRightRow, lower_right_column=lowerRightColumn, area=area, is_vertical=isVertical, category_data=categoryData,is_auto_get_serial_name=isAutoGetSerialName,title=title, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_put_worksheet_chart_legend(self):
        """
        Test case for cells_charts_put_worksheet_chart_legend

        Show legend in chart
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_put_worksheet_chart_legend(name, sheet_name, chartIndex , folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_charts_put_worksheet_chart_title(self):
        """
        Test case for cells_charts_put_worksheet_chart_title

        Add chart title / Set chart title visible
        """
        name ='myDocument.xlsx'
        sheet_name ='Sheet3'
        chartIndex = 0  
        title = Title()
        title.text = "test"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_charts_put_worksheet_chart_title(name, sheet_name, chartIndex ,title=title, folder=folder)
        self.assertEqual(result.code,200)
        pass


if __name__ == '__main__':
    unittest.main()
