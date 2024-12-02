"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/12"


# ▓ Original requirements
# ░ Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance
# ░ 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4
# ░ indicates that a tank is 75% full.
# ░
# ░ Implement a program that prompts the user, with message "Fraction: " for a fraction,
# ░ formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage
# ░ rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less
# ░ remains, output E instead to indicate that the tank is essentially empty. And if 99% or
# ░ more remains, output F instead to indicate that the tank is essentially full.
# ░
# ░ If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the
# ░ user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like
# ░ "ValueError" or "ZeroDivisionError".
# ░
# ░


# ▓ Hints
# ░ 1.- Recall that a str comes with quite a few methods, per
# ░     docs.python.org/3/library/stdtypes.html#string-methods, including split.
# ░ 2.- Note that you can handle two exceptions separately with code like:
# ░             try:
# ░                 ...
# ░             except ValueError:
# ░                 ...
# ░             except ZeroDivisionError:
# ░                 ...
# ░     Or you can handle two exceptions together with code like:
# ░             try:
# ░                 ...
# ░             except (ValueError, ZeroDivisionError):
# ░                 ...
# ░
# ░


# ▓ Extra work problem statement
# ░ None defined
# ░


# ▓ My pseudo code approach:
# ░ 1.- Define a function "get_int()" that will prompt the user, to enter a fraction.  The
# ░     function needs to evaluate if the input is valid.  If not, it will continue to ask
# ░     until the input is valid.
# ░     1.1.- The function needs to return two integers if input is valid.
# ░     1.2.- Use exception "ValueError" to catch strings that can't convert to integers.
# ░     1.3.- Prompt with "Fraction: ".
# ░     1.4.- Input is valid ONLY when:
# ░         1.4.1.- The string contains ONE forward slash.
# ░         1.4.2.- Either side of the slash contain an integer.
# ░         1.4.3- The first integer has to be less or equal to second integer
# ░         1.4.4.- The second integer is not a zero
# ░ 2.- Divide integer one by integer two.
# ░ 3.- Evaluate and process the division result:
# ░     3.1.- Print to the screen the percentage rounded to the nearest integer
# ░     3.2.- If the percentage is less than 1%, output "E"
# ░     3.2.- If the percentage is more than 99%, output "F"
# ░


# ▓ New Requirements :
# ░ Reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:
# ░ 1.- convert() expects a str in X/Y format as input, wherein each of X and Y is an integer,
# ░     and returns that fraction as a percentage rounded to the nearest int between 0 and 100,
# ░     inclusive. If X and / or Y is not an integer, or if X is greater than Y, then convert
# ░     should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
# ░ 2.- Gauge expects an int and returns a str that is:
# ░     2.1.- "E" if that int is less than or equal to 1,
# ░     2.2.- "F" if that int is greater than or equal to 99,
# ░     2.3.- and "Z%" otherwise, wherein Z is that same int.
# ░
# ░             def main():
# ░                 ...
# ░
# ░             def convert(fraction):
# ░                 ...
# ░
# ░             def gauge(percentage):
# ░                 ...
# ░
# ░             if __name__ == "__main__":
# ░                 main()
# ░
# ░
# ░ Reimplement two or more functions that collectively test your implementations of convert
# ░ and gauge thoroughly, each of whose names should begin with test_ so that you can execute
# ░ your tests with:
# ░
# ░             pytest test_fuel.py
# ░

# ▓ Hints:
# ░ 1.- Be sure to include
# ░
# ░             import fuel
# ░         or
# ░             from fuel import convert, gauge
# ░
# ░     atop test_fuel.py so that you can call convert and gauge in your tests.
# ░
# ░ 2.- Take care to return, not print, an int in convert and a str in gauge. Only main should call print.
# ░ 3.- Note that you can raise an exception like ValueError with code like:
# ░
# ░             raise ValueError
# ░
# ░ 4.- Note that you can check with pytest whether a function has raised an exception, per
# ░ docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions.
# ░

import sys


def convert(fraction: str) -> int:
    """
    convert
        Function accepts a string, which represents a fraction in the form of x/y and it returns
        an integer, rounded to the nearest integer, representing the x divided by y.

        The function should raise a error if:
           1.- if x or y are not integers raise a ValueError
           x is greater than y should raise a ValueError
           2.- if y is zero raise ZeroDivisionError

    Arguments:
        fraction -- must be a string containing two integers separated by "/".

    Returns:
        Returns integer
    """
    # Convert to a string now and split it.
    char_lst: list = fraction.split("/")

    if not char_lst[0].isnumeric() or not char_lst[1].isnumeric():
        raise ValueError()

    num_lst = [int(char_lst[0]), int(char_lst[1])]

    if num_lst[1] == 0:
        raise ZeroDivisionError('The second number cannot be a zero')

    if num_lst[0] > num_lst[1]:
        raise ValueError()
    else:
        return int(num_lst[0] / num_lst[1] * 100)


def gauge(percentage: int) -> str:
    """
    gauge
        Function accepts an integer and uses that integer to build a string representing the relative
        amount of fuel.  As follows:

            Returns "E" if that int is less than or equal to 1,
            Returns "F" if that int is greater than or equal to 99,
            Returns "Z%" wherein Z is that same int.

    Arguments:
        percentage -- Variable must be an integer

    Returns:
        A formatted string as defined in the specs
    """
    # tank_pct = int(my_nums[0] / my_nums[1] * 100)
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return str(percentage) + '%'


def get_input() -> str:
    """
    get_input
        Function asks the user for an input and returns that string as long as it has a slash
        separating two strings.

    Returns:
        Returns the valid string
    """
    num_lst = list()
    while True:
        resp_str = input("Fraction: ").strip()
        if len(resp_str) < 3 or "/" not in resp_str:
            continue
        else:
            return resp_str


def main():
    my_nums_str = get_input()

    # ? Now validate the string
    tank_pct = convert(my_nums_str)

    # ? Now get the tank string representation
    tank_str = gauge(tank_pct)
    print(tank_str)

    # print(f'Division is: {tank_pct}')


# Call main only when intended
if __name__ == '__main__':
    main()
