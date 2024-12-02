"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/23'

import pytest
import seasons
from datetime import date


def test_validate_date():
    assert seasons.validate_date('1964-07-04') == True
    assert seasons.validate_date('1966-07-04') == True
    assert seasons.validate_date('1966-074-10') == False


def test_get_input():
    assert type(seasons.get_input('1964-07-04')) is date


def test_get_the_words():
    date1 = date(1964, 7, 4)
    date2 = date(1964, 7, 5)
    difference = date2 - date1
    assert type(seasons.get_the_words(difference)) is str
