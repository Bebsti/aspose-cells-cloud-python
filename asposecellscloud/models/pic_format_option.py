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


class PicFormatOption(object):
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
        'right': 'float',
        'bottom': 'float',
        'top': 'float',
        'scale': 'float',
        'type': 'str',
        'left': 'float'
    }

    attribute_map = {
        'right': 'Right',
        'bottom': 'Bottom',
        'top': 'Top',
        'scale': 'Scale',
        'type': 'Type',
        'left': 'Left'
    }
    
    @staticmethod
    def get_swagger_types():
        return PicFormatOption.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return PicFormatOption.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, right=None, bottom=None, top=None, scale=None, type=None, left=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        PicFormatOption - a model defined in Swagger
        """

        self.container['right'] = None
        self.container['bottom'] = None
        self.container['top'] = None
        self.container['scale'] = None
        self.container['type'] = None
        self.container['left'] = None

        if right is not None:
          self.right = right
        if bottom is not None:
          self.bottom = bottom
        if top is not None:
          self.top = top
        if scale is not None:
          self.scale = scale
        if type is not None:
          self.type = type
        if left is not None:
          self.left = left

    @property
    def right(self):
        """
        Gets the right of this PicFormatOption.

        :return: The right of this PicFormatOption.
        :rtype: float
        """
        return self.container['right']

    @right.setter
    def right(self, right):
        """
        Sets the right of this PicFormatOption.

        :param right: The right of this PicFormatOption.
        :type: float
        """

        self.container['right'] = right

    @property
    def bottom(self):
        """
        Gets the bottom of this PicFormatOption.

        :return: The bottom of this PicFormatOption.
        :rtype: float
        """
        return self.container['bottom']

    @bottom.setter
    def bottom(self, bottom):
        """
        Sets the bottom of this PicFormatOption.

        :param bottom: The bottom of this PicFormatOption.
        :type: float
        """

        self.container['bottom'] = bottom

    @property
    def top(self):
        """
        Gets the top of this PicFormatOption.

        :return: The top of this PicFormatOption.
        :rtype: float
        """
        return self.container['top']

    @top.setter
    def top(self, top):
        """
        Sets the top of this PicFormatOption.

        :param top: The top of this PicFormatOption.
        :type: float
        """

        self.container['top'] = top

    @property
    def scale(self):
        """
        Gets the scale of this PicFormatOption.

        :return: The scale of this PicFormatOption.
        :rtype: float
        """
        return self.container['scale']

    @scale.setter
    def scale(self, scale):
        """
        Sets the scale of this PicFormatOption.

        :param scale: The scale of this PicFormatOption.
        :type: float
        """

        self.container['scale'] = scale

    @property
    def type(self):
        """
        Gets the type of this PicFormatOption.

        :return: The type of this PicFormatOption.
        :rtype: str
        """
        return self.container['type']

    @type.setter
    def type(self, type):
        """
        Sets the type of this PicFormatOption.

        :param type: The type of this PicFormatOption.
        :type: str
        """

        self.container['type'] = type

    @property
    def left(self):
        """
        Gets the left of this PicFormatOption.

        :return: The left of this PicFormatOption.
        :rtype: float
        """
        return self.container['left']

    @left.setter
    def left(self, left):
        """
        Sets the left of this PicFormatOption.

        :param left: The left of this PicFormatOption.
        :type: float
        """

        self.container['left'] = left

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
        if not isinstance(other, PicFormatOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
