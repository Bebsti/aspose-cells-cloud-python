# coding: utf-8
"""
<copyright company="Aspose" file="GetWorksheetColumnRequest.cs">
  Copyright (c) 2023 Aspose.Cells Cloud
</copyright>
<summary>
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
</summary>
"""

import json

from six import iteritems
from asposecellscloud import *
from asposecellscloud.models import *
from asposecellscloud.requests import *
from six.moves.urllib.parse import quote

class GetWorksheetColumnRequest(object):

    def __init__(self , name ,sheet_name ,column_index ,folder =None ,storage_name =None ):
        self.name = name 
        self.sheet_name = sheet_name 
        self.column_index = column_index 
        self.folder = folder 
        self.storage_name = storage_name 
    def create_http_request(self, api_client):

        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_worksheet_column`")


        # verify the required parameter 'sheet_name' is set
        if self.sheet_name is None:
            raise ValueError("Missing the required parameter `sheet_name` when calling `get_worksheet_column`")


        # verify the required parameter 'column_index' is set
        if self.column_index is None:
            raise ValueError("Missing the required parameter `column_index` when calling `get_worksheet_column`")


        collection_formats = {}

        path_params = {}
        if self.name is not None:
            path_params['name'] = self.name
        if self.sheet_name is not None:
            path_params['sheetName'] = self.sheet_name
        if self.column_index is not None:
            path_params['columnIndex'] = self.column_index
        query_params = []
        if self.folder is not None:
            query_params.append(('folder',self.folder ))
        if self.storage_name is not None:
            query_params.append(('storageName',self.storage_name ))

        header_params = {}

        form_params = []
        local_var_files = {}
        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = api_client.\
            select_header_content_type(['application/json'])


        # Authentication setting
        auth_settings = []
        resource_path = "/cells/{name}/worksheets/{sheetName}/cells/columns/{columnIndex}"
        # path parameters
        if path_params:
            path_params = api_client.sanitize_for_serialization(path_params)
            path_params = api_client.parameters_to_tuples(path_params, collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace('{%s}' % k, quote(str(v), safe='/'))
        return {
                "method": "GET",
                "path":resource_path,
                "query_params": query_params,
                "header_params": header_params,
                "form_params": form_params,
                "files":local_var_files,
                "auth_settings":auth_settings,
                "body": body_params,
                "collection_formats": collection_formats,
                "response_type": 'ColumnResponse'  
        }

