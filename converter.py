from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal

c = CurrencyRates()
code = CurrencyCodes()


def convert_currency(start, end, amount):
    """Convert given currencies and amount"""
    get_converted = c.convert(start, end, Decimal(amount))
    converted = round(get_converted, 2)
    return converted


def get_symbol(curr_code):
    """Get currency symbol based off code"""
    symbol = code.get_symbol(curr_code)
    return symbol


def get_rates(curr_code):
    """Get all conversion rates for a given currency code"""
    rates = c.get_rates(curr_code)
    return rates
