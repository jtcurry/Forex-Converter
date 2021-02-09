from unittest import TestCase
from app import app
from flask import request
from helpers import sort_dict
from converter import *


class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_sort_dict(self):
        """Test that sort_dict sorts dictionary alphabetically by key"""
        test_dict = {"b": "two", "c": "three", "a": "one"}
        result_dict = {"a": "one", "b": "two", "c": "three"}
        self.assertEqual(sort_dict(test_dict), result_dict)

    def test_home(self):
        """Make sure homepage is rendered properly"""
        response = self.client.get("/")
        html = response.get_data(as_text=True)
        self.assertIn('<h3>Select Currency</h3>', html)

    def test_convert_render(self):
        """Test converted currencies are rendered"""
        with self.client:
            response = self.client.get("/convert?from=USD&to=USD&amount=1")
            self.assertEqual(request.args["from"], "USD")
            self.assertEqual(request.args["to"], "USD")
            self.assertEqual(request.args["amount"], "1")
            converted = convert_currency(request.args["from"],
                                         request.args["to"],
                                         request.args["amount"])
            self.assertEqual(converted, Decimal("1.00"))
            html = response.get_data(as_text=True)
            self.assertIn('<p>USD <i class="fas fa-exchange-alt"></i> USD</p>',
                          html)

    def test_conversion(self):
        """Test if conversion of two currencies return correct amount"""
        converted = convert_currency("USD", "USD", "1")
        self.assertEqual(converted, Decimal("1.00"))

    def test_symbol(self):
        """Test symbol is returned from selected currency"""
        symbol = code.get_symbol("GBP")
        self.assertEqual(symbol, "£")

    # def test_invalid(self):
    #     with self.client:
    #         invcode = convert_currency("USwefwefD", "USD", "1")
    #         self.assertRaises(RatesNotAvailableError, invcode)
