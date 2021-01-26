# coding: utf-8

"""
Copyright (c) 2021 Aspose.Cells Cloud
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


class Cell(object):
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
        'link': 'Link',
        'style': 'LinkElement',
        'html_string': 'str',
        'name': 'str',
        'column': 'int',
        'worksheet': 'str',
        'is_in_table': 'bool',
        'is_array_header': 'bool',
        'value': 'str',
        'is_formula': 'bool',
        'is_style_set': 'bool',
        'is_in_array': 'bool',
        'is_error_value': 'bool',
        'is_merged': 'bool',
        'formula': 'str',
        'type': 'str',
        'row': 'int'
    }

    attribute_map = {
        'link': 'link',
        'style': 'Style',
        'html_string': 'HtmlString',
        'name': 'Name',
        'column': 'Column',
        'worksheet': 'Worksheet',
        'is_in_table': 'IsInTable',
        'is_array_header': 'IsArrayHeader',
        'value': 'Value',
        'is_formula': 'IsFormula',
        'is_style_set': 'IsStyleSet',
        'is_in_array': 'IsInArray',
        'is_error_value': 'IsErrorValue',
        'is_merged': 'IsMerged',
        'formula': 'Formula',
        'type': 'Type',
        'row': 'Row'
    }
    
    @staticmethod
    def get_swagger_types():
        return Cell.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Cell.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, style=None, html_string=None, name=None, column=None, worksheet=None, is_in_table=None, is_array_header=None, value=None, is_formula=None, is_style_set=None, is_in_array=None, is_error_value=None, is_merged=None, formula=None, type=None, row=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Cell - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['style'] = None
        self.container['html_string'] = None
        self.container['name'] = None
        self.container['column'] = None
        self.container['worksheet'] = None
        self.container['is_in_table'] = None
        self.container['is_array_header'] = None
        self.container['value'] = None
        self.container['is_formula'] = None
        self.container['is_style_set'] = None
        self.container['is_in_array'] = None
        self.container['is_error_value'] = None
        self.container['is_merged'] = None
        self.container['formula'] = None
        self.container['type'] = None
        self.container['row'] = None

        if link is not None:
          self.link = link
        if style is not None:
          self.style = style
        if html_string is not None:
          self.html_string = html_string
        if name is not None:
          self.name = name
        self.column = column
        if worksheet is not None:
          self.worksheet = worksheet
        self.is_in_table = is_in_table
        self.is_array_header = is_array_header
        if value is not None:
          self.value = value
        self.is_formula = is_formula
        self.is_style_set = is_style_set
        self.is_in_array = is_in_array
        self.is_error_value = is_error_value
        self.is_merged = is_merged
        if formula is not None:
          self.formula = formula
        if type is not None:
          self.type = type
        self.row = row

    @property
    def link(self):
        """
        Gets the link of this Cell.

        :return: The link of this Cell.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Cell.

        :param link: The link of this Cell.
        :type: Link
        """

        self.container['link'] = link

    @property
    def style(self):
        """
        Gets the style of this Cell.

        :return: The style of this Cell.
        :rtype: LinkElement
        """
        return self.container['style']

    @style.setter
    def style(self, style):
        """
        Sets the style of this Cell.

        :param style: The style of this Cell.
        :type: LinkElement
        """

        self.container['style'] = style

    @property
    def html_string(self):
        """
        Gets the html_string of this Cell.
        Gets and sets the html string which contains data and some formattings in this cell.             

        :return: The html_string of this Cell.
        :rtype: str
        """
        return self.container['html_string']

    @html_string.setter
    def html_string(self, html_string):
        """
        Sets the html_string of this Cell.
        Gets and sets the html string which contains data and some formattings in this cell.             

        :param html_string: The html_string of this Cell.
        :type: str
        """

        self.container['html_string'] = html_string

    @property
    def name(self):
        """
        Gets the name of this Cell.
        Gets the name of the cell.             

        :return: The name of this Cell.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this Cell.
        Gets the name of the cell.             

        :param name: The name of this Cell.
        :type: str
        """

        self.container['name'] = name

    @property
    def column(self):
        """
        Gets the column of this Cell.
        Gets column number (zero based) of the cell.             

        :return: The column of this Cell.
        :rtype: int
        """
        return self.container['column']

    @column.setter
    def column(self, column):
        """
        Sets the column of this Cell.
        Gets column number (zero based) of the cell.             

        :param column: The column of this Cell.
        :type: int
        """
        """
        if column is None:
            raise ValueError("Invalid value for `column`, must not be `None`")
        """

        self.container['column'] = column

    @property
    def worksheet(self):
        """
        Gets the worksheet of this Cell.
        Gets the parent worksheet.

        :return: The worksheet of this Cell.
        :rtype: str
        """
        return self.container['worksheet']

    @worksheet.setter
    def worksheet(self, worksheet):
        """
        Sets the worksheet of this Cell.
        Gets the parent worksheet.

        :param worksheet: The worksheet of this Cell.
        :type: str
        """

        self.container['worksheet'] = worksheet

    @property
    def is_in_table(self):
        """
        Gets the is_in_table of this Cell.
        Indicates whethe this cell is part of table formula.             

        :return: The is_in_table of this Cell.
        :rtype: bool
        """
        return self.container['is_in_table']

    @is_in_table.setter
    def is_in_table(self, is_in_table):
        """
        Sets the is_in_table of this Cell.
        Indicates whethe this cell is part of table formula.             

        :param is_in_table: The is_in_table of this Cell.
        :type: bool
        """
        """
        if is_in_table is None:
            raise ValueError("Invalid value for `is_in_table`, must not be `None`")
        """

        self.container['is_in_table'] = is_in_table

    @property
    def is_array_header(self):
        """
        Gets the is_array_header of this Cell.
        Inidicates the cell's formula is and array formula and it is the first cell of the array.

        :return: The is_array_header of this Cell.
        :rtype: bool
        """
        return self.container['is_array_header']

    @is_array_header.setter
    def is_array_header(self, is_array_header):
        """
        Sets the is_array_header of this Cell.
        Inidicates the cell's formula is and array formula and it is the first cell of the array.

        :param is_array_header: The is_array_header of this Cell.
        :type: bool
        """
        """
        if is_array_header is None:
            raise ValueError("Invalid value for `is_array_header`, must not be `None`")
        """

        self.container['is_array_header'] = is_array_header

    @property
    def value(self):
        """
        Gets the value of this Cell.

        :return: The value of this Cell.
        :rtype: str
        """
        return self.container['value']

    @value.setter
    def value(self, value):
        """
        Sets the value of this Cell.

        :param value: The value of this Cell.
        :type: str
        """

        self.container['value'] = value

    @property
    def is_formula(self):
        """
        Gets the is_formula of this Cell.
        Represents if the specified cell contains formula.             

        :return: The is_formula of this Cell.
        :rtype: bool
        """
        return self.container['is_formula']

    @is_formula.setter
    def is_formula(self, is_formula):
        """
        Sets the is_formula of this Cell.
        Represents if the specified cell contains formula.             

        :param is_formula: The is_formula of this Cell.
        :type: bool
        """
        """
        if is_formula is None:
            raise ValueError("Invalid value for `is_formula`, must not be `None`")
        """

        self.container['is_formula'] = is_formula

    @property
    def is_style_set(self):
        """
        Gets the is_style_set of this Cell.
        Indicates if the cell's style is set. If return false, it means this cell has a default cell format.             

        :return: The is_style_set of this Cell.
        :rtype: bool
        """
        return self.container['is_style_set']

    @is_style_set.setter
    def is_style_set(self, is_style_set):
        """
        Sets the is_style_set of this Cell.
        Indicates if the cell's style is set. If return false, it means this cell has a default cell format.             

        :param is_style_set: The is_style_set of this Cell.
        :type: bool
        """
        """
        if is_style_set is None:
            raise ValueError("Invalid value for `is_style_set`, must not be `None`")
        """

        self.container['is_style_set'] = is_style_set

    @property
    def is_in_array(self):
        """
        Gets the is_in_array of this Cell.
        Indicates whether the cell formula is an array formula.

        :return: The is_in_array of this Cell.
        :rtype: bool
        """
        return self.container['is_in_array']

    @is_in_array.setter
    def is_in_array(self, is_in_array):
        """
        Sets the is_in_array of this Cell.
        Indicates whether the cell formula is an array formula.

        :param is_in_array: The is_in_array of this Cell.
        :type: bool
        """
        """
        if is_in_array is None:
            raise ValueError("Invalid value for `is_in_array`, must not be `None`")
        """

        self.container['is_in_array'] = is_in_array

    @property
    def is_error_value(self):
        """
        Gets the is_error_value of this Cell.
        Checks if a formula can properly evaluate a result.             

        :return: The is_error_value of this Cell.
        :rtype: bool
        """
        return self.container['is_error_value']

    @is_error_value.setter
    def is_error_value(self, is_error_value):
        """
        Sets the is_error_value of this Cell.
        Checks if a formula can properly evaluate a result.             

        :param is_error_value: The is_error_value of this Cell.
        :type: bool
        """
        """
        if is_error_value is None:
            raise ValueError("Invalid value for `is_error_value`, must not be `None`")
        """

        self.container['is_error_value'] = is_error_value

    @property
    def is_merged(self):
        """
        Gets the is_merged of this Cell.
        Checks if a cell is part of a merged range or not.             

        :return: The is_merged of this Cell.
        :rtype: bool
        """
        return self.container['is_merged']

    @is_merged.setter
    def is_merged(self, is_merged):
        """
        Sets the is_merged of this Cell.
        Checks if a cell is part of a merged range or not.             

        :param is_merged: The is_merged of this Cell.
        :type: bool
        """
        """
        if is_merged is None:
            raise ValueError("Invalid value for `is_merged`, must not be `None`")
        """

        self.container['is_merged'] = is_merged

    @property
    def formula(self):
        """
        Gets the formula of this Cell.
        Gets or sets a formula of the Aspose.Cells.Cell.

        :return: The formula of this Cell.
        :rtype: str
        """
        return self.container['formula']

    @formula.setter
    def formula(self, formula):
        """
        Sets the formula of this Cell.
        Gets or sets a formula of the Aspose.Cells.Cell.

        :param formula: The formula of this Cell.
        :type: str
        """

        self.container['formula'] = formula

    @property
    def type(self):
        """
        Gets the type of this Cell.
        Specifies a cell value type.

        :return: The type of this Cell.
        :rtype: str
        """
        return self.container['type']

    @type.setter
    def type(self, type):
        """
        Sets the type of this Cell.
        Specifies a cell value type.

        :param type: The type of this Cell.
        :type: str
        """

        self.container['type'] = type

    @property
    def row(self):
        """
        Gets the row of this Cell.
        Gets row number (zero based) of the cell.             

        :return: The row of this Cell.
        :rtype: int
        """
        return self.container['row']

    @row.setter
    def row(self, row):
        """
        Sets the row of this Cell.
        Gets row number (zero based) of the cell.             

        :param row: The row of this Cell.
        :type: int
        """
        """
        if row is None:
            raise ValueError("Invalid value for `row`, must not be `None`")
        """

        self.container['row'] = row

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
        if not isinstance(other, Cell):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
