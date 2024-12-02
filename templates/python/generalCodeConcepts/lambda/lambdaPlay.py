"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/##/##'
__contact__ = 'john.rocha@outlook.com'
__version__ = '0.0.1'
__credits__ = 'Something'


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
    # < Info about Lambda and autopep8.  Autopep8 will rewrite all lambda expressions because it
    # < feels that we should not use it.  To stop autopep8 from doing this, you can put the lambda
    # < in parenthesis or add an exception to the json file controlling autopep8 functionality

    # < In lambda expressions, you can't assign a value to a variable.  See sample below

    lambda_sample_5()


#
#
#
# | ***********************************************************************************************
# | **************************    F U N C T I O N     S E C T I O N    ****************************
# | ***********************************************************************************************

# < Simple Lambda function
# < When we assign a lambda expression to a variable, that variable will become the function
# < method and the lambda parameters will become its parameters.  In the case below, y is the
# < lambda function, x is the lambda parameter and what is after the column, is what will
# < execute.
# < The components of a lambda expression is the exhibition.  In the case below, the exhibition
# < is x * x
def lambda_sample_1():
    y = (lambda x: x * x)
    print(y(1))


# < In lambda expressions, you can't assign a value to a variable.
def lambda_sample_2():
    x = 0
    y = 10
    try:
        #  math = (lambda y: y=x+y)
        pass
    except:
        # print(math(y))
        pass


# < You can run if statements in lambda expressions.  For example
def lambda_sample_3():
    age_check = (lambda age: True if age > 16 else False)
    print(age_check(12))
    print(age_check(33))


# < More complex expression inside lambda.  In this case, you are not passing a
# < parameter since the expression does not need it.  The expressions already has
# < a populated variable
def lambda_sample_4():
    names = ['john', 'joe', 'lucas', 'charlie', 'steve']
    remove = filter(lambda name: not name == 'steve', names)
    # result = filter(lambda x: x % 2 == 0, numbers)
    print(list(remove))

    first = 'John'
    last = 'Rocha'
    intro = (lambda first, last: f'Hello {first} {last}.  How are you?')
    print(intro(first, last))


# < Lambda functions are great for sorting where we are not sure what the key would be
def lambda_sample_5():
    authors = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke',
               'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'J. F. Kennedy',
               'Leigh Bracket']
    # < If we wanted to sort, we would need to split, find the last index and then sort
    # < by that.  That would be a lot of lines of code and perhaps never have to use the
    # < function again.  With Lambda we can simplify this.
    # < Here, we are splitting the string by spaces and accessing the last index of the
    # < array.  This is needed because some names have middle names or initials or no
    # < middle name at all.  We just want the last string.  And we want it lower() so it
    # < is case insensitive.
    authors.sort(key=lambda name: name.split(' ')[-1].lower())
    print(list(authors))


#
#
#
# | ***********************************************************************************************
# | **********************           C A L L   S E L F   M A I N           ************************
# | ***********************************************************************************************
# > Call main ONLY when intended
if __name__ == '__main__':
    main()
