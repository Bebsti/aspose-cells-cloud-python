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


class Validation(object):
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
        'link': 'Link',
        'formula2': 'str',
        'formula1': 'str',
        'show_error': 'bool',
        'error_message': 'str',
        'in_cell_drop_down': 'bool',
        'show_input': 'bool',
        'alert_style': 'str',
        'input_title': 'str',
        'ignore_blank': 'bool',
        'value2': 'str',
        'value1': 'str',
        'operator': 'str',
        'error_title': 'str',
        'type': 'str',
        'input_message': 'str',
        'area_list': 'list[CellArea]'
    }

    attribute_map = {
        'link': 'link',
        'formula2': 'Formula2',
        'formula1': 'Formula1',
        'show_error': 'ShowError',
        'error_message': 'ErrorMessage',
        'in_cell_drop_down': 'InCellDropDown',
        'show_input': 'ShowInput',
        'alert_style': 'AlertStyle',
        'input_title': 'InputTitle',
        'ignore_blank': 'IgnoreBlank',
        'value2': 'Value2',
        'value1': 'Value1',
        'operator': 'Operator',
        'error_title': 'ErrorTitle',
        'type': 'Type',
        'input_message': 'InputMessage',
        'area_list': 'AreaList'
    }
    
    @staticmethod
    def get_swagger_types():
        return Validation.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Validation.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, formula2=None, formula1=None, show_error=None, error_message=None, in_cell_drop_down=None, show_input=None, alert_style=None, input_title=None, ignore_blank=None, value2=None, value1=None, operator=None, error_title=None, type=None, input_message=None, area_list=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Validation - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['formula2'] = None
        self.container['formula1'] = None
        self.container['show_error'] = None
        self.container['error_message'] = None
        self.container['in_cell_drop_down'] = None
        self.container['show_input'] = None
        self.container['alert_style'] = None
        self.container['input_title'] = None
        self.container['ignore_blank'] = None
        self.container['value2'] = None
        self.container['value1'] = None
        self.container['operator'] = None
        self.container['error_title'] = None
        self.container['type'] = None
        self.container['input_message'] = None
        self.container['area_list'] = None

        if link is not None:
          self.link = link
        if formula2 is not None:
          self.formula2 = formula2
        if formula1 is not None:
          self.formula1 = formula1
        if show_error is not None:
          self.show_error = show_error
        if error_message is not None:
          self.error_message = error_message
        if in_cell_drop_down is not None:
          self.in_cell_drop_down = in_cell_drop_down
        if show_input is not None:
          self.show_input = show_input
        if alert_style is not None:
          self.alert_style = alert_style
        if input_title is not None:
          self.input_title = input_title
        if ignore_blank is not None:
          self.ignore_blank = ignore_blank
        if value2 is not None:
          self.value2 = value2
        if value1 is not None:
          self.value1 = value1
        if operator is not None:
          self.operator = operator
        if error_title is not None:
          self.error_title = error_title
        if type is not None:
          self.type = type
        if input_message is not None:
          self.input_message = input_message
        if area_list is not None:
          self.area_list = area_list

    @property
    def link(self):
        """
        Gets the link of this Validation.

        :return: The link of this Validation.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Validation.

        :param link: The link of this Validation.
        :type: Link
        """

        self.container['link'] = link

    @property
    def formula2(self):
        """
        Gets the formula2 of this Validation.
        Represents the value or expression associated with the second part of the    data validation.             

        :return: The formula2 of this Validation.
        :rtype: str
        """
        return self.container['formula2']

    @formula2.setter
    def formula2(self, formula2):
        """
        Sets the formula2 of this Validation.
        Represents the value or expression associated with the second part of the    data validation.             

        :param formula2: The formula2 of this Validation.
        :type: str
        """

        self.container['formula2'] = formula2

    @property
    def formula1(self):
        """
        Gets the formula1 of this Validation.
        Represents the value or expression associated with the data validation.

        :return: The formula1 of this Validation.
        :rtype: str
        """
        return self.container['formula1']

    @formula1.setter
    def formula1(self, formula1):
        """
        Sets the formula1 of this Validation.
        Represents the value or expression associated with the data validation.

        :param formula1: The formula1 of this Validation.
        :type: str
        """

        self.container['formula1'] = formula1

    @property
    def show_error(self):
        """
        Gets the show_error of this Validation.
        Indicates whether the data validation error message will be displayed whenever    the user enters invalid data.

        :return: The show_error of this Validation.
        :rtype: bool
        """
        return self.container['show_error']

    @show_error.setter
    def show_error(self, show_error):
        """
        Sets the show_error of this Validation.
        Indicates whether the data validation error message will be displayed whenever    the user enters invalid data.

        :param show_error: The show_error of this Validation.
        :type: bool
        """

        self.container['show_error'] = show_error

    @property
    def error_message(self):
        """
        Gets the error_message of this Validation.
        Represents the data validation error message.

        :return: The error_message of this Validation.
        :rtype: str
        """
        return self.container['error_message']

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this Validation.
        Represents the data validation error message.

        :param error_message: The error_message of this Validation.
        :type: str
        """

        self.container['error_message'] = error_message

    @property
    def in_cell_drop_down(self):
        """
        Gets the in_cell_drop_down of this Validation.
        Indicates whether data validation displays a drop-down list that contains    acceptable values.

        :return: The in_cell_drop_down of this Validation.
        :rtype: bool
        """
        return self.container['in_cell_drop_down']

    @in_cell_drop_down.setter
    def in_cell_drop_down(self, in_cell_drop_down):
        """
        Sets the in_cell_drop_down of this Validation.
        Indicates whether data validation displays a drop-down list that contains    acceptable values.

        :param in_cell_drop_down: The in_cell_drop_down of this Validation.
        :type: bool
        """

        self.container['in_cell_drop_down'] = in_cell_drop_down

    @property
    def show_input(self):
        """
        Gets the show_input of this Validation.
        Indicates whether the data validation input message will be displayed whenever    the user selects a cell in the data validation range.

        :return: The show_input of this Validation.
        :rtype: bool
        """
        return self.container['show_input']

    @show_input.setter
    def show_input(self, show_input):
        """
        Sets the show_input of this Validation.
        Indicates whether the data validation input message will be displayed whenever    the user selects a cell in the data validation range.

        :param show_input: The show_input of this Validation.
        :type: bool
        """

        self.container['show_input'] = show_input

    @property
    def alert_style(self):
        """
        Gets the alert_style of this Validation.
        Represents the validation alert style.Information,Stop,Warning             

        :return: The alert_style of this Validation.
        :rtype: str
        """
        return self.container['alert_style']

    @alert_style.setter
    def alert_style(self, alert_style):
        """
        Sets the alert_style of this Validation.
        Represents the validation alert style.Information,Stop,Warning             

        :param alert_style: The alert_style of this Validation.
        :type: str
        """

        self.container['alert_style'] = alert_style

    @property
    def input_title(self):
        """
        Gets the input_title of this Validation.
        Represents the title of the data-validation input dialog box.

        :return: The input_title of this Validation.
        :rtype: str
        """
        return self.container['input_title']

    @input_title.setter
    def input_title(self, input_title):
        """
        Sets the input_title of this Validation.
        Represents the title of the data-validation input dialog box.

        :param input_title: The input_title of this Validation.
        :type: str
        """

        self.container['input_title'] = input_title

    @property
    def ignore_blank(self):
        """
        Gets the ignore_blank of this Validation.
        Indicates whether blank values are permitted by the range data validation.

        :return: The ignore_blank of this Validation.
        :rtype: bool
        """
        return self.container['ignore_blank']

    @ignore_blank.setter
    def ignore_blank(self, ignore_blank):
        """
        Sets the ignore_blank of this Validation.
        Indicates whether blank values are permitted by the range data validation.

        :param ignore_blank: The ignore_blank of this Validation.
        :type: bool
        """

        self.container['ignore_blank'] = ignore_blank

    @property
    def value2(self):
        """
        Gets the value2 of this Validation.
        Represents the first value associated with the data validation.             

        :return: The value2 of this Validation.
        :rtype: str
        """
        return self.container['value2']

    @value2.setter
    def value2(self, value2):
        """
        Sets the value2 of this Validation.
        Represents the first value associated with the data validation.             

        :param value2: The value2 of this Validation.
        :type: str
        """

        self.container['value2'] = value2

    @property
    def value1(self):
        """
        Gets the value1 of this Validation.
        Represents the first value associated with the data validation.

        :return: The value1 of this Validation.
        :rtype: str
        """
        return self.container['value1']

    @value1.setter
    def value1(self, value1):
        """
        Sets the value1 of this Validation.
        Represents the first value associated with the data validation.

        :param value1: The value1 of this Validation.
        :type: str
        """

        self.container['value1'] = value1

    @property
    def operator(self):
        """
        Gets the operator of this Validation.
        Represents the operator for the data validation. Between,Equal,GreaterThan,GreaterOrEqual,LessThan,LessOrEqual,None,NotBetween,NotEqual

        :return: The operator of this Validation.
        :rtype: str
        """
        return self.container['operator']

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this Validation.
        Represents the operator for the data validation. Between,Equal,GreaterThan,GreaterOrEqual,LessThan,LessOrEqual,None,NotBetween,NotEqual

        :param operator: The operator of this Validation.
        :type: str
        """

        self.container['operator'] = operator

    @property
    def error_title(self):
        """
        Gets the error_title of this Validation.
        Represents the title of the data-validation error dialog box.

        :return: The error_title of this Validation.
        :rtype: str
        """
        return self.container['error_title']

    @error_title.setter
    def error_title(self, error_title):
        """
        Sets the error_title of this Validation.
        Represents the title of the data-validation error dialog box.

        :param error_title: The error_title of this Validation.
        :type: str
        """

        self.container['error_title'] = error_title

    @property
    def type(self):
        """
        Gets the type of this Validation.
        Represents the data validation type. AnyValue ,WholeNumber,Decimal,List,Date,Time,TextLength,Custom             

        :return: The type of this Validation.
        :rtype: str
        """
        return self.container['type']

    @type.setter
    def type(self, type):
        """
        Sets the type of this Validation.
        Represents the data validation type. AnyValue ,WholeNumber,Decimal,List,Date,Time,TextLength,Custom             

        :param type: The type of this Validation.
        :type: str
        """

        self.container['type'] = type

    @property
    def input_message(self):
        """
        Gets the input_message of this Validation.
        Represents the data validation input message.

        :return: The input_message of this Validation.
        :rtype: str
        """
        return self.container['input_message']

    @input_message.setter
    def input_message(self, input_message):
        """
        Sets the input_message of this Validation.
        Represents the data validation input message.

        :param input_message: The input_message of this Validation.
        :type: str
        """

        self.container['input_message'] = input_message

    @property
    def area_list(self):
        """
        Gets the area_list of this Validation.
        Represents a collection of Aspose.Cells.CellArea which contains the data     validation settings.

        :return: The area_list of this Validation.
        :rtype: list[CellArea]
        """
        return self.container['area_list']

    @area_list.setter
    def area_list(self, area_list):
        """
        Sets the area_list of this Validation.
        Represents a collection of Aspose.Cells.CellArea which contains the data     validation settings.

        :param area_list: The area_list of this Validation.
        :type: list[CellArea]
        """

        self.container['area_list'] = area_list

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
        if not isinstance(other, Validation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
