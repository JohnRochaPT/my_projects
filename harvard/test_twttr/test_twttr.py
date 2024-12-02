"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/14"


# Original Requirements:
# Implement one or more functions that collectively test your implementation of shorten
# thoroughly, each of whose names should begin with test_ so that you can execute your tests
# with:
#   Be sure to include atop test_twttr.py so that you can call shorten in your tests.
#       import twttr
#   or
#
#       from twttr import shorten
#
# Hints:
# Defined above
#
#
# Extra work requirements:
# Not applicable
#
#
# My pseudo code approach:
#   1.- Get an input from the user, with message, input
#

from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("AExIOU") == "x"
    assert shorten("1234") == "1234"
    assert shorten(".,!@?") == ".,!@?"


def main():
    test_shorten()


# Call main only when intended
if __name__ == "__main__":
    main()
