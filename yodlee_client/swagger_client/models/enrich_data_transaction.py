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


class EnrichDataTransaction(object):
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
        'container': 'str',
        'source_id': 'str',
        'amount': 'Money',
        'description': 'Description',
        'post_date': 'str',
        'user_login_name': 'str',
        'account_number': 'str',
        'transaction_date': 'str',
        'base_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'container': 'container',
        'source_id': 'sourceId',
        'amount': 'amount',
        'description': 'description',
        'post_date': 'postDate',
        'user_login_name': 'userLoginName',
        'account_number': 'accountNumber',
        'transaction_date': 'transactionDate',
        'base_type': 'baseType',
        'status': 'status'
    }

    def __init__(self, container=None, source_id=None, amount=None, description=None, post_date=None, user_login_name=None, account_number=None, transaction_date=None, base_type=None, status=None, _configuration=None):  # noqa: E501
        """EnrichDataTransaction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._container = None
        self._source_id = None
        self._amount = None
        self._description = None
        self._post_date = None
        self._user_login_name = None
        self._account_number = None
        self._transaction_date = None
        self._base_type = None
        self._status = None
        self.discriminator = None

        if container is not None:
            self.container = container
        if source_id is not None:
            self.source_id = source_id
        if amount is not None:
            self.amount = amount
        if description is not None:
            self.description = description
        if post_date is not None:
            self.post_date = post_date
        if user_login_name is not None:
            self.user_login_name = user_login_name
        if account_number is not None:
            self.account_number = account_number
        if transaction_date is not None:
            self.transaction_date = transaction_date
        if base_type is not None:
            self.base_type = base_type
        if status is not None:
            self.status = status

    @property
    def container(self):
        """Gets the container of this EnrichDataTransaction.  # noqa: E501

        The account's container.<br><br><b>Applicable containers</b>: bank,creditCard<br><b>Applicable Values</b><br>  # noqa: E501

        :return: The container of this EnrichDataTransaction.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this EnrichDataTransaction.

        The account's container.<br><br><b>Applicable containers</b>: bank,creditCard<br><b>Applicable Values</b><br>  # noqa: E501

        :param container: The container of this EnrichDataTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["bank", "creditCard", "investment", "insurance", "loan", "reward", "bill", "realEstate", "otherAssets", "otherLiabilities"]  # noqa: E501
        if (self._configuration.client_side_validation and
                container not in allowed_values):
            raise ValueError(
                "Invalid value for `container` ({0}), must be one of {1}"  # noqa: E501
                .format(container, allowed_values)
            )

        self._container = container

    @property
    def source_id(self):
        """Gets the source_id of this EnrichDataTransaction.  # noqa: E501

        A unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts.<br>Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts.  # noqa: E501

        :return: The source_id of this EnrichDataTransaction.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this EnrichDataTransaction.

        A unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts.<br>Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts.  # noqa: E501

        :param source_id: The source_id of this EnrichDataTransaction.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                source_id is not None and len(source_id) > 100):
            raise ValueError("Invalid value for `source_id`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                source_id is not None and len(source_id) < 1):
            raise ValueError("Invalid value for `source_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._source_id = source_id

    @property
    def amount(self):
        """Gets the amount of this EnrichDataTransaction.  # noqa: E501

        The amount of the transaction as it appears at the FI site. <br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :return: The amount of this EnrichDataTransaction.  # noqa: E501
        :rtype: Money
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EnrichDataTransaction.

        The amount of the transaction as it appears at the FI site. <br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :param amount: The amount of this EnrichDataTransaction.  # noqa: E501
        :type: Money
        """

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this EnrichDataTransaction.  # noqa: E501

        Description details<br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :return: The description of this EnrichDataTransaction.  # noqa: E501
        :rtype: Description
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnrichDataTransaction.

        Description details<br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :param description: The description of this EnrichDataTransaction.  # noqa: E501
        :type: Description
        """

        self._description = description

    @property
    def post_date(self):
        """Gets the post_date of this EnrichDataTransaction.  # noqa: E501

        The date on which the transaction is posted to the account.<br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :return: The post_date of this EnrichDataTransaction.  # noqa: E501
        :rtype: str
        """
        return self._post_date

    @post_date.setter
    def post_date(self, post_date):
        """Sets the post_date of this EnrichDataTransaction.

        The date on which the transaction is posted to the account.<br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :param post_date: The post_date of this EnrichDataTransaction.  # noqa: E501
        :type: str
        """

        self._post_date = post_date

    @property
    def user_login_name(self):
        """Gets the user_login_name of this EnrichDataTransaction.  # noqa: E501

        The loginName of the User.<br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :return: The user_login_name of this EnrichDataTransaction.  # noqa: E501
        :rtype: str
        """
        return self._user_login_name

    @user_login_name.setter
    def user_login_name(self, user_login_name):
        """Sets the user_login_name of this EnrichDataTransaction.

        The loginName of the User.<br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :param user_login_name: The user_login_name of this EnrichDataTransaction.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                user_login_name is not None and len(user_login_name) > 2147483647):
            raise ValueError("Invalid value for `user_login_name`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                user_login_name is not None and len(user_login_name) < 1):
            raise ValueError("Invalid value for `user_login_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_login_name = user_login_name

    @property
    def account_number(self):
        """Gets the account_number of this EnrichDataTransaction.  # noqa: E501

        The account number as it appears on the site. (The POST accounts service response return this field as number)<br><b>Additional Details</b>:<b> Bank/ Loan/ Insurance/ Investment/Bill</b>:<br> The account number for the bank account as it appears at the site.<br><b>Credit Card</b>: The account number of the card account as it appears at the site,<br>i.e., the card number.The account number can be full or partial based on how it is displayed in the account summary page of the site.In most cases, the site does not display the full account number in the account summary page and additional navigation is required to aggregate it.<br><b>Applicable containers</b>: All Containers<br><b>Aggregated / Manual</b>: Both <br><b>Endpoints</b>:<br><ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>POST accounts</li><li>POST dataExtracts/userData</li><li>POST dataEnrich/userData</li></ul>  # noqa: E501

        :return: The account_number of this EnrichDataTransaction.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this EnrichDataTransaction.

        The account number as it appears on the site. (The POST accounts service response return this field as number)<br><b>Additional Details</b>:<b> Bank/ Loan/ Insurance/ Investment/Bill</b>:<br> The account number for the bank account as it appears at the site.<br><b>Credit Card</b>: The account number of the card account as it appears at the site,<br>i.e., the card number.The account number can be full or partial based on how it is displayed in the account summary page of the site.In most cases, the site does not display the full account number in the account summary page and additional navigation is required to aggregate it.<br><b>Applicable containers</b>: All Containers<br><b>Aggregated / Manual</b>: Both <br><b>Endpoints</b>:<br><ul><li>GET accounts</li><li>GET accounts/{accountId}</li><li>POST accounts</li><li>POST dataExtracts/userData</li><li>POST dataEnrich/userData</li></ul>  # noqa: E501

        :param account_number: The account_number of this EnrichDataTransaction.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                account_number is not None and len(account_number) > 2147483647):
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                account_number is not None and len(account_number) < 1):
            raise ValueError("Invalid value for `account_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_number = account_number

    @property
    def transaction_date(self):
        """Gets the transaction_date of this EnrichDataTransaction.  # noqa: E501

        The date the transaction happens in the account. <br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :return: The transaction_date of this EnrichDataTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this EnrichDataTransaction.

        The date the transaction happens in the account. <br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :param transaction_date: The transaction_date of this EnrichDataTransaction.  # noqa: E501
        :type: str
        """

        self._transaction_date = transaction_date

    @property
    def base_type(self):
        """Gets the base_type of this EnrichDataTransaction.  # noqa: E501

        Indicates if the transaction appears as a debit or a credit transaction in the account. <br><br><b>Applicable containers</b>: bank,creditCard<br><b>Applicable Values</b><br>  # noqa: E501

        :return: The base_type of this EnrichDataTransaction.  # noqa: E501
        :rtype: str
        """
        return self._base_type

    @base_type.setter
    def base_type(self, base_type):
        """Sets the base_type of this EnrichDataTransaction.

        Indicates if the transaction appears as a debit or a credit transaction in the account. <br><br><b>Applicable containers</b>: bank,creditCard<br><b>Applicable Values</b><br>  # noqa: E501

        :param base_type: The base_type of this EnrichDataTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREDIT", "DEBIT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                base_type not in allowed_values):
            raise ValueError(
                "Invalid value for `base_type` ({0}), must be one of {1}"  # noqa: E501
                .format(base_type, allowed_values)
            )

        self._base_type = base_type

    @property
    def status(self):
        """Gets the status of this EnrichDataTransaction.  # noqa: E501


        :return: The status of this EnrichDataTransaction.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EnrichDataTransaction.


        :param status: The status of this EnrichDataTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["POSTED", "PENDING", "SCHEDULED", "FAILED", "CLEARED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(EnrichDataTransaction, dict):
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
        if not isinstance(other, EnrichDataTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnrichDataTransaction):
            return True

        return self.to_dict() != other.to_dict()
