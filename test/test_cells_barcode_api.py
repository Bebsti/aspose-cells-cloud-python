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
import shutil

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)) + "/..")
sys.path.append(ABSPATH)
import asposecellscloud
from asposecellscloud.rest import ApiException
from asposecellscloud.apis.cells_api import CellsApi
import AuthUtil
from asposecellscloud.models import BarcodeResponseList
from asposecellscloud.models import BarcodeResponse
global_api = None

class TestCellsBarcodeApi(unittest.TestCase):
    """ CellsWorkbookApi unit test stubs """

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global global_api
        if global_api is None:
           global_api = asposecellscloud.apis.cells_api.CellsApi(AuthUtil.GetClientId(),AuthUtil.GetClientSecret(),"v3.0",AuthUtil.GetBaseUrl())
        self.api = global_api

    def tearDown(self):
        pass

    def test_get_barcode(self):
        name ='Book1.xlsx'    
        folder = "PythonTest"
        AuthUtil.Ready(self.api, name, folder)
        
        result = self.api.cells_picture_get_extract_barcodes(name, 'Sheet8',0,folder=folder)
        self.assertIsNotNone(result)
        pass


if __name__ == '__main__':
    unittest.main()