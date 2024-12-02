"""
A eDX assignment.

This file shows how modules work

"""
__author__ = 'John Rocha'
__date__ = '2024/##/##'
__contact__ = 'john.rocha@outlook.com'
__version__ = '0.0.1'


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ User Story:                                                                                   │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ Requirements:                                                                                 │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘

#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ How to test:                                                                                  │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ My pseudo code approach:                                                                      │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ :                                                                      │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ :                                                                      │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ :                                                                      │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘


#+┌───────────────────────────────────────────────────────────────────────────────────────────────┐
#+│ :                                                                      │
#+├───────────────────────────────────────────────────────────────────────────────────────────────┤
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:│                                                                                               │
#:└───────────────────────────────────────────────────────────────────────────────────────────────┘



import sys
import re
import os


#++************************************************************************************************
#+  **********************           C L A S S    S E C T I O N            ************************
#++************************************************************************************************
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


#++************************************************************************************************
#+  **********************    M A I N    P R O G R A M    S E C T I O N    ************************
#++************************************************************************************************

def main():
    # > This is an inline code comment.
    Kit.clear_scr()
    print('Hello World')


#
#
#
#++************************************************************************************************
#+  **************************    F U N C T I O N     S E C T I O N    ****************************
#++************************************************************************************************
#
#
#
#
#++************************************************************************************************
#+  **********************           C A L L   S E L F   M A I N           ************************
#++************************************************************************************************
# > Call main ONLY when intended
if __name__ == '__main__':
    main()
