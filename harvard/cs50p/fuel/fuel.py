"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/12"


# Original requirements
# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance
# 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4
# indicates that a tank is 75% full.
#
# Implement a program that prompts the user, with message "Fraction: " for a fraction,
# formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage
# rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less
# remains, output E instead to indicate that the tank is essentially empty. And if 99% or
# more remains, output F instead to indicate that the tank is essentially full.
#
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the
# user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like
# "ValueError" or "ZeroDivisionError".
#
# Hints
#   1.- Recall that a str comes with quite a few methods, per
#       docs.python.org/3/library/stdtypes.html#string-methods, including split.
#   2.- Note that you can handle two exceptions separately with code like:
#           try:
#               ...
#           except ValueError:
#               ...
#           except ZeroDivisionError:
#               ...
#       Or you can handle two exceptions together with code like:
#           try:
#               ...
#           except (ValueError, ZeroDivisionError):
#               ...
#
# Extra work problem statement
# None defined
#
# My pseudo code approach:
#   1.- Define a function "get_int()" that will prompt the user, to enter a fraction.  The
#       function needs to evaluate if the input is valid.  If not, it will continue to ask
#       until the input is valid.
#       1.1.- The function needs to return two integers if input is valid.
#       1.2.- Use exception "ValueError" to catch strings that can't convert to integers.
#       1.3.- Prompt with "Fraction: ".
#       1.4.- Input is valid ONLY when:
#           1.4.1.- The string contains ONE forward slash.
#           1.4.2.- Either side of the slash contain an integer.
#           1.4.3- The first integer has to be less or equal to second integer
#           1.4.4.- The second integer is not a zero
#   2.- Divide integer one by integer two.
#   3.- Evaluate and process the division result:
#       3.1.- Print to the screen the percentage rounded to the nearest integer
#       3.2.- If the percentage is less than 1%, output "E"
#       3.2.- If the percentage is more than 99%, output "F"
#

def get_int() -> list:
    ''' Function prompts user, using input message "Fraction :", to enter a fraction. The
        function returns a list with three elements.  The first element is your first
        integer, the second element your second integer. While the input is not valid,
        continue to ask for a fraction.

        See notes above to understand when the input is valid.
    '''
    num_lst = list()
    while True:
        resp_str = input('Fraction: ').strip()
        if len(resp_str) < 3 or '/' not in resp_str:
            #            print(f'The number of characters is too short {
            #                  len(res_str)} or is missing a forward slash')
            continue

        # Convert to a string now and split it.
        char_lst: list = resp_str.split('/')
        try:
            num_lst = [int(char_lst[0]), int(char_lst[1])]
        #    num_lst.append(int(char_lst[0]))
        #    num_lst.append(int(char_lst[1]))
        except ValueError:
            #            print('Either number is not an integer.')
            continue
        if num_lst[0] > num_lst[1] or num_lst[1] == 0:
            continue
        else:
            return num_lst


def main():
    my_nums = get_int()

    # We are evaluating correctly and ready to do a division.
    # Decide what to display
    tank_pct = int(my_nums[0] / my_nums[1] * 100)
    # print('Tank percentage', tank_pct)

    if tank_pct <= 1:
        # It is ok to recast.  We are not using this again.
        tank_pct = 'E'
    elif tank_pct >= 99:
        tank_pct = 'F'
    else:
        tank_pct = str(tank_pct) + '%'

    # print(tank_pct)
    print(tank_pct)


# Call main only when intended
if __name__ == '__main__':
    main()
