# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. Yodlee supports the Java SDK and it is available <a href=\"https://developer.yodlee.com/java-sdk-overview \">here</a>. You can generate a client SDK for Python, Java, JavaScript, PHP, or other languages according to your development needs. For more details about the APIs, refer to <a href=\"https://developer.yodlee.com/docs/api/1.1/Overview\">Yodlee API v1.1 - Overview</a>.<br><br>You will have to set the header before making the API call. The following headers apply to all the APIs:<ul><li>Authorization: This header holds the access token</li> <li> Api-Version: 1.1</li></ul><b>Note</b>: If there are any API-specific headers, they are mentioned explicitly in the respective API's description.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_access_tokens(self, app_ids, **kwargs):  # noqa: E501
        """Get Access Tokens  # noqa: E501

        The Get Access Tokens service is used to retrieve the access tokens for the application id(s) provided.<br>URL in the response can be used to launch the application for which token is requested.<br><br><b>Note:</b> <li>This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_tokens(app_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_ids: appIds (required)
        :return: UserAccessTokensResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_access_tokens_with_http_info(app_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_access_tokens_with_http_info(app_ids, **kwargs)  # noqa: E501
            return data

    def get_access_tokens_with_http_info(self, app_ids, **kwargs):  # noqa: E501
        """Get Access Tokens  # noqa: E501

        The Get Access Tokens service is used to retrieve the access tokens for the application id(s) provided.<br>URL in the response can be used to launch the application for which token is requested.<br><br><b>Note:</b> <li>This endpoint is deprecated for customers using the API Key-based authentication and is applicable only to customers who use the SAML-based authentication.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_tokens_with_http_info(app_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_ids: appIds (required)
        :return: UserAccessTokensResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_tokens" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_ids' is set
        if self.api_client.client_side_validation and ('app_ids' not in params or
                                                       params['app_ids'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `app_ids` when calling `get_access_tokens`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_ids' in params:
            query_params.append(('appIds', params['app_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/accessTokens', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserAccessTokensResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user(self, **kwargs):  # noqa: E501
        """Get User Details  # noqa: E501

        The get user details service is used to get the user profile information and the application preferences set at the time of user registration.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_with_http_info(self, **kwargs):  # noqa: E501
        """Get User Details  # noqa: E501

        The get user details service is used to get the user profile information and the application preferences set at the time of user registration.<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: UserDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserDetailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_user(self, user_request, **kwargs):  # noqa: E501
        """Register User  # noqa: E501

        The register user service is used to register a user in Yodlee.<br>The loginName cannot include spaces and must be between 3 and 150 characters.<br>locale passed must be one of the supported locales for the customer. <br>Currency provided in the input will be respected in the derived services and the amount fields in the response will be provided in the preferred currency.<br>userParam is accepted as a body parameter. <br><br><b>Note:</b> <li>The content type has to be passed as application/json for the body parameter.</li>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_user(user_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserRequest user_request: userRequest (required)
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.register_user_with_http_info(user_request, **kwargs)  # noqa: E501
        else:
            (data) = self.register_user_with_http_info(user_request, **kwargs)  # noqa: E501
            return data

    def register_user_with_http_info(self, user_request, **kwargs):  # noqa: E501
        """Register User  # noqa: E501

        The register user service is used to register a user in Yodlee.<br>The loginName cannot include spaces and must be between 3 and 150 characters.<br>locale passed must be one of the supported locales for the customer. <br>Currency provided in the input will be respected in the derived services and the amount fields in the response will be provided in the preferred currency.<br>userParam is accepted as a body parameter. <br><br><b>Note:</b> <li>The content type has to be passed as application/json for the body parameter.</li>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_user_with_http_info(user_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UserRequest user_request: userRequest (required)
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_request' is set
        if self.api_client.client_side_validation and ('user_request' not in params or
                                                       params['user_request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_request` when calling `register_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_request' in params:
            body_params = params['user_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def saml_login(self, issuer, saml_response, **kwargs):  # noqa: E501
        """Saml Login  # noqa: E501

        The SAML login service is used to authenticate system users with a SAML response.<br>A new user will be created with the input provided if that user isn't already in the system.<br>For existing users, the system will make updates based on changes or new information.<br>When authentication is successful, a user session token is returned.<br><br><b>Note:</b> <li>The content type has to be passed as application/x-www-form-urlencoded. <li>issuer, source and samlResponse should be passed as body parameters.</li>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.saml_login(issuer, saml_response, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str issuer: issuer (required)
        :param str saml_response: samlResponse (required)
        :param str source: source
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.saml_login_with_http_info(issuer, saml_response, **kwargs)  # noqa: E501
        else:
            (data) = self.saml_login_with_http_info(issuer, saml_response, **kwargs)  # noqa: E501
            return data

    def saml_login_with_http_info(self, issuer, saml_response, **kwargs):  # noqa: E501
        """Saml Login  # noqa: E501

        The SAML login service is used to authenticate system users with a SAML response.<br>A new user will be created with the input provided if that user isn't already in the system.<br>For existing users, the system will make updates based on changes or new information.<br>When authentication is successful, a user session token is returned.<br><br><b>Note:</b> <li>The content type has to be passed as application/x-www-form-urlencoded. <li>issuer, source and samlResponse should be passed as body parameters.</li>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.saml_login_with_http_info(issuer, saml_response, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str issuer: issuer (required)
        :param str saml_response: samlResponse (required)
        :param str source: source
        :return: UserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['issuer', 'saml_response', 'source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method saml_login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'issuer' is set
        if self.api_client.client_side_validation and ('issuer' not in params or
                                                       params['issuer'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `issuer` when calling `saml_login`")  # noqa: E501
        # verify the required parameter 'saml_response' is set
        if self.api_client.client_side_validation and ('saml_response' not in params or
                                                       params['saml_response'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `saml_response` when calling `saml_login`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'issuer' in params:
            query_params.append(('issuer', params['issuer']))  # noqa: E501
        if 'saml_response' in params:
            query_params.append(('samlResponse', params['saml_response']))  # noqa: E501
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/samlLogin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unregister(self, **kwargs):  # noqa: E501
        """Delete User  # noqa: E501

        The delete user service is used to delete or unregister a user from Yodlee. <br>Once deleted, the information related to the users cannot be retrieved. <br>The HTTP response code is 204 (Success without content)<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unregister(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unregister_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.unregister_with_http_info(**kwargs)  # noqa: E501
            return data

    def unregister_with_http_info(self, **kwargs):  # noqa: E501
        """Delete User  # noqa: E501

        The delete user service is used to delete or unregister a user from Yodlee. <br>Once deleted, the information related to the users cannot be retrieved. <br>The HTTP response code is 204 (Success without content)<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unregister_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unregister" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/unregister', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user(self, user_request, **kwargs):  # noqa: E501
        """Update User Details  # noqa: E501

        The update user details service is used to update user details like name, address, currency preference, etc.<br>Currency provided in the input will be respected in the <a href=\"https://developer.yodlee.com/api-reference#tag/Derived\">derived</a> services and the amount fields in the response will be provided in the preferred currency.<br>The HTTP response code is 204 (Success without content). <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user(user_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateUserRequest user_request: userRequest (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_with_http_info(user_request, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_with_http_info(user_request, **kwargs)  # noqa: E501
            return data

    def update_user_with_http_info(self, user_request, **kwargs):  # noqa: E501
        """Update User Details  # noqa: E501

        The update user details service is used to update user details like name, address, currency preference, etc.<br>Currency provided in the input will be respected in the <a href=\"https://developer.yodlee.com/api-reference#tag/Derived\">derived</a> services and the amount fields in the response will be provided in the preferred currency.<br>The HTTP response code is 204 (Success without content). <br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_with_http_info(user_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateUserRequest user_request: userRequest (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_request' is set
        if self.api_client.client_side_validation and ('user_request' not in params or
                                                       params['user_request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `user_request` when calling `update_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_request' in params:
            body_params = params['user_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_logout(self, **kwargs):  # noqa: E501
        """User Logout  # noqa: E501

        <b>Deprecated</b>: This endpoint is deprecated for API Key-based authentication. The user logout service allows the user to log out of the application.<br>The service does not return a response body. The HTTP response code is 204 (Success with no content).<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_logout(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_logout_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.user_logout_with_http_info(**kwargs)  # noqa: E501
            return data

    def user_logout_with_http_info(self, **kwargs):  # noqa: E501
        """User Logout  # noqa: E501

        <b>Deprecated</b>: This endpoint is deprecated for API Key-based authentication. The user logout service allows the user to log out of the application.<br>The service does not return a response body. The HTTP response code is 204 (Success with no content).<br>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_logout_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_logout" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/user/logout', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
