"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/22'

import working
import pytest


def test_exception():
    with pytest.raises(ValueError):
        working.convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        working.convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        working.convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        working.convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        working.convert("9 AM5 PM")
    with pytest.raises(ValueError):
        working.convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        working.convert("9:72 to 6:30")


def test_convert_with_minutes():
    assert working.convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    assert working.convert('12:01 AM to 12 PM') == '00:01 to 12:00'
    assert working.convert('12:01 AM to 12:01 PM') == '00:01 to 12:01'


def test_convert_without_minute():
    assert working.convert('12 AM to 12 PM') == '00:00 to 12:00'
    assert working.convert('12 PM to 12 AM') == '12:00 to 00:00'
    assert working.convert('9 AM to 9 PM') == '09:00 to 21:00'
