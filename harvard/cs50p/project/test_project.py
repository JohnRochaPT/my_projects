"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/30'


import pytest
import project


def test_get_zip():
    # < The way the function returns the zip code ONLY if the zip code is an actual US zip
    # < code.
    assert project.get_zip('05468') == '05468'
    assert project.get_zip('90210') == '90210'


def test_get_zip_bad():
    # < This function tests that bad zip codes, although formatted correctly, do not return
    # < an item.  If the function returns None, it means that the zip code is not a valid
    # < zip code
    assert project.get_zip('00000') == None
    assert project.get_zip('00002') == None
    assert project.get_zip('99999') == None
    assert project.get_zip('00001') == None


def test_get_state():
    # < Function accepts a string and returns the name of the US State if there is a match
    # < to a real US State.
    assert project.get_state('NY') == 'New York'
    assert project.get_state('New York') == 'New York'


def test_get_state_bad_state():
    # < Function accepts a string and returns the name of the US State if there is a match
    # < to a real US State.  Here we are testing passing strings that would not result in
    # < a match to a real state
    assert project.get_state('TT') == None
    assert project.get_state('New House') == None


def test_load_list_a():
    result = project.load_list_a()
    assert isinstance(result, list)
    assert len(result) == 5


def test_load_list_b():
    result = project.load_list_b()
    assert isinstance(result, list)
    assert len(result) == 8


def test_load_list_c():
    result = project.load_list_c()
    assert isinstance(result, list)
    assert len(result) == 8
    assert result[0]['Doc Name'] == 'U.S. Social Security Card'


def test_format_validator_successful():
    # < Format_validator is a context aware function that accepts a string and confirms that the
    # < string matches the pattern that the user requests.
    matches = project.Kit.format_validator(str_to_validate='1-800-555-5555', pattern_cd='phone')
    assert matches
    matches = project.Kit.format_validator(str_to_validate='123-45-6789', pattern_cd='ssn')
    assert matches


def test_format_validator_not_successful():
    # < Here we are testing how if we pass a string, that is supposed to be a social security
    # < number but it not correctly formatted, it will not return a valid object.
    matches = project.Kit.format_validator(str_to_validate='123-454-6789', pattern_cd='ssn')
    assert matches == None
    matches = project.Kit.format_validator(str_to_validate='ABC', pattern_cd='zip')
    assert matches == None
