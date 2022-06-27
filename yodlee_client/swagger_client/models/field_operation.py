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


class FieldOperation(object):
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
        'field': 'str',
        'operation': 'str',
        'value': 'object'
    }

    attribute_map = {
        'field': 'field',
        'operation': 'operation',
        'value': 'value'
    }

    def __init__(self, field=None, operation=None, value=None, _configuration=None):  # noqa: E501
        """FieldOperation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._field = None
        self._operation = None
        self._value = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if operation is not None:
            self.operation = operation
        if value is not None:
            self.value = value

    @property
    def field(self):
        """Gets the field of this FieldOperation.  # noqa: E501

        Field for which the clause is created.<br><br><b>Applicable containers</b>: bank, creditCard, investment, insurance, loan<br><b>Applicable Values</b>:<ul><li>amount</li><li>description</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The field of this FieldOperation.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this FieldOperation.

        Field for which the clause is created.<br><br><b>Applicable containers</b>: bank, creditCard, investment, insurance, loan<br><b>Applicable Values</b>:<ul><li>amount</li><li>description</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param field: The field of this FieldOperation.  # noqa: E501
        :type: str
        """
        allowed_values = ["amount", "description"]  # noqa: E501
        if (self._configuration.client_side_validation and
                field not in allowed_values):
            raise ValueError(
                "Invalid value for `field` ({0}), must be one of {1}"  # noqa: E501
                .format(field, allowed_values)
            )

        self._field = field

    @property
    def operation(self):
        """Gets the operation of this FieldOperation.  # noqa: E501

        Operation for which the clause is created.<br><br><b>Applicable containers</b>: bank, creditCard, investment, insurance, loan<br><b>Applicable values (depends on the value of field)</b>:<ul><li>field is <b>description</b> -> operation can be<ol><li>stringEquals</li><li>stringContains</li></ol></li><li>field is <b>amount</b> -> operation can be<ol><li>numberEquals</li><li>numberLessThan</li><li>numberLessThanEquals</li><li>numberGreaterThan</li><li>numberGreaterThanEquals</li></ol></li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The operation of this FieldOperation.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this FieldOperation.

        Operation for which the clause is created.<br><br><b>Applicable containers</b>: bank, creditCard, investment, insurance, loan<br><b>Applicable values (depends on the value of field)</b>:<ul><li>field is <b>description</b> -> operation can be<ol><li>stringEquals</li><li>stringContains</li></ol></li><li>field is <b>amount</b> -> operation can be<ol><li>numberEquals</li><li>numberLessThan</li><li>numberLessThanEquals</li><li>numberGreaterThan</li><li>numberGreaterThanEquals</li></ol></li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param operation: The operation of this FieldOperation.  # noqa: E501
        :type: str
        """
        allowed_values = ["numberEquals", "numberLessThan", "numberLessThanEquals", "numberGreaterThan", "numberGreaterThanEquals", "stringEquals", "stringContains"]  # noqa: E501
        if (self._configuration.client_side_validation and
                operation not in allowed_values):
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def value(self):
        """Gets the value of this FieldOperation.  # noqa: E501

        The value would be the amount value in case of amount based rule clause or the string value in case of description based rule clause.<br><br><b>Applicable containers</b>: bank, creditCard, investment, insurance, loan<br><b>Applicable Values</b>:<ul><li>field is <b>description</b> -> value should be <b>min of 3 and max of 50 characters</b></li><li>field is <b>amount</b> -> value should be <b> min value of 0 and a max value of 99999999999.99</b></li></ul>  # noqa: E501

        :return: The value of this FieldOperation.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FieldOperation.

        The value would be the amount value in case of amount based rule clause or the string value in case of description based rule clause.<br><br><b>Applicable containers</b>: bank, creditCard, investment, insurance, loan<br><b>Applicable Values</b>:<ul><li>field is <b>description</b> -> value should be <b>min of 3 and max of 50 characters</b></li><li>field is <b>amount</b> -> value should be <b> min value of 0 and a max value of 99999999999.99</b></li></ul>  # noqa: E501

        :param value: The value of this FieldOperation.  # noqa: E501
        :type: object
        """

        self._value = value

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
        if issubclass(FieldOperation, dict):
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
        if not isinstance(other, FieldOperation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldOperation):
            return True

        return self.to_dict() != other.to_dict()