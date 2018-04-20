# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConditionalFormattings(object):
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
        'conditional_formatting_list': 'list[ConditionalFormatting]'
    }

    attribute_map = {
        'link': 'link',
        'count': 'Count',
        'conditional_formatting_list': 'ConditionalFormattingList'
    }
    
    @staticmethod
    def get_swagger_types():
        return ConditionalFormattings.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return ConditionalFormattings.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, count=None, conditional_formatting_list=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        ConditionalFormattings - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['count'] = None
        self.container['conditional_formatting_list'] = None

        if link is not None:
          self.link = link
        self.count = count
        if conditional_formatting_list is not None:
          self.conditional_formatting_list = conditional_formatting_list

    @property
    def link(self):
        """
        Gets the link of this ConditionalFormattings.

        :return: The link of this ConditionalFormattings.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this ConditionalFormattings.

        :param link: The link of this ConditionalFormattings.
        :type: Link
        """

        self.container['link'] = link

    @property
    def count(self):
        """
        Gets the count of this ConditionalFormattings.

        :return: The count of this ConditionalFormattings.
        :rtype: int
        """
        return self.container['count']

    @count.setter
    def count(self, count):
        """
        Sets the count of this ConditionalFormattings.

        :param count: The count of this ConditionalFormattings.
        :type: int
        """
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")
        """

        self.container['count'] = count

    @property
    def conditional_formatting_list(self):
        """
        Gets the conditional_formatting_list of this ConditionalFormattings.

        :return: The conditional_formatting_list of this ConditionalFormattings.
        :rtype: list[ConditionalFormatting]
        """
        return self.container['conditional_formatting_list']

    @conditional_formatting_list.setter
    def conditional_formatting_list(self, conditional_formatting_list):
        """
        Sets the conditional_formatting_list of this ConditionalFormattings.

        :param conditional_formatting_list: The conditional_formatting_list of this ConditionalFormattings.
        :type: list[ConditionalFormatting]
        """

        self.container['conditional_formatting_list'] = conditional_formatting_list

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
        if not isinstance(other, ConditionalFormattings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
