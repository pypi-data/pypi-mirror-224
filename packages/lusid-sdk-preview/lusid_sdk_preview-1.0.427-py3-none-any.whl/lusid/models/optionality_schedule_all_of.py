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


class OptionalityScheduleAllOf(object):
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
        'exercise_type': 'str',
        'option_entries': 'list[OptionEntry]',
        'option_type': 'str',
        'schedule_type': 'str'
    }

    attribute_map = {
        'exercise_type': 'exerciseType',
        'option_entries': 'optionEntries',
        'option_type': 'optionType',
        'schedule_type': 'scheduleType'
    }

    required_map = {
        'exercise_type': 'optional',
        'option_entries': 'optional',
        'option_type': 'optional',
        'schedule_type': 'required'
    }

    def __init__(self, exercise_type=None, option_entries=None, option_type=None, schedule_type=None, local_vars_configuration=None):  # noqa: E501
        """OptionalityScheduleAllOf - a model defined in OpenAPI"
        
        :param exercise_type:  The exercise type of the optionality schedule (American or European).  For American type, the bond is perpetually callable from a given exercise date until it matures, or the next date in the schedule.  For European type, the bond is only callable on a given exercise date.    Supported string (enumeration) values are: [European, American].
        :type exercise_type: str
        :param option_entries:  The dates at which the bond call/put may be actioned, and associated strikes.
        :type option_entries: list[lusid.OptionEntry]
        :param option_type:  Type of optionality for the schedule.    Supported string (enumeration) values are: [Call, Put].
        :type option_type: str
        :param schedule_type:  The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, Invalid (required)
        :type schedule_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._exercise_type = None
        self._option_entries = None
        self._option_type = None
        self._schedule_type = None
        self.discriminator = None

        self.exercise_type = exercise_type
        self.option_entries = option_entries
        self.option_type = option_type
        self.schedule_type = schedule_type

    @property
    def exercise_type(self):
        """Gets the exercise_type of this OptionalityScheduleAllOf.  # noqa: E501

        The exercise type of the optionality schedule (American or European).  For American type, the bond is perpetually callable from a given exercise date until it matures, or the next date in the schedule.  For European type, the bond is only callable on a given exercise date.    Supported string (enumeration) values are: [European, American].  # noqa: E501

        :return: The exercise_type of this OptionalityScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._exercise_type

    @exercise_type.setter
    def exercise_type(self, exercise_type):
        """Sets the exercise_type of this OptionalityScheduleAllOf.

        The exercise type of the optionality schedule (American or European).  For American type, the bond is perpetually callable from a given exercise date until it matures, or the next date in the schedule.  For European type, the bond is only callable on a given exercise date.    Supported string (enumeration) values are: [European, American].  # noqa: E501

        :param exercise_type: The exercise_type of this OptionalityScheduleAllOf.  # noqa: E501
        :type exercise_type: str
        """

        self._exercise_type = exercise_type

    @property
    def option_entries(self):
        """Gets the option_entries of this OptionalityScheduleAllOf.  # noqa: E501

        The dates at which the bond call/put may be actioned, and associated strikes.  # noqa: E501

        :return: The option_entries of this OptionalityScheduleAllOf.  # noqa: E501
        :rtype: list[lusid.OptionEntry]
        """
        return self._option_entries

    @option_entries.setter
    def option_entries(self, option_entries):
        """Sets the option_entries of this OptionalityScheduleAllOf.

        The dates at which the bond call/put may be actioned, and associated strikes.  # noqa: E501

        :param option_entries: The option_entries of this OptionalityScheduleAllOf.  # noqa: E501
        :type option_entries: list[lusid.OptionEntry]
        """

        self._option_entries = option_entries

    @property
    def option_type(self):
        """Gets the option_type of this OptionalityScheduleAllOf.  # noqa: E501

        Type of optionality for the schedule.    Supported string (enumeration) values are: [Call, Put].  # noqa: E501

        :return: The option_type of this OptionalityScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this OptionalityScheduleAllOf.

        Type of optionality for the schedule.    Supported string (enumeration) values are: [Call, Put].  # noqa: E501

        :param option_type: The option_type of this OptionalityScheduleAllOf.  # noqa: E501
        :type option_type: str
        """

        self._option_type = option_type

    @property
    def schedule_type(self):
        """Gets the schedule_type of this OptionalityScheduleAllOf.  # noqa: E501

        The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, Invalid  # noqa: E501

        :return: The schedule_type of this OptionalityScheduleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this OptionalityScheduleAllOf.

        The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, Invalid  # noqa: E501

        :param schedule_type: The schedule_type of this OptionalityScheduleAllOf.  # noqa: E501
        :type schedule_type: str
        """
        if self.local_vars_configuration.client_side_validation and schedule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FixedSchedule", "FloatSchedule", "OptionalitySchedule", "StepSchedule", "Exercise", "FxRateSchedule", "Invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and schedule_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"  # noqa: E501
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

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
        if not isinstance(other, OptionalityScheduleAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionalityScheduleAllOf):
            return True

        return self.to_dict() != other.to_dict()
