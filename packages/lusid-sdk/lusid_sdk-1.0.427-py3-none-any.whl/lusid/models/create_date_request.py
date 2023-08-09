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


class CreateDateRequest(object):
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
        'date_id': 'str',
        'from_utc': 'datetime',
        'to_utc': 'datetime',
        'time_zone': 'str',
        'description': 'str',
        'type': 'str',
        'attributes': 'DateAttributes',
        'source_data': 'dict(str, str)'
    }

    attribute_map = {
        'date_id': 'dateId',
        'from_utc': 'fromUtc',
        'to_utc': 'toUtc',
        'time_zone': 'timeZone',
        'description': 'description',
        'type': 'type',
        'attributes': 'attributes',
        'source_data': 'sourceData'
    }

    required_map = {
        'date_id': 'required',
        'from_utc': 'required',
        'to_utc': 'required',
        'time_zone': 'required',
        'description': 'required',
        'type': 'optional',
        'attributes': 'optional',
        'source_data': 'optional'
    }

    def __init__(self, date_id=None, from_utc=None, to_utc=None, time_zone=None, description=None, type=None, attributes=None, source_data=None, local_vars_configuration=None):  # noqa: E501
        """CreateDateRequest - a model defined in OpenAPI"
        
        :param date_id:  (required)
        :type date_id: str
        :param from_utc:  (required)
        :type from_utc: datetime
        :param to_utc:  (required)
        :type to_utc: datetime
        :param time_zone:  (required)
        :type time_zone: str
        :param description:  (required)
        :type description: str
        :param type: 
        :type type: str
        :param attributes: 
        :type attributes: lusid.DateAttributes
        :param source_data: 
        :type source_data: dict(str, str)

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._date_id = None
        self._from_utc = None
        self._to_utc = None
        self._time_zone = None
        self._description = None
        self._type = None
        self._attributes = None
        self._source_data = None
        self.discriminator = None

        self.date_id = date_id
        self.from_utc = from_utc
        self.to_utc = to_utc
        self.time_zone = time_zone
        self.description = description
        self.type = type
        if attributes is not None:
            self.attributes = attributes
        self.source_data = source_data

    @property
    def date_id(self):
        """Gets the date_id of this CreateDateRequest.  # noqa: E501


        :return: The date_id of this CreateDateRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_id

    @date_id.setter
    def date_id(self, date_id):
        """Sets the date_id of this CreateDateRequest.


        :param date_id: The date_id of this CreateDateRequest.  # noqa: E501
        :type date_id: str
        """
        if self.local_vars_configuration.client_side_validation and date_id is None:  # noqa: E501
            raise ValueError("Invalid value for `date_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                date_id is not None and len(date_id) > 256):
            raise ValueError("Invalid value for `date_id`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                date_id is not None and len(date_id) < 1):
            raise ValueError("Invalid value for `date_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                date_id is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', date_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `date_id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._date_id = date_id

    @property
    def from_utc(self):
        """Gets the from_utc of this CreateDateRequest.  # noqa: E501


        :return: The from_utc of this CreateDateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._from_utc

    @from_utc.setter
    def from_utc(self, from_utc):
        """Sets the from_utc of this CreateDateRequest.


        :param from_utc: The from_utc of this CreateDateRequest.  # noqa: E501
        :type from_utc: datetime
        """
        if self.local_vars_configuration.client_side_validation and from_utc is None:  # noqa: E501
            raise ValueError("Invalid value for `from_utc`, must not be `None`")  # noqa: E501

        self._from_utc = from_utc

    @property
    def to_utc(self):
        """Gets the to_utc of this CreateDateRequest.  # noqa: E501


        :return: The to_utc of this CreateDateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._to_utc

    @to_utc.setter
    def to_utc(self, to_utc):
        """Sets the to_utc of this CreateDateRequest.


        :param to_utc: The to_utc of this CreateDateRequest.  # noqa: E501
        :type to_utc: datetime
        """
        if self.local_vars_configuration.client_side_validation and to_utc is None:  # noqa: E501
            raise ValueError("Invalid value for `to_utc`, must not be `None`")  # noqa: E501

        self._to_utc = to_utc

    @property
    def time_zone(self):
        """Gets the time_zone of this CreateDateRequest.  # noqa: E501


        :return: The time_zone of this CreateDateRequest.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this CreateDateRequest.


        :param time_zone: The time_zone of this CreateDateRequest.  # noqa: E501
        :type time_zone: str
        """
        if self.local_vars_configuration.client_side_validation and time_zone is None:  # noqa: E501
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time_zone is not None and len(time_zone) > 5):
            raise ValueError("Invalid value for `time_zone`, length must be less than or equal to `5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time_zone is not None and len(time_zone) < 0):
            raise ValueError("Invalid value for `time_zone`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time_zone is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', time_zone)):  # noqa: E501
            raise ValueError(r"Invalid value for `time_zone`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._time_zone = time_zone

    @property
    def description(self):
        """Gets the description of this CreateDateRequest.  # noqa: E501


        :return: The description of this CreateDateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDateRequest.


        :param description: The description of this CreateDateRequest.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 100):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this CreateDateRequest.  # noqa: E501


        :return: The type of this CreateDateRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateDateRequest.


        :param type: The type of this CreateDateRequest.  # noqa: E501
        :type type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 10):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 0):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', type)):  # noqa: E501
            raise ValueError(r"Invalid value for `type`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this CreateDateRequest.  # noqa: E501


        :return: The attributes of this CreateDateRequest.  # noqa: E501
        :rtype: lusid.DateAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CreateDateRequest.


        :param attributes: The attributes of this CreateDateRequest.  # noqa: E501
        :type attributes: lusid.DateAttributes
        """

        self._attributes = attributes

    @property
    def source_data(self):
        """Gets the source_data of this CreateDateRequest.  # noqa: E501


        :return: The source_data of this CreateDateRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._source_data

    @source_data.setter
    def source_data(self, source_data):
        """Sets the source_data of this CreateDateRequest.


        :param source_data: The source_data of this CreateDateRequest.  # noqa: E501
        :type source_data: dict(str, str)
        """

        self._source_data = source_data

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
        if not isinstance(other, CreateDateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDateRequest):
            return True

        return self.to_dict() != other.to_dict()
