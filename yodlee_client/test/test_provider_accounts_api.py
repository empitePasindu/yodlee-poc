# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available <a href=\"https://developer.yodlee.com/java-sdk-overview \">here</a>. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/Overview\">Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.provider_accounts_api import ProviderAccountsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProviderAccountsApi(unittest.TestCase):
    """ProviderAccountsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.provider_accounts_api.ProviderAccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_provider_account(self):
        """Test case for delete_provider_account

        Delete Provider Account  # noqa: E501
        """
        pass

    def test_edit_credentials_or_refresh_provider_account(self):
        """Test case for edit_credentials_or_refresh_provider_account

        Update Account  # noqa: E501
        """
        pass

    def test_get_all_provider_accounts(self):
        """Test case for get_all_provider_accounts

        Get Provider Accounts  # noqa: E501
        """
        pass

    def test_get_provider_account(self):
        """Test case for get_provider_account

        Get Provider Account Details  # noqa: E501
        """
        pass

    def test_get_provider_account_profiles(self):
        """Test case for get_provider_account_profiles

        Get User Profile Details  # noqa: E501
        """
        pass

    def test_link_provider_account(self):
        """Test case for link_provider_account

        Add Account  # noqa: E501
        """
        pass

    def test_update_preferences(self):
        """Test case for update_preferences

        Update Preferences  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()