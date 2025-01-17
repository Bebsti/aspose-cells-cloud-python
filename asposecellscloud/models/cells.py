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


class Cells(object):
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
        'rows': 'LinkElement',
        'cell_count': 'int',
        'max_row': 'int',
        'cell_list': 'list[LinkElement]',
        'max_column': 'int',
        'columns': 'LinkElement'
    }

    attribute_map = {
        'link': 'link',
        'rows': 'Rows',
        'cell_count': 'CellCount',
        'max_row': 'MaxRow',
        'cell_list': 'CellList',
        'max_column': 'MaxColumn',
        'columns': 'Columns'
    }
    
    @staticmethod
    def get_swagger_types():
        return Cells.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Cells.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, rows=None, cell_count=None, max_row=None, cell_list=None, max_column=None, columns=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Cells - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['rows'] = None
        self.container['cell_count'] = None
        self.container['max_row'] = None
        self.container['cell_list'] = None
        self.container['max_column'] = None
        self.container['columns'] = None

        if link is not None:
          self.link = link
        if rows is not None:
          self.rows = rows
        self.cell_count = cell_count
        self.max_row = max_row
        if cell_list is not None:
          self.cell_list = cell_list
        self.max_column = max_column
        if columns is not None:
          self.columns = columns

    @property
    def link(self):
        """
        Gets the link of this Cells.

        :return: The link of this Cells.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Cells.

        :param link: The link of this Cells.
        :type: Link
        """

        self.container['link'] = link

    @property
    def rows(self):
        """
        Gets the rows of this Cells.

        :return: The rows of this Cells.
        :rtype: LinkElement
        """
        return self.container['rows']

    @rows.setter
    def rows(self, rows):
        """
        Sets the rows of this Cells.

        :param rows: The rows of this Cells.
        :type: LinkElement
        """

        self.container['rows'] = rows

    @property
    def cell_count(self):
        """
        Gets the cell_count of this Cells.

        :return: The cell_count of this Cells.
        :rtype: int
        """
        return self.container['cell_count']

    @cell_count.setter
    def cell_count(self, cell_count):
        """
        Sets the cell_count of this Cells.

        :param cell_count: The cell_count of this Cells.
        :type: int
        """
        """
        if cell_count is None:
            raise ValueError("Invalid value for `cell_count`, must not be `None`")
        """

        self.container['cell_count'] = cell_count

    @property
    def max_row(self):
        """
        Gets the max_row of this Cells.

        :return: The max_row of this Cells.
        :rtype: int
        """
        return self.container['max_row']

    @max_row.setter
    def max_row(self, max_row):
        """
        Sets the max_row of this Cells.

        :param max_row: The max_row of this Cells.
        :type: int
        """
        """
        if max_row is None:
            raise ValueError("Invalid value for `max_row`, must not be `None`")
        """

        self.container['max_row'] = max_row

    @property
    def cell_list(self):
        """
        Gets the cell_list of this Cells.

        :return: The cell_list of this Cells.
        :rtype: list[LinkElement]
        """
        return self.container['cell_list']

    @cell_list.setter
    def cell_list(self, cell_list):
        """
        Sets the cell_list of this Cells.

        :param cell_list: The cell_list of this Cells.
        :type: list[LinkElement]
        """

        self.container['cell_list'] = cell_list

    @property
    def max_column(self):
        """
        Gets the max_column of this Cells.
        Maximum column index of cell which contains data.             

        :return: The max_column of this Cells.
        :rtype: int
        """
        return self.container['max_column']

    @max_column.setter
    def max_column(self, max_column):
        """
        Sets the max_column of this Cells.
        Maximum column index of cell which contains data.             

        :param max_column: The max_column of this Cells.
        :type: int
        """
        """
        if max_column is None:
            raise ValueError("Invalid value for `max_column`, must not be `None`")
        """

        self.container['max_column'] = max_column

    @property
    def columns(self):
        """
        Gets the columns of this Cells.

        :return: The columns of this Cells.
        :rtype: LinkElement
        """
        return self.container['columns']

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this Cells.

        :param columns: The columns of this Cells.
        :type: LinkElement
        """

        self.container['columns'] = columns

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
        if not isinstance(other, Cells):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
