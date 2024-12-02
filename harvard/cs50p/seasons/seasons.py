"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/23'


# .User Story:
# : Assuming there are 365 days in a year, there are 365 x 24 x 60 = 525,600 minutes in that same
# : year (because there are 24 hours in a day and 60 minutes in an hour). But how many minutes are
# : there in two or more years? Well, it depends on how many of those are leap years with 366 days,
# : per the Gregorian calendar, as some of them could have 1 x 24 x 60 = 1,400 additional
# : minutes. In fact, how many minutes has it been since you were born? Well, that, too, depends
# : on how many leap years there have been since! There is an algorithm for such, but let’s not
# : reinvent that wheel. Let’s use a library instead. Fortunately, Python comes with a datetime
# : module that has a class called date that can help, per
# : docs.python.org/3/library/datetime.html#date-objects.
# :
# :

#
# .Original Requirements:
# : In a file called seasons.py, implement a program that prompts the user for their date of birth
# : in YYYY-MM-DD format and then sings/prints how old they are in minutes, rounded to the nearest
# : integer, using English words instead of numerals, just like the song from Rent, without any
# : "and" between words. Since a user might not know the time at which they were born, assume, for
# : simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that
# : the current time is also midnight. In other words, even if the user runs the program at noon,
# : assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s
# : date, per docs.python.org/3/library/datetime.html#datetime.date.today.
# :
# : Structure your program per the below, not only with a main function but also with one or more
# : other functions as well:
# :
# :             from datetime import date
# :
# :
# :             def main():
# :                 ...
# :
# :
# :             ...
# :
# :
# :             if __name__ == "__main__":
# :                 main()
# :
# : You’re welcome to import other (built-in) libraries, or any that are specified in the below
# : hints. Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that
# : your program will not raise any exceptions.
# :
# : Either before or after you implement seasons.py, additionally implement, in a file called
# : test_seasons.py, one or more functions that test your implementation of any functions besides
# : main in seasons.py thoroughly, each of whose names should begin with test_ so that you can
# : execute your tests with:
# :
# :             pytest test_seasons.py
# :


#
# .Hints:
# : 1.- Note that the date class comes with quite a few methods and “supported operations,” per
# :     docs.python.org/3/library/datetime.html#date-objects. In particular, the class implements
# :     __sub__, per docs.python.org/3/library/operator.html#operator.__sub__, overloading - in
# :     such a way that subtracting one date object from another returns a timedelta object, which
# :     itself comes with several (read-only) “instance attributes,” per
# :     docs.python.org/3/library/datetime.html#timedelta-objects.
# :
# : 2.- Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect.
# :     You can install it with:
# :
# :             pip install inflect
# :
# :


#
# .Extra work requirements:
# : None defined
# :
# :
# :


#
# .My pseudo code approach:
# : 1.- Prompt the user, with message "Date of Birth: " and obtain their birthdate in the format
# :     of "YYYY-MM-DD"
# :     1.1.- If the user enters a badly formatted date, exit via sys library.
# :
# : 2.- Assume that the user was born at exactly midnight (00:00:00).  Also, assume that today
# :     the time is midnight.
# :
# : 3.- Implement at least one function, outside of main
# :
# : 4.- Calculate the number of minutes, since the use was born, using English words like if the
# :     user enters "1999-01-01" as the birthdate, the program will output:
# :
# :         Five hundred twenty-five thousand, six hundred minutes
# :
# : 5.- In a separate program called "test_seasons.py", implement pytest and write multiple
# :     functions that test every function in the "seasons.py" program except for main().
# :     5.1.- Each function needs to be named "test_" plus the name, from the "seasons"
# :           function name.
# :
# :

import sys
from datetime import date, timedelta
import inflect


# | ***********************************************************************************************
# | **********************    M A I N    P R O G R A M    S E C T I O N    ************************
# | ***********************************************************************************************

p = inflect.engine()


def main():
    # > Get the birthdate
    # bd_date_str = input('Date of Birth: ').strip()
    birth_dt = get_input()
    if birth_dt:
        pass
    else:
        sys.exit(1)

    date_of_today = date.today()

    # > Get the difference
    difference = date_of_today - birth_dt
    words = get_the_words(difference)
    print(words, 'minutes')


#
#
#
# | ***********************************************************************************************
# | **************************    F U N C T I O N     S E C T I O N    ****************************
# | ***********************************************************************************************

def validate_date(dt_str: str) -> bool:
    """
    validate_date
        Function accepts a string and validates that it is a string.

        Function will ensure that the string meets a specific format where as the date is entered
        in format "YYYY-MM-DD"

    Returns:
        Function returns True if it is a date exists if it not.
    """
    date_splits = dt_str.split('-')
    try:
        bd_date = date(int(date_splits[0]), int(
            date_splits[1]), int(date_splits[2]))
        return True
    except:
        return False


def get_input(in_dt: str = '') -> date:
    """
    get_input Function asks the user for an input and returns a date if the input is fine

    Returns:
        Returns a validated date or None if the date is not valid
    """
    if len(in_dt) == 0:
        bd_date_str = input('Date of Birth: ').strip()
    else:
        bd_date_str = in_dt

    if validate_date(bd_date_str):
        return date(int(bd_date_str[0:4]), int(bd_date_str[5:7]), int(bd_date_str[8:10]))
    else:
        return None

# > Computes minutes and passes the formatted words as per the specs


def get_the_words(diff: timedelta) -> str:
    """
    get_the_words
        Function accepts a timedelta object, computes the minutes and then returns, using
        the inflect library, the number of minutes in words

    Arguments:
        diff -- A timedelta object

    Returns:
        Returns a string representing the minutes in words.
    """
    if diff.days == 0:
        return None
    minutes = diff.days * 24 * 60
    print_out = p.number_to_words(minutes, andword='').capitalize()
    return print_out


#
#
#
#
# | ***********************************************************************************************
# | **********************           C A L L   S E L F   M A I N           ************************
# | ***********************************************************************************************
# # > Call main ONLY when intended
if __name__ == '__main__':
    main()
