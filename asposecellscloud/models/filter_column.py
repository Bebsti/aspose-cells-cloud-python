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


class FilterColumn(object):
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
        'filter_type': 'str',
        'multiple_filters': 'MultipleFilters',
        'custom_filters': 'list[CustomFilter]',
        'dynamic_filter': 'DynamicFilter',
        'color_filter': 'ColorFilter',
        'field_index': 'int',
        'top10_filter': 'Top10Filter',
        'icon_filter': 'IconFilter',
        'visibledropdown': 'str'
    }

    attribute_map = {
        'filter_type': 'FilterType',
        'multiple_filters': 'MultipleFilters',
        'custom_filters': 'CustomFilters',
        'dynamic_filter': 'DynamicFilter',
        'color_filter': 'ColorFilter',
        'field_index': 'FieldIndex',
        'top10_filter': 'Top10Filter',
        'icon_filter': 'IconFilter',
        'visibledropdown': 'Visibledropdown'
    }
    
    @staticmethod
    def get_swagger_types():
        return FilterColumn.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return FilterColumn.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, filter_type=None, multiple_filters=None, custom_filters=None, dynamic_filter=None, color_filter=None, field_index=None, top10_filter=None, icon_filter=None, visibledropdown=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        FilterColumn - a model defined in Swagger
        """

        self.container['filter_type'] = None
        self.container['multiple_filters'] = None
        self.container['custom_filters'] = None
        self.container['dynamic_filter'] = None
        self.container['color_filter'] = None
        self.container['field_index'] = None
        self.container['top10_filter'] = None
        self.container['icon_filter'] = None
        self.container['visibledropdown'] = None

        if filter_type is not None:
          self.filter_type = filter_type
        if multiple_filters is not None:
          self.multiple_filters = multiple_filters
        if custom_filters is not None:
          self.custom_filters = custom_filters
        if dynamic_filter is not None:
          self.dynamic_filter = dynamic_filter
        if color_filter is not None:
          self.color_filter = color_filter
        self.field_index = field_index
        if top10_filter is not None:
          self.top10_filter = top10_filter
        if icon_filter is not None:
          self.icon_filter = icon_filter
        if visibledropdown is not None:
          self.visibledropdown = visibledropdown

    @property
    def filter_type(self):
        """
        Gets the filter_type of this FilterColumn.

        :return: The filter_type of this FilterColumn.
        :rtype: str
        """
        return self.container['filter_type']

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this FilterColumn.

        :param filter_type: The filter_type of this FilterColumn.
        :type: str
        """

        self.container['filter_type'] = filter_type

    @property
    def multiple_filters(self):
        """
        Gets the multiple_filters of this FilterColumn.

        :return: The multiple_filters of this FilterColumn.
        :rtype: MultipleFilters
        """
        return self.container['multiple_filters']

    @multiple_filters.setter
    def multiple_filters(self, multiple_filters):
        """
        Sets the multiple_filters of this FilterColumn.

        :param multiple_filters: The multiple_filters of this FilterColumn.
        :type: MultipleFilters
        """

        self.container['multiple_filters'] = multiple_filters

    @property
    def custom_filters(self):
        """
        Gets the custom_filters of this FilterColumn.

        :return: The custom_filters of this FilterColumn.
        :rtype: list[CustomFilter]
        """
        return self.container['custom_filters']

    @custom_filters.setter
    def custom_filters(self, custom_filters):
        """
        Sets the custom_filters of this FilterColumn.

        :param custom_filters: The custom_filters of this FilterColumn.
        :type: list[CustomFilter]
        """

        self.container['custom_filters'] = custom_filters

    @property
    def dynamic_filter(self):
        """
        Gets the dynamic_filter of this FilterColumn.

        :return: The dynamic_filter of this FilterColumn.
        :rtype: DynamicFilter
        """
        return self.container['dynamic_filter']

    @dynamic_filter.setter
    def dynamic_filter(self, dynamic_filter):
        """
        Sets the dynamic_filter of this FilterColumn.

        :param dynamic_filter: The dynamic_filter of this FilterColumn.
        :type: DynamicFilter
        """

        self.container['dynamic_filter'] = dynamic_filter

    @property
    def color_filter(self):
        """
        Gets the color_filter of this FilterColumn.

        :return: The color_filter of this FilterColumn.
        :rtype: ColorFilter
        """
        return self.container['color_filter']

    @color_filter.setter
    def color_filter(self, color_filter):
        """
        Sets the color_filter of this FilterColumn.

        :param color_filter: The color_filter of this FilterColumn.
        :type: ColorFilter
        """

        self.container['color_filter'] = color_filter

    @property
    def field_index(self):
        """
        Gets the field_index of this FilterColumn.

        :return: The field_index of this FilterColumn.
        :rtype: int
        """
        return self.container['field_index']

    @field_index.setter
    def field_index(self, field_index):
        """
        Sets the field_index of this FilterColumn.

        :param field_index: The field_index of this FilterColumn.
        :type: int
        """
        """
        if field_index is None:
            raise ValueError("Invalid value for `field_index`, must not be `None`")
        """

        self.container['field_index'] = field_index

    @property
    def top10_filter(self):
        """
        Gets the top10_filter of this FilterColumn.

        :return: The top10_filter of this FilterColumn.
        :rtype: Top10Filter
        """
        return self.container['top10_filter']

    @top10_filter.setter
    def top10_filter(self, top10_filter):
        """
        Sets the top10_filter of this FilterColumn.

        :param top10_filter: The top10_filter of this FilterColumn.
        :type: Top10Filter
        """

        self.container['top10_filter'] = top10_filter

    @property
    def icon_filter(self):
        """
        Gets the icon_filter of this FilterColumn.

        :return: The icon_filter of this FilterColumn.
        :rtype: IconFilter
        """
        return self.container['icon_filter']

    @icon_filter.setter
    def icon_filter(self, icon_filter):
        """
        Sets the icon_filter of this FilterColumn.

        :param icon_filter: The icon_filter of this FilterColumn.
        :type: IconFilter
        """

        self.container['icon_filter'] = icon_filter

    @property
    def visibledropdown(self):
        """
        Gets the visibledropdown of this FilterColumn.

        :return: The visibledropdown of this FilterColumn.
        :rtype: str
        """
        return self.container['visibledropdown']

    @visibledropdown.setter
    def visibledropdown(self, visibledropdown):
        """
        Sets the visibledropdown of this FilterColumn.

        :param visibledropdown: The visibledropdown of this FilterColumn.
        :type: str
        """

        self.container['visibledropdown'] = visibledropdown

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
        if not isinstance(other, FilterColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
