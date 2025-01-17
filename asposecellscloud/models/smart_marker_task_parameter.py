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

class SmartMarkerTaskParameter(TaskParameter):
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
        'source_workbook': 'FileSource',
        'xml_file': 'FileSource',
        'destination_workbook': 'FileSource'
    }

    attribute_map = {
        'source_workbook': 'SourceWorkbook',
        'xml_file': 'xmlFile',
        'destination_workbook': 'DestinationWorkbook'
    }
    
    @staticmethod
    def get_swagger_types():
        return dict(SmartMarkerTaskParameter.swagger_types, **TaskParameter.get_swagger_types())
    
    @staticmethod
    def get_attribute_map():
        return dict(SmartMarkerTaskParameter.attribute_map, **TaskParameter.get_attribute_map())
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, source_workbook=None, xml_file=None, destination_workbook=None, **kw):
        super(SmartMarkerTaskParameter, self).__init__(**kw)
		    
        """
        SmartMarkerTaskParameter - a model defined in Swagger
        """

        self.container['source_workbook'] = None
        self.container['xml_file'] = None
        self.container['destination_workbook'] = None

        if source_workbook is not None:
          self.source_workbook = source_workbook
        if xml_file is not None:
          self.xml_file = xml_file
        if destination_workbook is not None:
          self.destination_workbook = destination_workbook

    @property
    def source_workbook(self):
        """
        Gets the source_workbook of this SmartMarkerTaskParameter.

        :return: The source_workbook of this SmartMarkerTaskParameter.
        :rtype: FileSource
        """
        return self.container['source_workbook']

    @source_workbook.setter
    def source_workbook(self, source_workbook):
        """
        Sets the source_workbook of this SmartMarkerTaskParameter.

        :param source_workbook: The source_workbook of this SmartMarkerTaskParameter.
        :type: FileSource
        """

        self.container['source_workbook'] = source_workbook

    @property
    def xml_file(self):
        """
        Gets the xml_file of this SmartMarkerTaskParameter.

        :return: The xml_file of this SmartMarkerTaskParameter.
        :rtype: FileSource
        """
        return self.container['xml_file']

    @xml_file.setter
    def xml_file(self, xml_file):
        """
        Sets the xml_file of this SmartMarkerTaskParameter.

        :param xml_file: The xml_file of this SmartMarkerTaskParameter.
        :type: FileSource
        """

        self.container['xml_file'] = xml_file

    @property
    def destination_workbook(self):
        """
        Gets the destination_workbook of this SmartMarkerTaskParameter.

        :return: The destination_workbook of this SmartMarkerTaskParameter.
        :rtype: FileSource
        """
        return self.container['destination_workbook']

    @destination_workbook.setter
    def destination_workbook(self, destination_workbook):
        """
        Sets the destination_workbook of this SmartMarkerTaskParameter.

        :param destination_workbook: The destination_workbook of this SmartMarkerTaskParameter.
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
        if not isinstance(other, SmartMarkerTaskParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
