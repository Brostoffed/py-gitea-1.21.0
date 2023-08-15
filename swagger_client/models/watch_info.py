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


class WatchInfo(object):
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
        'created_at': 'datetime',
        'ignored': 'bool',
        'reason': 'object',
        'repository_url': 'str',
        'subscribed': 'bool',
        'url': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'ignored': 'ignored',
        'reason': 'reason',
        'repository_url': 'repository_url',
        'subscribed': 'subscribed',
        'url': 'url'
    }

    def __init__(self, created_at=None, ignored=None, reason=None, repository_url=None, subscribed=None, url=None, _configuration=None):  # noqa: E501
        """WatchInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._ignored = None
        self._reason = None
        self._repository_url = None
        self._subscribed = None
        self._url = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if ignored is not None:
            self.ignored = ignored
        if reason is not None:
            self.reason = reason
        if repository_url is not None:
            self.repository_url = repository_url
        if subscribed is not None:
            self.subscribed = subscribed
        if url is not None:
            self.url = url

    @property
    def created_at(self):
        """Gets the created_at of this WatchInfo.  # noqa: E501


        :return: The created_at of this WatchInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WatchInfo.


        :param created_at: The created_at of this WatchInfo.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def ignored(self):
        """Gets the ignored of this WatchInfo.  # noqa: E501


        :return: The ignored of this WatchInfo.  # noqa: E501
        :rtype: bool
        """
        return self._ignored

    @ignored.setter
    def ignored(self, ignored):
        """Sets the ignored of this WatchInfo.


        :param ignored: The ignored of this WatchInfo.  # noqa: E501
        :type: bool
        """

        self._ignored = ignored

    @property
    def reason(self):
        """Gets the reason of this WatchInfo.  # noqa: E501


        :return: The reason of this WatchInfo.  # noqa: E501
        :rtype: object
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this WatchInfo.


        :param reason: The reason of this WatchInfo.  # noqa: E501
        :type: object
        """

        self._reason = reason

    @property
    def repository_url(self):
        """Gets the repository_url of this WatchInfo.  # noqa: E501


        :return: The repository_url of this WatchInfo.  # noqa: E501
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """Sets the repository_url of this WatchInfo.


        :param repository_url: The repository_url of this WatchInfo.  # noqa: E501
        :type: str
        """

        self._repository_url = repository_url

    @property
    def subscribed(self):
        """Gets the subscribed of this WatchInfo.  # noqa: E501


        :return: The subscribed of this WatchInfo.  # noqa: E501
        :rtype: bool
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """Sets the subscribed of this WatchInfo.


        :param subscribed: The subscribed of this WatchInfo.  # noqa: E501
        :type: bool
        """

        self._subscribed = subscribed

    @property
    def url(self):
        """Gets the url of this WatchInfo.  # noqa: E501


        :return: The url of this WatchInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WatchInfo.


        :param url: The url of this WatchInfo.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(WatchInfo, dict):
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
        if not isinstance(other, WatchInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WatchInfo):
            return True

        return self.to_dict() != other.to_dict()
