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


class RangeSetOutlineBorderRequest(object):
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
        'border_color': 'Color',
        'range': 'Range',
        'border_style': 'str',
        'border_edge': 'str'
    }

    attribute_map = {
        'border_color': 'BorderColor',
        'range': 'Range',
        'border_style': 'BorderStyle',
        'border_edge': 'BorderEdge'
    }
    
    @staticmethod
    def get_swagger_types():
        return RangeSetOutlineBorderRequest.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return RangeSetOutlineBorderRequest.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, border_color=None, range=None, border_style=None, border_edge=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        RangeSetOutlineBorderRequest - a model defined in Swagger
        """

        self.container['border_color'] = None
        self.container['range'] = None
        self.container['border_style'] = None
        self.container['border_edge'] = None

        if border_color is not None:
          self.border_color = border_color
        if range is not None:
          self.range = range
        if border_style is not None:
          self.border_style = border_style
        if border_edge is not None:
          self.border_edge = border_edge

    @property
    def border_color(self):
        """
        Gets the border_color of this RangeSetOutlineBorderRequest.

        :return: The border_color of this RangeSetOutlineBorderRequest.
        :rtype: Color
        """
        return self.container['border_color']

    @border_color.setter
    def border_color(self, border_color):
        """
        Sets the border_color of this RangeSetOutlineBorderRequest.

        :param border_color: The border_color of this RangeSetOutlineBorderRequest.
        :type: Color
        """

        self.container['border_color'] = border_color

    @property
    def range(self):
        """
        Gets the range of this RangeSetOutlineBorderRequest.

        :return: The range of this RangeSetOutlineBorderRequest.
        :rtype: Range
        """
        return self.container['range']

    @range.setter
    def range(self, range):
        """
        Sets the range of this RangeSetOutlineBorderRequest.

        :param range: The range of this RangeSetOutlineBorderRequest.
        :type: Range
        """

        self.container['range'] = range

    @property
    def border_style(self):
        """
        Gets the border_style of this RangeSetOutlineBorderRequest.

        :return: The border_style of this RangeSetOutlineBorderRequest.
        :rtype: str
        """
        return self.container['border_style']

    @border_style.setter
    def border_style(self, border_style):
        """
        Sets the border_style of this RangeSetOutlineBorderRequest.

        :param border_style: The border_style of this RangeSetOutlineBorderRequest.
        :type: str
        """

        self.container['border_style'] = border_style

    @property
    def border_edge(self):
        """
        Gets the border_edge of this RangeSetOutlineBorderRequest.

        :return: The border_edge of this RangeSetOutlineBorderRequest.
        :rtype: str
        """
        return self.container['border_edge']

    @border_edge.setter
    def border_edge(self, border_edge):
        """
        Sets the border_edge of this RangeSetOutlineBorderRequest.

        :param border_edge: The border_edge of this RangeSetOutlineBorderRequest.
        :type: str
        """

        self.container['border_edge'] = border_edge

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
        if not isinstance(other, RangeSetOutlineBorderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
