# coding: utf-8

"""
    LOD API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SourceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_source_record_by_entity_and_entity_id(self, id, source_index, **kwargs):  # noqa: E501
        """get_source_record_by_entity_and_entity_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_source_record_by_entity_and_entity_id(id, source_index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID-String of the entity to access. (required)
        :param str source_index: The name of the source-index to access the source-data.Allowed Values: ['swb-aut', 'gnd_marc21', 'kxp-de14'] (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_source_record_by_entity_and_entity_id_with_http_info(id, source_index, **kwargs)  # noqa: E501
        else:
            (data) = self.get_source_record_by_entity_and_entity_id_with_http_info(id, source_index, **kwargs)  # noqa: E501
            return data

    def get_source_record_by_entity_and_entity_id_with_http_info(self, id, source_index, **kwargs):  # noqa: E501
        """get_source_record_by_entity_and_entity_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_source_record_by_entity_and_entity_id_with_http_info(id, source_index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID-String of the entity to access. (required)
        :param str source_index: The name of the source-index to access the source-data.Allowed Values: ['swb-aut', 'gnd_marc21', 'kxp-de14'] (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'source_index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_source_record_by_entity_and_entity_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_source_record_by_entity_and_entity_id`")  # noqa: E501
        # verify the required parameter 'source_index' is set
        if self.api_client.client_side_validation and ('source_index' not in params or
                                                       params['source_index'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `source_index` when calling `get_source_record_by_entity_and_entity_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'source_index' in params:
            path_params['source_index'] = params['source_index']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/source/{source_index}/{id}', 'GET',
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
