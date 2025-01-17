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


class Hyperlink(object):
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
        'screen_tip': 'str',
        'area': 'CellArea',
        'text_to_display': 'str',
        'address': 'str'
    }

    attribute_map = {
        'link': 'link',
        'screen_tip': 'ScreenTip',
        'area': 'Area',
        'text_to_display': 'TextToDisplay',
        'address': 'Address'
    }
    
    @staticmethod
    def get_swagger_types():
        return Hyperlink.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Hyperlink.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, screen_tip=None, area=None, text_to_display=None, address=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Hyperlink - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['screen_tip'] = None
        self.container['area'] = None
        self.container['text_to_display'] = None
        self.container['address'] = None

        if link is not None:
          self.link = link
        if screen_tip is not None:
          self.screen_tip = screen_tip
        if area is not None:
          self.area = area
        if text_to_display is not None:
          self.text_to_display = text_to_display
        if address is not None:
          self.address = address

    @property
    def link(self):
        """
        Gets the link of this Hyperlink.

        :return: The link of this Hyperlink.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Hyperlink.

        :param link: The link of this Hyperlink.
        :type: Link
        """

        self.container['link'] = link

    @property
    def screen_tip(self):
        """
        Gets the screen_tip of this Hyperlink.

        :return: The screen_tip of this Hyperlink.
        :rtype: str
        """
        return self.container['screen_tip']

    @screen_tip.setter
    def screen_tip(self, screen_tip):
        """
        Sets the screen_tip of this Hyperlink.

        :param screen_tip: The screen_tip of this Hyperlink.
        :type: str
        """

        self.container['screen_tip'] = screen_tip

    @property
    def area(self):
        """
        Gets the area of this Hyperlink.

        :return: The area of this Hyperlink.
        :rtype: CellArea
        """
        return self.container['area']

    @area.setter
    def area(self, area):
        """
        Sets the area of this Hyperlink.

        :param area: The area of this Hyperlink.
        :type: CellArea
        """

        self.container['area'] = area

    @property
    def text_to_display(self):
        """
        Gets the text_to_display of this Hyperlink.

        :return: The text_to_display of this Hyperlink.
        :rtype: str
        """
        return self.container['text_to_display']

    @text_to_display.setter
    def text_to_display(self, text_to_display):
        """
        Sets the text_to_display of this Hyperlink.

        :param text_to_display: The text_to_display of this Hyperlink.
        :type: str
        """

        self.container['text_to_display'] = text_to_display

    @property
    def address(self):
        """
        Gets the address of this Hyperlink.

        :return: The address of this Hyperlink.
        :rtype: str
        """
        return self.container['address']

    @address.setter
    def address(self, address):
        """
        Sets the address of this Hyperlink.

        :param address: The address of this Hyperlink.
        :type: str
        """

        self.container['address'] = address

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
        if not isinstance(other, Hyperlink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
