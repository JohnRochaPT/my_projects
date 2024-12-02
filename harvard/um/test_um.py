import um
import pytest


def test_count():
    assert um.count('Hello There') == 0
    assert um.count('Hello um and um') == 2


def test_count_empty_string():
    assert um.count('') == 0


def test_count_empty_no_case():
    assert um.count('Um and um') == 2


def test_count_empty_with_period():
    assert um.count('um.py') == 1


def test_count_matches_in_words():
    assert um.count('yum means delicious') == 0
