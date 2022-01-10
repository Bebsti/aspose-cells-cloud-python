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


class Hyperlinks(object):
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
        'count': 'int',
        'hyperlink_list': 'list[LinkElement]'
    }

    attribute_map = {
        'link': 'link',
        'count': 'Count',
        'hyperlink_list': 'HyperlinkList'
    }
    
    @staticmethod
    def get_swagger_types():
        return Hyperlinks.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Hyperlinks.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, count=None, hyperlink_list=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Hyperlinks - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['count'] = None
        self.container['hyperlink_list'] = None

        if link is not None:
          self.link = link
        self.count = count
        if hyperlink_list is not None:
          self.hyperlink_list = hyperlink_list

    @property
    def link(self):
        """
        Gets the link of this Hyperlinks.

        :return: The link of this Hyperlinks.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Hyperlinks.

        :param link: The link of this Hyperlinks.
        :type: Link
        """

        self.container['link'] = link

    @property
    def count(self):
        """
        Gets the count of this Hyperlinks.

        :return: The count of this Hyperlinks.
        :rtype: int
        """
        return self.container['count']

    @count.setter
    def count(self, count):
        """
        Sets the count of this Hyperlinks.

        :param count: The count of this Hyperlinks.
        :type: int
        """
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")
        """

        self.container['count'] = count

    @property
    def hyperlink_list(self):
        """
        Gets the hyperlink_list of this Hyperlinks.

        :return: The hyperlink_list of this Hyperlinks.
        :rtype: list[LinkElement]
        """
        return self.container['hyperlink_list']

    @hyperlink_list.setter
    def hyperlink_list(self, hyperlink_list):
        """
        Sets the hyperlink_list of this Hyperlinks.

        :param hyperlink_list: The hyperlink_list of this Hyperlinks.
        :type: list[LinkElement]
        """

        self.container['hyperlink_list'] = hyperlink_list

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
        if not isinstance(other, Hyperlinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
