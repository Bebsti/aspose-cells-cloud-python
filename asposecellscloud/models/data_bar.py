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


class DataBar(object):
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
        'direction': 'str',
        'max_cfvo': 'ConditionalFormattingValue',
        'color': 'Color',
        'min_length': 'int',
        'bar_fill_type': 'str',
        'min_cfvo': 'ConditionalFormattingValue',
        'axis_position': 'str',
        'negative_bar_format': 'NegativeBarFormat',
        'bar_border': 'DataBarBorder',
        'axis_color': 'Color',
        'max_length': 'int',
        'show_value': 'bool'
    }

    attribute_map = {
        'direction': 'Direction',
        'max_cfvo': 'MaxCfvo',
        'color': 'Color',
        'min_length': 'MinLength',
        'bar_fill_type': 'BarFillType',
        'min_cfvo': 'MinCfvo',
        'axis_position': 'AxisPosition',
        'negative_bar_format': 'NegativeBarFormat',
        'bar_border': 'BarBorder',
        'axis_color': 'AxisColor',
        'max_length': 'MaxLength',
        'show_value': 'ShowValue'
    }
    
    @staticmethod
    def get_swagger_types():
        return DataBar.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return DataBar.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, direction=None, max_cfvo=None, color=None, min_length=None, bar_fill_type=None, min_cfvo=None, axis_position=None, negative_bar_format=None, bar_border=None, axis_color=None, max_length=None, show_value=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        DataBar - a model defined in Swagger
        """

        self.container['direction'] = None
        self.container['max_cfvo'] = None
        self.container['color'] = None
        self.container['min_length'] = None
        self.container['bar_fill_type'] = None
        self.container['min_cfvo'] = None
        self.container['axis_position'] = None
        self.container['negative_bar_format'] = None
        self.container['bar_border'] = None
        self.container['axis_color'] = None
        self.container['max_length'] = None
        self.container['show_value'] = None

        if direction is not None:
          self.direction = direction
        if max_cfvo is not None:
          self.max_cfvo = max_cfvo
        if color is not None:
          self.color = color
        if min_length is not None:
          self.min_length = min_length
        if bar_fill_type is not None:
          self.bar_fill_type = bar_fill_type
        if min_cfvo is not None:
          self.min_cfvo = min_cfvo
        if axis_position is not None:
          self.axis_position = axis_position
        if negative_bar_format is not None:
          self.negative_bar_format = negative_bar_format
        if bar_border is not None:
          self.bar_border = bar_border
        if axis_color is not None:
          self.axis_color = axis_color
        if max_length is not None:
          self.max_length = max_length
        if show_value is not None:
          self.show_value = show_value

    @property
    def direction(self):
        """
        Gets the direction of this DataBar.
        Gets or sets the direction the databar is displayed.

        :return: The direction of this DataBar.
        :rtype: str
        """
        return self.container['direction']

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this DataBar.
        Gets or sets the direction the databar is displayed.

        :param direction: The direction of this DataBar.
        :type: str
        """

        self.container['direction'] = direction

    @property
    def max_cfvo(self):
        """
        Gets the max_cfvo of this DataBar.
        Get or set this DataBar's max value object.  Cannot set null or CFValueObject    with type FormatConditionValueType.Min to it.             

        :return: The max_cfvo of this DataBar.
        :rtype: ConditionalFormattingValue
        """
        return self.container['max_cfvo']

    @max_cfvo.setter
    def max_cfvo(self, max_cfvo):
        """
        Sets the max_cfvo of this DataBar.
        Get or set this DataBar's max value object.  Cannot set null or CFValueObject    with type FormatConditionValueType.Min to it.             

        :param max_cfvo: The max_cfvo of this DataBar.
        :type: ConditionalFormattingValue
        """

        self.container['max_cfvo'] = max_cfvo

    @property
    def color(self):
        """
        Gets the color of this DataBar.
        Get or set this DataBar's Color.             

        :return: The color of this DataBar.
        :rtype: Color
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this DataBar.
        Get or set this DataBar's Color.             

        :param color: The color of this DataBar.
        :type: Color
        """

        self.container['color'] = color

    @property
    def min_length(self):
        """
        Gets the min_length of this DataBar.
        Represents the min length of data bar .             

        :return: The min_length of this DataBar.
        :rtype: int
        """
        return self.container['min_length']

    @min_length.setter
    def min_length(self, min_length):
        """
        Sets the min_length of this DataBar.
        Represents the min length of data bar .             

        :param min_length: The min_length of this DataBar.
        :type: int
        """

        self.container['min_length'] = min_length

    @property
    def bar_fill_type(self):
        """
        Gets the bar_fill_type of this DataBar.
        Gets or sets how a data bar is filled with color.

        :return: The bar_fill_type of this DataBar.
        :rtype: str
        """
        return self.container['bar_fill_type']

    @bar_fill_type.setter
    def bar_fill_type(self, bar_fill_type):
        """
        Sets the bar_fill_type of this DataBar.
        Gets or sets how a data bar is filled with color.

        :param bar_fill_type: The bar_fill_type of this DataBar.
        :type: str
        """

        self.container['bar_fill_type'] = bar_fill_type

    @property
    def min_cfvo(self):
        """
        Gets the min_cfvo of this DataBar.
        Get or set this DataBar's min value object.  Cannot set null or CFValueObject   with type FormatConditionValueType.Max to it.             

        :return: The min_cfvo of this DataBar.
        :rtype: ConditionalFormattingValue
        """
        return self.container['min_cfvo']

    @min_cfvo.setter
    def min_cfvo(self, min_cfvo):
        """
        Sets the min_cfvo of this DataBar.
        Get or set this DataBar's min value object.  Cannot set null or CFValueObject   with type FormatConditionValueType.Max to it.             

        :param min_cfvo: The min_cfvo of this DataBar.
        :type: ConditionalFormattingValue
        """

        self.container['min_cfvo'] = min_cfvo

    @property
    def axis_position(self):
        """
        Gets the axis_position of this DataBar.
        Gets or sets the position of the axis of the data bars specified by a conditional    formatting rule.

        :return: The axis_position of this DataBar.
        :rtype: str
        """
        return self.container['axis_position']

    @axis_position.setter
    def axis_position(self, axis_position):
        """
        Sets the axis_position of this DataBar.
        Gets or sets the position of the axis of the data bars specified by a conditional    formatting rule.

        :param axis_position: The axis_position of this DataBar.
        :type: str
        """

        self.container['axis_position'] = axis_position

    @property
    def negative_bar_format(self):
        """
        Gets the negative_bar_format of this DataBar.
        Gets the NegativeBarFormat object associated with a data bar conditional     formatting rule.

        :return: The negative_bar_format of this DataBar.
        :rtype: NegativeBarFormat
        """
        return self.container['negative_bar_format']

    @negative_bar_format.setter
    def negative_bar_format(self, negative_bar_format):
        """
        Sets the negative_bar_format of this DataBar.
        Gets the NegativeBarFormat object associated with a data bar conditional     formatting rule.

        :param negative_bar_format: The negative_bar_format of this DataBar.
        :type: NegativeBarFormat
        """

        self.container['negative_bar_format'] = negative_bar_format

    @property
    def bar_border(self):
        """
        Gets the bar_border of this DataBar.
        Gets an object that specifies the border of a data bar.

        :return: The bar_border of this DataBar.
        :rtype: DataBarBorder
        """
        return self.container['bar_border']

    @bar_border.setter
    def bar_border(self, bar_border):
        """
        Sets the bar_border of this DataBar.
        Gets an object that specifies the border of a data bar.

        :param bar_border: The bar_border of this DataBar.
        :type: DataBarBorder
        """

        self.container['bar_border'] = bar_border

    @property
    def axis_color(self):
        """
        Gets the axis_color of this DataBar.
        Gets the color of the axis for cells with conditional formatting as data bars.

        :return: The axis_color of this DataBar.
        :rtype: Color
        """
        return self.container['axis_color']

    @axis_color.setter
    def axis_color(self, axis_color):
        """
        Sets the axis_color of this DataBar.
        Gets the color of the axis for cells with conditional formatting as data bars.

        :param axis_color: The axis_color of this DataBar.
        :type: Color
        """

        self.container['axis_color'] = axis_color

    @property
    def max_length(self):
        """
        Gets the max_length of this DataBar.
        Represents the max length of data bar .

        :return: The max_length of this DataBar.
        :rtype: int
        """
        return self.container['max_length']

    @max_length.setter
    def max_length(self, max_length):
        """
        Sets the max_length of this DataBar.
        Represents the max length of data bar .

        :param max_length: The max_length of this DataBar.
        :type: int
        """

        self.container['max_length'] = max_length

    @property
    def show_value(self):
        """
        Gets the show_value of this DataBar.
        Get or set the flag indicating whether to show the values of the cells on   which this data bar is applied.  Default value is true.             

        :return: The show_value of this DataBar.
        :rtype: bool
        """
        return self.container['show_value']

    @show_value.setter
    def show_value(self, show_value):
        """
        Sets the show_value of this DataBar.
        Get or set the flag indicating whether to show the values of the cells on   which this data bar is applied.  Default value is true.             

        :param show_value: The show_value of this DataBar.
        :type: bool
        """

        self.container['show_value'] = show_value

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
        if not isinstance(other, DataBar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
