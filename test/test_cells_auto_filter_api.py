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
from asposecellscloud.apis.cells_auto_filter_api import CellsAutoFilterApi
import AuthUtil

from asposecellscloud.models import ColorFilterRequest
from asposecellscloud.models import Color
from asposecellscloud.models import CellsColor

class TestCellsAutoFilterApi(unittest.TestCase):
    """ CellsAutoFilterApi unit test stubs """

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.api_client = AuthUtil.GetApiClient()
        self.api = asposecellscloud.apis.cells_auto_filter_api.CellsAutoFilterApi(self.api_client)

    def tearDown(self):
        pass

    def test_cells_auto_filter_delete_worksheet_date_filter(self):
        """
        Test case for cells_auto_filter_delete_worksheet_date_filter

        Removes a date filter.             
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        fieldIndex = 0  
        dateTimeGroupingType ="Day"
        year = 2010
        month = 10
        day = 10
        hour = 10
        minute = 10
        second = 10
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_delete_worksheet_date_filter(name, sheet_name,fieldIndex, dateTimeGroupingType,year=year,month=month,day=day,hour=hour,minute=minute,second=second,folder=folder)
        pass

    def test_cells_auto_filter_delete_worksheet_filter(self):
        """
        Test case for cells_auto_filter_delete_worksheet_filter

        Delete a filter for a filter column.             
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        fieldIndex = 0  
        criteria ="Day"       
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_delete_worksheet_filter(name, sheet_name,fieldIndex, criteria=criteria,folder=folder)
        pass

    def test_cells_auto_filter_get_worksheet_auto_filter(self):
        """
        Test case for cells_auto_filter_get_worksheet_auto_filter

        Get Auto filter Description
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'     
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_get_worksheet_auto_filter(name, sheet_name, folder=folder)
        pass

    def test_cells_auto_filter_post_worksheet_auto_filter_refresh(self):
        """
        Test case for cells_auto_filter_post_worksheet_auto_filter_refresh

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'     
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_post_worksheet_auto_filter_refresh(name, sheet_name,folder=folder)
        pass

    def test_cells_auto_filter_post_worksheet_match_blanks(self):
        """
        Test case for cells_auto_filter_post_worksheet_match_blanks

        Match all blank cell in the list.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        fieldIndex = 0  
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_post_worksheet_match_blanks(name, sheet_name,fieldIndex, folder=folder)
        pass

    def test_cells_auto_filter_post_worksheet_match_non_blanks(self):
        """
        Test case for cells_auto_filter_post_worksheet_match_non_blanks

        Match all not blank cell in the list.             
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        fieldIndex = 0  
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_post_worksheet_match_non_blanks(name, sheet_name,fieldIndex, folder=folder)
        pass

    def test_cells_auto_filter_put_worksheet_color_filter(self):
        """
        Test case for cells_auto_filter_put_worksheet_color_filter

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        colorFilter = ColorFilterRequest()
        color = Color(0, 255, 0, 0)
        cellColor = CellsColor()
        cellColor.color = color
        colorFilter.foreground_color = cellColor
        colorFilter.pattern = 'Solid'
        matchBlanks = True
        refresh = True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_color_filter(name, sheet_name,range ,fieldIndex, color_filter = colorFilter , match_blanks = matchBlanks, refresh = refresh, folder = folder)
        pass

    def test_cells_auto_filter_put_worksheet_custom_filter(self):
        """
        Test case for cells_auto_filter_put_worksheet_custom_filter

        Filters a list with a custom criteria.             
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        operatorType1 = "LessOrEqual"
        criteria1 = "test"
        isAnd = True
        operatorType2 = "LessOrEqual"
        criteria2 = "test"
        matchBlanks = True
        refresh = True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_custom_filter(name, sheet_name,range ,fieldIndex, operatorType1 , criteria1,is_and=isAnd, operator_type2=operatorType2 , criteria2=criteria2,match_blanks=matchBlanks, refresh=refresh, folder=folder)
        pass

    def test_cells_auto_filter_put_worksheet_date_filter(self):
        """
        Test case for cells_auto_filter_put_worksheet_date_filter

        add date filter in worksheet 
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        dateTimeGroupingType ="Day"
        year = 2010
        month = 10
        day = 10
        hour = 10
        minute = 10
        second = 10
        matchBlanks =True
        refresh =True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_date_filter(name, sheet_name, range,fieldIndex, dateTimeGroupingType,year=year,month=month,day=day,hour=hour,minute=minute,second=second,match_blanks=matchBlanks, refresh=refresh,folder=folder)
        pass

    def test_cells_auto_filter_put_worksheet_dynamic_filter(self):
        """
        Test case for cells_auto_filter_put_worksheet_dynamic_filter

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        dynamicFilterType = "May"        
        matchBlanks =True
        refresh =True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_dynamic_filter(name, sheet_name, range,fieldIndex, dynamicFilterType,match_blanks=matchBlanks, refresh=refresh,folder=folder)
        pass

    def test_cells_auto_filter_put_worksheet_filter(self):
        """
        Test case for cells_auto_filter_put_worksheet_filter

        Adds a filter for a filter column.             
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        criteria ="May"        
        matchBlanks =True
        refresh =True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_filter(name, sheet_name, range,fieldIndex, criteria,match_blanks=matchBlanks, refresh=refresh,folder=folder)
        pass

    def test_cells_auto_filter_put_worksheet_filter_top10(self):
        """
        Test case for cells_auto_filter_put_worksheet_filter_top10

        Filter the top 10 item in the list
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        isTop =True
        isPercent =True
        itemCount =1        
        matchBlanks =True
        refresh =True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_filter_top10(name, sheet_name, range,fieldIndex, isTop,isPercent, itemCount,match_blanks= matchBlanks,refresh= refresh,folder=folder)
        pass

    def test_cells_auto_filter_put_worksheet_icon_filter(self):
        """
        Test case for cells_auto_filter_put_worksheet_icon_filter

        Adds an icon filter.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        range ='A1:C10'
        fieldIndex = 0  
        iconSetType ='None'
        iconId =1        
        matchBlanks =True
        refresh =True
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_auto_filter_put_worksheet_icon_filter(name, sheet_name, range,fieldIndex, iconSetType,iconId, match_blanks=matchBlanks, refresh=refresh,folder=folder)
        pass


if __name__ == '__main__':
    unittest.main()
