# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.427
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid.models.lusid_problem_details import LusidProblemDetails
from lusid.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid.models.resource_list_of_address_key_definition import ResourceListOfAddressKeyDefinition


class StructuredResultDataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_address_key_definitions_for_document(self, scope, code, source, result_type, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetAddressKeyDefinitionsForDocument: Get AddressKeyDefinitions for a virtual document.  # noqa: E501

        For a given virtual document retrieve all the address key definitions that are in use.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_address_key_definitions_for_document(scope, code, source, result_type, async_req=True)
        >>> result = thread.get()

        :param scope: The scope of the document for which address key definitions are retrieved. (required)
        :type scope: str
        :param code: The code of the document for which address key definitions are retrieved. (required)
        :type code: str
        :param source: The source of the document for which address key definitions are retrieved. (required)
        :type source: str
        :param result_type: The result type of the document for which address key definitions are retrieved. (required)
        :type result_type: str
        :param effective_at: The effective datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified.
        :type effective_at: str
        :param as_at: The asAt datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified.
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListOfAddressKeyDefinition
        """
        kwargs['_return_http_data_only'] = True
        return self.get_address_key_definitions_for_document_with_http_info(scope, code, source, result_type, **kwargs)  # noqa: E501

    def get_address_key_definitions_for_document_with_http_info(self, scope, code, source, result_type, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetAddressKeyDefinitionsForDocument: Get AddressKeyDefinitions for a virtual document.  # noqa: E501

        For a given virtual document retrieve all the address key definitions that are in use.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_address_key_definitions_for_document_with_http_info(scope, code, source, result_type, async_req=True)
        >>> result = thread.get()

        :param scope: The scope of the document for which address key definitions are retrieved. (required)
        :type scope: str
        :param code: The code of the document for which address key definitions are retrieved. (required)
        :type code: str
        :param source: The source of the document for which address key definitions are retrieved. (required)
        :type source: str
        :param result_type: The result type of the document for which address key definitions are retrieved. (required)
        :type result_type: str
        :param effective_at: The effective datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified.
        :type effective_at: str
        :param as_at: The asAt datetime to query the document for which the address key definitions are retrieved.              Defaults to querying the latest version if not specified.
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (ResourceListOfAddressKeyDefinition, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'scope',
            'code',
            'source',
            'result_type',
            'effective_at',
            'as_at'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_address_key_definitions_for_document" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if self.api_client.client_side_validation and ('scope' not in local_var_params or  # noqa: E501
                                                        local_var_params['scope'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scope` when calling `get_address_key_definitions_for_document`")  # noqa: E501
        # verify the required parameter 'code' is set
        if self.api_client.client_side_validation and ('code' not in local_var_params or  # noqa: E501
                                                        local_var_params['code'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `code` when calling `get_address_key_definitions_for_document`")  # noqa: E501
        # verify the required parameter 'source' is set
        if self.api_client.client_side_validation and ('source' not in local_var_params or  # noqa: E501
                                                        local_var_params['source'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `source` when calling `get_address_key_definitions_for_document`")  # noqa: E501
        # verify the required parameter 'result_type' is set
        if self.api_client.client_side_validation and ('result_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['result_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `result_type` when calling `get_address_key_definitions_for_document`")  # noqa: E501

        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) > 256):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_address_key_definitions_for_document`, length must be less than or equal to `256`")  # noqa: E501
        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_address_key_definitions_for_document`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_address_key_definitions_for_document`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['code']) > 256):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_address_key_definitions_for_document`, length must be less than or equal to `256`")  # noqa: E501
        if self.api_client.client_side_validation and ('code' in local_var_params and  # noqa: E501
                                                        len(local_var_params['code']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_address_key_definitions_for_document`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_address_key_definitions_for_document`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('source' in local_var_params and  # noqa: E501
                                                        len(local_var_params['source']) > 256):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `source` when calling `get_address_key_definitions_for_document`, length must be less than or equal to `256`")  # noqa: E501
        if self.api_client.client_side_validation and ('source' in local_var_params and  # noqa: E501
                                                        len(local_var_params['source']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `source` when calling `get_address_key_definitions_for_document`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'source' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['source']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `source` when calling `get_address_key_definitions_for_document`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501
        if 'source' in local_var_params:
            path_params['source'] = local_var_params['source']  # noqa: E501
        if 'result_type' in local_var_params:
            path_params['resultType'] = local_var_params['result_type']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params and local_var_params['effective_at'] is not None:  # noqa: E501
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.0.427'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "ResourceListOfAddressKeyDefinition",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/unitresults/virtualdocument/{scope}/{code}/{source}/{resultType}/addresskeydefinitions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
