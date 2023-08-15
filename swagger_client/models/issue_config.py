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


class IssueConfig(object):
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
        'blank_issues_enabled': 'bool',
        'contact_links': 'list[IssueConfigContactLink]'
    }

    attribute_map = {
        'blank_issues_enabled': 'blank_issues_enabled',
        'contact_links': 'contact_links'
    }

    def __init__(self, blank_issues_enabled=None, contact_links=None, _configuration=None):  # noqa: E501
        """IssueConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._blank_issues_enabled = None
        self._contact_links = None
        self.discriminator = None

        if blank_issues_enabled is not None:
            self.blank_issues_enabled = blank_issues_enabled
        if contact_links is not None:
            self.contact_links = contact_links

    @property
    def blank_issues_enabled(self):
        """Gets the blank_issues_enabled of this IssueConfig.  # noqa: E501


        :return: The blank_issues_enabled of this IssueConfig.  # noqa: E501
        :rtype: bool
        """
        return self._blank_issues_enabled

    @blank_issues_enabled.setter
    def blank_issues_enabled(self, blank_issues_enabled):
        """Sets the blank_issues_enabled of this IssueConfig.


        :param blank_issues_enabled: The blank_issues_enabled of this IssueConfig.  # noqa: E501
        :type: bool
        """

        self._blank_issues_enabled = blank_issues_enabled

    @property
    def contact_links(self):
        """Gets the contact_links of this IssueConfig.  # noqa: E501


        :return: The contact_links of this IssueConfig.  # noqa: E501
        :rtype: list[IssueConfigContactLink]
        """
        return self._contact_links

    @contact_links.setter
    def contact_links(self, contact_links):
        """Sets the contact_links of this IssueConfig.


        :param contact_links: The contact_links of this IssueConfig.  # noqa: E501
        :type: list[IssueConfigContactLink]
        """

        self._contact_links = contact_links

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
        if issubclass(IssueConfig, dict):
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
        if not isinstance(other, IssueConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IssueConfig):
            return True

        return self.to_dict() != other.to_dict()
