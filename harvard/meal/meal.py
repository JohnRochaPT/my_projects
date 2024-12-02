"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/11"


# Original requirements
# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00
# and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t
# it be nice if you had a program that could tell you what to eat when
#
# Implement a program that prompts the user for a time and outputs whether it’s breakfast
# time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at
# all. Assume that the user’s input will be formatted in 24-hour time as #:## or
# ##:##. And assume that each meal’s time range is inclusive. For instance, whether
# it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
#
# Structure your program per the below, wherein convert is a function (that can be called
# by main) that converts time, a str in 24-hour format, to the corresponding number of
# hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30
# minutes), convert should return 7.5 (i.e., 7.5 hours).
#
# Recall that a str comes with quite a few methods, per
# docs.python.org/3/library/std types.html#string-methods, including split, which separates
# a str into a sequence of values, all of which can be assigned to variables at once.
# For instance, if time is a str like "7:30", then hours, minutes = time.split(":")
# will assign "7" to hours and "30" to minutes.
#
# Keep in mind that there are 60 minutes in 1 hour.
#

# Extra work problem statement
# None defined

# My pseudo code approach:
#   1.- Prompt the user, with a message of "What time is it: " and accept its value.
#     1.1.- Assuming that the user entered either "#:##" or "##:##"
#   2.- Times are inclusive of the ends.  So 7:00 to 8:00 includes anything from 7:00
#       to 8:00
#   3.- Create function called "convert" that accepts a string and returns a float.
#     3.1.- The return will be a float representation of the time.  Example: if
#           the user enters 7:30, the function will return 7.5 hours
#   4.- Have main call the function "converter" and print out as follows:
#     4.1.- If time is between 7:00 and 8:00 then print out "breakfast time"
#     4.2.- If time is between 12:00 and 13:00 then print out "lunch time"
#     4.3.- If time is between 18:00 and 19:00 then print out "dinner time"
#

def convert(timeStr: str) -> float:
    '''
        Function convert(str) requires the passing of a string and returns a float

        The function will accept the string formatted already as #:## or ##:## and will
        return the converted time in the form of a decimal number.  It will convert the
        minutes to decimals.  For example, if the minutes are 30, the decimal part of
        the float will be 50.  Example:
            7:30 will convert to 7.5
    '''
    # Split the time string into hours and minutes.
    timeParts = timeStr.split(':')

    # Now convert the parts into integers
    # timeHrs = int(timeParts[0])
    # timeMin = int(timeParts[1]) / 60
    # print('Hours is:', timeHrs)
    # print('Minutes is:', timeMin)
    return int(timeParts[0]) + int(timeParts[1]) / 60


def main():
    myStr = 'What time is it? '

    # Ask for the time
    respStr = input(myStr).strip()

    # Call the convert function passing the imputed string
    myTime = convert(respStr)

    # Now print the desired response
    if 7 <= myTime <= 8:
        print('breakfast time')
    elif 12 <= myTime <= 13:
        print('lunch time')
    elif 18 <= myTime <= 19:
        print('dinner time')


if __name__ == '__main__':
    main()
