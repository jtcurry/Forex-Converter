currency_code_dict = {
    "EUR": "Euro Member Countries",
    "IDR": "Indonesia Rupiah",
    "BGN": "Bulgaria Lev",
    "ILS": "Israel Shekel",
    "GBP": "United Kingdom Pound",
    "DKK": "Denmark Krone",
    "CAD": "Canada Dollar",
    "JPY": "Japan Yen",
    "HUF": "Hungary Forint",
    "RON": "Romania New Leu",
    "MYR": "Malaysia Ringgit",
    "SEK": "Sweden Krona",
    "SGD": "Singapore Dollar",
    "HKD": "Hong Kong Dollar",
    "AUD": "Australia Dollar",
    "CHF": "Switzerland Franc",
    "KRW": "Korea (South) Won",
    "CNY": "China Yuan Renminbi",
    "TRY": "Turkey Lira",
    "HRK": "Croatia Kuna",
    "NZD": "New Zealand Dollar",
    "THB": "Thailand Baht",
    "USD": "United States Dollar",
    "NOK": "Norway Krone",
    "RUB": "Russia Ruble",
    "INR": "India Rupee",
    "MXN": "Mexico Peso",
    "CZK": "Czech Republic Koruna",
    "BRL": "Brazil Real",
    "PLN": "Poland Zloty",
    "PHP": "Philippines Peso",
    "ZAR": "South Africa Rand"
}


def sort_dict(test_dict):
    """Sort dictionary alphabetically"""
    sorted_dict = {}
    for k, v in sorted(test_dict.items()):
        sorted_dict[k] = v
    return sorted_dict


def check_pos_num(num):
    """Check if a positive number was entered"""
    if (float(num) <= 0):
        return False
    else:
        return True