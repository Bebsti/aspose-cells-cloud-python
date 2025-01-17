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
from . import ImportOption

class ImportPictureOption(ImportOption):
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
        'upper_left_row': 'int',
        'upper_left_column': 'int',
        'lower_right_row': 'int',
        'lower_right_column': 'int',
        'filename': 'str',
        'data': 'str'
    }

    attribute_map = {
        'upper_left_row': 'UpperLeftRow',
        'upper_left_column': 'UpperLeftColumn',
        'lower_right_row': 'LowerRightRow',
        'lower_right_column': 'LowerRightColumn',
        'filename': 'Filename',
        'data': 'Data'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(ImportPictureOption.swagger_types, **ImportOption.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(ImportPictureOption.attribute_map, **ImportOption.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, upper_left_row=None, upper_left_column=None, lower_right_row=None, lower_right_column=None, filename=None, data=None, **kw):
        super(ImportPictureOption, self).__init__(**kw)
		    
        """
        ImportPictureOption - a model defined in Swagger
        """

        self.container['upper_left_row'] = None
        self.container['upper_left_column'] = None
        self.container['lower_right_row'] = None
        self.container['lower_right_column'] = None
        self.container['filename'] = None
        self.container['data'] = None

        if upper_left_row is not None:
          self.upper_left_row = upper_left_row
        if upper_left_column is not None:
          self.upper_left_column = upper_left_column
        if lower_right_row is not None:
          self.lower_right_row = lower_right_row
        if lower_right_column is not None:
          self.lower_right_column = lower_right_column
        if filename is not None:
          self.filename = filename
        if data is not None:
          self.data = data

    @property
    def upper_left_row(self):
        """
        Gets the upper_left_row of this ImportPictureOption.
        Upper Left Row.

        :return: The upper_left_row of this ImportPictureOption.
        :rtype: int
        """
        return self.container['upper_left_row']

    @upper_left_row.setter
    def upper_left_row(self, upper_left_row):
        """
        Sets the upper_left_row of this ImportPictureOption.
        Upper Left Row.

        :param upper_left_row: The upper_left_row of this ImportPictureOption.
        :type: int
        """

        self.container['upper_left_row'] = upper_left_row

    @property
    def upper_left_column(self):
        """
        Gets the upper_left_column of this ImportPictureOption.
        Upper Left Column.

        :return: The upper_left_column of this ImportPictureOption.
        :rtype: int
        """
        return self.container['upper_left_column']

    @upper_left_column.setter
    def upper_left_column(self, upper_left_column):
        """
        Sets the upper_left_column of this ImportPictureOption.
        Upper Left Column.

        :param upper_left_column: The upper_left_column of this ImportPictureOption.
        :type: int
        """

        self.container['upper_left_column'] = upper_left_column

    @property
    def lower_right_row(self):
        """
        Gets the lower_right_row of this ImportPictureOption.
        Lower Right Row.

        :return: The lower_right_row of this ImportPictureOption.
        :rtype: int
        """
        return self.container['lower_right_row']

    @lower_right_row.setter
    def lower_right_row(self, lower_right_row):
        """
        Sets the lower_right_row of this ImportPictureOption.
        Lower Right Row.

        :param lower_right_row: The lower_right_row of this ImportPictureOption.
        :type: int
        """

        self.container['lower_right_row'] = lower_right_row

    @property
    def lower_right_column(self):
        """
        Gets the lower_right_column of this ImportPictureOption.
        Lower Right Column.

        :return: The lower_right_column of this ImportPictureOption.
        :rtype: int
        """
        return self.container['lower_right_column']

    @lower_right_column.setter
    def lower_right_column(self, lower_right_column):
        """
        Sets the lower_right_column of this ImportPictureOption.
        Lower Right Column.

        :param lower_right_column: The lower_right_column of this ImportPictureOption.
        :type: int
        """

        self.container['lower_right_column'] = lower_right_column

    @property
    def filename(self):
        """
        Gets the filename of this ImportPictureOption.
        Filename.

        :return: The filename of this ImportPictureOption.
        :rtype: str
        """
        return self.container['filename']

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this ImportPictureOption.
        Filename.

        :param filename: The filename of this ImportPictureOption.
        :type: str
        """

        self.container['filename'] = filename

    @property
    def data(self):
        """
        Gets the data of this ImportPictureOption.
        data : base64  string.

        :return: The data of this ImportPictureOption.
        :rtype: str
        """
        return self.container['data']

    @data.setter
    def data(self, data):
        """
        Sets the data of this ImportPictureOption.
        data : base64  string.

        :param data: The data of this ImportPictureOption.
        :type: str
        """

        self.container['data'] = data

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
        if not isinstance(other, ImportPictureOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
