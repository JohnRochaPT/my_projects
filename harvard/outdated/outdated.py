"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/13"


# Original Requirements:
# In the United States, dates are typically formatted in month-day-year order
# (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in
# that format can’t be easily sorted because the date’s year comes last instead of first. Try
# sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any
# program (e.g., a spreadsheet).
#
# Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but
# 9/8/1636 could also be interpreted as August 9, 1636!
#
# Fortunately, computers tend to use ISO 8601, an international standard that prescribes that
# dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country,
# formatting years with four digits, months with two digits, and days with two digits,
# “padding” each with leading zeroes as needed.
#
# Implement a program that prompts the user for a date, anno Domini, in month-day-year order,
# formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any
# of the values in the list below:
#       [
#           "January",
#           "February",
#           "March",
#           "April",
#           "May",
#           "June",
#           "July",
#           "August",
#           "September",
#           "October",
#           "November",
#           "December"
#       ]
# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in
# either format, prompt the user again. Assume that every month has no more than 31 days; no
# need to validate whether a month has 28, 29, 30, or 31 days.
#
#
# Hints:
#   1.- Recall that a str comes with quite a few methods, per
#       docs.python.org/3/library/stdtypes.html#string-methods, including split.
#   2.- Recall that a list comes with quite a few methods, per
#       docs.python.org/3/tutorial/datastructures.html#more-on-lists, among which is index.
#   3.- Note that you can format an int with leading zeroes with code like
#               print(f"{n:02}")
#       wherein, if n is a single digit, it will be prefixed with one 0, per
#       docs.python.org/3/library/string.html#format-string-syntax.
#
#
# Test cases:
#   1.- Type 9/8/1636 and press Enter. Your program should output: "1636-09-08"
#   2.- Type September 8, 1636 and press Enter. Your program should output: "1636-09-08"
#   3.- Type December 80, 1980 and press Enter. Your program should re-prompt the user as the
#       date is invalid.

# Extra work requirements:
# None defined
#
#
#

# My pseudo code approach:
#   1.- Load the month list as described above.
#   2.- Prompt, with message "Date: ", to ask the user to input an address and keep asking
#       until the address is valid.  The user will enter MM-DD-YYYY if all the parts are
#       numeric or "MonthName DayPart, Year" - "January 1, 1970"
#       words also.  A date is valid when:
#       2.1.- Ensure that any spaces are stripped from the date parts.
#       2.2.- There are no more than 31 days per month.
#       2.3.- If the month portion is numeric, that the number is not less than 1 or greater
#             than 12
#       2.4.- The day portion must be greater than 0 and not less or equal to 31
#       2.5.- The year portion is numeric and between 0 and 3000?


def get_month() -> list:
    """
    get_month Function returns a list, already properly sorted, where the elements are
    the month name for each month.

    Returns:
        A list with 12 elements with all the month names.
    """
    return [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


def get_date(m_list: list) -> list:
    """
    get_date
        Function returns a list with three elements where the first element is the user's
        imputed month, the second element is the day and the third element is the year. The month
        part can either be numeric or a string containing the month name, as defined in
        get_month() returned list.

        The function will continue to ask for a date if the date is not as expected.  The user
        must enter a date in the following two formats:\n
                    MM/DD/YYY - Although they may enter leading zeroes or not.
                    MonthName + space + DD + comma + space + YYYY

    Arguments:
        m_list -- Argument needs to have the list of the month names

    Returns:
        A list with three elements. First element is the month - either in number form or
        numeric, the second element is the numeric day and the third element is the numeric year.
    """
    while True:
        resp_str: str = input('Date: ').title().strip()
        if len(resp_str) < 1:
            continue

        # Check to see if they entered a month by entering the month name or numbers.  If the
        # string has spaces, it is supposed to be name.  If no spaces, it needs to have
        # slashes.
        # Check first for spaces.
        if ' ' in resp_str:
            if resp_str.split(',')[0].split(' ')[0] in m_list:
                try:
                    if (1 <= int(resp_str.split(',')[0].split(' ')[1]) <= 31) and (1 <= int(resp_str.split(',')[1]) <= 3000):
                        # print('Date has spaces')
                        return [resp_str.split(',')[0].split(' ')[0],
                                int(resp_str.split(',')[
                                    0].split(' ')[1].strip()),
                                int(resp_str.split(',')[1].strip())]
                except:
                    continue
                else:
                    continue
            else:
                continue

        # If we are here, we did not find spaces so we need to check for slashes
        if '/' in resp_str:
            if len(resp_str.split('/')) == 3:
                try:
                    if ((1 <= int(resp_str.split('/')[0]) <= 12)
                        and (1 <= int(resp_str.split('/')[1]) <= 31)
                            and (1 <= int(resp_str.split('/')[2]) <= 3000)):
                        # print('Date has slashes')
                        return [int(resp_str.split('/')[0]), int(resp_str.split('/')[1]), int(resp_str.split('/')[2])]
                    else:
                        continue
                except:
                    continue
            else:
                continue
        else:
            continue


def main():
    mon_lst = get_month()
    resp: list = get_date(mon_lst)
    # (YYYY-MM-DD)
    year = resp[2]
    month = resp[0]
    if not str(month).isnumeric():
        #    print('Month is supposed to be string')
        month = mon_lst.index(resp[0]) + 1
    day = resp[1]
    print(f'{year:04}-{month:02}-{day:02}')
    # print(year)
    # print(month)
    # print(day)

    # if str(resp[0]).isnumeric():
    #     print(f'{resp[2]:04}-{resp[0]:02}-{resp[1]:02}')
    # else:
    #     print(f'{resp[2]:04}-{(mon_lst.index(resp[0]) + 1):02}-{resp[1]:02}')
    # if str(resp[0]).isnumeric():
    #     print(f'{resp[2]}/{(resp[1]):02}/{(mon_lst.index(resp[0]) + 1):02}')
    # else:
    #     print('Has Name')


# Call main only when intended
if __name__ == '__main__':
    main()
