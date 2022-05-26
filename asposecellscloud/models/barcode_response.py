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


class BarcodeResponse(object):
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
        'barcode_value': 'str',
        'barcode_type': 'str',
        'checksum': 'str'
    }

    attribute_map = {
        'barcode_value': 'BarcodeValue',
        'barcode_type': 'BarcodeType',
        'checksum': 'Checksum'
    }
    
    @staticmethod
    def get_swagger_types():
        return BarcodeResponse.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return BarcodeResponse.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, barcode_value=None, barcode_type=None, checksum=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        BarcodeResponse - a model defined in Swagger
        """

        self.container['barcode_value'] = None
        self.container['barcode_type'] = None
        self.container['checksum'] = None

        if barcode_value is not None:
          self.barcode_value = barcode_value
        if barcode_type is not None:
          self.barcode_type = barcode_type
        if checksum is not None:
          self.checksum = checksum


    @property
    def barcode_value(self):
        """
        Gets the barcode_value of this BarcodeResponse.

        :return: The barcode_value of this BarcodeResponse.
        :rtype: str
        """
        return self.container['barcode_value']

    @barcode_value.setter
    def barcode_value(self, barcode_value):
        """
        Sets the barcode_value of this BarcodeResponse.

        :param barcode_value: The barcode_value of this BarcodeResponse.
        :type: str
        """

        self.container['barcode_value'] = barcode_value

    @property
    def barcode_type(self):
        """
        Gets the barcode_type of this BarcodeResponse.

        :return: The barcode_type of this BarcodeResponse.
        :rtype: str
        """
        return self.container['barcode_type']

    @barcode_type.setter
    def barcode_type(self, barcode_type):
        """
        Sets the barcode_type of this BarcodeResponse.

        :param barcode_type: The barcode_type of this BarcodeResponse.
        :type: str
        """

        self.container['barcode_type'] = barcode_type

    @property
    def checksum(self):
        """
        Gets the checksum of this BarcodeResponse.

        :return: The checksum of this BarcodeResponse.
        :rtype: str
        """
        return self.container['checksum']

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this BarcodeResponse.

        :param checksum: The checksum of this BarcodeResponse.
        :type: str
        """

        self.container['checksum'] = checksum


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
        if not isinstance(other, BarcodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
