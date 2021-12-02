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


class SettingMeta(object):
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
        'id': 'int',
        'choices': 'object',
        'example': 'object',
        'default': 'object',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'key': 'str',
        'enabled': 'bool',
        'required': 'bool',
        'namespace': 'str',
        'region': 'str',
        'category_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'choices': 'choices',
        'example': 'example',
        'default': 'default',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'key': 'key',
        'enabled': 'enabled',
        'required': 'required',
        'namespace': 'namespace',
        'region': 'region',
        'category_type': 'category_type'
    }

    def __init__(self, id=None, choices=None, example=None, default=None, create_time=None, update_time=None, key=None, enabled=None, required=None, namespace='general', region=None, category_type=None):  # noqa: E501
        """SettingMeta - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._choices = None
        self._example = None
        self._default = None
        self._create_time = None
        self._update_time = None
        self._key = None
        self._enabled = None
        self._required = None
        self._namespace = None
        self._region = None
        self._category_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.choices = choices
        self.example = example
        self.default = default
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        self.key = key
        if enabled is not None:
            self.enabled = enabled
        if required is not None:
            self.required = required
        if namespace is not None:
            self.namespace = namespace
        if region is not None:
            self.region = region
        self.category_type = category_type

    @property
    def id(self):
        """Gets the id of this SettingMeta.  # noqa: E501


        :return: The id of this SettingMeta.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SettingMeta.


        :param id: The id of this SettingMeta.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def choices(self):
        """Gets the choices of this SettingMeta.  # noqa: E501


        :return: The choices of this SettingMeta.  # noqa: E501
        :rtype: object
        """
        return self._choices

    @choices.setter
    def choices(self, choices):
        """Sets the choices of this SettingMeta.


        :param choices: The choices of this SettingMeta.  # noqa: E501
        :type: object
        """
        if choices is None:
            raise ValueError("Invalid value for `choices`, must not be `None`")  # noqa: E501

        self._choices = choices

    @property
    def example(self):
        """Gets the example of this SettingMeta.  # noqa: E501


        :return: The example of this SettingMeta.  # noqa: E501
        :rtype: object
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this SettingMeta.


        :param example: The example of this SettingMeta.  # noqa: E501
        :type: object
        """
        if example is None:
            raise ValueError("Invalid value for `example`, must not be `None`")  # noqa: E501

        self._example = example

    @property
    def default(self):
        """Gets the default of this SettingMeta.  # noqa: E501


        :return: The default of this SettingMeta.  # noqa: E501
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this SettingMeta.


        :param default: The default of this SettingMeta.  # noqa: E501
        :type: object
        """
        if default is None:
            raise ValueError("Invalid value for `default`, must not be `None`")  # noqa: E501

        self._default = default

    @property
    def create_time(self):
        """Gets the create_time of this SettingMeta.  # noqa: E501


        :return: The create_time of this SettingMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SettingMeta.


        :param create_time: The create_time of this SettingMeta.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this SettingMeta.  # noqa: E501


        :return: The update_time of this SettingMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this SettingMeta.


        :param update_time: The update_time of this SettingMeta.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def key(self):
        """Gets the key of this SettingMeta.  # noqa: E501


        :return: The key of this SettingMeta.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SettingMeta.


        :param key: The key of this SettingMeta.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def enabled(self):
        """Gets the enabled of this SettingMeta.  # noqa: E501


        :return: The enabled of this SettingMeta.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this SettingMeta.


        :param enabled: The enabled of this SettingMeta.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def required(self):
        """Gets the required of this SettingMeta.  # noqa: E501


        :return: The required of this SettingMeta.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this SettingMeta.


        :param required: The required of this SettingMeta.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def namespace(self):
        """Gets the namespace of this SettingMeta.  # noqa: E501


        :return: The namespace of this SettingMeta.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this SettingMeta.


        :param namespace: The namespace of this SettingMeta.  # noqa: E501
        :type: str
        """
        allowed_values = ["general", "password", "connection", "fields"]  # noqa: E501
        if namespace not in allowed_values:
            raise ValueError(
                "Invalid value for `namespace` ({0}), must be one of {1}"  # noqa: E501
                .format(namespace, allowed_values)
            )

        self._namespace = namespace

    @property
    def region(self):
        """Gets the region of this SettingMeta.  # noqa: E501


        :return: The region of this SettingMeta.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SettingMeta.


        :param region: The region of this SettingMeta.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def category_type(self):
        """Gets the category_type of this SettingMeta.  # noqa: E501


        :return: The category_type of this SettingMeta.  # noqa: E501
        :rtype: str
        """
        return self._category_type

    @category_type.setter
    def category_type(self, category_type):
        """Sets the category_type of this SettingMeta.


        :param category_type: The category_type of this SettingMeta.  # noqa: E501
        :type: str
        """
        if category_type is None:
            raise ValueError("Invalid value for `category_type`, must not be `None`")  # noqa: E501
        allowed_values = ["local", "mad", "ldap", "custom", "pluggable"]  # noqa: E501
        if category_type not in allowed_values:
            raise ValueError(
                "Invalid value for `category_type` ({0}), must be one of {1}"  # noqa: E501
                .format(category_type, allowed_values)
            )

        self._category_type = category_type

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
        if issubclass(SettingMeta, dict):
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
        if not isinstance(other, SettingMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
