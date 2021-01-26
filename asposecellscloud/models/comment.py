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


class Comment(object):
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
        'auto_size': 'bool',
        'author': 'str',
        'is_visible': 'bool',
        'text_orientation_type': 'str',
        'height': 'int',
        'note': 'str',
        'width': 'int',
        'text_vertical_alignment': 'str',
        'cell_name': 'str',
        'html_note': 'str',
        'text_horizontal_alignment': 'str'
    }

    attribute_map = {
        'link': 'link',
        'auto_size': 'AutoSize',
        'author': 'Author',
        'is_visible': 'IsVisible',
        'text_orientation_type': 'TextOrientationType',
        'height': 'Height',
        'note': 'Note',
        'width': 'Width',
        'text_vertical_alignment': 'TextVerticalAlignment',
        'cell_name': 'CellName',
        'html_note': 'HtmlNote',
        'text_horizontal_alignment': 'TextHorizontalAlignment'
    }
    
    @staticmethod
    def get_swagger_types():
        return Comment.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return Comment.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, auto_size=None, author=None, is_visible=None, text_orientation_type=None, height=None, note=None, width=None, text_vertical_alignment=None, cell_name=None, html_note=None, text_horizontal_alignment=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        Comment - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['auto_size'] = None
        self.container['author'] = None
        self.container['is_visible'] = None
        self.container['text_orientation_type'] = None
        self.container['height'] = None
        self.container['note'] = None
        self.container['width'] = None
        self.container['text_vertical_alignment'] = None
        self.container['cell_name'] = None
        self.container['html_note'] = None
        self.container['text_horizontal_alignment'] = None

        if link is not None:
          self.link = link
        if auto_size is not None:
          self.auto_size = auto_size
        if author is not None:
          self.author = author
        if is_visible is not None:
          self.is_visible = is_visible
        if text_orientation_type is not None:
          self.text_orientation_type = text_orientation_type
        if height is not None:
          self.height = height
        if note is not None:
          self.note = note
        if width is not None:
          self.width = width
        if text_vertical_alignment is not None:
          self.text_vertical_alignment = text_vertical_alignment
        if cell_name is not None:
          self.cell_name = cell_name
        if html_note is not None:
          self.html_note = html_note
        if text_horizontal_alignment is not None:
          self.text_horizontal_alignment = text_horizontal_alignment

    @property
    def link(self):
        """
        Gets the link of this Comment.

        :return: The link of this Comment.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Comment.

        :param link: The link of this Comment.
        :type: Link
        """

        self.container['link'] = link

    @property
    def auto_size(self):
        """
        Gets the auto_size of this Comment.

        :return: The auto_size of this Comment.
        :rtype: bool
        """
        return self.container['auto_size']

    @auto_size.setter
    def auto_size(self, auto_size):
        """
        Sets the auto_size of this Comment.

        :param auto_size: The auto_size of this Comment.
        :type: bool
        """

        self.container['auto_size'] = auto_size

    @property
    def author(self):
        """
        Gets the author of this Comment.

        :return: The author of this Comment.
        :rtype: str
        """
        return self.container['author']

    @author.setter
    def author(self, author):
        """
        Sets the author of this Comment.

        :param author: The author of this Comment.
        :type: str
        """

        self.container['author'] = author

    @property
    def is_visible(self):
        """
        Gets the is_visible of this Comment.

        :return: The is_visible of this Comment.
        :rtype: bool
        """
        return self.container['is_visible']

    @is_visible.setter
    def is_visible(self, is_visible):
        """
        Sets the is_visible of this Comment.

        :param is_visible: The is_visible of this Comment.
        :type: bool
        """

        self.container['is_visible'] = is_visible

    @property
    def text_orientation_type(self):
        """
        Gets the text_orientation_type of this Comment.

        :return: The text_orientation_type of this Comment.
        :rtype: str
        """
        return self.container['text_orientation_type']

    @text_orientation_type.setter
    def text_orientation_type(self, text_orientation_type):
        """
        Sets the text_orientation_type of this Comment.

        :param text_orientation_type: The text_orientation_type of this Comment.
        :type: str
        """

        self.container['text_orientation_type'] = text_orientation_type

    @property
    def height(self):
        """
        Gets the height of this Comment.

        :return: The height of this Comment.
        :rtype: int
        """
        return self.container['height']

    @height.setter
    def height(self, height):
        """
        Sets the height of this Comment.

        :param height: The height of this Comment.
        :type: int
        """

        self.container['height'] = height

    @property
    def note(self):
        """
        Gets the note of this Comment.

        :return: The note of this Comment.
        :rtype: str
        """
        return self.container['note']

    @note.setter
    def note(self, note):
        """
        Sets the note of this Comment.

        :param note: The note of this Comment.
        :type: str
        """

        self.container['note'] = note

    @property
    def width(self):
        """
        Gets the width of this Comment.

        :return: The width of this Comment.
        :rtype: int
        """
        return self.container['width']

    @width.setter
    def width(self, width):
        """
        Sets the width of this Comment.

        :param width: The width of this Comment.
        :type: int
        """

        self.container['width'] = width

    @property
    def text_vertical_alignment(self):
        """
        Gets the text_vertical_alignment of this Comment.

        :return: The text_vertical_alignment of this Comment.
        :rtype: str
        """
        return self.container['text_vertical_alignment']

    @text_vertical_alignment.setter
    def text_vertical_alignment(self, text_vertical_alignment):
        """
        Sets the text_vertical_alignment of this Comment.

        :param text_vertical_alignment: The text_vertical_alignment of this Comment.
        :type: str
        """

        self.container['text_vertical_alignment'] = text_vertical_alignment

    @property
    def cell_name(self):
        """
        Gets the cell_name of this Comment.

        :return: The cell_name of this Comment.
        :rtype: str
        """
        return self.container['cell_name']

    @cell_name.setter
    def cell_name(self, cell_name):
        """
        Sets the cell_name of this Comment.

        :param cell_name: The cell_name of this Comment.
        :type: str
        """

        self.container['cell_name'] = cell_name

    @property
    def html_note(self):
        """
        Gets the html_note of this Comment.

        :return: The html_note of this Comment.
        :rtype: str
        """
        return self.container['html_note']

    @html_note.setter
    def html_note(self, html_note):
        """
        Sets the html_note of this Comment.

        :param html_note: The html_note of this Comment.
        :type: str
        """

        self.container['html_note'] = html_note

    @property
    def text_horizontal_alignment(self):
        """
        Gets the text_horizontal_alignment of this Comment.

        :return: The text_horizontal_alignment of this Comment.
        :rtype: str
        """
        return self.container['text_horizontal_alignment']

    @text_horizontal_alignment.setter
    def text_horizontal_alignment(self, text_horizontal_alignment):
        """
        Sets the text_horizontal_alignment of this Comment.

        :param text_horizontal_alignment: The text_horizontal_alignment of this Comment.
        :type: str
        """

        self.container['text_horizontal_alignment'] = text_horizontal_alignment

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
        if not isinstance(other, Comment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
