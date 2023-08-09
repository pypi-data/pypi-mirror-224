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


class ComplianceRuleResult(object):
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
        'rule_id': 'str',
        'rule_name': 'str',
        'rule_description': 'str',
        'portfolio': 'ResourceId',
        'passed': 'bool',
        'result_value': 'float',
        'rule_information_match': 'str',
        'rule_information_key': 'str',
        'rule_lower_limit': 'float',
        'rule_upper_limit': 'float'
    }

    attribute_map = {
        'rule_id': 'ruleId',
        'rule_name': 'ruleName',
        'rule_description': 'ruleDescription',
        'portfolio': 'portfolio',
        'passed': 'passed',
        'result_value': 'resultValue',
        'rule_information_match': 'ruleInformationMatch',
        'rule_information_key': 'ruleInformationKey',
        'rule_lower_limit': 'ruleLowerLimit',
        'rule_upper_limit': 'ruleUpperLimit'
    }

    required_map = {
        'rule_id': 'required',
        'rule_name': 'required',
        'rule_description': 'required',
        'portfolio': 'required',
        'passed': 'required',
        'result_value': 'required',
        'rule_information_match': 'required',
        'rule_information_key': 'required',
        'rule_lower_limit': 'required',
        'rule_upper_limit': 'required'
    }

    def __init__(self, rule_id=None, rule_name=None, rule_description=None, portfolio=None, passed=None, result_value=None, rule_information_match=None, rule_information_key=None, rule_lower_limit=None, rule_upper_limit=None, local_vars_configuration=None):  # noqa: E501
        """ComplianceRuleResult - a model defined in OpenAPI"
        
        :param rule_id:  The unique identifierof a compliance rule (required)
        :type rule_id: str
        :param rule_name:  The User-given name of the rule (required)
        :type rule_name: str
        :param rule_description:  The User-given description of the rule (required)
        :type rule_description: str
        :param portfolio:  (required)
        :type portfolio: lusid.ResourceId
        :param passed:  The result of an individual compliance run, true if passed (required)
        :type passed: bool
        :param result_value:  The calculation result that was used to confirm a pass/fail (required)
        :type result_value: float
        :param rule_information_match:  The value matched by the rule (required)
        :type rule_information_match: str
        :param rule_information_key:  The property key matched by the rule (required)
        :type rule_information_key: str
        :param rule_lower_limit:  The lower limit of the rule (required)
        :type rule_lower_limit: float
        :param rule_upper_limit:  The upper limit of the rule (required)
        :type rule_upper_limit: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._rule_id = None
        self._rule_name = None
        self._rule_description = None
        self._portfolio = None
        self._passed = None
        self._result_value = None
        self._rule_information_match = None
        self._rule_information_key = None
        self._rule_lower_limit = None
        self._rule_upper_limit = None
        self.discriminator = None

        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_description = rule_description
        self.portfolio = portfolio
        self.passed = passed
        self.result_value = result_value
        self.rule_information_match = rule_information_match
        self.rule_information_key = rule_information_key
        self.rule_lower_limit = rule_lower_limit
        self.rule_upper_limit = rule_upper_limit

    @property
    def rule_id(self):
        """Gets the rule_id of this ComplianceRuleResult.  # noqa: E501

        The unique identifierof a compliance rule  # noqa: E501

        :return: The rule_id of this ComplianceRuleResult.  # noqa: E501
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ComplianceRuleResult.

        The unique identifierof a compliance rule  # noqa: E501

        :param rule_id: The rule_id of this ComplianceRuleResult.  # noqa: E501
        :type rule_id: str
        """
        if self.local_vars_configuration.client_side_validation and rule_id is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_id is not None and len(rule_id) < 1):
            raise ValueError("Invalid value for `rule_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._rule_id = rule_id

    @property
    def rule_name(self):
        """Gets the rule_name of this ComplianceRuleResult.  # noqa: E501

        The User-given name of the rule  # noqa: E501

        :return: The rule_name of this ComplianceRuleResult.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ComplianceRuleResult.

        The User-given name of the rule  # noqa: E501

        :param rule_name: The rule_name of this ComplianceRuleResult.  # noqa: E501
        :type rule_name: str
        """
        if self.local_vars_configuration.client_side_validation and rule_name is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_name is not None and len(rule_name) < 1):
            raise ValueError("Invalid value for `rule_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._rule_name = rule_name

    @property
    def rule_description(self):
        """Gets the rule_description of this ComplianceRuleResult.  # noqa: E501

        The User-given description of the rule  # noqa: E501

        :return: The rule_description of this ComplianceRuleResult.  # noqa: E501
        :rtype: str
        """
        return self._rule_description

    @rule_description.setter
    def rule_description(self, rule_description):
        """Sets the rule_description of this ComplianceRuleResult.

        The User-given description of the rule  # noqa: E501

        :param rule_description: The rule_description of this ComplianceRuleResult.  # noqa: E501
        :type rule_description: str
        """
        if self.local_vars_configuration.client_side_validation and rule_description is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_description is not None and len(rule_description) < 1):
            raise ValueError("Invalid value for `rule_description`, length must be greater than or equal to `1`")  # noqa: E501

        self._rule_description = rule_description

    @property
    def portfolio(self):
        """Gets the portfolio of this ComplianceRuleResult.  # noqa: E501


        :return: The portfolio of this ComplianceRuleResult.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio

    @portfolio.setter
    def portfolio(self, portfolio):
        """Sets the portfolio of this ComplianceRuleResult.


        :param portfolio: The portfolio of this ComplianceRuleResult.  # noqa: E501
        :type portfolio: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and portfolio is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio`, must not be `None`")  # noqa: E501

        self._portfolio = portfolio

    @property
    def passed(self):
        """Gets the passed of this ComplianceRuleResult.  # noqa: E501

        The result of an individual compliance run, true if passed  # noqa: E501

        :return: The passed of this ComplianceRuleResult.  # noqa: E501
        :rtype: bool
        """
        return self._passed

    @passed.setter
    def passed(self, passed):
        """Sets the passed of this ComplianceRuleResult.

        The result of an individual compliance run, true if passed  # noqa: E501

        :param passed: The passed of this ComplianceRuleResult.  # noqa: E501
        :type passed: bool
        """
        if self.local_vars_configuration.client_side_validation and passed is None:  # noqa: E501
            raise ValueError("Invalid value for `passed`, must not be `None`")  # noqa: E501

        self._passed = passed

    @property
    def result_value(self):
        """Gets the result_value of this ComplianceRuleResult.  # noqa: E501

        The calculation result that was used to confirm a pass/fail  # noqa: E501

        :return: The result_value of this ComplianceRuleResult.  # noqa: E501
        :rtype: float
        """
        return self._result_value

    @result_value.setter
    def result_value(self, result_value):
        """Sets the result_value of this ComplianceRuleResult.

        The calculation result that was used to confirm a pass/fail  # noqa: E501

        :param result_value: The result_value of this ComplianceRuleResult.  # noqa: E501
        :type result_value: float
        """
        if self.local_vars_configuration.client_side_validation and result_value is None:  # noqa: E501
            raise ValueError("Invalid value for `result_value`, must not be `None`")  # noqa: E501

        self._result_value = result_value

    @property
    def rule_information_match(self):
        """Gets the rule_information_match of this ComplianceRuleResult.  # noqa: E501

        The value matched by the rule  # noqa: E501

        :return: The rule_information_match of this ComplianceRuleResult.  # noqa: E501
        :rtype: str
        """
        return self._rule_information_match

    @rule_information_match.setter
    def rule_information_match(self, rule_information_match):
        """Sets the rule_information_match of this ComplianceRuleResult.

        The value matched by the rule  # noqa: E501

        :param rule_information_match: The rule_information_match of this ComplianceRuleResult.  # noqa: E501
        :type rule_information_match: str
        """
        if self.local_vars_configuration.client_side_validation and rule_information_match is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_information_match`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_information_match is not None and len(rule_information_match) < 1):
            raise ValueError("Invalid value for `rule_information_match`, length must be greater than or equal to `1`")  # noqa: E501

        self._rule_information_match = rule_information_match

    @property
    def rule_information_key(self):
        """Gets the rule_information_key of this ComplianceRuleResult.  # noqa: E501

        The property key matched by the rule  # noqa: E501

        :return: The rule_information_key of this ComplianceRuleResult.  # noqa: E501
        :rtype: str
        """
        return self._rule_information_key

    @rule_information_key.setter
    def rule_information_key(self, rule_information_key):
        """Sets the rule_information_key of this ComplianceRuleResult.

        The property key matched by the rule  # noqa: E501

        :param rule_information_key: The rule_information_key of this ComplianceRuleResult.  # noqa: E501
        :type rule_information_key: str
        """
        if self.local_vars_configuration.client_side_validation and rule_information_key is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_information_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                rule_information_key is not None and len(rule_information_key) < 1):
            raise ValueError("Invalid value for `rule_information_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._rule_information_key = rule_information_key

    @property
    def rule_lower_limit(self):
        """Gets the rule_lower_limit of this ComplianceRuleResult.  # noqa: E501

        The lower limit of the rule  # noqa: E501

        :return: The rule_lower_limit of this ComplianceRuleResult.  # noqa: E501
        :rtype: float
        """
        return self._rule_lower_limit

    @rule_lower_limit.setter
    def rule_lower_limit(self, rule_lower_limit):
        """Sets the rule_lower_limit of this ComplianceRuleResult.

        The lower limit of the rule  # noqa: E501

        :param rule_lower_limit: The rule_lower_limit of this ComplianceRuleResult.  # noqa: E501
        :type rule_lower_limit: float
        """
        if self.local_vars_configuration.client_side_validation and rule_lower_limit is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_lower_limit`, must not be `None`")  # noqa: E501

        self._rule_lower_limit = rule_lower_limit

    @property
    def rule_upper_limit(self):
        """Gets the rule_upper_limit of this ComplianceRuleResult.  # noqa: E501

        The upper limit of the rule  # noqa: E501

        :return: The rule_upper_limit of this ComplianceRuleResult.  # noqa: E501
        :rtype: float
        """
        return self._rule_upper_limit

    @rule_upper_limit.setter
    def rule_upper_limit(self, rule_upper_limit):
        """Sets the rule_upper_limit of this ComplianceRuleResult.

        The upper limit of the rule  # noqa: E501

        :param rule_upper_limit: The rule_upper_limit of this ComplianceRuleResult.  # noqa: E501
        :type rule_upper_limit: float
        """
        if self.local_vars_configuration.client_side_validation and rule_upper_limit is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_upper_limit`, must not be `None`")  # noqa: E501

        self._rule_upper_limit = rule_upper_limit

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
        if not isinstance(other, ComplianceRuleResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplianceRuleResult):
            return True

        return self.to_dict() != other.to_dict()
