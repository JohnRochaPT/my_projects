"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/21'

# .Original Requirements:
#: In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28, which
#: isn’t actually a valid IPv4 (or IPv6) address.
#:
#: An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate
#: on the internet, akin to a postal address in the real world, typically formatted in dot-decimal
#: notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to
#: say 275 is not in that range! If only NUMB3RS had validated the address in that scene!
#:
#: Implement a function called validate that expects an IPv4 address as input as a str and then
#: returns True or False, respectively, if that input is a valid IPv4 address or not.
#:
#: Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other
#: functions as you see fit, but you may not import any other libraries. You’re welcome, but not
#: required, to use re and/or sys.
#:
#:              import re
#:              import sys
#:
#:              def main():
#:                  print(validate(input("IPv4 Address: ")))
#:
#:
#:              def validate(ip):
#:                  ...
#:
#:
#:                  ...
#:
#:
#:              if __name__ == "__main__":
#:                  main()
#:
#:
#: Either before or after you implement validate in numb3rs.py, additionally implement, in a file
#: called test_numb3rs.py, two or more functions that collectively test your implementation of
#: validate thoroughly, each of whose names should begin with test_ so that you can execute your
#: tests with:
#:
#:              pytest test_numb3rs.py
#:
#:


# .Hints:
#: 1.- Recall that the re module comes with quite a few functions, per
#:     docs.python.org/3/library/re.html, including search.
#:
#: 2.- Recall that regular expressions support quite a few special characters, per
#:     docs.python.org/3/library/re.html#regular-expression-syntax.
#:
#: 3.- Because backslashes in regular expressions could be mistaken for escape sequences (like \n),
#:     best to use Python’s raw string notation for regular expression patterns, else pytest will
#:     warn with DeprecationWarning: invalid escape sequence. Just as format strings are prefixed
#:     with f, so are raw strings prefixed with r. For instance, instead of "harvard\.edu", use
#:     r"harvard\.edu".
#:
#: 4.- Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns
#:     a “match object,” per docs.python.org/3/library/re.html#match-objects, wherein matches are
#:     1-indexed, which you can access individually with group, per
#:     docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per
#:     docs.python.org/3/library/re.html#re.Match.groups.
#:
#:


# .Extra work requirements:
#: None defined
#:


# .My pseudo code approach:
#: 1.- Prompt and capture from the user, with "IPv4 Address: ", so they an IP address.
#:
#: 2.- Code a function named "validate()".  The function needs to:
#:     2.1.- Function needs to accept a required parameter that is a string.
#:     2.2.- Validate that the input matches format "###.###.###.###".
#:     2.3.- Returns "True" if the string is a valid IP address or "False" if it is not.
#:
#: 3.- Create a fle called "test_numb3rs.py" to test the functions in "numb3rs.py"
#:     3.1.- Program needs to have at least one function, whose name needs to begin with
#:           "text_" and followed by the function name, in numb3rs.py we are testing.
#:


import re


def validate(ip: str) -> bool:
    """
    validate
        Function accepts a string and compares the string to an expected format pattern.

        The required format needs to be "N.N.N.N" where "N" is a positive integer
        between 0 and 255 where 0 and 255 are accepted numbers.
            Example 1: String = "1.1.1.1" would return True
            Example 2: String = "0.255.1.1" would return True
            Example 3: String = "101.101.1" would return False
            Example 4: String = "1.1.1.256" would return False
            Example 5: String = "1.A.1.1" would return False
            Example 6: String = "-101.1.1.1" would return False

    Arguments:
        ip -- A non empty string

    Returns:
        Returns True if the string matches a valid IP address.  Returns False if not.
    """
    # match = re.search(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ip)
    # r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    match = re.search(
        r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip)
    if match:
        return True
    else:
        return False


def get_input() -> str:
    """
    get_input
        Function will ask the user for an IP address, passing message "IPv4 Address: "

        The function will accept any string, except for an empty string.  If it is empty,
        it should continue to prompt until the string contains at least one character.

    Returns:
        Returns a non empty string.
    """
    while True:
        response = input('IPv4 Address: ').strip()
        if len(response) > 0:
            return response


def main():
    # > Get the user's input
    response = get_input()
    # response = '255.1.0.255'
    if validate(response):
        print('True')
    else:
        print('False')


# > Call main ONLY when intended
if __name__ == '__main__':
    main()

