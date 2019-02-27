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
from asposecellscloud.apis.cells_pictures_api import CellsPicturesApi
import AuthUtil
from asposecellscloud.models import Picture

class TestCellsPicturesApi(unittest.TestCase):
    """ CellsPicturesApi unit test stubs """

    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        self.api_client = AuthUtil.GetApiClient()
        self.api = asposecellscloud.apis.cells_pictures_api.CellsPicturesApi(self.api_client)

    def tearDown(self):
        pass

    def test_cells_pictures_delete_worksheet_pictures(self):
        """
        Test case for cells_pictures_delete_worksheet_pictures

        Delete all pictures in worksheet.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        index = 0         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pictures_delete_worksheet_pictures(name, sheet_name,folder=folder)
        pass

    def test_cells_pictures_delete_worksheet_picture(self):
        """
        Test case for cells_pictures_delete_worksheet_picture

        Delete a picture object in worksheet
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        pictureIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pictures_delete_worksheet_picture(name, sheet_name,pictureIndex,folder=folder)
        pass

    def test_cells_pictures_get_worksheet_picture(self):
        """
        Test case for cells_pictures_get_worksheet_picture

        GRead worksheet picture by number.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        pictureIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pictures_get_worksheet_picture(name, sheet_name,pictureIndex,folder=folder)
        pass

    def test_cells_pictures_get_worksheet_picture_format(self):
        """
        Test case for cells_pictures_get_worksheet_picture_format

        GRead worksheet picture by number.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        pictureIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pictures_get_worksheet_picture(name, sheet_name,pictureIndex,format="png", folder=folder)
        pass

    def test_cells_pictures_get_worksheet_pictures(self):
        """
        Test case for cells_pictures_get_worksheet_pictures

        Read worksheet pictures.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        pictureIndex = 0         
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pictures_get_worksheet_pictures(name, sheet_name,folder=folder)
        pass

    def test_cells_pictures_post_worksheet_picture(self):
        """
        Test case for cells_pictures_post_worksheet_picture

        Update worksheet picture by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'
        pictureIndex = 0   
        picture = Picture()
        picture.left = 10
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pictures_post_worksheet_picture(name, sheet_name, pictureIndex , picture=picture,folder=folder)
        pass

    def test_cells_pictures_put_worksheet_add_picture(self):
        """
        Test case for cells_pictures_put_worksheet_add_picture

        Add a new worksheet picture.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet6'       
        picture = None
        upperLeftRow = 1   
        upperLeftColumn = 1   
        lowerRightRow = 10   
        lowerRightColumn = 10   
        picturePath = 'WaterMark.png'        
        folder = "Temp"
        AuthUtil.Ready(name, folder)
        result = self.api.cells_pictures_put_worksheet_add_picture(name, sheet_name, picture=picture, upper_left_row=upperLeftRow,upper_left_column=upperLeftColumn,lower_right_row=lowerRightRow,lower_right_column=lowerRightColumn,picture_path=picturePath, folder=folder)
        pass


if __name__ == '__main__':
    unittest.main()
