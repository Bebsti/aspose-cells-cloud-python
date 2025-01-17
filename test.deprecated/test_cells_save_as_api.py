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
from asposecellscloud.models import PdfSaveOptions
import AuthUtil
global_api = None

class TestCellsSaveAsApi(unittest.TestCase):
    """ CellsSaveAsApi unit test stubs """

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_cells_save_as_post_document_save_as(self):
        """
        Test case for cells_save_as_post_document_save_as

        Convert document and save result to storage.
        """
        name ='Book1.xlsx'    
        saveOptions = None
        newfilename = "newbook.xlsx"
        isAutoFitRows= True
        isAutoFitColumns= True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_save_as_post_document_save_as(name, save_options=saveOptions, newfilename=(folder +'/' + newfilename),is_auto_fit_rows=isAutoFitRows, is_auto_fit_columns=isAutoFitColumns,folder=folder)
        self.assertEqual(result.code,200)
        pass
    def test_cells_save_as_post_document_save_as_md(self):
        """
        Test case for cells_save_as_post_document_save_as

        Convert document and save result to storage.
        """
        name ='Book1.xlsx'    
        saveOptions = None
        newfilename = "newbook.md"
        isAutoFitRows= True
        isAutoFitColumns= True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_save_as_post_document_save_as(name, save_options=saveOptions, newfilename=(folder +'/' + newfilename),is_auto_fit_rows=isAutoFitRows, is_auto_fit_columns=isAutoFitColumns,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_save_as_post_document_save_as_pdf(self):
        """
        Test case for cells_save_as_post_document_save_as

        Convert document and save result to storage.
        """
        name ='Book1.xlsx'    
        saveOptions = PdfSaveOptions()
        saveOptions.OnePagePerSheet = True
        saveOptions.SaveFormat = "pdf"
        newfilename = "newbook.pdf"
        isAutoFitRows= True
        isAutoFitColumns= True
        folder = "PythonTest"
        result = AuthUtil.Ready(self.api, name, folder)
        self.assertTrue(len(result.uploaded)>0) 
        result = self.api.cells_save_as_post_document_save_as(name, save_options=saveOptions, newfilename=(folder +'/' + newfilename),is_auto_fit_rows=isAutoFitRows, is_auto_fit_columns=isAutoFitColumns,folder=folder)
        self.assertEqual(result.code,200)
        pass

    def test_cells_save_as_post_document_save_as_pdf_dropbox(self):
        """
        Test case for cells_save_as_post_document_save_as

        Convert document and save result to storage.
        """
        name ='Book1.xlsx'    
        saveOptions = PdfSaveOptions()
        saveOptions.OnePagePerSheet = True
        saveOptions.SaveFormat = "pdf"
        newfilename = "newbook.pdf"
        isAutoFitRows= True
        isAutoFitColumns= True
        folder = "PythonTest"
        storage = "DropBox"
        AuthUtil.Ready(self.api, name, folder)
        AuthUtil.Ready(self.api,name, folder, storage=storage)
        
        result = self.api.cells_save_as_post_document_save_as(name, save_options=saveOptions, newfilename=(folder +'/' + newfilename),is_auto_fit_rows=isAutoFitRows, is_auto_fit_columns=isAutoFitColumns,folder=folder, storage_name=storage)
        self.assertEqual(result.code,200)
        pass

    def test_cells_save_as_post_document_save_as_pdf_extend(self):
        """
        Test case for cells_save_as_post_document_save_as

        Convert document and save result to storage.
        """
        name ='Book1.xlsx'    
        saveOptions = PdfSaveOptions()
        saveOptions.OnePagePerSheet = True
        saveOptions.SaveFormat = "pdf"
        newfilename = "newbook.pdf"
        isAutoFitRows= True
        isAutoFitColumns= True
        folder = "PythonTest"
        AuthUtil.Ready(self.api, name, folder)
        
        result = self.api.cells_save_as_post_document_save_as(name, save_options=saveOptions, newfilename=(folder +'/' + newfilename),is_auto_fit_rows=isAutoFitRows, is_auto_fit_columns=isAutoFitColumns,folder=folder,  extended_query_parameters ={"OnePagePerSheet":"false"})
        self.assertEqual(result.code,200)
        pass
if __name__ == '__main__':
    unittest.main()
