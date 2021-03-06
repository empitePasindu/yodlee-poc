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


class UpdateTransaction(object):
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
        'category_source': 'str',
        'container': 'str',
        'is_physical': 'bool',
        'detail_category_id': 'int',
        'description': 'Description',
        'memo': 'str',
        'merchant_type': 'str',
        'category_id': 'int'
    }

    attribute_map = {
        'category_source': 'categorySource',
        'container': 'container',
        'is_physical': 'isPhysical',
        'detail_category_id': 'detailCategoryId',
        'description': 'description',
        'memo': 'memo',
        'merchant_type': 'merchantType',
        'category_id': 'categoryId'
    }

    def __init__(self, category_source=None, container=None, is_physical=None, detail_category_id=None, description=None, memo=None, merchant_type=None, category_id=None, _configuration=None):  # noqa: E501
        """UpdateTransaction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._category_source = None
        self._container = None
        self._is_physical = None
        self._detail_category_id = None
        self._description = None
        self._memo = None
        self._merchant_type = None
        self._category_id = None
        self.discriminator = None

        self.category_source = category_source
        self.container = container
        if is_physical is not None:
            self.is_physical = is_physical
        if detail_category_id is not None:
            self.detail_category_id = detail_category_id
        if description is not None:
            self.description = description
        if memo is not None:
            self.memo = memo
        if merchant_type is not None:
            self.merchant_type = merchant_type
        self.category_id = category_id

    @property
    def category_source(self):
        """Gets the category_source of this UpdateTransaction.  # noqa: E501


        :return: The category_source of this UpdateTransaction.  # noqa: E501
        :rtype: str
        """
        return self._category_source

    @category_source.setter
    def category_source(self, category_source):
        """Sets the category_source of this UpdateTransaction.


        :param category_source: The category_source of this UpdateTransaction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and category_source is None:
            raise ValueError("Invalid value for `category_source`, must not be `None`")  # noqa: E501
        allowed_values = ["SYSTEM", "USER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                category_source not in allowed_values):
            raise ValueError(
                "Invalid value for `category_source` ({0}), must be one of {1}"  # noqa: E501
                .format(category_source, allowed_values)
            )

        self._category_source = category_source

    @property
    def container(self):
        """Gets the container of this UpdateTransaction.  # noqa: E501


        :return: The container of this UpdateTransaction.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this UpdateTransaction.


        :param container: The container of this UpdateTransaction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and container is None:
            raise ValueError("Invalid value for `container`, must not be `None`")  # noqa: E501
        allowed_values = ["bank", "creditCard", "investment", "insurance", "loan", "reward", "bill", "realEstate", "otherAssets", "otherLiabilities"]  # noqa: E501
        if (self._configuration.client_side_validation and
                container not in allowed_values):
            raise ValueError(
                "Invalid value for `container` ({0}), must be one of {1}"  # noqa: E501
                .format(container, allowed_values)
            )

        self._container = container

    @property
    def is_physical(self):
        """Gets the is_physical of this UpdateTransaction.  # noqa: E501


        :return: The is_physical of this UpdateTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_physical

    @is_physical.setter
    def is_physical(self, is_physical):
        """Sets the is_physical of this UpdateTransaction.


        :param is_physical: The is_physical of this UpdateTransaction.  # noqa: E501
        :type: bool
        """

        self._is_physical = is_physical

    @property
    def detail_category_id(self):
        """Gets the detail_category_id of this UpdateTransaction.  # noqa: E501


        :return: The detail_category_id of this UpdateTransaction.  # noqa: E501
        :rtype: int
        """
        return self._detail_category_id

    @detail_category_id.setter
    def detail_category_id(self, detail_category_id):
        """Sets the detail_category_id of this UpdateTransaction.


        :param detail_category_id: The detail_category_id of this UpdateTransaction.  # noqa: E501
        :type: int
        """

        self._detail_category_id = detail_category_id

    @property
    def description(self):
        """Gets the description of this UpdateTransaction.  # noqa: E501


        :return: The description of this UpdateTransaction.  # noqa: E501
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTransaction.


        :param description: The description of this UpdateTransaction.  # noqa: E501
        :type: Description
        """

        self._description = description

    @property
    def memo(self):
        """Gets the memo of this UpdateTransaction.  # noqa: E501


        :return: The memo of this UpdateTransaction.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this UpdateTransaction.


        :param memo: The memo of this UpdateTransaction.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def merchant_type(self):
        """Gets the merchant_type of this UpdateTransaction.  # noqa: E501


        :return: The merchant_type of this UpdateTransaction.  # noqa: E501
        :rtype: str
        """
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, merchant_type):
        """Sets the merchant_type of this UpdateTransaction.


        :param merchant_type: The merchant_type of this UpdateTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["BILLERS", "SUBSCRIPTION", "OTHERS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                merchant_type not in allowed_values):
            raise ValueError(
                "Invalid value for `merchant_type` ({0}), must be one of {1}"  # noqa: E501
                .format(merchant_type, allowed_values)
            )

        self._merchant_type = merchant_type

    @property
    def category_id(self):
        """Gets the category_id of this UpdateTransaction.  # noqa: E501


        :return: The category_id of this UpdateTransaction.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this UpdateTransaction.


        :param category_id: The category_id of this UpdateTransaction.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

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
        if issubclass(UpdateTransaction, dict):
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
        if not isinstance(other, UpdateTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTransaction):
            return True

        return self.to_dict() != other.to_dict()
