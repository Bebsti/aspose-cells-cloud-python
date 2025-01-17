# coding: utf-8

"""
Copyright (c) 2022 Aspose.Cells Cloud
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
"""


from pprint import pformat
from six import iteritems
import re
from . import SaveOptions

class MHtmlSaveOptions(SaveOptions):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'attached_files_directory': 'str',
        'attached_files_url_prefix': 'str',
        'encoding': 'str',
        'export_active_worksheet_only': 'bool',
        'export_chart_image_format': 'str',
        'export_images_as_base64': 'bool',
        'hidden_col_display_type': 'str',
        'hidden_row_display_type': 'str',
        'html_cross_string_type': 'str',
        'is_exp_image_to_temp_dir': 'bool',
        'page_title': 'str',
        'parse_html_tag_in_cell': 'bool'
    }

    attribute_map = {
        'attached_files_directory': 'AttachedFilesDirectory',
        'attached_files_url_prefix': 'AttachedFilesUrlPrefix',
        'encoding': 'Encoding',
        'export_active_worksheet_only': 'ExportActiveWorksheetOnly',
        'export_chart_image_format': 'ExportChartImageFormat',
        'export_images_as_base64': 'ExportImagesAsBase64',
        'hidden_col_display_type': 'HiddenColDisplayType',
        'hidden_row_display_type': 'HiddenRowDisplayType',
        'html_cross_string_type': 'HtmlCrossStringType',
        'is_exp_image_to_temp_dir': 'IsExpImageToTempDir',
        'page_title': 'PageTitle',
        'parse_html_tag_in_cell': 'ParseHtmlTagInCell'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(MHtmlSaveOptions.swagger_types, **SaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(MHtmlSaveOptions.attribute_map, **SaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, attached_files_directory=None, attached_files_url_prefix=None, encoding=None, export_active_worksheet_only=None, export_chart_image_format=None, export_images_as_base64=None, hidden_col_display_type=None, hidden_row_display_type=None, html_cross_string_type=None, is_exp_image_to_temp_dir=None, page_title=None, parse_html_tag_in_cell=None, **kw):
        super(MHtmlSaveOptions, self).__init__(**kw)
		    
        """
        MHtmlSaveOptions - a model defined in Swagger
        """

        self.container['attached_files_directory'] = None
        self.container['attached_files_url_prefix'] = None
        self.container['encoding'] = None
        self.container['export_active_worksheet_only'] = None
        self.container['export_chart_image_format'] = None
        self.container['export_images_as_base64'] = None
        self.container['hidden_col_display_type'] = None
        self.container['hidden_row_display_type'] = None
        self.container['html_cross_string_type'] = None
        self.container['is_exp_image_to_temp_dir'] = None
        self.container['page_title'] = None
        self.container['parse_html_tag_in_cell'] = None

        if attached_files_directory is not None:
          self.attached_files_directory = attached_files_directory
        if attached_files_url_prefix is not None:
          self.attached_files_url_prefix = attached_files_url_prefix
        if encoding is not None:
          self.encoding = encoding
        if export_active_worksheet_only is not None:
          self.export_active_worksheet_only = export_active_worksheet_only
        if export_chart_image_format is not None:
          self.export_chart_image_format = export_chart_image_format
        if export_images_as_base64 is not None:
          self.export_images_as_base64 = export_images_as_base64
        if hidden_col_display_type is not None:
          self.hidden_col_display_type = hidden_col_display_type
        if hidden_row_display_type is not None:
          self.hidden_row_display_type = hidden_row_display_type
        if html_cross_string_type is not None:
          self.html_cross_string_type = html_cross_string_type
        if is_exp_image_to_temp_dir is not None:
          self.is_exp_image_to_temp_dir = is_exp_image_to_temp_dir
        if page_title is not None:
          self.page_title = page_title
        if parse_html_tag_in_cell is not None:
          self.parse_html_tag_in_cell = parse_html_tag_in_cell

    @property
    def attached_files_directory(self):
        """
        Gets the attached_files_directory of this MHtmlSaveOptions.

        :return: The attached_files_directory of this MHtmlSaveOptions.
        :rtype: str
        """
        return self.container['attached_files_directory']

    @attached_files_directory.setter
    def attached_files_directory(self, attached_files_directory):
        """
        Sets the attached_files_directory of this MHtmlSaveOptions.

        :param attached_files_directory: The attached_files_directory of this MHtmlSaveOptions.
        :type: str
        """

        self.container['attached_files_directory'] = attached_files_directory

    @property
    def attached_files_url_prefix(self):
        """
        Gets the attached_files_url_prefix of this MHtmlSaveOptions.

        :return: The attached_files_url_prefix of this MHtmlSaveOptions.
        :rtype: str
        """
        return self.container['attached_files_url_prefix']

    @attached_files_url_prefix.setter
    def attached_files_url_prefix(self, attached_files_url_prefix):
        """
        Sets the attached_files_url_prefix of this MHtmlSaveOptions.

        :param attached_files_url_prefix: The attached_files_url_prefix of this MHtmlSaveOptions.
        :type: str
        """

        self.container['attached_files_url_prefix'] = attached_files_url_prefix

    @property
    def encoding(self):
        """
        Gets the encoding of this MHtmlSaveOptions.

        :return: The encoding of this MHtmlSaveOptions.
        :rtype: str
        """
        return self.container['encoding']

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this MHtmlSaveOptions.

        :param encoding: The encoding of this MHtmlSaveOptions.
        :type: str
        """

        self.container['encoding'] = encoding

    @property
    def export_active_worksheet_only(self):
        """
        Gets the export_active_worksheet_only of this MHtmlSaveOptions.

        :return: The export_active_worksheet_only of this MHtmlSaveOptions.
        :rtype: bool
        """
        return self.container['export_active_worksheet_only']

    @export_active_worksheet_only.setter
    def export_active_worksheet_only(self, export_active_worksheet_only):
        """
        Sets the export_active_worksheet_only of this MHtmlSaveOptions.

        :param export_active_worksheet_only: The export_active_worksheet_only of this MHtmlSaveOptions.
        :type: bool
        """

        self.container['export_active_worksheet_only'] = export_active_worksheet_only

    @property
    def export_chart_image_format(self):
        """
        Gets the export_chart_image_format of this MHtmlSaveOptions.

        :return: The export_chart_image_format of this MHtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_chart_image_format']

    @export_chart_image_format.setter
    def export_chart_image_format(self, export_chart_image_format):
        """
        Sets the export_chart_image_format of this MHtmlSaveOptions.

        :param export_chart_image_format: The export_chart_image_format of this MHtmlSaveOptions.
        :type: str
        """

        self.container['export_chart_image_format'] = export_chart_image_format

    @property
    def export_images_as_base64(self):
        """
        Gets the export_images_as_base64 of this MHtmlSaveOptions.

        :return: The export_images_as_base64 of this MHtmlSaveOptions.
        :rtype: bool
        """
        return self.container['export_images_as_base64']

    @export_images_as_base64.setter
    def export_images_as_base64(self, export_images_as_base64):
        """
        Sets the export_images_as_base64 of this MHtmlSaveOptions.

        :param export_images_as_base64: The export_images_as_base64 of this MHtmlSaveOptions.
        :type: bool
        """

        self.container['export_images_as_base64'] = export_images_as_base64

    @property
    def hidden_col_display_type(self):
        """
        Gets the hidden_col_display_type of this MHtmlSaveOptions.

        :return: The hidden_col_display_type of this MHtmlSaveOptions.
        :rtype: str
        """
        return self.container['hidden_col_display_type']

    @hidden_col_display_type.setter
    def hidden_col_display_type(self, hidden_col_display_type):
        """
        Sets the hidden_col_display_type of this MHtmlSaveOptions.

        :param hidden_col_display_type: The hidden_col_display_type of this MHtmlSaveOptions.
        :type: str
        """

        self.container['hidden_col_display_type'] = hidden_col_display_type

    @property
    def hidden_row_display_type(self):
        """
        Gets the hidden_row_display_type of this MHtmlSaveOptions.

        :return: The hidden_row_display_type of this MHtmlSaveOptions.
        :rtype: str
        """
        return self.container['hidden_row_display_type']

    @hidden_row_display_type.setter
    def hidden_row_display_type(self, hidden_row_display_type):
        """
        Sets the hidden_row_display_type of this MHtmlSaveOptions.

        :param hidden_row_display_type: The hidden_row_display_type of this MHtmlSaveOptions.
        :type: str
        """

        self.container['hidden_row_display_type'] = hidden_row_display_type

    @property
    def html_cross_string_type(self):
        """
        Gets the html_cross_string_type of this MHtmlSaveOptions.

        :return: The html_cross_string_type of this MHtmlSaveOptions.
        :rtype: str
        """
        return self.container['html_cross_string_type']

    @html_cross_string_type.setter
    def html_cross_string_type(self, html_cross_string_type):
        """
        Sets the html_cross_string_type of this MHtmlSaveOptions.

        :param html_cross_string_type: The html_cross_string_type of this MHtmlSaveOptions.
        :type: str
        """

        self.container['html_cross_string_type'] = html_cross_string_type

    @property
    def is_exp_image_to_temp_dir(self):
        """
        Gets the is_exp_image_to_temp_dir of this MHtmlSaveOptions.

        :return: The is_exp_image_to_temp_dir of this MHtmlSaveOptions.
        :rtype: bool
        """
        return self.container['is_exp_image_to_temp_dir']

    @is_exp_image_to_temp_dir.setter
    def is_exp_image_to_temp_dir(self, is_exp_image_to_temp_dir):
        """
        Sets the is_exp_image_to_temp_dir of this MHtmlSaveOptions.

        :param is_exp_image_to_temp_dir: The is_exp_image_to_temp_dir of this MHtmlSaveOptions.
        :type: bool
        """

        self.container['is_exp_image_to_temp_dir'] = is_exp_image_to_temp_dir

    @property
    def page_title(self):
        """
        Gets the page_title of this MHtmlSaveOptions.

        :return: The page_title of this MHtmlSaveOptions.
        :rtype: str
        """
        return self.container['page_title']

    @page_title.setter
    def page_title(self, page_title):
        """
        Sets the page_title of this MHtmlSaveOptions.

        :param page_title: The page_title of this MHtmlSaveOptions.
        :type: str
        """

        self.container['page_title'] = page_title

    @property
    def parse_html_tag_in_cell(self):
        """
        Gets the parse_html_tag_in_cell of this MHtmlSaveOptions.

        :return: The parse_html_tag_in_cell of this MHtmlSaveOptions.
        :rtype: bool
        """
        return self.container['parse_html_tag_in_cell']

    @parse_html_tag_in_cell.setter
    def parse_html_tag_in_cell(self, parse_html_tag_in_cell):
        """
        Sets the parse_html_tag_in_cell of this MHtmlSaveOptions.

        :param parse_html_tag_in_cell: The parse_html_tag_in_cell of this MHtmlSaveOptions.
        :type: bool
        """

        self.container['parse_html_tag_in_cell'] = parse_html_tag_in_cell

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, MHtmlSaveOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
