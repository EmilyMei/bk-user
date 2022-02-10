# coding: utf-8

"""
    蓝鲸用户管理 API

    蓝鲸用户管理后台服务 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bkuser_sdk.api_client import ApiClient


class BatchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v2_batch_departments_multiple_retrieve_profiles(self, department_ids, **kwargs):  # noqa: E501
        """v2_batch_departments_multiple_retrieve_profiles  # noqa: E501

        批量获取组织的用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_batch_departments_multiple_retrieve_profiles(department_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str department_ids: department id 列表，以 , 分隔 (required)
        :param bool recursive:
        :return: list[Profile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_batch_departments_multiple_retrieve_profiles_with_http_info(department_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_batch_departments_multiple_retrieve_profiles_with_http_info(department_ids, **kwargs)  # noqa: E501
            return data

    def v2_batch_departments_multiple_retrieve_profiles_with_http_info(self, department_ids, **kwargs):  # noqa: E501
        """v2_batch_departments_multiple_retrieve_profiles  # noqa: E501

        批量获取组织的用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_batch_departments_multiple_retrieve_profiles_with_http_info(department_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str department_ids: department id 列表，以 , 分隔 (required)
        :param bool recursive:
        :return: list[Profile]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['department_ids', 'recursive']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_batch_departments_multiple_retrieve_profiles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'department_ids' is set
        if ('department_ids' not in params or
                params['department_ids'] is None):
            raise ValueError("Missing the required parameter `department_ids` when calling `v2_batch_departments_multiple_retrieve_profiles`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'department_ids' in params:
            query_params.append(('department_ids', params['department_ids']))  # noqa: E501
        if 'recursive' in params:
            query_params.append(('recursive', params['recursive']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/batch/departments/profiles/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Profile]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_batch_profiles_delete(self, body, **kwargs):  # noqa: E501
        """v2_batch_profiles_delete  # noqa: E501

        批量删除用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_batch_profiles_delete(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[UpdateProfile] body: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_batch_profiles_delete_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_batch_profiles_delete_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v2_batch_profiles_delete_with_http_info(self, body, **kwargs):  # noqa: E501
        """v2_batch_profiles_delete  # noqa: E501

        批量删除用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_batch_profiles_delete_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[UpdateProfile] body: (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_batch_profiles_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v2_batch_profiles_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/batch/profiles/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_batch_profiles_partial_update(self, body, **kwargs):  # noqa: E501
        """v2_batch_profiles_partial_update  # noqa: E501

        批量更新用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_batch_profiles_partial_update(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[UpdateProfile] body: (required)
        :return: list[Profile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_batch_profiles_partial_update_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_batch_profiles_partial_update_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v2_batch_profiles_partial_update_with_http_info(self, body, **kwargs):  # noqa: E501
        """v2_batch_profiles_partial_update  # noqa: E501

        批量更新用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_batch_profiles_partial_update_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[UpdateProfile] body: (required)
        :return: list[Profile]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_batch_profiles_partial_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v2_batch_profiles_partial_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/batch/profiles/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Profile]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_batch_profiles_read(self, query_ids, **kwargs):  # noqa: E501
        """v2_batch_profiles_read  # noqa: E501

        批量获取用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_batch_profiles_read(query_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query_ids: 查询 id 列表，以 , 分隔 (required)
        :return: list[Profile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_batch_profiles_read_with_http_info(query_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_batch_profiles_read_with_http_info(query_ids, **kwargs)  # noqa: E501
            return data

    def v2_batch_profiles_read_with_http_info(self, query_ids, **kwargs):  # noqa: E501
        """v2_batch_profiles_read  # noqa: E501

        批量获取用户  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_batch_profiles_read_with_http_info(query_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query_ids: 查询 id 列表，以 , 分隔 (required)
        :return: list[Profile]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_batch_profiles_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_ids' is set
        if ('query_ids' not in params or
                params['query_ids'] is None):
            raise ValueError("Missing the required parameter `query_ids` when calling `v2_batch_profiles_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query_ids' in params:
            query_params.append(('query_ids', params['query_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/batch/profiles/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Profile]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)