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
from swagger_client.models.cobrand_login_response import CobrandLoginResponse  # noqa: E501
from swagger_client.rest import ApiException


class TestCobrandLoginResponse(unittest.TestCase):
    """CobrandLoginResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCobrandLoginResponse(self):
        """Test CobrandLoginResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.cobrand_login_response.CobrandLoginResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
