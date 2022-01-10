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


class OperateObjectPosition(object):
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
        'chart_index': 'int',
        'list_object_index': 'int',
        'sheet_name': 'str',
        'shape_index': 'int',
        'cell_name': 'str',
        'workbook': 'FileSource'
    }

    attribute_map = {
        'chart_index': 'ChartIndex',
        'list_object_index': 'ListObjectIndex',
        'sheet_name': 'SheetName',
        'shape_index': 'ShapeIndex',
        'cell_name': 'CellName',
        'workbook': 'Workbook'
    }
    
    @staticmethod
    def get_swagger_types():
        return OperateObjectPosition.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return OperateObjectPosition.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, chart_index=None, list_object_index=None, sheet_name=None, shape_index=None, cell_name=None, workbook=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        OperateObjectPosition - a model defined in Swagger
        """

        self.container['chart_index'] = None
        self.container['list_object_index'] = None
        self.container['sheet_name'] = None
        self.container['shape_index'] = None
        self.container['cell_name'] = None
        self.container['workbook'] = None

        if chart_index is not None:
          self.chart_index = chart_index
        if list_object_index is not None:
          self.list_object_index = list_object_index
        if sheet_name is not None:
          self.sheet_name = sheet_name
        if shape_index is not None:
          self.shape_index = shape_index
        if cell_name is not None:
          self.cell_name = cell_name
        if workbook is not None:
          self.workbook = workbook

    @property
    def chart_index(self):
        """
        Gets the chart_index of this OperateObjectPosition.

        :return: The chart_index of this OperateObjectPosition.
        :rtype: int
        """
        return self.container['chart_index']

    @chart_index.setter
    def chart_index(self, chart_index):
        """
        Sets the chart_index of this OperateObjectPosition.

        :param chart_index: The chart_index of this OperateObjectPosition.
        :type: int
        """

        self.container['chart_index'] = chart_index

    @property
    def list_object_index(self):
        """
        Gets the list_object_index of this OperateObjectPosition.

        :return: The list_object_index of this OperateObjectPosition.
        :rtype: int
        """
        return self.container['list_object_index']

    @list_object_index.setter
    def list_object_index(self, list_object_index):
        """
        Sets the list_object_index of this OperateObjectPosition.

        :param list_object_index: The list_object_index of this OperateObjectPosition.
        :type: int
        """

        self.container['list_object_index'] = list_object_index

    @property
    def sheet_name(self):
        """
        Gets the sheet_name of this OperateObjectPosition.

        :return: The sheet_name of this OperateObjectPosition.
        :rtype: str
        """
        return self.container['sheet_name']

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        """
        Sets the sheet_name of this OperateObjectPosition.

        :param sheet_name: The sheet_name of this OperateObjectPosition.
        :type: str
        """

        self.container['sheet_name'] = sheet_name

    @property
    def shape_index(self):
        """
        Gets the shape_index of this OperateObjectPosition.

        :return: The shape_index of this OperateObjectPosition.
        :rtype: int
        """
        return self.container['shape_index']

    @shape_index.setter
    def shape_index(self, shape_index):
        """
        Sets the shape_index of this OperateObjectPosition.

        :param shape_index: The shape_index of this OperateObjectPosition.
        :type: int
        """

        self.container['shape_index'] = shape_index

    @property
    def cell_name(self):
        """
        Gets the cell_name of this OperateObjectPosition.

        :return: The cell_name of this OperateObjectPosition.
        :rtype: str
        """
        return self.container['cell_name']

    @cell_name.setter
    def cell_name(self, cell_name):
        """
        Sets the cell_name of this OperateObjectPosition.

        :param cell_name: The cell_name of this OperateObjectPosition.
        :type: str
        """

        self.container['cell_name'] = cell_name

    @property
    def workbook(self):
        """
        Gets the workbook of this OperateObjectPosition.

        :return: The workbook of this OperateObjectPosition.
        :rtype: FileSource
        """
        return self.container['workbook']

    @workbook.setter
    def workbook(self, workbook):
        """
        Sets the workbook of this OperateObjectPosition.

        :param workbook: The workbook of this OperateObjectPosition.
        :type: FileSource
        """

        self.container['workbook'] = workbook

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
        if not isinstance(other, OperateObjectPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
