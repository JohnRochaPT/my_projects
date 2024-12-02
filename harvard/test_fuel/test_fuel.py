"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/##/##'


# ▓Original Requirements:
# ░ Test function "values" in bank.py within this folder.
# ░
# ░

import fuel
import pytest

#
#
# ? from bank import value
# ? Either from an import or local definition
# ? def functionToBeTestedName(): ...


def test_convert():
    assert fuel.convert('1/100') == 1
    assert fuel.convert('1/2') == 50
    assert fuel.convert('1/3') == 33


def test_gauge():
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(99) == 'F'
    assert fuel.gauge(2) == '2%'
    assert fuel.gauge(50) == '50%'


def test_raises_typeError():
    with pytest.raises(ValueError):
        fuel.convert('2/1')
    with pytest.raises(ValueError):
        fuel.convert('a/b')
    with pytest.raises(ZeroDivisionError):
        fuel.convert('1/0')


# def test_raises_zeroDivisionError():
#    with pytest.raises(ZeroDivisionError):
#        fuel.convert('2/0')
