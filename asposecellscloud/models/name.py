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


class Name(object):
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
        'comment': 'str',
        'text': 'str',
        'worksheet_index': 'int',
        'r1_c1_refers_to': 'str',
        'refers_to': 'str',
        'is_referred': 'bool',
        'is_visible': 'bool'
    }

    attribute_map = {
        'link': 'link',
        'comment': 'Comment',
        'text': 'Text',
        'worksheet_index': 'WorksheetIndex',
        'r1_c1_refers_to': 'R1C1RefersTo',
        'refers_to': 'RefersTo',
        'is_referred': 'IsReferred',
        'is_visible': 'IsVisible'
    }
    
    @staticmethod
    def get_swagger_types():
        return Name.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Name.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, comment=None, text=None, worksheet_index=None, r1_c1_refers_to=None, refers_to=None, is_referred=None, is_visible=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Name - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['comment'] = None
        self.container['text'] = None
        self.container['worksheet_index'] = None
        self.container['r1_c1_refers_to'] = None
        self.container['refers_to'] = None
        self.container['is_referred'] = None
        self.container['is_visible'] = None

        if link is not None:
          self.link = link
        if comment is not None:
          self.comment = comment
        if text is not None:
          self.text = text
        self.worksheet_index = worksheet_index
        if r1_c1_refers_to is not None:
          self.r1_c1_refers_to = r1_c1_refers_to
        if refers_to is not None:
          self.refers_to = refers_to
        self.is_referred = is_referred
        self.is_visible = is_visible

    @property
    def link(self):
        """
        Gets the link of this Name.

        :return: The link of this Name.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Name.

        :param link: The link of this Name.
        :type: Link
        """

        self.container['link'] = link

    @property
    def comment(self):
        """
        Gets the comment of this Name.

        :return: The comment of this Name.
        :rtype: str
        """
        return self.container['comment']

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Name.

        :param comment: The comment of this Name.
        :type: str
        """

        self.container['comment'] = comment

    @property
    def text(self):
        """
        Gets the text of this Name.

        :return: The text of this Name.
        :rtype: str
        """
        return self.container['text']

    @text.setter
    def text(self, text):
        """
        Sets the text of this Name.

        :param text: The text of this Name.
        :type: str
        """

        self.container['text'] = text

    @property
    def worksheet_index(self):
        """
        Gets the worksheet_index of this Name.

        :return: The worksheet_index of this Name.
        :rtype: int
        """
        return self.container['worksheet_index']

    @worksheet_index.setter
    def worksheet_index(self, worksheet_index):
        """
        Sets the worksheet_index of this Name.

        :param worksheet_index: The worksheet_index of this Name.
        :type: int
        """
        """
        if worksheet_index is None:
            raise ValueError("Invalid value for `worksheet_index`, must not be `None`")
        """

        self.container['worksheet_index'] = worksheet_index

    @property
    def r1_c1_refers_to(self):
        """
        Gets the r1_c1_refers_to of this Name.

        :return: The r1_c1_refers_to of this Name.
        :rtype: str
        """
        return self.container['r1_c1_refers_to']

    @r1_c1_refers_to.setter
    def r1_c1_refers_to(self, r1_c1_refers_to):
        """
        Sets the r1_c1_refers_to of this Name.

        :param r1_c1_refers_to: The r1_c1_refers_to of this Name.
        :type: str
        """

        self.container['r1_c1_refers_to'] = r1_c1_refers_to

    @property
    def refers_to(self):
        """
        Gets the refers_to of this Name.

        :return: The refers_to of this Name.
        :rtype: str
        """
        return self.container['refers_to']

    @refers_to.setter
    def refers_to(self, refers_to):
        """
        Sets the refers_to of this Name.

        :param refers_to: The refers_to of this Name.
        :type: str
        """

        self.container['refers_to'] = refers_to

    @property
    def is_referred(self):
        """
        Gets the is_referred of this Name.

        :return: The is_referred of this Name.
        :rtype: bool
        """
        return self.container['is_referred']

    @is_referred.setter
    def is_referred(self, is_referred):
        """
        Sets the is_referred of this Name.

        :param is_referred: The is_referred of this Name.
        :type: bool
        """
        """
        if is_referred is None:
            raise ValueError("Invalid value for `is_referred`, must not be `None`")
        """

        self.container['is_referred'] = is_referred

    @property
    def is_visible(self):
        """
        Gets the is_visible of this Name.

        :return: The is_visible of this Name.
        :rtype: bool
        """
        return self.container['is_visible']

    @is_visible.setter
    def is_visible(self, is_visible):
        """
        Sets the is_visible of this Name.

        :param is_visible: The is_visible of this Name.
        :type: bool
        """
        """
        if is_visible is None:
            raise ValueError("Invalid value for `is_visible`, must not be `None`")
        """

        self.container['is_visible'] = is_visible

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
        if not isinstance(other, Name):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
