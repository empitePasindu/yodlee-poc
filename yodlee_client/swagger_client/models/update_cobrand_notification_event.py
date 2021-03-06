# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available <a href=\"https://developer.yodlee.com/java-sdk-overview \">here</a>. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/Overview\">Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class UpdateCobrandNotificationEvent(object):
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
        'callback_url': 'str'
    }

    attribute_map = {
        'callback_url': 'callbackUrl'
    }

    def __init__(self, callback_url=None, _configuration=None):  # noqa: E501
        """UpdateCobrandNotificationEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._callback_url = None
        self.discriminator = None

        if callback_url is not None:
            self.callback_url = callback_url

    @property
    def callback_url(self):
        """Gets the callback_url of this UpdateCobrandNotificationEvent.  # noqa: E501

        URL to which the notification should be posted.<br><br><b>Endpoints</b>:<ul><li>GET cobrand/config/notifications/events</li></ul>  # noqa: E501

        :return: The callback_url of this UpdateCobrandNotificationEvent.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this UpdateCobrandNotificationEvent.

        URL to which the notification should be posted.<br><br><b>Endpoints</b>:<ul><li>GET cobrand/config/notifications/events</li></ul>  # noqa: E501

        :param callback_url: The callback_url of this UpdateCobrandNotificationEvent.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                callback_url is not None and len(callback_url) > 2147483647):
            raise ValueError("Invalid value for `callback_url`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                callback_url is not None and len(callback_url) < 1):
            raise ValueError("Invalid value for `callback_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._callback_url = callback_url

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
        if issubclass(UpdateCobrandNotificationEvent, dict):
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
        if not isinstance(other, UpdateCobrandNotificationEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateCobrandNotificationEvent):
            return True

        return self.to_dict() != other.to_dict()
