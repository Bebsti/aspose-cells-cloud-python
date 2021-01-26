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


class GradientFill(object):
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
        'fill_type': 'str',
        'angle': 'float',
        'gradient_stops': 'list[GradientFillStop]',
        'direction_type': 'str'
    }

    attribute_map = {
        'fill_type': 'FillType',
        'angle': 'Angle',
        'gradient_stops': 'GradientStops',
        'direction_type': 'DirectionType'
    }
    
    @staticmethod
    def get_swagger_types():
        return GradientFill.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return GradientFill.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, fill_type=None, angle=None, gradient_stops=None, direction_type=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        GradientFill - a model defined in Swagger
        """

        self.container['fill_type'] = None
        self.container['angle'] = None
        self.container['gradient_stops'] = None
        self.container['direction_type'] = None

        if fill_type is not None:
          self.fill_type = fill_type
        if angle is not None:
          self.angle = angle
        if gradient_stops is not None:
          self.gradient_stops = gradient_stops
        if direction_type is not None:
          self.direction_type = direction_type

    @property
    def fill_type(self):
        """
        Gets the fill_type of this GradientFill.

        :return: The fill_type of this GradientFill.
        :rtype: str
        """
        return self.container['fill_type']

    @fill_type.setter
    def fill_type(self, fill_type):
        """
        Sets the fill_type of this GradientFill.

        :param fill_type: The fill_type of this GradientFill.
        :type: str
        """

        self.container['fill_type'] = fill_type

    @property
    def angle(self):
        """
        Gets the angle of this GradientFill.

        :return: The angle of this GradientFill.
        :rtype: float
        """
        return self.container['angle']

    @angle.setter
    def angle(self, angle):
        """
        Sets the angle of this GradientFill.

        :param angle: The angle of this GradientFill.
        :type: float
        """

        self.container['angle'] = angle

    @property
    def gradient_stops(self):
        """
        Gets the gradient_stops of this GradientFill.

        :return: The gradient_stops of this GradientFill.
        :rtype: list[GradientFillStop]
        """
        return self.container['gradient_stops']

    @gradient_stops.setter
    def gradient_stops(self, gradient_stops):
        """
        Sets the gradient_stops of this GradientFill.

        :param gradient_stops: The gradient_stops of this GradientFill.
        :type: list[GradientFillStop]
        """

        self.container['gradient_stops'] = gradient_stops

    @property
    def direction_type(self):
        """
        Gets the direction_type of this GradientFill.

        :return: The direction_type of this GradientFill.
        :rtype: str
        """
        return self.container['direction_type']

    @direction_type.setter
    def direction_type(self, direction_type):
        """
        Sets the direction_type of this GradientFill.

        :param direction_type: The direction_type of this GradientFill.
        :type: str
        """

        self.container['direction_type'] = direction_type

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
        if not isinstance(other, GradientFill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
