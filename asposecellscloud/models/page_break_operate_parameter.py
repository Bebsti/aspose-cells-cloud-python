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
from . import OperateParameter

class PageBreakOperateParameter(OperateParameter):
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
        'index': 'int',
        'end_index': 'int',
        'column': 'int',
        'start_index': 'int',
        'page_break_type': 'str',
        'row': 'int'
    }

    attribute_map = {
        'index': 'Index',
        'end_index': 'EndIndex',
        'column': 'Column',
        'start_index': 'StartIndex',
        'page_break_type': 'PageBreakType',
        'row': 'Row'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(PageBreakOperateParameter.swagger_types, **OperateParameter.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(PageBreakOperateParameter.attribute_map, **OperateParameter.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, index=None, end_index=None, column=None, start_index=None, page_break_type=None, row=None, **kw):
        super(PageBreakOperateParameter, self).__init__(**kw)
		    
        """
        PageBreakOperateParameter - a model defined in Swagger
        """

        self.container['index'] = None
        self.container['end_index'] = None
        self.container['column'] = None
        self.container['start_index'] = None
        self.container['page_break_type'] = None
        self.container['row'] = None

        if index is not None:
          self.index = index
        if end_index is not None:
          self.end_index = end_index
        if column is not None:
          self.column = column
        if start_index is not None:
          self.start_index = start_index
        if page_break_type is not None:
          self.page_break_type = page_break_type
        if row is not None:
          self.row = row

    @property
    def index(self):
        """
        Gets the index of this PageBreakOperateParameter.

        :return: The index of this PageBreakOperateParameter.
        :rtype: int
        """
        return self.container['index']

    @index.setter
    def index(self, index):
        """
        Sets the index of this PageBreakOperateParameter.

        :param index: The index of this PageBreakOperateParameter.
        :type: int
        """

        self.container['index'] = index

    @property
    def end_index(self):
        """
        Gets the end_index of this PageBreakOperateParameter.

        :return: The end_index of this PageBreakOperateParameter.
        :rtype: int
        """
        return self.container['end_index']

    @end_index.setter
    def end_index(self, end_index):
        """
        Sets the end_index of this PageBreakOperateParameter.

        :param end_index: The end_index of this PageBreakOperateParameter.
        :type: int
        """

        self.container['end_index'] = end_index

    @property
    def column(self):
        """
        Gets the column of this PageBreakOperateParameter.

        :return: The column of this PageBreakOperateParameter.
        :rtype: int
        """
        return self.container['column']

    @column.setter
    def column(self, column):
        """
        Sets the column of this PageBreakOperateParameter.

        :param column: The column of this PageBreakOperateParameter.
        :type: int
        """

        self.container['column'] = column

    @property
    def start_index(self):
        """
        Gets the start_index of this PageBreakOperateParameter.

        :return: The start_index of this PageBreakOperateParameter.
        :rtype: int
        """
        return self.container['start_index']

    @start_index.setter
    def start_index(self, start_index):
        """
        Sets the start_index of this PageBreakOperateParameter.

        :param start_index: The start_index of this PageBreakOperateParameter.
        :type: int
        """

        self.container['start_index'] = start_index

    @property
    def page_break_type(self):
        """
        Gets the page_break_type of this PageBreakOperateParameter.

        :return: The page_break_type of this PageBreakOperateParameter.
        :rtype: str
        """
        return self.container['page_break_type']

    @page_break_type.setter
    def page_break_type(self, page_break_type):
        """
        Sets the page_break_type of this PageBreakOperateParameter.

        :param page_break_type: The page_break_type of this PageBreakOperateParameter.
        :type: str
        """

        self.container['page_break_type'] = page_break_type

    @property
    def row(self):
        """
        Gets the row of this PageBreakOperateParameter.

        :return: The row of this PageBreakOperateParameter.
        :rtype: int
        """
        return self.container['row']

    @row.setter
    def row(self, row):
        """
        Sets the row of this PageBreakOperateParameter.

        :param row: The row of this PageBreakOperateParameter.
        :type: int
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
        if not isinstance(other, PageBreakOperateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
