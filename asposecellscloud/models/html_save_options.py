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

class HtmlSaveOptions(SaveOptions):
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
        'save_as_single_file': 'str',
        'export_hidden_worksheet': 'str',
        'export_grid_lines': 'str',
        'presentation_preference': 'str',
        'cell_css_prefix': 'str',
        'table_css_id': 'str',
        'is_full_path_link': 'str',
        'export_worksheet_css_separately': 'str',
        'export_similar_border_style': 'str',
        'merge_empty_td_forcely': 'str',
        'export_cell_coordinate': 'str',
        'export_extra_headings': 'str',
        'export_headings': 'str',
        'export_formula': 'str',
        'add_tooltip_text': 'str',
        'export_bogus_row_data': 'str',
        'exclude_unused_styles': 'str',
        'export_document_properties': 'str',
        'export_worksheet_properties': 'str',
        'export_workbook_properties': 'str',
        'export_frame_scripts_and_properties': 'str',
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
        'save_as_single_file': 'SaveAsSingleFile',
        'export_hidden_worksheet': 'ExportHiddenWorksheet',
        'export_grid_lines': 'ExportGridLines',
        'presentation_preference': 'PresentationPreference',
        'cell_css_prefix': 'CellCssPrefix',
        'table_css_id': 'TableCssId',
        'is_full_path_link': 'IsFullPathLink',
        'export_worksheet_css_separately': 'ExportWorksheetCSSSeparately',
        'export_similar_border_style': 'ExportSimilarBorderStyle',
        'merge_empty_td_forcely': 'MergeEmptyTdForcely',
        'export_cell_coordinate': 'ExportCellCoordinate',
        'export_extra_headings': 'ExportExtraHeadings',
        'export_headings': 'ExportHeadings',
        'export_formula': 'ExportFormula',
        'add_tooltip_text': 'AddTooltipText',
        'export_bogus_row_data': 'ExportBogusRowData',
        'exclude_unused_styles': 'ExcludeUnusedStyles',
        'export_document_properties': 'ExportDocumentProperties',
        'export_worksheet_properties': 'ExportWorksheetProperties',
        'export_workbook_properties': 'ExportWorkbookProperties',
        'export_frame_scripts_and_properties': 'ExportFrameScriptsAndProperties',
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
        return dict(HtmlSaveOptions.swagger_types, **SaveOptions.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(HtmlSaveOptions.attribute_map, **SaveOptions.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, save_as_single_file=None, export_hidden_worksheet=None, export_grid_lines=None, presentation_preference=None, cell_css_prefix=None, table_css_id=None, is_full_path_link=None, export_worksheet_css_separately=None, export_similar_border_style=None, merge_empty_td_forcely=None, export_cell_coordinate=None, export_extra_headings=None, export_headings=None, export_formula=None, add_tooltip_text=None, export_bogus_row_data=None, exclude_unused_styles=None, export_document_properties=None, export_worksheet_properties=None, export_workbook_properties=None, export_frame_scripts_and_properties=None, attached_files_directory=None, attached_files_url_prefix=None, encoding=None, export_active_worksheet_only=None, export_chart_image_format=None, export_images_as_base64=None, hidden_col_display_type=None, hidden_row_display_type=None, html_cross_string_type=None, is_exp_image_to_temp_dir=None, page_title=None, parse_html_tag_in_cell=None, **kw):
        super(HtmlSaveOptions, self).__init__(**kw)
		    
        """
        HtmlSaveOptions - a model defined in Swagger
        """

        self.container['save_as_single_file'] = None
        self.container['export_hidden_worksheet'] = None
        self.container['export_grid_lines'] = None
        self.container['presentation_preference'] = None
        self.container['cell_css_prefix'] = None
        self.container['table_css_id'] = None
        self.container['is_full_path_link'] = None
        self.container['export_worksheet_css_separately'] = None
        self.container['export_similar_border_style'] = None
        self.container['merge_empty_td_forcely'] = None
        self.container['export_cell_coordinate'] = None
        self.container['export_extra_headings'] = None
        self.container['export_headings'] = None
        self.container['export_formula'] = None
        self.container['add_tooltip_text'] = None
        self.container['export_bogus_row_data'] = None
        self.container['exclude_unused_styles'] = None
        self.container['export_document_properties'] = None
        self.container['export_worksheet_properties'] = None
        self.container['export_workbook_properties'] = None
        self.container['export_frame_scripts_and_properties'] = None
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

        if save_as_single_file is not None:
          self.save_as_single_file = save_as_single_file
        if export_hidden_worksheet is not None:
          self.export_hidden_worksheet = export_hidden_worksheet
        if export_grid_lines is not None:
          self.export_grid_lines = export_grid_lines
        if presentation_preference is not None:
          self.presentation_preference = presentation_preference
        if cell_css_prefix is not None:
          self.cell_css_prefix = cell_css_prefix
        if table_css_id is not None:
          self.table_css_id = table_css_id
        if is_full_path_link is not None:
          self.is_full_path_link = is_full_path_link
        if export_worksheet_css_separately is not None:
          self.export_worksheet_css_separately = export_worksheet_css_separately
        if export_similar_border_style is not None:
          self.export_similar_border_style = export_similar_border_style
        if merge_empty_td_forcely is not None:
          self.merge_empty_td_forcely = merge_empty_td_forcely
        if export_cell_coordinate is not None:
          self.export_cell_coordinate = export_cell_coordinate
        if export_extra_headings is not None:
          self.export_extra_headings = export_extra_headings
        if export_headings is not None:
          self.export_headings = export_headings
        if export_formula is not None:
          self.export_formula = export_formula
        if add_tooltip_text is not None:
          self.add_tooltip_text = add_tooltip_text
        if export_bogus_row_data is not None:
          self.export_bogus_row_data = export_bogus_row_data
        if exclude_unused_styles is not None:
          self.exclude_unused_styles = exclude_unused_styles
        if export_document_properties is not None:
          self.export_document_properties = export_document_properties
        if export_worksheet_properties is not None:
          self.export_worksheet_properties = export_worksheet_properties
        if export_workbook_properties is not None:
          self.export_workbook_properties = export_workbook_properties
        if export_frame_scripts_and_properties is not None:
          self.export_frame_scripts_and_properties = export_frame_scripts_and_properties
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
    def save_as_single_file(self):
        """
        Gets the save_as_single_file of this HtmlSaveOptions.

        :return: The save_as_single_file of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['save_as_single_file']

    @save_as_single_file.setter
    def save_as_single_file(self, save_as_single_file):
        """
        Sets the save_as_single_file of this HtmlSaveOptions.

        :param save_as_single_file: The save_as_single_file of this HtmlSaveOptions.
        :type: str
        """

        self.container['save_as_single_file'] = save_as_single_file

    @property
    def export_hidden_worksheet(self):
        """
        Gets the export_hidden_worksheet of this HtmlSaveOptions.

        :return: The export_hidden_worksheet of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_hidden_worksheet']

    @export_hidden_worksheet.setter
    def export_hidden_worksheet(self, export_hidden_worksheet):
        """
        Sets the export_hidden_worksheet of this HtmlSaveOptions.

        :param export_hidden_worksheet: The export_hidden_worksheet of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_hidden_worksheet'] = export_hidden_worksheet

    @property
    def export_grid_lines(self):
        """
        Gets the export_grid_lines of this HtmlSaveOptions.

        :return: The export_grid_lines of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_grid_lines']

    @export_grid_lines.setter
    def export_grid_lines(self, export_grid_lines):
        """
        Sets the export_grid_lines of this HtmlSaveOptions.

        :param export_grid_lines: The export_grid_lines of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_grid_lines'] = export_grid_lines

    @property
    def presentation_preference(self):
        """
        Gets the presentation_preference of this HtmlSaveOptions.

        :return: The presentation_preference of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['presentation_preference']

    @presentation_preference.setter
    def presentation_preference(self, presentation_preference):
        """
        Sets the presentation_preference of this HtmlSaveOptions.

        :param presentation_preference: The presentation_preference of this HtmlSaveOptions.
        :type: str
        """

        self.container['presentation_preference'] = presentation_preference

    @property
    def cell_css_prefix(self):
        """
        Gets the cell_css_prefix of this HtmlSaveOptions.

        :return: The cell_css_prefix of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['cell_css_prefix']

    @cell_css_prefix.setter
    def cell_css_prefix(self, cell_css_prefix):
        """
        Sets the cell_css_prefix of this HtmlSaveOptions.

        :param cell_css_prefix: The cell_css_prefix of this HtmlSaveOptions.
        :type: str
        """

        self.container['cell_css_prefix'] = cell_css_prefix

    @property
    def table_css_id(self):
        """
        Gets the table_css_id of this HtmlSaveOptions.

        :return: The table_css_id of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['table_css_id']

    @table_css_id.setter
    def table_css_id(self, table_css_id):
        """
        Sets the table_css_id of this HtmlSaveOptions.

        :param table_css_id: The table_css_id of this HtmlSaveOptions.
        :type: str
        """

        self.container['table_css_id'] = table_css_id

    @property
    def is_full_path_link(self):
        """
        Gets the is_full_path_link of this HtmlSaveOptions.

        :return: The is_full_path_link of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['is_full_path_link']

    @is_full_path_link.setter
    def is_full_path_link(self, is_full_path_link):
        """
        Sets the is_full_path_link of this HtmlSaveOptions.

        :param is_full_path_link: The is_full_path_link of this HtmlSaveOptions.
        :type: str
        """

        self.container['is_full_path_link'] = is_full_path_link

    @property
    def export_worksheet_css_separately(self):
        """
        Gets the export_worksheet_css_separately of this HtmlSaveOptions.

        :return: The export_worksheet_css_separately of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_worksheet_css_separately']

    @export_worksheet_css_separately.setter
    def export_worksheet_css_separately(self, export_worksheet_css_separately):
        """
        Sets the export_worksheet_css_separately of this HtmlSaveOptions.

        :param export_worksheet_css_separately: The export_worksheet_css_separately of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_worksheet_css_separately'] = export_worksheet_css_separately

    @property
    def export_similar_border_style(self):
        """
        Gets the export_similar_border_style of this HtmlSaveOptions.

        :return: The export_similar_border_style of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_similar_border_style']

    @export_similar_border_style.setter
    def export_similar_border_style(self, export_similar_border_style):
        """
        Sets the export_similar_border_style of this HtmlSaveOptions.

        :param export_similar_border_style: The export_similar_border_style of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_similar_border_style'] = export_similar_border_style

    @property
    def merge_empty_td_forcely(self):
        """
        Gets the merge_empty_td_forcely of this HtmlSaveOptions.

        :return: The merge_empty_td_forcely of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['merge_empty_td_forcely']

    @merge_empty_td_forcely.setter
    def merge_empty_td_forcely(self, merge_empty_td_forcely):
        """
        Sets the merge_empty_td_forcely of this HtmlSaveOptions.

        :param merge_empty_td_forcely: The merge_empty_td_forcely of this HtmlSaveOptions.
        :type: str
        """

        self.container['merge_empty_td_forcely'] = merge_empty_td_forcely

    @property
    def export_cell_coordinate(self):
        """
        Gets the export_cell_coordinate of this HtmlSaveOptions.

        :return: The export_cell_coordinate of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_cell_coordinate']

    @export_cell_coordinate.setter
    def export_cell_coordinate(self, export_cell_coordinate):
        """
        Sets the export_cell_coordinate of this HtmlSaveOptions.

        :param export_cell_coordinate: The export_cell_coordinate of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_cell_coordinate'] = export_cell_coordinate

    @property
    def export_extra_headings(self):
        """
        Gets the export_extra_headings of this HtmlSaveOptions.

        :return: The export_extra_headings of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_extra_headings']

    @export_extra_headings.setter
    def export_extra_headings(self, export_extra_headings):
        """
        Sets the export_extra_headings of this HtmlSaveOptions.

        :param export_extra_headings: The export_extra_headings of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_extra_headings'] = export_extra_headings

    @property
    def export_headings(self):
        """
        Gets the export_headings of this HtmlSaveOptions.

        :return: The export_headings of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_headings']

    @export_headings.setter
    def export_headings(self, export_headings):
        """
        Sets the export_headings of this HtmlSaveOptions.

        :param export_headings: The export_headings of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_headings'] = export_headings

    @property
    def export_formula(self):
        """
        Gets the export_formula of this HtmlSaveOptions.

        :return: The export_formula of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_formula']

    @export_formula.setter
    def export_formula(self, export_formula):
        """
        Sets the export_formula of this HtmlSaveOptions.

        :param export_formula: The export_formula of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_formula'] = export_formula

    @property
    def add_tooltip_text(self):
        """
        Gets the add_tooltip_text of this HtmlSaveOptions.

        :return: The add_tooltip_text of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['add_tooltip_text']

    @add_tooltip_text.setter
    def add_tooltip_text(self, add_tooltip_text):
        """
        Sets the add_tooltip_text of this HtmlSaveOptions.

        :param add_tooltip_text: The add_tooltip_text of this HtmlSaveOptions.
        :type: str
        """

        self.container['add_tooltip_text'] = add_tooltip_text

    @property
    def export_bogus_row_data(self):
        """
        Gets the export_bogus_row_data of this HtmlSaveOptions.

        :return: The export_bogus_row_data of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_bogus_row_data']

    @export_bogus_row_data.setter
    def export_bogus_row_data(self, export_bogus_row_data):
        """
        Sets the export_bogus_row_data of this HtmlSaveOptions.

        :param export_bogus_row_data: The export_bogus_row_data of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_bogus_row_data'] = export_bogus_row_data

    @property
    def exclude_unused_styles(self):
        """
        Gets the exclude_unused_styles of this HtmlSaveOptions.

        :return: The exclude_unused_styles of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['exclude_unused_styles']

    @exclude_unused_styles.setter
    def exclude_unused_styles(self, exclude_unused_styles):
        """
        Sets the exclude_unused_styles of this HtmlSaveOptions.

        :param exclude_unused_styles: The exclude_unused_styles of this HtmlSaveOptions.
        :type: str
        """

        self.container['exclude_unused_styles'] = exclude_unused_styles

    @property
    def export_document_properties(self):
        """
        Gets the export_document_properties of this HtmlSaveOptions.

        :return: The export_document_properties of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_document_properties']

    @export_document_properties.setter
    def export_document_properties(self, export_document_properties):
        """
        Sets the export_document_properties of this HtmlSaveOptions.

        :param export_document_properties: The export_document_properties of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_document_properties'] = export_document_properties

    @property
    def export_worksheet_properties(self):
        """
        Gets the export_worksheet_properties of this HtmlSaveOptions.

        :return: The export_worksheet_properties of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_worksheet_properties']

    @export_worksheet_properties.setter
    def export_worksheet_properties(self, export_worksheet_properties):
        """
        Sets the export_worksheet_properties of this HtmlSaveOptions.

        :param export_worksheet_properties: The export_worksheet_properties of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_worksheet_properties'] = export_worksheet_properties

    @property
    def export_workbook_properties(self):
        """
        Gets the export_workbook_properties of this HtmlSaveOptions.

        :return: The export_workbook_properties of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_workbook_properties']

    @export_workbook_properties.setter
    def export_workbook_properties(self, export_workbook_properties):
        """
        Sets the export_workbook_properties of this HtmlSaveOptions.

        :param export_workbook_properties: The export_workbook_properties of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_workbook_properties'] = export_workbook_properties

    @property
    def export_frame_scripts_and_properties(self):
        """
        Gets the export_frame_scripts_and_properties of this HtmlSaveOptions.

        :return: The export_frame_scripts_and_properties of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_frame_scripts_and_properties']

    @export_frame_scripts_and_properties.setter
    def export_frame_scripts_and_properties(self, export_frame_scripts_and_properties):
        """
        Sets the export_frame_scripts_and_properties of this HtmlSaveOptions.

        :param export_frame_scripts_and_properties: The export_frame_scripts_and_properties of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_frame_scripts_and_properties'] = export_frame_scripts_and_properties

    @property
    def attached_files_directory(self):
        """
        Gets the attached_files_directory of this HtmlSaveOptions.

        :return: The attached_files_directory of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['attached_files_directory']

    @attached_files_directory.setter
    def attached_files_directory(self, attached_files_directory):
        """
        Sets the attached_files_directory of this HtmlSaveOptions.

        :param attached_files_directory: The attached_files_directory of this HtmlSaveOptions.
        :type: str
        """

        self.container['attached_files_directory'] = attached_files_directory

    @property
    def attached_files_url_prefix(self):
        """
        Gets the attached_files_url_prefix of this HtmlSaveOptions.

        :return: The attached_files_url_prefix of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['attached_files_url_prefix']

    @attached_files_url_prefix.setter
    def attached_files_url_prefix(self, attached_files_url_prefix):
        """
        Sets the attached_files_url_prefix of this HtmlSaveOptions.

        :param attached_files_url_prefix: The attached_files_url_prefix of this HtmlSaveOptions.
        :type: str
        """

        self.container['attached_files_url_prefix'] = attached_files_url_prefix

    @property
    def encoding(self):
        """
        Gets the encoding of this HtmlSaveOptions.

        :return: The encoding of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['encoding']

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this HtmlSaveOptions.

        :param encoding: The encoding of this HtmlSaveOptions.
        :type: str
        """

        self.container['encoding'] = encoding

    @property
    def export_active_worksheet_only(self):
        """
        Gets the export_active_worksheet_only of this HtmlSaveOptions.

        :return: The export_active_worksheet_only of this HtmlSaveOptions.
        :rtype: bool
        """
        return self.container['export_active_worksheet_only']

    @export_active_worksheet_only.setter
    def export_active_worksheet_only(self, export_active_worksheet_only):
        """
        Sets the export_active_worksheet_only of this HtmlSaveOptions.

        :param export_active_worksheet_only: The export_active_worksheet_only of this HtmlSaveOptions.
        :type: bool
        """

        self.container['export_active_worksheet_only'] = export_active_worksheet_only

    @property
    def export_chart_image_format(self):
        """
        Gets the export_chart_image_format of this HtmlSaveOptions.

        :return: The export_chart_image_format of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['export_chart_image_format']

    @export_chart_image_format.setter
    def export_chart_image_format(self, export_chart_image_format):
        """
        Sets the export_chart_image_format of this HtmlSaveOptions.

        :param export_chart_image_format: The export_chart_image_format of this HtmlSaveOptions.
        :type: str
        """

        self.container['export_chart_image_format'] = export_chart_image_format

    @property
    def export_images_as_base64(self):
        """
        Gets the export_images_as_base64 of this HtmlSaveOptions.

        :return: The export_images_as_base64 of this HtmlSaveOptions.
        :rtype: bool
        """
        return self.container['export_images_as_base64']

    @export_images_as_base64.setter
    def export_images_as_base64(self, export_images_as_base64):
        """
        Sets the export_images_as_base64 of this HtmlSaveOptions.

        :param export_images_as_base64: The export_images_as_base64 of this HtmlSaveOptions.
        :type: bool
        """

        self.container['export_images_as_base64'] = export_images_as_base64

    @property
    def hidden_col_display_type(self):
        """
        Gets the hidden_col_display_type of this HtmlSaveOptions.

        :return: The hidden_col_display_type of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['hidden_col_display_type']

    @hidden_col_display_type.setter
    def hidden_col_display_type(self, hidden_col_display_type):
        """
        Sets the hidden_col_display_type of this HtmlSaveOptions.

        :param hidden_col_display_type: The hidden_col_display_type of this HtmlSaveOptions.
        :type: str
        """

        self.container['hidden_col_display_type'] = hidden_col_display_type

    @property
    def hidden_row_display_type(self):
        """
        Gets the hidden_row_display_type of this HtmlSaveOptions.

        :return: The hidden_row_display_type of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['hidden_row_display_type']

    @hidden_row_display_type.setter
    def hidden_row_display_type(self, hidden_row_display_type):
        """
        Sets the hidden_row_display_type of this HtmlSaveOptions.

        :param hidden_row_display_type: The hidden_row_display_type of this HtmlSaveOptions.
        :type: str
        """

        self.container['hidden_row_display_type'] = hidden_row_display_type

    @property
    def html_cross_string_type(self):
        """
        Gets the html_cross_string_type of this HtmlSaveOptions.

        :return: The html_cross_string_type of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['html_cross_string_type']

    @html_cross_string_type.setter
    def html_cross_string_type(self, html_cross_string_type):
        """
        Sets the html_cross_string_type of this HtmlSaveOptions.

        :param html_cross_string_type: The html_cross_string_type of this HtmlSaveOptions.
        :type: str
        """

        self.container['html_cross_string_type'] = html_cross_string_type

    @property
    def is_exp_image_to_temp_dir(self):
        """
        Gets the is_exp_image_to_temp_dir of this HtmlSaveOptions.

        :return: The is_exp_image_to_temp_dir of this HtmlSaveOptions.
        :rtype: bool
        """
        return self.container['is_exp_image_to_temp_dir']

    @is_exp_image_to_temp_dir.setter
    def is_exp_image_to_temp_dir(self, is_exp_image_to_temp_dir):
        """
        Sets the is_exp_image_to_temp_dir of this HtmlSaveOptions.

        :param is_exp_image_to_temp_dir: The is_exp_image_to_temp_dir of this HtmlSaveOptions.
        :type: bool
        """

        self.container['is_exp_image_to_temp_dir'] = is_exp_image_to_temp_dir

    @property
    def page_title(self):
        """
        Gets the page_title of this HtmlSaveOptions.

        :return: The page_title of this HtmlSaveOptions.
        :rtype: str
        """
        return self.container['page_title']

    @page_title.setter
    def page_title(self, page_title):
        """
        Sets the page_title of this HtmlSaveOptions.

        :param page_title: The page_title of this HtmlSaveOptions.
        :type: str
        """

        self.container['page_title'] = page_title

    @property
    def parse_html_tag_in_cell(self):
        """
        Gets the parse_html_tag_in_cell of this HtmlSaveOptions.

        :return: The parse_html_tag_in_cell of this HtmlSaveOptions.
        :rtype: bool
        """
        return self.container['parse_html_tag_in_cell']

    @parse_html_tag_in_cell.setter
    def parse_html_tag_in_cell(self, parse_html_tag_in_cell):
        """
        Sets the parse_html_tag_in_cell of this HtmlSaveOptions.

        :param parse_html_tag_in_cell: The parse_html_tag_in_cell of this HtmlSaveOptions.
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
        if not isinstance(other, HtmlSaveOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
