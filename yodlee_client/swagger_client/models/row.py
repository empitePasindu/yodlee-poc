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


class Row(object):
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
        'field_row_choice': 'str',
        'field': 'list[Field]',
        'form': 'str',
        'id': 'str',
        'label': 'str'
    }

    attribute_map = {
        'field_row_choice': 'fieldRowChoice',
        'field': 'field',
        'form': 'form',
        'id': 'id',
        'label': 'label'
    }

    def __init__(self, field_row_choice=None, field=None, form=None, id=None, label=None, _configuration=None):  # noqa: E501
        """Row - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._field_row_choice = None
        self._field = None
        self._form = None
        self._id = None
        self._label = None
        self.discriminator = None

        if field_row_choice is not None:
            self.field_row_choice = field_row_choice
        if field is not None:
            self.field = field
        if form is not None:
            self.form = form
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label

    @property
    def field_row_choice(self):
        """Gets the field_row_choice of this Row.  # noqa: E501

        Fields that belong to a particular choice are collected together using this field.<br><b>Recommendations</b>: All the field row choices label to be grouped and displayed as options to the customer. On choosing a particular choice field, we recommend displaying the fields relevant to them. First field choice could be selected by default.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :return: The field_row_choice of this Row.  # noqa: E501
        :rtype: str
        """
        return self._field_row_choice

    @field_row_choice.setter
    def field_row_choice(self, field_row_choice):
        """Sets the field_row_choice of this Row.

        Fields that belong to a particular choice are collected together using this field.<br><b>Recommendations</b>: All the field row choices label to be grouped and displayed as options to the customer. On choosing a particular choice field, we recommend displaying the fields relevant to them. First field choice could be selected by default.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :param field_row_choice: The field_row_choice of this Row.  # noqa: E501
        :type: str
        """

        self._field_row_choice = field_row_choice

    @property
    def field(self):
        """Gets the field of this Row.  # noqa: E501

        Details of fields that belong to the row.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :return: The field of this Row.  # noqa: E501
        :rtype: list[Field]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Row.

        Details of fields that belong to the row.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :param field: The field of this Row.  # noqa: E501
        :type: list[Field]
        """

        self._field = field

    @property
    def form(self):
        """Gets the form of this Row.  # noqa: E501

        Form denotes the set of the fields that are related. <br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :return: The form of this Row.  # noqa: E501
        :rtype: str
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this Row.

        Form denotes the set of the fields that are related. <br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :param form: The form of this Row.  # noqa: E501
        :type: str
        """

        self._form = form

    @property
    def id(self):
        """Gets the id of this Row.  # noqa: E501

        Unique identifier of the row.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :return: The id of this Row.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Row.

        Unique identifier of the row.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :param id: The id of this Row.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Row.  # noqa: E501

        The label text displayed for a row in the form.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :return: The label of this Row.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Row.

        The label text displayed for a row in the form.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts/{providerAccountId}</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :param label: The label of this Row.  # noqa: E501
        :type: str
        """

        self._label = label

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
        if issubclass(Row, dict):
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
        if not isinstance(other, Row):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Row):
            return True

        return self.to_dict() != other.to_dict()
