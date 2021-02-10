from flask import Flask, render_template, request, flash, redirect
from helpers import *
from converter import *
from forex_python.converter import RatesNotAvailableError
from decimal import InvalidOperation

app = Flask(__name__)

app.config['SECRET_KEY'] = "newKey"

codes = sort_dict(currency_code_dict)


@app.route("/")
def show_home():
    """Render home page with valid currency codes visible"""
    return render_template("index.html", codes=codes)


@app.route("/convert")
def convert():
    """Convert currency if amount and codes are valid"""
    convert_from = request.args["from"].upper()
    convert_to = request.args["to"].upper()
    convert_amount = request.args["amount"]

    try:
        if (check_pos_num(convert_amount) == False):
            raise InvalidOperation
        converted = convert_currency(convert_from, convert_to, convert_amount)
        from_symbol = get_symbol(convert_from)
        to_symbol = get_symbol(convert_to)
        rates = get_rates(convert_from)
        return render_template("conversion.html",
                               convert_from=convert_from,
                               convert_to=convert_to,
                               convert_amount=convert_amount,
                               converted=converted,
                               from_symbol=from_symbol,
                               to_symbol=to_symbol,
                               rates=rates,
                               codes=codes)
    except RatesNotAvailableError:
        flash("Invalid Currency Code", "error")
        return render_template("index.html", codes=codes)
    except InvalidOperation:
        flash("Invalid Currency Amount", "error")
        return render_template("index.html", codes=codes)
