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
from asposecellscloud.models import ListObject
from asposecellscloud.models import DataSorter
from asposecellscloud.models import CreatePivotTableRequest
global_api = None
class TestCellsListObjectsApi(unittest.TestCase):
    """ CellsListObjectsApi unit test stubs """

    def setUp(self):
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetAPPSID(),AuthUtil.GetAPPKey(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_list_objects_delete_worksheet_list_object(self):
        """
        Test case for cells_list_objects_delete_worksheet_list_object

        Delete worksheet list object by index
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet7'
        listObjectIndex = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_list_objects_delete_worksheet_list_object(name, sheet_name , listObjectIndex , folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_list_objects_delete_worksheet_list_objects(self):
        """
        Test case for cells_list_objects_delete_worksheet_list_objects

        Delete worksheet list objects
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet7'
        listObjectIndex = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_list_objects_delete_worksheet_list_objects(name, sheet_name,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_list_objects_get_worksheet_list_object(self):
        """
        Test case for cells_list_objects_get_worksheet_list_object

        Get worksheet list object info by index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet7'
        listObjectIndex = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_list_objects_get_worksheet_list_object(name, sheet_name,listObjectIndex,folder=folder)
        # self.assertEqual(result.code,200)
        pass

    def test_cells_list_objects_get_worksheet_list_objects(self):
        """
        Test case for cells_list_objects_get_worksheet_list_objects

        Get worksheet listobjects info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet7'
        listObjectIndex = 0         
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_list_objects_get_worksheet_list_objects(name, sheet_name,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_list_objects_post_worksheet_list_object(self):
        """
        Test case for cells_list_objects_post_worksheet_list_object

        Update  list object 
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet7'
        listObjectIndex = 0   
        listObject = ListObject()
        listObject.show_header_row = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_list_objects_post_worksheet_list_object(name, sheet_name,listObjectIndex,list_object=listObject,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_list_objects_post_worksheet_list_object_convert_to_range(self):
        """
        Test case for cells_list_objects_post_worksheet_list_object_convert_to_range

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet7'
        listObjectIndex = 0   
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_list_objects_post_worksheet_list_object_convert_to_range(name, sheet_name,listObjectIndex,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_list_objects_post_worksheet_list_object_sort_table(self):
        """
        Test case for cells_list_objects_post_worksheet_list_object_sort_table

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet7'
        listObjectIndex = 0   
        dataSorter = DataSorter()
        dataSorter.case_sensitive = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_list_objects_post_worksheet_list_object_sort_table(name, sheet_name,listObjectIndex,data_sorter=dataSorter,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table(self):
        """
        Test case for cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet7'
        listObjectIndex = 0 
        destsheetName = "Sheet2"  
        request = CreatePivotTableRequest(use_same_source = True)
        request.dest_cell_name = 'C1'
        request.name = 'testp'
        request.pivot_field_columns = [2]
        request.pivot_field_data = [0]
        request.pivot_field_rows = [1]
        request.source_data = '=Sheet2!A1:E8'
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_list_objects_post_worksheet_list_object_summarize_with_pivot_table(name, sheet_name,listObjectIndex,destsheetName, request=request,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_list_objects_put_worksheet_list_object(self):
        """
        Test case for cells_list_objects_put_worksheet_list_object

        Add a list object into worksheet.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet7'        
        startRow = 1      
        startColumn =1 
        endRow = 2 
        endColumn = 3         
        folder = "PythonTest"
        hasHeaders = True 
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_list_objects_put_worksheet_list_object(name, sheet_name,startRow,startColumn, endRow, endColumn,folder=folder,has_headers=hasHeaders)
        self.assertEqual(result.code,200)
        pass


if __name__ == '__main__':
    unittest.main()
