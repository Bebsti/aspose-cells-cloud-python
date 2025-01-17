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


class ImportOption(object):
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
        'source': 'FileSource',
        'import_data_type': 'str',
        'destination_worksheet': 'str',
        'is_insert': 'bool'
    }

    attribute_map = {
        'source': 'Source',
        'import_data_type': 'ImportDataType',
        'destination_worksheet': 'DestinationWorksheet',
        'is_insert': 'IsInsert'
    }
    
    @staticmethod
    def get_swagger_types():
        return ImportOption.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ImportOption.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, source=None, import_data_type=None, destination_worksheet=None, is_insert=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ImportOption - a model defined in Swagger
        """

        self.container['source'] = None
        self.container['import_data_type'] = None
        self.container['destination_worksheet'] = None
        self.container['is_insert'] = None

        if source is not None:
          self.source = source
        if import_data_type is not None:
          self.import_data_type = import_data_type
        if destination_worksheet is not None:
          self.destination_worksheet = destination_worksheet
        if is_insert is not None:
          self.is_insert = is_insert

    @property
    def source(self):
        """
        Gets the source of this ImportOption.

        :return: The source of this ImportOption.
        :rtype: FileSource
        """
        return self.container['source']

    @source.setter
    def source(self, source):
        """
        Sets the source of this ImportOption.

        :param source: The source of this ImportOption.
        :type: FileSource
        """

        self.container['source'] = source

    @property
    def import_data_type(self):
        """
        Gets the import_data_type of this ImportOption.

        :return: The import_data_type of this ImportOption.
        :rtype: str
        """
        return self.container['import_data_type']

    @import_data_type.setter
    def import_data_type(self, import_data_type):
        """
        Sets the import_data_type of this ImportOption.

        :param import_data_type: The import_data_type of this ImportOption.
        :type: str
        """

        self.container['import_data_type'] = import_data_type

    @property
    def destination_worksheet(self):
        """
        Gets the destination_worksheet of this ImportOption.

        :return: The destination_worksheet of this ImportOption.
        :rtype: str
        """
        return self.container['destination_worksheet']

    @destination_worksheet.setter
    def destination_worksheet(self, destination_worksheet):
        """
        Sets the destination_worksheet of this ImportOption.

        :param destination_worksheet: The destination_worksheet of this ImportOption.
        :type: str
        """

        self.container['destination_worksheet'] = destination_worksheet

    @property
    def is_insert(self):
        """
        Gets the is_insert of this ImportOption.

        :return: The is_insert of this ImportOption.
        :rtype: bool
        """
        return self.container['is_insert']

    @is_insert.setter
    def is_insert(self, is_insert):
        """
        Sets the is_insert of this ImportOption.

        :param is_insert: The is_insert of this ImportOption.
        :type: bool
        """

        self.container['is_insert'] = is_insert

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
        if not isinstance(other, ImportOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
