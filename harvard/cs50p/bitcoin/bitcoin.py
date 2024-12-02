"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/15"

# ▓ Original Requirements:
# ░ Implement a program that:
# ░ 1.- Expects the user to specify as a command-line argument the number of Bitcoins,"n", that
# ░     they would like to buy. If that argument cannot be converted to a float, the program
# ░     should exit via sys.exit with an error message.
# ░
# ░ 2.- Queries the API for the CoinDesk Bitcoin Price Index at
# ░     https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among
# ░     whose nested keys is the current price of Bitcoin as a float. Be sure to catch any
# ░     exceptions, as with code like:
# ░
# ░                      import requests
# ░                      try:
# ░                          ...
# ░                      except requests.RequestException:
# ░                          ...
# ░
# ░ 3.- Outputs the current cost of "n" Bitcoins in USD to four decimal places, using, as a
# ░     thousands separator.
# ░


# ▓ Hints:
# ░ 1.- Recall that the sys module comes with argv, per
# ░     docs.python.org/3/library/sys.html#sys.argv.
# ░
# ░ 2.- Note that the requests module comes with quite a few methods, per
# ░     requests.readthedocs.io/en/latest, among which are get, per
# ░     requests.readthedocs.io/en/latest/user/quickstart.html#make-a-request, and json, per
# ░     requests.readthedocs.io/en/latest/user/quickstart.html#json-response-content. You can install
# ░     it with:
# ░
# ░                 pip install requests
# ░
# ░ 3.- Note that CoinDesk’s API returns a JSON response like:
# ░             {
# ░                 "time": {
# ░                     "updated": "May 2, 2022 15:27:00 UTC",
# ░                     "updatedISO": "2022-05-02T15:27:00+00:00",
# ░                     "updateduk": "May 2, 2022 at 16:27 BST"
# ░                 },
# ░                 "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
# ░                "chartName": "Bitcoin",
# ░                 "bpi": {
# ░                     "USD": {
# ░                         "code": "USD",
# ░                         "symbol": "&#36;",
# ░                         "rate": "38,761.0833",
# ░                         "description": "United States Dollar",
# ░                         "rate_float": 38761.0833
# ░                     },
# ░                     "GBP": {
# ░                         "code": "GBP",
# ░                         "symbol": "&pound;",
# ░                         "rate": "30,827.6198",
# ░                         "description": "British Pound Sterling",
# ░                         "rate_float": 30827.6198
# ░                     },
# ░                     "EUR": {
# ░                         "code": "EUR",
# ░                         "symbol": "&euro;",
# ░                         "rate": "36,800.2764",
# ░                         "description": "Euro",
# ░                         "rate_float": 36800.2764
# ░                     }
# ░                 }
# ░             }
# ░
# ░ 4.- Recall that you can format USD to four decimal places with a thousands separator with
# ░     code like:
# ░             print(f"${amount:,.4f}")
# ░


# ▓ Extra work requirements:
# ░ None defined.
# ░
# ░

# ▓ My pseudo code approach:
# ░ 1.- If not already installed in the Anaconda environment, install library "requests"
# ░
# ░ 2.- The program needs to accept one argument that represents the number of Bitcoins that
# ░     the user would like to buy.  Validate as follows:
# ░    2.1.- There has to be one argument.  If there is no argument, exit the program via
# ░          sys.exit with an error message.
# ░        2.1.1.- The output message needs to be "Missing command-line argument"
# ░    2.2.- If the parameter cannot be converted to a float, exit the program via sys.exit
# ░          with an error message.
# ░        2.2.1.- The output message needs to be "Command-line argument is not a number"
# ░
# ░ 3.- Using methods and functions from "requests", ask website
# ░     https://api.coindesk.com/v1/bpi/currentprice.json for the current price of Bitcoins.
# ░    3.1.- Ensure that you safeguard the calls to the site and handle errors gracefully.
# ░    3.2.- Site returns a JSON structure.
# ░         3.2.1.- Look for exceptions with requests.RequestException:
# ░         3.2.2.- Confirm that the JSON response is indeed JSON.  If there is a problem
# ░                 with the response, exit gracefully.
# ░         3.2.3.- Confirm that the structure contains a dictionary entry containing the
# ░                 current price of Bitcoin.
# ░
# ░ 4.- Outputs the current cost of "n" Bitcoins in USD to four decimal places, using, as a
# ░     thousands separator.  Use formula print(f"${amount:,.4f}")
# ░
# ░
# ░
# ░

import requests
import sys
import json


def check_arg():
    """
    check_arg
        Function needs to confirm that the program was called passing the arguments it needs

        The program requires a float to be passed as a parameter when calling the program.  If
        the there is no parameter, it must be convertible to a float and must be positive.

    """
    try:
        my_first_parameter = sys.argv[1]
    except:
        sys.exit('Missing command-line argument')

    try:
        float(sys.argv[1])
    except:
        sys.exit(
            'Command-line argument is not a number')


def main():
    # ? Call function check_args()
    check_arg()

    # ? Get the json structure so we can look for the key.
    resp = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    # ? Now that we have a response, load it to a json variable.
    resp_j = resp.json()

    # ? Now get the rate
    # ? The rate will have commas and need to be removed.
    bit_rate = float(str(resp_j['bpi']['USD']['rate']).replace(',', ''))

    # ? Now output in the right format
    print(f"${(float(sys.argv[1]) * bit_rate):,.4f}")


# ? Call main ONLY when intended
if __name__ == "__main__":
    main()
