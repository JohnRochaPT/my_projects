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

#
#

from plates import is_valid
# ? Either from an import or local definition
# ? def functionToBeTestedName(): ...


def test_functionName():
    assert is_valid('AA1234') == True
    assert is_valid('AAA123') == True
    assert is_valid('11A234') == False
    assert is_valid('AAA1A1') == False
    assert is_valid('AAA1') == True
    assert is_valid('AA0123') == False
    assert is_valid('AAABBA') == True
    assert is_valid('AAABBBBAA') == False
    assert is_valid('1AS188') == False
    assert is_valid('A1') == False
    assert is_valid('AA,F') == False
