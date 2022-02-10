# coding: utf-8

"""
    蓝鲸用户管理 API

    蓝鲸用户管理后台服务 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class RelatedResourceSLZ(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'type_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'type_name': 'type_name'
    }

    def __init__(self, id=None, name=None, type=None, type_name=None):  # noqa: E501
        """RelatedResourceSLZ - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._type = None
        self._type_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if type_name is not None:
            self.type_name = type_name

    @property
    def id(self):
        """Gets the id of this RelatedResourceSLZ.  # noqa: E501


        :return: The id of this RelatedResourceSLZ.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelatedResourceSLZ.


        :param id: The id of this RelatedResourceSLZ.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this RelatedResourceSLZ.  # noqa: E501


        :return: The name of this RelatedResourceSLZ.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RelatedResourceSLZ.


        :param name: The name of this RelatedResourceSLZ.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this RelatedResourceSLZ.  # noqa: E501


        :return: The type of this RelatedResourceSLZ.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RelatedResourceSLZ.


        :param type: The type of this RelatedResourceSLZ.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def type_name(self):
        """Gets the type_name of this RelatedResourceSLZ.  # noqa: E501


        :return: The type_name of this RelatedResourceSLZ.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this RelatedResourceSLZ.


        :param type_name: The type_name of this RelatedResourceSLZ.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
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
        if issubclass(RelatedResourceSLZ, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelatedResourceSLZ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other