"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/21'

# .User Story:
#: Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly,
#: instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”),
#: wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”,
#: wherein “meridiem” means midday (i.e., noon).
#:
#: Conversion Table:
#: Just as “12:00 AM” in 12-hour format would be “00:00” in 24-hour format, so would “12:01 AM”
#: through “12:59 AM” be “00:01” through “00:59”, respectively.
#:
#:
# .Original Requirements:
#: In a file called working.py, implement a function called convert that expects a str in any of the 12-hour
#: formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM
#: and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume
#: that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.
#:
#:              9:00 AM to 5:00 PM
#:              9 AM to 5 PM
#:              9:00 AM to 5 PM
#:              9 AM to 5:00 PM
#:
#: Raise a ValueError instead if the input to convert is not in either of those formats or if either time
#: is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante
#: meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
#:
#: Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions
#: as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re
#: and/or sys.
#:
#:              import re
#:              import sys
#:
#:              def main():
#:                  print(convert(input("Hours: ")))
#:
#:              def convert(s):
#:                  ...
#:
#:              if __name__ == "__main__":
#:                  main()
#:
#: Either before or after you implement convert in working.py, additionally implement, in a file called
#: test_working.py, three or more functions that collectively test your implementation of convert
#: thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
#:
#:              pytest test_working.py
#:
#:
#:
#:


# .Hints:
#: 1.- Recall that the re module comes with quite a few functions, per
#:     docs.python.org/3/library/re.html, including search.
#:
#: 2.- Recall that regular expressions support quite a few special characters, per
#:     docs.python.org/3/library/re.html#regular-expression-syntax.
#:
#: 3.- Because backslashes in regular expressions could be mistaken for escape sequences (like \n), best
#:     to use Python’s raw string notation for regular expression patterns, else pytest will warn with
#:     DeprecationWarning: invalid escape sequence. Just as format strings are prefixed with f, so are
#:     raw strings prefixed with r. For instance, instead of "harvard\.edu", use r"harvard\.edu".
#:
#: 4.- Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a
#:     “match object,” per docs.python.org/3/library/re.html#match-objects, wherein matches are
#:     1-indexed, which you can access individually with group, per
#:     docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per
#:     docs.python.org/3/library/re.html#re.Match.groups.
#:
#: 7.- Note that you can format an int with leading zeroes with code like
#:
#:                  print(f"{n:02}")
#:
#:     Wherein, if n is a single digit, it will be prefixed with one 0, per
#:     docs.python.org/3/library/string.html#format-string-syntax.
#:
#: 8.- Prompt with "Hours: "
#:
#: 9.- Samples:
#:          Input => "9 AM to 5 PM"             Output => "09:00 to 17:00"
#:
#:          Input => "9:00 AM to 5:00 PM"       Output => "09:00 to 17:00"
#:
#:          Input => "10 AM to 8:50 PM"         Output => "10:00 to 20:50"
#:
#:          Input => "10:30 PM to 8 AM"         Output => "22:30 to 08:00"
#:
#:          Input => "9:60 AM to 5:60 PM"       Output => "ValueError"
#:
#:          Input => "9 AM - 5 PM"              Output => "ValueError"
#:
#:          Input => "09:00 AM - 17:00 PM"      Output => "ValueError"
#:

# .Extra work requirements:
#: None defined
#:


# .My pseudo code approach:
#: 1.- Program will use "re" and "sys" library.  Program name is "working.py"
#:
#: 2.- Prompt the user with message "Hours: " and accept a string.  If the user does not enter
#:     anything, keep asking.
#:
#: 3.- Once the user enters a string, pass that string to a function called "convert()".  The
#:     function will:
#:     3.1.- Confirm, through the use of regex, that the string fits one of the following
#:           formats:
#:                      9:00 AM to 5:00 PM
#:                      9 AM to 5 PM
#:                      9:00 AM to 5 PM
#:                      9 AM to 5:00 PM
#:     3.2.- If the format is accepted, using AM and PM, convert to military format, using
#:           leading zeroes when required.
#:     3.3.- Make sure that the inputted time is valid.  For example, 13:00 AM is not a valid time
#:
#: 4.- Once the validation and conversion is done, output the inputted time in military format
#:     as follows:
#:                      09:00 to 17:00
#:
#: 5.- Write an additional program and name it "test_working.py".  In this program:
#:     5.1.- Write two or three functions, named "test_*" to test "working.py"'s validate()
#:           function so we can run "pytest test_working.py".  Use the test cases above, in
#:           hints, to develop all the assert statements.
#:

import re
import sys


def convert(time_str: str) -> str:
    """
    convert
        Function accepts a string and validates it to be the correct format.  If it is not,
        it will raise a ValueError.

    _extended_summary_

    Arguments:
        time_str -- String needs to be the correct format

    Returns:
        Returns the same string but reformatted to military format.
    """
    new_format = str()
    pattern = r'^(?P<from_hour>(([0-9][02]*))):*(?P<from_min>([0-5][0-9])*) (?P<from_day_part>([A|P]M)) to (?P<to_hour>(([0-9][02]*))):*(?P<to_min>([0-5][0-9])*) (?P<to_day_part>([A|P]M))$'

    matches = re.search(pattern, time_str, re.IGNORECASE)
    if matches:
        pass
    else:
        raise ValueError('Could not match the string')

    # > Now check for minutes
    f_hrs = int(matches.group('from_hour'))
    if matches.group('from_min') == '':
        f_min = 0
    else:
        f_min = int(matches.group('from_min'))

    # > Now check for minutes
    t_hrs = int(matches.group('to_hour'))
    if matches.group('to_min') == '':
        t_min = 0
    else:
        t_min = int(matches.group('to_min'))

    # > Convert hours to military
    if matches.group('from_day_part') == 'AM':
        if f_hrs == 12:
            f_hrs = 0
    else:
        if f_hrs < 12:
            f_hrs += 12

    if matches.group('to_day_part') == 'AM':
        if t_hrs == 12:
            t_hrs = 0
    else:
        if t_hrs < 12:
            t_hrs += 12

    # > Now build the string to return.
    new_format = f'{f_hrs:02}:{f_min:02} to {t_hrs:02}:{t_min:02}'

    return new_format


def get_input() -> str:
    """
    get_input
        Function asks the user for an input with represents the working hours of a day

        The function will only accept a string that is greater than one character.  If it has
        less than one character, it should keep asking for an input.

    Returns:
        Returns the inputted string.
    """
    while True:
        response = input('Hours: ').strip()
        if len(response) > 0:
            return response


def main():
    # > This is an inline code comment.
    response = get_input()
    # /* response = '9:00 AM to 5:00 PM'

    # > Validate that the dictionary has values
    formatted = convert(response)

    print(formatted)


# > Call main ONLY when intended
if __name__ == '__main__':
    main()


# def get_input() -> str:
#     """
#     get_input
#         Function asks the user for an input with represents the working hours of a day

#         The function will only accept a string that is greater than one character.  If it has
#         less than one character, it should keep asking for an input.

#     Returns:
#         Returns the inputted string.
#     """
#     while True:
#         response = input('Hours :').strip()
#         if len(response) > 0:
#             return response


# def validate_init(time_str: str) -> dict:
#     """
#     validate
#         Function accepts a string and ensures that the format matches one of the required
#         formats.

#         The function accepts a string and validates the string to match one of the following
#         formats:
#              "9:00 AM to 5:00 PM" or "9 AM to 5 PM" or "9:00 AM to 5 PM" or "9 AM to 5:00 PM"

#         If the string does not meet any of the formats, it will raise a ValueError message
#         and exit the application with a sys.exit() function.

#     Arguments:
#         time_str -- A non empty string

#     Returns:
#         Returns a fully populated dictionary with all the values needed to output in the new
#         format.
#     """
#     # > Split the string into two sections first, splitting with 'to'
#     left, right = time_str.split('to')
#     left = left.strip()
#     right = right.strip()

#     if len(left) == 0 or len(right) == 0:
#         raise ValueError('String does not contain a to')

#     # > left check format of "00:00 AM"
#     times = dict()
#     left_got_match = False
#     right_got_match = False
#     matches = re.search(
#         r'^(?P<from_hour>[0-9]?[0-9]):(?P<from_min>[0-9][0-9]) (?P<from_day_part>AM|PM)', left, re.IGNORECASE)
#     if matches:
#         left_got_match = True
#         times['from_hour'] = int(matches.group('from_hour'))
#         times['from_min'] = int(matches.group('from_min'))
#         times['from_day_part'] = matches.group('from_day_part')
#         # > Check for midnight
#         if times['from_day_part'] == 'AM' and times['from_hour'] == 12:
#             times['from_hour'] = 0

#         # > Check for 12 PM
#         if times['from_day_part'] == 'PM' and times['from_hour'] < 12:
#             times['from_hour'] = times['from_hour'] + 12
#         else:
#             if times['from_hour'] == 12:
#                 times['from_hour'] = 0

#     # > left check format of "00 AM"
#     if not left_got_match:
#         matches = re.search(
#             r'^(?P<from_hour>[0-9]?[0-9]) (?P<from_day_part>AM|PM)', left, re.IGNORECASE)
#         if matches:
#             left_got_match = True
#             times['from_hour'] = int(matches.group('from_hour'))
#             times['from_min'] = 0
#             times['from_day_part'] = matches.group('from_day_part')

#             # > Check for midnight
#             if times['from_day_part'] == 'AM' and times['from_hour'] == 12:
#                 times['from_hour'] = 0

#             # > Check for 12 PM
#             if times['from_day_part'] == 'PM' and times['from_hour'] < 12:
#                 times['from_hour'] = times['from_hour'] + 12
#             else:
#                 if times['from_hour'] == 12:
#                     times['from_hour'] = 0
#         else:
#             raise ValueError('There is a problem with your input')

#     if 0 <= times['from_hour'] <= 23 and 0 <= times['from_min'] <= 59:
#         pass
#     else:
#         raise ValueError("Input not acceptable")

#     # > Now check the right portion
#     # > right check format of "00:00 AM"
#     matches = re.search(
#         r'^(?P<to_hour>[0-9]?[0-9]):(?P<to_min>[0-9][0-9]) (?P<to_day_part>AM|PM)', right, re.IGNORECASE)
#     if matches:
#         right_got_match = True
#         times['to_hour'] = int(matches.group('to_hour'))
#         times['to_min'] = int(matches.group('to_min'))
#         times['to_day_part'] = matches.group('to_day_part')

#         # > Check for midnight
#         if times['to_day_part'] == 'AM' and times['to_hour'] == 12:
#             times['to_hour'] = 0

#         # > Check for 12 PM
#         if times['to_day_part'] == 'PM' and times['to_hour'] < 12:
#             times['to_hour'] = times['to_hour'] + 12

#         if 0 <= times['to_hour'] <= 23 and 0 <= times['to_min'] <= 59:
#             return times
#         else:
#             raise ValueError('Input not acceptable')

#     # > left check format of "00 AM"
#     if not right_got_match:
#         matches = re.search(
#             r'^(?P<to_hour>[0-9]?[0-9]) (?P<to_day_part>AM|PM)', right, re.IGNORECASE)
#         if matches:
#             right_got_match = True
#             times['to_hour'] = int(matches.group('to_hour'))
#             times['to_min'] = 0
#             times['to_day_part'] = matches.group('to_day_part')

#             # > Check for midnight
#             if times['to_day_part'] == 'AM' and times['to_hour'] == 12:
#                 times['to_hour'] = 0

#             # > Check for 12 PM
#             if times['to_day_part'] == 'PM' and times['to_hour'] < 12:
#                 times['to_hour'] = times['to_hour'] + 12

#             if 0 <= times['to_hour'] <= 23 and 0 <= times['to_min'] <= 59:
#                 return times
#             else:
#                 raise ValueError('Input not acceptable')
#         else:
#             raise ValueError('There is a problem with your input')


# def convert(time_str: str) -> bool:
#     """
#     convert
#         Function accepts a string and ensures that the format matches one of the required
#         formats.

#         The function accepts a string and validates the string to match one of the following
#         formats:
#              "9:00 AM to 5:00 PM" or "9 AM to 5 PM" or "9:00 AM to 5 PM" or "9 AM to 5:00 PM"

#         If the string does not meet any of the formats, it will raise a ValueError message
#         and exit the application with a sys.exit() function.

#     Arguments:
#         time_str -- A non empty string

#     Returns:
#         Returns True if it passes all conditions or False if it does not.
#     """
#     # > Split the string into two sections first, splitting with 'to'
#     left, right = time_str.split('to')
#     left = left.strip()
#     right = right.strip()

#     if len(left) == 0 or len(right) == 0:
#         raise ValueError('String does not contain a to')

#     # > left check format of "00:00 AM"
#     times = dict()
#     left_got_match = False
#     right_got_match = False
#     has_from_minutes = bool()
#     has_to_minutes = bool()
#     matches = re.search(
#         r'^(?P<from_hour>[0-9]?[0-9]):(?P<from_min>[0-9][0-9]) (?P<from_day_part>AM|PM)', left, re.IGNORECASE)
#     if matches:
#         left_got_match = True
#         times['from_hour'] = int(matches.group('from_hour'))
#         times['from_min'] = int(matches.group('from_min'))
#         has_from_minutes = True
#         times['from_day_part'] = matches.group('from_day_part')
#         # > Check for midnight
#         if times['from_day_part'] == 'AM' and times['from_hour'] == 12:
#             times['from_hour'] = 0

#         # > Check for 12 PM
#         if times['from_day_part'] == 'PM' and times['from_hour'] < 12:
#             times['from_hour'] = times['from_hour'] + 12
#         else:
#             if times['from_hour'] == 12:
#                 times['from_hour'] = 0

#     # > left check format of "00 AM"
#     if not left_got_match:
#         matches = re.search(
#             r'^(?P<from_hour>[0-9]?[0-9]) (?P<from_day_part>AM|PM)', left, re.IGNORECASE)
#         if matches:
#             left_got_match = True
#             times['from_hour'] = int(matches.group('from_hour'))
#             times['from_min'] = 0
#             times['from_day_part'] = matches.group('from_day_part')
#             has_from_minutes = False
#             # > Check for midnight
#             if times['from_day_part'] == 'AM' and times['from_hour'] == 12:
#                 times['from_hour'] = 0

#             # > Check for 12 PM
#             if times['from_day_part'] == 'PM' and times['from_hour'] < 12:
#                 times['from_hour'] = times['from_hour'] + 12
#             else:
#                 if times['from_hour'] == 12:
#                     times['from_hour'] = 0
#         else:
#             raise ValueError('There is a problem with your input')

#     if 0 <= times['from_hour'] <= 23 and 0 <= times['from_min'] <= 59:
#         pass
#     else:
#         raise ValueError("Input not acceptable")

#     # > Now check the right portion
#     # > right check format of "00:00 AM"
#     matches = re.search(
#         r'^(?P<to_hour>[0-9]?[0-9]):(?P<to_min>[0-9][0-9]) (?P<to_day_part>AM|PM)', right, re.IGNORECASE)
#     if matches:
#         right_got_match = True
#         times['to_hour'] = int(matches.group('to_hour'))
#         times['to_min'] = int(matches.group('to_min'))
#         has_to_minutes = True
#         times['to_day_part'] = matches.group('to_day_part')

#         # > Check for midnight
#         if times['to_day_part'] == 'AM' and times['to_hour'] == 12:
#             times['to_hour'] = 0

#         # > Check for 12 PM
#         if times['to_day_part'] == 'PM' and times['to_hour'] < 12:
#             times['to_hour'] = times['to_hour'] + 12

#         if 0 <= times['to_hour'] <= 23 and 0 <= times['to_min'] <= 59:
#             if has_from_minutes == has_to_minutes:
#                 return True
#             else:
#                 raise ValueError('Input not acceptable')
#         else:
#             raise ValueError('Input not acceptable')

#     # > left check format of "00 AM"
#     if not right_got_match:
#         matches = re.search(
#             r'^(?P<to_hour>[0-9]?[0-9]) (?P<to_day_part>AM|PM)', right, re.IGNORECASE)
#         if matches:
#             right_got_match = True
#             times['to_hour'] = int(matches.group('to_hour'))
#             times['to_min'] = 0
#             has_to_minutes = False
#             times['to_day_part'] = matches.group('to_day_part')

#             # > Check for midnight
#             if times['to_day_part'] == 'AM' and times['to_hour'] == 12:
#                 times['to_hour'] = 0

#             # > Check for 12 PM
#             if times['to_day_part'] == 'PM' and times['to_hour'] < 12:
#                 times['to_hour'] = times['to_hour'] + 12

#             if 0 <= times['to_hour'] <= 23 and 0 <= times['to_min'] <= 59:
#                 if has_from_minutes == has_to_minutes:
#                     return True
#                 else:
#                     raise ValueError('Input not acceptable')
#             else:
#                 raise ValueError('Input not acceptable')
#         else:
#             raise ValueError('There is a problem with your input')


# def print_times(times: dict):
#     """
#     convert_times
#         Function accepts a dictionary with all of the time properties and converts them to the
#         correct format.  At this point, the entire dictionary only contains valid time

#     _extended_summary_

#     Arguments:
#         times -- _description_
#     """
#     response = f'{times['from_hour']:02}:{times['from_min']:02} to '
#     response += f'{times['to_hour']:02}:{times['to_min']:02}'
#     print(response)


# def main():
#     # > This is an inline code comment.
#     response = get_input()
#     # /* response = '9 AM to 5 PM'

#     # > Validate that the dictionary has values
#     if convert(response):
#         pass

#     times = validate_init(response)

#     print_times(times)


# # > Call main ONLY when intended
# if __name__ == '__main__':
#     main()
