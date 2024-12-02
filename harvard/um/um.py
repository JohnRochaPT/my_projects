"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/30'
__version__ = '0.0.1'
__credits__ = 'Something'

# .User Story:
#: It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The
#: more you do it, though, the more noticeable it tends to be!
#:
#: In a file called um.py, implement a function called count that expects a line of text as input
#: as a str and returns, as an int, the number of times that “um” appears in that text,
#: case-insensitively, as a word unto itself, not as a substring of some other word. For
#: instance, given text like hello, um, world, the function should return 1. Given text like
#: yummy, though, the function should return 0.
#:
#: Structure um.py as follows, wherein you’re welcome to modify main and/or implement other
#: functions as you see fit, but you may not import any other libraries. You’re welcome, but not
#: required, to use re and/or sys.
#:
#:              import re
#:              import sys
#:
#:
#:              def main():
#:                  print(count(input("Text: ")))
#:
#:
#:              def count(s):
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
#: Either before or after you implement count in um.py, additionally implement, in a file called
#: test_um.py, three or more functions that collectively test your implementation of count
#: thoroughly, each of whose names should begin with test_ so that you can execute your tests
#: with:
#:
#:              pytest test_um.py
#:
#:


# .Hints:
#: 1.- Recall that the re module comes with quite a few functions, per
#:     docs.python.org/3/library/re.html, including findall.
#:
#: 2.- Recall that regular expressions support quite a few special characters, per
#:     docs.python.org/3/library/re.html#regular-expression-syntax.
#:
#: 3.- Because backslashes in regular expressions could be mistaken for escape sequences
#:     (like \n), best to use Python’s raw string notation for regular expression patterns. Just
#:     as format strings are prefixed with f, so are raw strings prefixed with r. For instance,
#:     instead of "harvard\.edu", use r"harvard\.edu".
#:
#: 4.- Note that \b is “defined as the boundary between a \w and a \W character (or vice versa),
#:     or between \w at the beginning/end of the string,” per
#:     docs.python.org/3/library/re.html#regular-expression-syntax.
#:
#: 5.- You might find regex101.com or regexr.com helpful for testing regular expressions (and
#:     visualizing matches).
#:
#: 6.- See thefreedictionary.com/words-containing-um for some words that contain “um”.
#:
#:


# .My pseudo code approach:
#:
#:
#:
#:
#:
#:
#:
#:
#:
#:
#:

import sys
import re
import os


# | ***********************************************************************************************
# | **********************           C L A S S    S E C T I O N            ************************
# | ***********************************************************************************************
class Kit():
    """
    MyKit
        Class contains class methods that are used as workhorses to perform functions that I use
        often

    """

    @staticmethod
    def get_str_input(msg: str) -> str:
        """
        get_str_input
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user must input at least one character.  If the input is not valid, it will
            keep asking for an input.


        Arguments:
            msg -- A string.  Can be an empty string.

        Returns:
            Returns a string of at least one character
        """
        while True:
            response = input(msg).strip()
            if len(response) == 0:
                pass
            else:
                return response

    @staticmethod
    def get_str_input_even_empty(msg: str) -> str:
        """
        get_str_input_even_empty
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user can choose to enter something or nothing, by hitting enter.  The
            function allows for empty strings

        Arguments:
            msg -- A string.  Can be an empty string.

        Returns:
            Returns a string.  Can be a string of zero length
        """
        return input(msg).strip()

    @staticmethod
    def get_pos_int_input(msg: str) -> str:
        """
        get_pos_int_input
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user must enter at least one positive integer.  If the input is not
            valid, it will keep asking for an input until the user enters a valid integer.

        Arguments:
            msg -- A string.  Can be empty string.

        Returns:
            Returns an integer.
        """
        while True:
            try:
                response = input(msg).strip()
                if '.' in response:
                    pass
                else:
                    response = int(response)
                    return response
            except:
                pass

    @staticmethod
    def get_pos_flt_input(msg: str) -> str:
        """
        get_pos_int_input
            Function accepts a string and with that string, as a message, asks the user for an
            input.  The user must enter a positive float.  If the input is not valid, it will
            keep asking for an input until the user enters a valid integer.

        Arguments:
            msg -- A string.  Can be empty string.

        Returns:
            Returns an float.
        """
        while True:
            try:
                response = input(msg).strip()
                if '.' in response:
                    response = float(response)
                    return response
                else:
                    pass
            except:
                pass

    @staticmethod
    def lines():
        """
         lines
            Function prints a separator section to make it easier to read when looking at the
            terminal window.  Use it instead of multiple print() lines
        """
        name = __file__.split('\\')[len(__file__.split('\\'))-1]
        stars = int(((80-len(name))/2))
        line = '\n' * 6 + '=' * stars + ' ' * 5 + name + ' ' * 5 + '=' * stars + '\n'
        print(line, end='')

    @staticmethod
    def clear_scr():
        """
        clear_scr
            Function clears the screen.  Function is OS aware
        """
        os.system('cls' if (os.name == 'nt') else 'clear')
        Kit.lines()

    @staticmethod
    def format_validator(str_to_validate: str, pattern_cd: str) -> re.Match:
        """
        format_validator
            Function facilitates the validating of strings against certain formats.

            Function uses the "re" library to perform regular expression matches.  If the
            contents of the string matches the pattern, it returns True.  If there is no
            match, it returns false.  When calling this function send the string to be
            validated and the following codes for specialized formats:

                "zip" when validating the format for zip codes
                "phone" when validating a phone number
                "date" when validating YYYY-MM-DD for dates
                "SSN" when validating Social Security Numbers

        Arguments:
            str_to_validate -- Non empty string to use matched against a pattern
            pattern_cd -- Regular expression pattern.

        Returns:
            Returns a re.Match object.  Either empty or not.  If not empty, there
            was a match
        """
        match pattern_cd:
            case 'zip':
                pattern = r'^[0-9]{5}$'
            case 'phone':
                pattern = r'^[0-9](-|.| )[0-9]{3}(-|.| )[0-9]{3}(-|.| )[0-9]{4}$'
            case 'date':
                pattern = r'^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$'
            case 'ssn':
                pattern = r'^[0-9]{3}-[0-9]{2}-[0-9]{4}$'

        return re.search(pattern, str_to_validate, re.IGNORECASE)


# | ***********************************************************************************************
# | **********************    M A I N    P R O G R A M    S E C T I O N    ************************
# | ***********************************************************************************************


def main():
    # > This is an inline code comment.
    # > This is an inline code comment.
    # < Get an input from the user
    # < response = Kit.get_str_input('Enter an input: ')
    # < print(response)
    Kit.lines()
    response = input('Input: ').strip().lower()
    print(count(response.lower()))


#
#
#
# | ***********************************************************************************************
# | **************************    F U N C T I O N     S E C T I O N    ****************************
# | ***********************************************************************************************
def count(str: str) -> int:
    """
    count
        Function receives a string and counts how many times the word "um" exists.  It returns
        that as an integer

    Arguments:
        str -- A non empty string

    Returns:
        An integer containing the number of ums found.
    """
    pattern = r'\b\W*um\b\W*'
    return len(re.findall(pattern, str, re.IGNORECASE))


#
#
#
#
# | ***********************************************************************************************
# | **********************           C A L L   S E L F   M A I N           ************************
# | ***********************************************************************************************
# > Call main ONLY when intended
if __name__ == '__main__':
    main()
