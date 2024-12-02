"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/16"


# ▓Original Requirements:
# ░ Test function "values" in bank.py within this folder.
# ░
# ░


from bank import value

# Either from an import or local definition
# def functionToBeTestedName(): ...


def test_value():
    assert value('Hello') == 0
    assert value('Hi John') == 20
    assert value('Ola John') == 100
