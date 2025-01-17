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
from . import TaskParameter

class ImportDataTaskParameter(TaskParameter):
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
        'workbook': 'FileSource',
        'import_option': 'ImportOption',
        'destination_workbook': 'FileSource'
    }

    attribute_map = {
        'workbook': 'Workbook',
        'import_option': 'ImportOption',
        'destination_workbook': 'DestinationWorkbook'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(ImportDataTaskParameter.swagger_types, **TaskParameter.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(ImportDataTaskParameter.attribute_map, **TaskParameter.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, workbook=None, import_option=None, destination_workbook=None, **kw):
        super(ImportDataTaskParameter, self).__init__(**kw)
		    
        """
        ImportDataTaskParameter - a model defined in Swagger
        """

        self.container['workbook'] = None
        self.container['import_option'] = None
        self.container['destination_workbook'] = None

        if workbook is not None:
          self.workbook = workbook
        if import_option is not None:
          self.import_option = import_option
        if destination_workbook is not None:
          self.destination_workbook = destination_workbook

    @property
    def workbook(self):
        """
        Gets the workbook of this ImportDataTaskParameter.

        :return: The workbook of this ImportDataTaskParameter.
        :rtype: FileSource
        """
        return self.container['workbook']

    @workbook.setter
    def workbook(self, workbook):
        """
        Sets the workbook of this ImportDataTaskParameter.

        :param workbook: The workbook of this ImportDataTaskParameter.
        :type: FileSource
        """

        self.container['workbook'] = workbook

    @property
    def import_option(self):
        """
        Gets the import_option of this ImportDataTaskParameter.

        :return: The import_option of this ImportDataTaskParameter.
        :rtype: ImportOption
        """
        return self.container['import_option']

    @import_option.setter
    def import_option(self, import_option):
        """
        Sets the import_option of this ImportDataTaskParameter.

        :param import_option: The import_option of this ImportDataTaskParameter.
        :type: ImportOption
        """

        self.container['import_option'] = import_option

    @property
    def destination_workbook(self):
        """
        Gets the destination_workbook of this ImportDataTaskParameter.

        :return: The destination_workbook of this ImportDataTaskParameter.
        :rtype: FileSource
        """
        return self.container['destination_workbook']

    @destination_workbook.setter
    def destination_workbook(self, destination_workbook):
        """
        Sets the destination_workbook of this ImportDataTaskParameter.

        :param destination_workbook: The destination_workbook of this ImportDataTaskParameter.
        :type: FileSource
        """

        self.container['destination_workbook'] = destination_workbook

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
        if not isinstance(other, ImportDataTaskParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
