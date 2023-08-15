# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.21.0+dev-543-gced34bab1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Attachment(object):
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
        'browser_download_url': 'str',
        'created_at': 'datetime',
        'download_count': 'int',
        'id': 'int',
        'name': 'str',
        'size': 'int',
        'uuid': 'str'
    }

    attribute_map = {
        'browser_download_url': 'browser_download_url',
        'created_at': 'created_at',
        'download_count': 'download_count',
        'id': 'id',
        'name': 'name',
        'size': 'size',
        'uuid': 'uuid'
    }

    def __init__(self, browser_download_url=None, created_at=None, download_count=None, id=None, name=None, size=None, uuid=None, _configuration=None):  # noqa: E501
        """Attachment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._browser_download_url = None
        self._created_at = None
        self._download_count = None
        self._id = None
        self._name = None
        self._size = None
        self._uuid = None
        self.discriminator = None

        if browser_download_url is not None:
            self.browser_download_url = browser_download_url
        if created_at is not None:
            self.created_at = created_at
        if download_count is not None:
            self.download_count = download_count
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if uuid is not None:
            self.uuid = uuid

    @property
    def browser_download_url(self):
        """Gets the browser_download_url of this Attachment.  # noqa: E501


        :return: The browser_download_url of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._browser_download_url

    @browser_download_url.setter
    def browser_download_url(self, browser_download_url):
        """Sets the browser_download_url of this Attachment.


        :param browser_download_url: The browser_download_url of this Attachment.  # noqa: E501
        :type: str
        """

        self._browser_download_url = browser_download_url

    @property
    def created_at(self):
        """Gets the created_at of this Attachment.  # noqa: E501


        :return: The created_at of this Attachment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Attachment.


        :param created_at: The created_at of this Attachment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def download_count(self):
        """Gets the download_count of this Attachment.  # noqa: E501


        :return: The download_count of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._download_count

    @download_count.setter
    def download_count(self, download_count):
        """Sets the download_count of this Attachment.


        :param download_count: The download_count of this Attachment.  # noqa: E501
        :type: int
        """

        self._download_count = download_count

    @property
    def id(self):
        """Gets the id of this Attachment.  # noqa: E501


        :return: The id of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Attachment.


        :param id: The id of this Attachment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Attachment.  # noqa: E501


        :return: The name of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Attachment.


        :param name: The name of this Attachment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this Attachment.  # noqa: E501


        :return: The size of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Attachment.


        :param size: The size of this Attachment.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def uuid(self):
        """Gets the uuid of this Attachment.  # noqa: E501


        :return: The uuid of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Attachment.


        :param uuid: The uuid of this Attachment.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(Attachment, dict):
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
        if not isinstance(other, Attachment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Attachment):
            return True

        return self.to_dict() != other.to_dict()