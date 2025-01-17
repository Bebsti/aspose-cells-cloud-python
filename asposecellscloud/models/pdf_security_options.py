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


class PdfSecurityOptions(object):
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
        'annotations_permission': 'bool',
        'assemble_document_permission': 'bool',
        'extract_content_permission': 'bool',
        'extract_content_permission_obsolete': 'bool',
        'fill_forms_permission': 'bool',
        'full_quality_print_permission': 'bool',
        'modify_document_permission': 'bool',
        'owner_password': 'str',
        'print_permission': 'bool',
        'user_password': 'str'
    }

    attribute_map = {
        'annotations_permission': 'AnnotationsPermission',
        'assemble_document_permission': 'AssembleDocumentPermission',
        'extract_content_permission': 'ExtractContentPermission',
        'extract_content_permission_obsolete': 'ExtractContentPermissionObsolete',
        'fill_forms_permission': 'FillFormsPermission',
        'full_quality_print_permission': 'FullQualityPrintPermission',
        'modify_document_permission': 'ModifyDocumentPermission',
        'owner_password': 'OwnerPassword',
        'print_permission': 'PrintPermission',
        'user_password': 'UserPassword'
    }
    
    @staticmethod
    def get_swagger_types():
        return PdfSecurityOptions.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return PdfSecurityOptions.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, annotations_permission=None, assemble_document_permission=None, extract_content_permission=None, extract_content_permission_obsolete=None, fill_forms_permission=None, full_quality_print_permission=None, modify_document_permission=None, owner_password=None, print_permission=None, user_password=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        PdfSecurityOptions - a model defined in Swagger
        """

        self.container['annotations_permission'] = None
        self.container['assemble_document_permission'] = None
        self.container['extract_content_permission'] = None
        self.container['extract_content_permission_obsolete'] = None
        self.container['fill_forms_permission'] = None
        self.container['full_quality_print_permission'] = None
        self.container['modify_document_permission'] = None
        self.container['owner_password'] = None
        self.container['print_permission'] = None
        self.container['user_password'] = None

        if annotations_permission is not None:
          self.annotations_permission = annotations_permission
        if assemble_document_permission is not None:
          self.assemble_document_permission = assemble_document_permission
        if extract_content_permission is not None:
          self.extract_content_permission = extract_content_permission
        if extract_content_permission_obsolete is not None:
          self.extract_content_permission_obsolete = extract_content_permission_obsolete
        if fill_forms_permission is not None:
          self.fill_forms_permission = fill_forms_permission
        if full_quality_print_permission is not None:
          self.full_quality_print_permission = full_quality_print_permission
        if modify_document_permission is not None:
          self.modify_document_permission = modify_document_permission
        if owner_password is not None:
          self.owner_password = owner_password
        if print_permission is not None:
          self.print_permission = print_permission
        if user_password is not None:
          self.user_password = user_password

    @property
    def annotations_permission(self):
        """
        Gets the annotations_permission of this PdfSecurityOptions.

        :return: The annotations_permission of this PdfSecurityOptions.
        :rtype: bool
        """
        return self.container['annotations_permission']

    @annotations_permission.setter
    def annotations_permission(self, annotations_permission):
        """
        Sets the annotations_permission of this PdfSecurityOptions.

        :param annotations_permission: The annotations_permission of this PdfSecurityOptions.
        :type: bool
        """

        self.container['annotations_permission'] = annotations_permission

    @property
    def assemble_document_permission(self):
        """
        Gets the assemble_document_permission of this PdfSecurityOptions.

        :return: The assemble_document_permission of this PdfSecurityOptions.
        :rtype: bool
        """
        return self.container['assemble_document_permission']

    @assemble_document_permission.setter
    def assemble_document_permission(self, assemble_document_permission):
        """
        Sets the assemble_document_permission of this PdfSecurityOptions.

        :param assemble_document_permission: The assemble_document_permission of this PdfSecurityOptions.
        :type: bool
        """

        self.container['assemble_document_permission'] = assemble_document_permission

    @property
    def extract_content_permission(self):
        """
        Gets the extract_content_permission of this PdfSecurityOptions.
        Make the workbook empty after saving the file.

        :return: The extract_content_permission of this PdfSecurityOptions.
        :rtype: bool
        """
        return self.container['extract_content_permission']

    @extract_content_permission.setter
    def extract_content_permission(self, extract_content_permission):
        """
        Sets the extract_content_permission of this PdfSecurityOptions.
        Make the workbook empty after saving the file.

        :param extract_content_permission: The extract_content_permission of this PdfSecurityOptions.
        :type: bool
        """

        self.container['extract_content_permission'] = extract_content_permission

    @property
    def extract_content_permission_obsolete(self):
        """
        Gets the extract_content_permission_obsolete of this PdfSecurityOptions.
        The cached file folder is used to store some large data.

        :return: The extract_content_permission_obsolete of this PdfSecurityOptions.
        :rtype: bool
        """
        return self.container['extract_content_permission_obsolete']

    @extract_content_permission_obsolete.setter
    def extract_content_permission_obsolete(self, extract_content_permission_obsolete):
        """
        Sets the extract_content_permission_obsolete of this PdfSecurityOptions.
        The cached file folder is used to store some large data.

        :param extract_content_permission_obsolete: The extract_content_permission_obsolete of this PdfSecurityOptions.
        :type: bool
        """

        self.container['extract_content_permission_obsolete'] = extract_content_permission_obsolete

    @property
    def fill_forms_permission(self):
        """
        Gets the fill_forms_permission of this PdfSecurityOptions.
        Indicates whether validate merged areas before saving the file. The default value is false.             

        :return: The fill_forms_permission of this PdfSecurityOptions.
        :rtype: bool
        """
        return self.container['fill_forms_permission']

    @fill_forms_permission.setter
    def fill_forms_permission(self, fill_forms_permission):
        """
        Sets the fill_forms_permission of this PdfSecurityOptions.
        Indicates whether validate merged areas before saving the file. The default value is false.             

        :param fill_forms_permission: The fill_forms_permission of this PdfSecurityOptions.
        :type: bool
        """

        self.container['fill_forms_permission'] = fill_forms_permission

    @property
    def full_quality_print_permission(self):
        """
        Gets the full_quality_print_permission of this PdfSecurityOptions.

        :return: The full_quality_print_permission of this PdfSecurityOptions.
        :rtype: bool
        """
        return self.container['full_quality_print_permission']

    @full_quality_print_permission.setter
    def full_quality_print_permission(self, full_quality_print_permission):
        """
        Sets the full_quality_print_permission of this PdfSecurityOptions.

        :param full_quality_print_permission: The full_quality_print_permission of this PdfSecurityOptions.
        :type: bool
        """

        self.container['full_quality_print_permission'] = full_quality_print_permission

    @property
    def modify_document_permission(self):
        """
        Gets the modify_document_permission of this PdfSecurityOptions.
        If true and the directory does not exist, the directory will be automatically created before saving the file.             

        :return: The modify_document_permission of this PdfSecurityOptions.
        :rtype: bool
        """
        return self.container['modify_document_permission']

    @modify_document_permission.setter
    def modify_document_permission(self, modify_document_permission):
        """
        Sets the modify_document_permission of this PdfSecurityOptions.
        If true and the directory does not exist, the directory will be automatically created before saving the file.             

        :param modify_document_permission: The modify_document_permission of this PdfSecurityOptions.
        :type: bool
        """

        self.container['modify_document_permission'] = modify_document_permission

    @property
    def owner_password(self):
        """
        Gets the owner_password of this PdfSecurityOptions.

        :return: The owner_password of this PdfSecurityOptions.
        :rtype: str
        """
        return self.container['owner_password']

    @owner_password.setter
    def owner_password(self, owner_password):
        """
        Sets the owner_password of this PdfSecurityOptions.

        :param owner_password: The owner_password of this PdfSecurityOptions.
        :type: str
        """

        self.container['owner_password'] = owner_password

    @property
    def print_permission(self):
        """
        Gets the print_permission of this PdfSecurityOptions.

        :return: The print_permission of this PdfSecurityOptions.
        :rtype: bool
        """
        return self.container['print_permission']

    @print_permission.setter
    def print_permission(self, print_permission):
        """
        Sets the print_permission of this PdfSecurityOptions.

        :param print_permission: The print_permission of this PdfSecurityOptions.
        :type: bool
        """

        self.container['print_permission'] = print_permission

    @property
    def user_password(self):
        """
        Gets the user_password of this PdfSecurityOptions.

        :return: The user_password of this PdfSecurityOptions.
        :rtype: str
        """
        return self.container['user_password']

    @user_password.setter
    def user_password(self, user_password):
        """
        Sets the user_password of this PdfSecurityOptions.

        :param user_password: The user_password of this PdfSecurityOptions.
        :type: str
        """

        self.container['user_password'] = user_password

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
        if not isinstance(other, PdfSecurityOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
