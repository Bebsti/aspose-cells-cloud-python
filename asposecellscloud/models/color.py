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


class Color(object):
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
        'a': 'int',
        'r': 'int',
        'g': 'int',
        'b': 'int'
    }

    attribute_map = {
        'a': 'A',
        'r': 'R',
        'g': 'G',
        'b': 'B'
    }
    
    @staticmethod
    def get_swagger_types():
        return Color.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Color.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, a=None, r=None, g=None, b=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Color - a model defined in Swagger
        """

        self.container['a'] = None
        self.container['r'] = None
        self.container['g'] = None
        self.container['b'] = None

        self.a = a
        self.r = r
        self.g = g
        self.b = b

    @property
    def a(self):
        """
        Gets the a of this Color.

        :return: The a of this Color.
        :rtype: int
        """
        return self.container['a']

    @a.setter
    def a(self, a):
        """
        Sets the a of this Color.

        :param a: The a of this Color.
        :type: int
        """
        """
        if a is None:
            raise ValueError("Invalid value for `a`, must not be `None`")
        """

        self.container['a'] = a

    @property
    def r(self):
        """
        Gets the r of this Color.

        :return: The r of this Color.
        :rtype: int
        """
        return self.container['r']

    @r.setter
    def r(self, r):
        """
        Sets the r of this Color.

        :param r: The r of this Color.
        :type: int
        """
        """
        if r is None:
            raise ValueError("Invalid value for `r`, must not be `None`")
        """

        self.container['r'] = r

    @property
    def g(self):
        """
        Gets the g of this Color.

        :return: The g of this Color.
        :rtype: int
        """
        return self.container['g']

    @g.setter
    def g(self, g):
        """
        Sets the g of this Color.

        :param g: The g of this Color.
        :type: int
        """
        """
        if g is None:
            raise ValueError("Invalid value for `g`, must not be `None`")
        """

        self.container['g'] = g

    @property
    def b(self):
        """
        Gets the b of this Color.

        :return: The b of this Color.
        :rtype: int
        """
        return self.container['b']

    @b.setter
    def b(self, b):
        """
        Sets the b of this Color.

        :param b: The b of this Color.
        :type: int
        """
        """
        if b is None:
            raise ValueError("Invalid value for `b`, must not be `None`")
        """

        self.container['b'] = b

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
        if not isinstance(other, Color):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
