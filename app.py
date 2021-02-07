from flask import Flask, render_template, request, flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from decimal import Decimal, InvalidOperation
from helpers import *

app = Flask(__name__)
c = CurrencyRates()
code = CurrencyCodes()
app.config['SECRET_KEY'] = "newKey"

codes = sort_dict(currency_code_dict)


@app.route("/")
def show_home():
    return render_template("index.html", codes=codes)


@app.route("/convert")
def convert():
    convert_from = request.args["from"]
    convert_to = request.args["to"]
    convert_amount = request.args["amount"]
    get_converted = c.convert(convert_from, convert_to,
                              Decimal(convert_amount))
    converted = round(get_converted, 2)
    from_symbol = code.get_symbol(convert_from)
    to_symbol = code.get_symbol(convert_to)
    rates = c.get_rates(convert_from)
    return render_template("conversion.html",
                           convert_from=convert_from,
                           convert_to=convert_to,
                           convert_amount=convert_amount,
                           converted=converted,
                           from_symbol=from_symbol,
                           to_symbol=to_symbol,
                           rates=rates,
                           codes=codes)
