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


class ColorFilter(object):
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
        'color': 'CellsColor',
        'pattern': 'str',
        'background_color': 'CellsColor',
        'foreground_color_color': 'CellsColor',
        'filter_by_fill_color': 'str'
    }

    attribute_map = {
        'color': 'Color',
        'pattern': 'Pattern',
        'background_color': 'BackgroundColor',
        'foreground_color_color': 'ForegroundColorColor',
        'filter_by_fill_color': 'FilterByFillColor'
    }
    
    @staticmethod
    def get_swagger_types():
        return ColorFilter.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ColorFilter.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, color=None, pattern=None, background_color=None, foreground_color_color=None, filter_by_fill_color=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ColorFilter - a model defined in Swagger
        """

        self.container['color'] = None
        self.container['pattern'] = None
        self.container['background_color'] = None
        self.container['foreground_color_color'] = None
        self.container['filter_by_fill_color'] = None

        if color is not None:
          self.color = color
        if pattern is not None:
          self.pattern = pattern
        if background_color is not None:
          self.background_color = background_color
        if foreground_color_color is not None:
          self.foreground_color_color = foreground_color_color
        if filter_by_fill_color is not None:
          self.filter_by_fill_color = filter_by_fill_color

    @property
    def color(self):
        """
        Gets the color of this ColorFilter.

        :return: The color of this ColorFilter.
        :rtype: CellsColor
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this ColorFilter.

        :param color: The color of this ColorFilter.
        :type: CellsColor
        """

        self.container['color'] = color

    @property
    def pattern(self):
        """
        Gets the pattern of this ColorFilter.

        :return: The pattern of this ColorFilter.
        :rtype: str
        """
        return self.container['pattern']

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this ColorFilter.

        :param pattern: The pattern of this ColorFilter.
        :type: str
        """

        self.container['pattern'] = pattern

    @property
    def background_color(self):
        """
        Gets the background_color of this ColorFilter.

        :return: The background_color of this ColorFilter.
        :rtype: CellsColor
        """
        return self.container['background_color']

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color of this ColorFilter.

        :param background_color: The background_color of this ColorFilter.
        :type: CellsColor
        """

        self.container['background_color'] = background_color

    @property
    def foreground_color_color(self):
        """
        Gets the foreground_color_color of this ColorFilter.

        :return: The foreground_color_color of this ColorFilter.
        :rtype: CellsColor
        """
        return self.container['foreground_color_color']

    @foreground_color_color.setter
    def foreground_color_color(self, foreground_color_color):
        """
        Sets the foreground_color_color of this ColorFilter.

        :param foreground_color_color: The foreground_color_color of this ColorFilter.
        :type: CellsColor
        """

        self.container['foreground_color_color'] = foreground_color_color

    @property
    def filter_by_fill_color(self):
        """
        Gets the filter_by_fill_color of this ColorFilter.

        :return: The filter_by_fill_color of this ColorFilter.
        :rtype: str
        """
        return self.container['filter_by_fill_color']

    @filter_by_fill_color.setter
    def filter_by_fill_color(self, filter_by_fill_color):
        """
        Sets the filter_by_fill_color of this ColorFilter.

        :param filter_by_fill_color: The filter_by_fill_color of this ColorFilter.
        :type: str
        """

        self.container['filter_by_fill_color'] = filter_by_fill_color

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
        if not isinstance(other, ColorFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
