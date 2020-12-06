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
from asposecellscloud.models import ProtectSheetParameter
from asposecellscloud.models import AutoFitterOptions
from asposecellscloud.models import CopyOptions
from asposecellscloud.models import WorksheetMovingRequest
from asposecellscloud.models import Worksheet
from asposecellscloud.models import Comment
from asposecellscloud.models import DataSorter
from asposecellscloud.models import ProtectSheetParameter
global_api = None

class TestCellsWorksheetsApi(unittest.TestCase):
    """ CellsWorksheetsApi unit test stubs """

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_worksheets_delete_unprotect_worksheet(self):
        """
        Test case for cells_worksheets_delete_unprotect_worksheet

        Unprotect worksheet.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'
        protectParameter = ProtectSheetParameter()
        protectParameter.password = "12345"
        protectParameter.protection_type = "All"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_delete_unprotect_worksheet(name, sheet_name, protect_parameter=protectParameter, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_delete_worksheet_background(self):
        """
        Test case for cells_worksheets_delete_worksheet_background

        Set worksheet background image.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'       
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_delete_worksheet_background(name, sheet_name, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_delete_worksheet_comment(self):
        """
        Test case for cells_worksheets_delete_worksheet_comment

        Delete worksheet's cell comment.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        cellName = "C1"      
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_delete_worksheet_comment(name, sheet_name, cellName, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_delete_worksheet_comments(self):
        """
        Test case for cells_worksheets_delete_worksheet_comments

        Delete all comments for worksheet.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'   
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_delete_worksheet_comments(name, sheet_name,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_delete_worksheet(self):
        """
        Test case for cells_worksheets_delete_worksheet

        Delete worksheet.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'   
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_delete_worksheet(name, sheet_name,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_delete_worksheet_freeze_panes(self):
        """
        Test case for cells_worksheets_delete_worksheet_freeze_panes

        Unfreeze panes
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        row = 1
        column = 1
        freezedRows = 2
        freezedColumns = 2
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_delete_worksheet_freeze_panes(name, sheet_name, row, column, freezedRows, freezedColumns, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_get_named_ranges(self):
        """
        Test case for cells_worksheets_get_named_ranges

        Read worksheets ranges info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1'   
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_get_named_ranges(name,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_get_worksheet(self):
        """
        Test case for cells_worksheets_get_worksheet

        Read worksheet info or export.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        verticalResolution =100  
        horizontalResolution =90
        format = "png"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_get_worksheet(name, sheet_name, format=format, vertical_resolution=verticalResolution, horizontal_resolution=horizontalResolution, _preload_content=False, folder=folder)
        # self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_get_worksheet_calculate_formula(self):
        """
        Test case for cells_worksheets_get_worksheet_calculate_formula

        Calculate formula value.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        formula = "=NOW()"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_get_worksheet_calculate_formula(name, sheet_name, formula, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_get_worksheet_comment(self):
        """
        Test case for cells_worksheets_get_worksheet_comment

        Get worksheet comment by cell name.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        cellName = "B3"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_get_worksheet_comment(name, sheet_name, cellName, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_get_worksheet_comments(self):
        """
        Test case for cells_worksheets_get_worksheet_comments

        Get worksheet comments.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        cellName = "B3"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_get_worksheet_comments(name, sheet_name, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_get_worksheet_merged_cell(self):
        """
        Test case for cells_worksheets_get_worksheet_merged_cell

        Get worksheet merged cell by its index.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        mergedCellIndex =1
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_get_worksheet_merged_cell(name, sheet_name,mergedCellIndex, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_get_worksheet_merged_cells(self):
        """
        Test case for cells_worksheets_get_worksheet_merged_cells

        Get worksheet merged cells.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_get_worksheet_merged_cells(name, sheet_name, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_get_worksheet_text_items(self):
        """
        Test case for cells_worksheets_get_worksheet_text_items

        Get worksheet text items.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_get_worksheet_text_items(name, sheet_name, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_get_worksheets(self):
        """
        Test case for cells_worksheets_get_worksheets

        Read worksheets info.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_get_worksheets(name,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_autofit_worksheet_columns(self):
        """
        Test case for cells_worksheets_post_autofit_worksheet_columns

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        firstColumn = 1
        lastColumn = 10
        autoFitterOptions = None
        firstRow = 1
        lastRow = 19
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_autofit_worksheet_columns(name, sheet_name,firstColumn, lastColumn, auto_fitter_options=autoFitterOptions, first_row=firstRow, last_row=lastRow,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_autofit_worksheet_row(self):
        """
        Test case for cells_worksheets_post_autofit_worksheet_row

        
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        rowIndex =1
        firstColumn = 1
        lastColumn = 10
        autoFitterOptions = AutoFitterOptions(True, True, True)
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_autofit_worksheet_row(name, sheet_name, rowIndex,firstColumn, lastColumn, auto_fitter_options=autoFitterOptions,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_autofit_worksheet_rows(self):
        """
        Test case for cells_worksheets_post_autofit_worksheet_rows

        Autofit worksheet rows.
        """
        name ='Book1.xlsx'
        sheet_name ='Sheet1' 
        startRow =1
        endRow = 1
        onlyAuto = True
        autoFitterOptions = AutoFitterOptions(True, True, True)
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_autofit_worksheet_rows(name, sheet_name, auto_fitter_options = autoFitterOptions, start_row=startRow,end_row=endRow, only_auto=onlyAuto, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_copy_worksheet(self):
        """
        Test case for cells_worksheets_post_copy_worksheet

        
        """
        name = "NewCopy.xlsx"
        sheet_name ='Sheet5' 
        sourceSheet ='Sheet6' 
        options = CopyOptions()
        options.column_character_width = True
        sourceWorkbook = 'Book1.xlsx'
        sourceFolder = "PythonTest"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_copy_worksheet(name, sheet_name,  sourceSheet, options=options,source_workbook=sourceWorkbook, source_folder=sourceFolder, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_move_worksheet(self):
        """
        Test case for cells_worksheets_post_move_worksheet

        Move worksheet.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        moving = WorksheetMovingRequest()
        moving.destination_worksheet = 'Sheet3'
        moving.position = "after"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_move_worksheet(name, sheet_name,  moving=moving,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_rename_worksheet(self):
        """
        Test case for cells_worksheets_post_rename_worksheet

        Rename worksheet
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        newname = "renametest"     
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_rename_worksheet(name, sheet_name,  newname,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_update_worksheet_property(self):
        """
        Test case for cells_worksheets_post_update_worksheet_property

        Update worksheet property
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        sheet = Worksheet(index=1, is_protected=True)
        sheet.is_gridlines_visible = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_update_worksheet_property(name, sheet_name, sheet = sheet,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_update_worksheet_zoom(self):
        """
        Test case for cells_worksheets_post_update_worksheet_zoom

        
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        value = 1
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_update_worksheet_zoom(name, sheet_name,  value,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_worksheet_comment(self):
        """
        Test case for cells_worksheets_post_worksheet_comment

        Update worksheet's cell comment.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        cellName = "B3"
        comment = Comment()
        comment.author = "Roy"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_worksheet_comment(name, sheet_name,  cellName, comment=comment, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_worksheet_text_search(self):
        """
        Test case for cells_worksheets_post_worksheet_text_search

        Search text.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        text = "B3"       
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_worksheet_text_search(name, sheet_name,  text,  folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_worksheet_range_sort(self):
        """
        Test case for cells_worksheets_post_worksheet_range_sort

        Sort worksheet range.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        cellArea = 'A1:E10'   
        dataSorter = DataSorter()
        dataSorter.case_sensitive = True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_worksheet_range_sort(name, sheet_name,  cellArea, data_sorter=dataSorter, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_post_worsheet_text_replace(self):
        """
        Test case for cells_worksheets_post_worsheet_text_replace

        Replace text.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        oldValue = "1234"    
        newValue = "wewew4"  
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_post_worsheet_text_replace(name, sheet_name,  oldValue, newValue, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_put_add_new_worksheet(self):
        """
        Test case for cells_worksheets_put_add_new_worksheet

        Add new worksheet.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        position = 1  
        sheettype = "VB" 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_put_add_new_worksheet(name, sheet_name,  position=position, sheettype=sheettype, folder=folder)
        self.assertEqual(result.code,201)
        pass

    def test_cells_worksheets_put_change_visibility_worksheet(self):
        """
        Test case for cells_worksheets_put_change_visibility_worksheet

        Change worksheet visibility.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        isVisible = True
        sheettype = "VB" 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_put_change_visibility_worksheet(name, sheet_name,  isVisible, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_put_protect_worksheet(self):
        """
        Test case for cells_worksheets_put_protect_worksheet

        Protect worksheet.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        protectParameter = ProtectSheetParameter()
        protectParameter.password = "12345"
        protectParameter.protection_type = "All"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_put_protect_worksheet(name, sheet_name, protect_parameter= protectParameter, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_put_worksheet_background(self):
        """
        Test case for cells_worksheets_put_worksheet_background

        Set worksheet background image.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        isVisible = True
        sheettype = "VB" 
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        fullfilename = os.path.dirname(os.path.realpath(__file__)) + "/../TestData/" + "WaterMark.png"
        f = open(fullfilename, 'rb')
        png = f.read()
        f.close()
        result = self.api.cells_worksheets_put_worksheet_background(name, sheet_name, png, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_put_worksheet_comment(self):
        """
        Test case for cells_worksheets_put_worksheet_comment

        Add worksheet's cell comment.
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        cellName = "C1"
        comment = Comment()
        comment.author = "Roy"
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_put_worksheet_comment(name, sheet_name,  cellName, comment=comment, folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_worksheets_put_worksheet_freeze_panes(self):
        """
        Test case for cells_worksheets_put_worksheet_freeze_panes

        Set freeze panes
        """
        name = "Book1.xlsx"
        sheet_name ='Sheet1' 
        row = 1
        column = 1
        freezedRows = 4
        freezedColumns = 5
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_worksheets_put_worksheet_freeze_panes(name, sheet_name,  row, column,freezedRows,freezedColumns, folder=folder)
        self.assertEqual(result.code,200)
        pass


if __name__ == '__main__':
    unittest.main()
