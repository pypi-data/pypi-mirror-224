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


class TermDepositAllOf(object):
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
        'start_date': 'datetime',
        'maturity_date': 'datetime',
        'contract_size': 'float',
        'flow_convention': 'FlowConventions',
        'rate': 'float',
        'dom_ccy': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'contract_size': 'contractSize',
        'flow_convention': 'flowConvention',
        'rate': 'rate',
        'dom_ccy': 'domCcy',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'required',
        'contract_size': 'required',
        'flow_convention': 'required',
        'rate': 'required',
        'dom_ccy': 'optional',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, contract_size=None, flow_convention=None, rate=None, dom_ccy=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """TermDepositAllOf - a model defined in OpenAPI"
        
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. (required)
        :type maturity_date: datetime
        :param contract_size:  With an OTC we have the problem of multiple ways of booking a quantity.              e.g.              If buying a swap do you have a holding of size 1 of 100,000,000 notional swap or a holding of 100,000,000 size of 1 notional swap, or any combination that multiplies to 10^8.              When you get for a price for a 'unit swap' what do you mean? The definition must be consistent across all quotes. This includes bonds which have a face value and              fx-forwards which often trade in standard contract sizes. When we look up a price, and there are no units, we are assuming it is a price for a contract size of 1.              The logical effect of this is that              instrument clean price = contract size * quoted unit price              holding clean price    = holding quantity * instrument clean price = holding quantity * contract size * quoted unit price              In calculating accrued interest the same should hold.              NB: The real problem is that people store \"prices\" without complete units. Everything should really be \"x ccy for n units\". Where the n is implicit the above has to hold. (required)
        :type contract_size: float
        :param flow_convention:  (required)
        :type flow_convention: lusid.FlowConventions
        :param rate:  The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest (required)
        :type rate: float
        :param dom_ccy:  DomCcy of the TermDeposit. If provided, must match the currency of FlowConvention.
        :type dom_ccy: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._contract_size = None
        self._flow_convention = None
        self._rate = None
        self._dom_ccy = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        self.maturity_date = maturity_date
        self.contract_size = contract_size
        self.flow_convention = flow_convention
        self.rate = rate
        self.dom_ccy = dom_ccy
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this TermDepositAllOf.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this TermDepositAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TermDepositAllOf.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this TermDepositAllOf.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this TermDepositAllOf.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :return: The maturity_date of this TermDepositAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this TermDepositAllOf.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.  # noqa: E501

        :param maturity_date: The maturity_date of this TermDepositAllOf.  # noqa: E501
        :type maturity_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and maturity_date is None:  # noqa: E501
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def contract_size(self):
        """Gets the contract_size of this TermDepositAllOf.  # noqa: E501

        With an OTC we have the problem of multiple ways of booking a quantity.              e.g.              If buying a swap do you have a holding of size 1 of 100,000,000 notional swap or a holding of 100,000,000 size of 1 notional swap, or any combination that multiplies to 10^8.              When you get for a price for a 'unit swap' what do you mean? The definition must be consistent across all quotes. This includes bonds which have a face value and              fx-forwards which often trade in standard contract sizes. When we look up a price, and there are no units, we are assuming it is a price for a contract size of 1.              The logical effect of this is that              instrument clean price = contract size * quoted unit price              holding clean price    = holding quantity * instrument clean price = holding quantity * contract size * quoted unit price              In calculating accrued interest the same should hold.              NB: The real problem is that people store \"prices\" without complete units. Everything should really be \"x ccy for n units\". Where the n is implicit the above has to hold.  # noqa: E501

        :return: The contract_size of this TermDepositAllOf.  # noqa: E501
        :rtype: float
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this TermDepositAllOf.

        With an OTC we have the problem of multiple ways of booking a quantity.              e.g.              If buying a swap do you have a holding of size 1 of 100,000,000 notional swap or a holding of 100,000,000 size of 1 notional swap, or any combination that multiplies to 10^8.              When you get for a price for a 'unit swap' what do you mean? The definition must be consistent across all quotes. This includes bonds which have a face value and              fx-forwards which often trade in standard contract sizes. When we look up a price, and there are no units, we are assuming it is a price for a contract size of 1.              The logical effect of this is that              instrument clean price = contract size * quoted unit price              holding clean price    = holding quantity * instrument clean price = holding quantity * contract size * quoted unit price              In calculating accrued interest the same should hold.              NB: The real problem is that people store \"prices\" without complete units. Everything should really be \"x ccy for n units\". Where the n is implicit the above has to hold.  # noqa: E501

        :param contract_size: The contract_size of this TermDepositAllOf.  # noqa: E501
        :type contract_size: float
        """
        if self.local_vars_configuration.client_side_validation and contract_size is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_size`, must not be `None`")  # noqa: E501

        self._contract_size = contract_size

    @property
    def flow_convention(self):
        """Gets the flow_convention of this TermDepositAllOf.  # noqa: E501


        :return: The flow_convention of this TermDepositAllOf.  # noqa: E501
        :rtype: lusid.FlowConventions
        """
        return self._flow_convention

    @flow_convention.setter
    def flow_convention(self, flow_convention):
        """Sets the flow_convention of this TermDepositAllOf.


        :param flow_convention: The flow_convention of this TermDepositAllOf.  # noqa: E501
        :type flow_convention: lusid.FlowConventions
        """
        if self.local_vars_configuration.client_side_validation and flow_convention is None:  # noqa: E501
            raise ValueError("Invalid value for `flow_convention`, must not be `None`")  # noqa: E501

        self._flow_convention = flow_convention

    @property
    def rate(self):
        """Gets the rate of this TermDepositAllOf.  # noqa: E501

        The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest  # noqa: E501

        :return: The rate of this TermDepositAllOf.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this TermDepositAllOf.

        The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest  # noqa: E501

        :param rate: The rate of this TermDepositAllOf.  # noqa: E501
        :type rate: float
        """
        if self.local_vars_configuration.client_side_validation and rate is None:  # noqa: E501
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this TermDepositAllOf.  # noqa: E501

        DomCcy of the TermDeposit. If provided, must match the currency of FlowConvention.  # noqa: E501

        :return: The dom_ccy of this TermDepositAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this TermDepositAllOf.

        DomCcy of the TermDeposit. If provided, must match the currency of FlowConvention.  # noqa: E501

        :param dom_ccy: The dom_ccy of this TermDepositAllOf.  # noqa: E501
        :type dom_ccy: str
        """

        self._dom_ccy = dom_ccy

    @property
    def instrument_type(self):
        """Gets the instrument_type of this TermDepositAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :return: The instrument_type of this TermDepositAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this TermDepositAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan  # noqa: E501

        :param instrument_type: The instrument_type of this TermDepositAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond", "InflationSwap", "SimpleCashFlowLoan"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, TermDepositAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TermDepositAllOf):
            return True

        return self.to_dict() != other.to_dict()
