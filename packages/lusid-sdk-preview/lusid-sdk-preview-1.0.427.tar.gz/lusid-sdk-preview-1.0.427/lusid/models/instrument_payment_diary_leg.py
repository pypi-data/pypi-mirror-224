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


class InstrumentPaymentDiaryLeg(object):
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
        'leg_id': 'str',
        'rows': 'list[InstrumentPaymentDiaryRow]'
    }

    attribute_map = {
        'leg_id': 'legId',
        'rows': 'rows'
    }

    required_map = {
        'leg_id': 'optional',
        'rows': 'optional'
    }

    def __init__(self, leg_id=None, rows=None, local_vars_configuration=None):  # noqa: E501
        """InstrumentPaymentDiaryLeg - a model defined in OpenAPI"
        
        :param leg_id:  Identifier for the leg of a payment diary.
        :type leg_id: str
        :param rows:  List of individual cashflows within the payment diary.
        :type rows: list[lusid.InstrumentPaymentDiaryRow]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._leg_id = None
        self._rows = None
        self.discriminator = None

        self.leg_id = leg_id
        self.rows = rows

    @property
    def leg_id(self):
        """Gets the leg_id of this InstrumentPaymentDiaryLeg.  # noqa: E501

        Identifier for the leg of a payment diary.  # noqa: E501

        :return: The leg_id of this InstrumentPaymentDiaryLeg.  # noqa: E501
        :rtype: str
        """
        return self._leg_id

    @leg_id.setter
    def leg_id(self, leg_id):
        """Sets the leg_id of this InstrumentPaymentDiaryLeg.

        Identifier for the leg of a payment diary.  # noqa: E501

        :param leg_id: The leg_id of this InstrumentPaymentDiaryLeg.  # noqa: E501
        :type leg_id: str
        """

        self._leg_id = leg_id

    @property
    def rows(self):
        """Gets the rows of this InstrumentPaymentDiaryLeg.  # noqa: E501

        List of individual cashflows within the payment diary.  # noqa: E501

        :return: The rows of this InstrumentPaymentDiaryLeg.  # noqa: E501
        :rtype: list[lusid.InstrumentPaymentDiaryRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this InstrumentPaymentDiaryLeg.

        List of individual cashflows within the payment diary.  # noqa: E501

        :param rows: The rows of this InstrumentPaymentDiaryLeg.  # noqa: E501
        :type rows: list[lusid.InstrumentPaymentDiaryRow]
        """

        self._rows = rows

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
        if not isinstance(other, InstrumentPaymentDiaryLeg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstrumentPaymentDiaryLeg):
            return True

        return self.to_dict() != other.to_dict()
