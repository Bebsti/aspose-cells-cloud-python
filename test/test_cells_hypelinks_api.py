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
from asposecellscloud.models import Hyperlink
global_api = None
class TestCellsHypelinksApi(unittest.TestCase):
    """ CellsHypelinksApi unit test stubs """

    def setUp(self):
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api



    def tearDown(self):
        pass

    def test_cells_hypelinks_delete_worksheet_hyperlink(self):
        """
        Test case for cells_hypelinks_delete_worksheet_hyperlink

        Delete worksheet hyperlink by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_hypelinks_delete_worksheet_hyperlink(name, sheet_name,hyperlinkIndex,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_hypelinks_delete_worksheet_hyperlinks(self):
        """
        Test case for cells_hypelinks_delete_worksheet_hyperlinks

        Delete all hyperlinks in worksheet.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_hypelinks_delete_worksheet_hyperlinks(name, sheet_name,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_hypelinks_get_worksheet_hyperlink(self):
        """
        Test case for cells_hypelinks_get_worksheet_hyperlink

        Get worksheet hyperlink by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_hypelinks_get_worksheet_hyperlink(name, sheet_name,hyperlinkIndex,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_hypelinks_get_worksheet_hyperlinks(self):
        """
        Test case for cells_hypelinks_get_worksheet_hyperlinks

        Get worksheet hyperlinks.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_hypelinks_get_worksheet_hyperlinks(name, sheet_name,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_hypelinks_post_worksheet_hyperlink(self):
        """
        Test case for cells_hypelinks_post_worksheet_hyperlink

        Update worksheet hyperlink by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        hyperlinkIndex = 0         
        folder = "PythonTest"
        hyperlink = Hyperlink()
        hyperlink.address = 'http://wwww.aspose.com'
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_hypelinks_post_worksheet_hyperlink(name, sheet_name, hyperlinkIndex , hyperlink = hyperlink , folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_hypelinks_put_worksheet_hyperlink(self):
        """
        Test case for cells_hypelinks_put_worksheet_hyperlink

        Add worksheet hyperlink.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        firstRow = 1      
        firstColumn =1 
        totalRows = 2 
        totalColumns = 3 
        address = 'http://www.aspose.com'    
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0)
        result = self.api.cells_hypelinks_put_worksheet_hyperlink(name, sheet_name,firstRow,firstColumn,totalRows,totalColumns,address,folder=folder)
        self.assertEqual(result.code,200)
        pass


if __name__ == '__main__':
    unittest.main()
