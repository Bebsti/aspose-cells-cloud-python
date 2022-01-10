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


class GradientFillStop(object):
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
        'color': 'Color',
        'position': 'float',
        'transparency': 'float'
    }

    attribute_map = {
        'color': 'Color',
        'position': 'Position',
        'transparency': 'Transparency'
    }
    
    @staticmethod
    def get_swagger_types():
        return GradientFillStop.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return GradientFillStop.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, color=None, position=None, transparency=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        GradientFillStop - a model defined in Swagger
        """

        self.container['color'] = None
        self.container['position'] = None
        self.container['transparency'] = None

        if color is not None:
          self.color = color
        self.position = position
        self.transparency = transparency

    @property
    def color(self):
        """
        Gets the color of this GradientFillStop.

        :return: The color of this GradientFillStop.
        :rtype: Color
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this GradientFillStop.

        :param color: The color of this GradientFillStop.
        :type: Color
        """

        self.container['color'] = color

    @property
    def position(self):
        """
        Gets the position of this GradientFillStop.

        :return: The position of this GradientFillStop.
        :rtype: float
        """
        return self.container['position']

    @position.setter
    def position(self, position):
        """
        Sets the position of this GradientFillStop.

        :param position: The position of this GradientFillStop.
        :type: float
        """
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")
        """

        self.container['position'] = position

    @property
    def transparency(self):
        """
        Gets the transparency of this GradientFillStop.

        :return: The transparency of this GradientFillStop.
        :rtype: float
        """
        return self.container['transparency']

    @transparency.setter
    def transparency(self, transparency):
        """
        Sets the transparency of this GradientFillStop.

        :param transparency: The transparency of this GradientFillStop.
        :type: float
        """
        """
        if transparency is None:
            raise ValueError("Invalid value for `transparency`, must not be `None`")
        """

        self.container['transparency'] = transparency

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
        if not isinstance(other, GradientFillStop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
