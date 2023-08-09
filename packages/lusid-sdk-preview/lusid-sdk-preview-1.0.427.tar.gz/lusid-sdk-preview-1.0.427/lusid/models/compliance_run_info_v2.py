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


class ComplianceRunInfoV2(object):
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
        'run_id': 'ResourceId',
        'instigated_at': 'datetime',
        'completed_at': 'datetime',
        'schedule': 'str',
        'instigated_by': 'str'
    }

    attribute_map = {
        'run_id': 'runId',
        'instigated_at': 'instigatedAt',
        'completed_at': 'completedAt',
        'schedule': 'schedule',
        'instigated_by': 'instigatedBy'
    }

    required_map = {
        'run_id': 'required',
        'instigated_at': 'required',
        'completed_at': 'required',
        'schedule': 'required',
        'instigated_by': 'required'
    }

    def __init__(self, run_id=None, instigated_at=None, completed_at=None, schedule=None, instigated_by=None, local_vars_configuration=None):  # noqa: E501
        """ComplianceRunInfoV2 - a model defined in OpenAPI"
        
        :param run_id:  (required)
        :type run_id: lusid.ResourceId
        :param instigated_at:  (required)
        :type instigated_at: datetime
        :param completed_at:  (required)
        :type completed_at: datetime
        :param schedule:  (required)
        :type schedule: str
        :param instigated_by:  (required)
        :type instigated_by: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._run_id = None
        self._instigated_at = None
        self._completed_at = None
        self._schedule = None
        self._instigated_by = None
        self.discriminator = None

        self.run_id = run_id
        self.instigated_at = instigated_at
        self.completed_at = completed_at
        self.schedule = schedule
        self.instigated_by = instigated_by

    @property
    def run_id(self):
        """Gets the run_id of this ComplianceRunInfoV2.  # noqa: E501


        :return: The run_id of this ComplianceRunInfoV2.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ComplianceRunInfoV2.


        :param run_id: The run_id of this ComplianceRunInfoV2.  # noqa: E501
        :type run_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and run_id is None:  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def instigated_at(self):
        """Gets the instigated_at of this ComplianceRunInfoV2.  # noqa: E501


        :return: The instigated_at of this ComplianceRunInfoV2.  # noqa: E501
        :rtype: datetime
        """
        return self._instigated_at

    @instigated_at.setter
    def instigated_at(self, instigated_at):
        """Sets the instigated_at of this ComplianceRunInfoV2.


        :param instigated_at: The instigated_at of this ComplianceRunInfoV2.  # noqa: E501
        :type instigated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and instigated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `instigated_at`, must not be `None`")  # noqa: E501

        self._instigated_at = instigated_at

    @property
    def completed_at(self):
        """Gets the completed_at of this ComplianceRunInfoV2.  # noqa: E501


        :return: The completed_at of this ComplianceRunInfoV2.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this ComplianceRunInfoV2.


        :param completed_at: The completed_at of this ComplianceRunInfoV2.  # noqa: E501
        :type completed_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and completed_at is None:  # noqa: E501
            raise ValueError("Invalid value for `completed_at`, must not be `None`")  # noqa: E501

        self._completed_at = completed_at

    @property
    def schedule(self):
        """Gets the schedule of this ComplianceRunInfoV2.  # noqa: E501


        :return: The schedule of this ComplianceRunInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ComplianceRunInfoV2.


        :param schedule: The schedule of this ComplianceRunInfoV2.  # noqa: E501
        :type schedule: str
        """
        if self.local_vars_configuration.client_side_validation and schedule is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                schedule is not None and len(schedule) < 1):
            raise ValueError("Invalid value for `schedule`, length must be greater than or equal to `1`")  # noqa: E501

        self._schedule = schedule

    @property
    def instigated_by(self):
        """Gets the instigated_by of this ComplianceRunInfoV2.  # noqa: E501


        :return: The instigated_by of this ComplianceRunInfoV2.  # noqa: E501
        :rtype: str
        """
        return self._instigated_by

    @instigated_by.setter
    def instigated_by(self, instigated_by):
        """Sets the instigated_by of this ComplianceRunInfoV2.


        :param instigated_by: The instigated_by of this ComplianceRunInfoV2.  # noqa: E501
        :type instigated_by: str
        """
        if self.local_vars_configuration.client_side_validation and instigated_by is None:  # noqa: E501
            raise ValueError("Invalid value for `instigated_by`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instigated_by is not None and len(instigated_by) < 1):
            raise ValueError("Invalid value for `instigated_by`, length must be greater than or equal to `1`")  # noqa: E501

        self._instigated_by = instigated_by

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
        if not isinstance(other, ComplianceRunInfoV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceRunInfoV2):
            return True

        return self.to_dict() != other.to_dict()
