# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.427
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class CustomEntityResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'href': 'str',
        'entity_type': 'str',
        'version': 'Version',
        'display_name': 'str',
        'description': 'str',
        'identifiers': 'list[CustomEntityId]',
        'fields': 'list[CustomEntityField]',
        'relationships': 'list[Relationship]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'entity_type': 'entityType',
        'version': 'version',
        'display_name': 'displayName',
        'description': 'description',
        'identifiers': 'identifiers',
        'fields': 'fields',
        'relationships': 'relationships',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'entity_type': 'required',
        'version': 'required',
        'display_name': 'required',
        'description': 'optional',
        'identifiers': 'required',
        'fields': 'required',
        'relationships': 'required',
        'links': 'optional'
    }

    def __init__(self, href=None, entity_type=None, version=None, display_name=None, description=None, identifiers=None, fields=None, relationships=None, links=None, local_vars_configuration=None):  # noqa: E501
        """CustomEntityResponse - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param entity_type:  The type of custom entity this is. (required)
        :type entity_type: str
        :param version:  (required)
        :type version: lusid.Version
        :param display_name:  A display label for the custom entity. (required)
        :type display_name: str
        :param description:  A description of the custom entity.
        :type description: str
        :param identifiers:  The identifiers the custom entity will be upserted with. (required)
        :type identifiers: list[lusid.CustomEntityId]
        :param fields:  The fields that decorate the custom entity. (required)
        :type fields: list[lusid.CustomEntityField]
        :param relationships:  A set of relationships associated to the custom entity. (required)
        :type relationships: list[lusid.Relationship]
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._entity_type = None
        self._version = None
        self._display_name = None
        self._description = None
        self._identifiers = None
        self._fields = None
        self._relationships = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.entity_type = entity_type
        self.version = version
        self.display_name = display_name
        self.description = description
        self.identifiers = identifiers
        self.fields = fields
        self.relationships = relationships
        self.links = links

    @property
    def href(self):
        """Gets the href of this CustomEntityResponse.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this CustomEntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CustomEntityResponse.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this CustomEntityResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def entity_type(self):
        """Gets the entity_type of this CustomEntityResponse.  # noqa: E501

        The type of custom entity this is.  # noqa: E501

        :return: The entity_type of this CustomEntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this CustomEntityResponse.

        The type of custom entity this is.  # noqa: E501

        :param entity_type: The entity_type of this CustomEntityResponse.  # noqa: E501
        :type entity_type: str
        """
        if self.local_vars_configuration.client_side_validation and entity_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entity_type is not None and len(entity_type) < 1):
            raise ValueError("Invalid value for `entity_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def version(self):
        """Gets the version of this CustomEntityResponse.  # noqa: E501


        :return: The version of this CustomEntityResponse.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CustomEntityResponse.


        :param version: The version of this CustomEntityResponse.  # noqa: E501
        :type version: lusid.Version
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def display_name(self):
        """Gets the display_name of this CustomEntityResponse.  # noqa: E501

        A display label for the custom entity.  # noqa: E501

        :return: The display_name of this CustomEntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CustomEntityResponse.

        A display label for the custom entity.  # noqa: E501

        :param display_name: The display_name of this CustomEntityResponse.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CustomEntityResponse.  # noqa: E501

        A description of the custom entity.  # noqa: E501

        :return: The description of this CustomEntityResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomEntityResponse.

        A description of the custom entity.  # noqa: E501

        :param description: The description of this CustomEntityResponse.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def identifiers(self):
        """Gets the identifiers of this CustomEntityResponse.  # noqa: E501

        The identifiers the custom entity will be upserted with.  # noqa: E501

        :return: The identifiers of this CustomEntityResponse.  # noqa: E501
        :rtype: list[lusid.CustomEntityId]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this CustomEntityResponse.

        The identifiers the custom entity will be upserted with.  # noqa: E501

        :param identifiers: The identifiers of this CustomEntityResponse.  # noqa: E501
        :type identifiers: list[lusid.CustomEntityId]
        """
        if self.local_vars_configuration.client_side_validation and identifiers is None:  # noqa: E501
            raise ValueError("Invalid value for `identifiers`, must not be `None`")  # noqa: E501

        self._identifiers = identifiers

    @property
    def fields(self):
        """Gets the fields of this CustomEntityResponse.  # noqa: E501

        The fields that decorate the custom entity.  # noqa: E501

        :return: The fields of this CustomEntityResponse.  # noqa: E501
        :rtype: list[lusid.CustomEntityField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CustomEntityResponse.

        The fields that decorate the custom entity.  # noqa: E501

        :param fields: The fields of this CustomEntityResponse.  # noqa: E501
        :type fields: list[lusid.CustomEntityField]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def relationships(self):
        """Gets the relationships of this CustomEntityResponse.  # noqa: E501

        A set of relationships associated to the custom entity.  # noqa: E501

        :return: The relationships of this CustomEntityResponse.  # noqa: E501
        :rtype: list[lusid.Relationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this CustomEntityResponse.

        A set of relationships associated to the custom entity.  # noqa: E501

        :param relationships: The relationships of this CustomEntityResponse.  # noqa: E501
        :type relationships: list[lusid.Relationship]
        """
        if self.local_vars_configuration.client_side_validation and relationships is None:  # noqa: E501
            raise ValueError("Invalid value for `relationships`, must not be `None`")  # noqa: E501

        self._relationships = relationships

    @property
    def links(self):
        """Gets the links of this CustomEntityResponse.  # noqa: E501


        :return: The links of this CustomEntityResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CustomEntityResponse.


        :param links: The links of this CustomEntityResponse.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomEntityResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomEntityResponse):
            return True

        return self.to_dict() != other.to_dict()
