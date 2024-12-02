"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/10"


# Original Requirements
# In the United States, it’s customary to leave a tip for your server after dining in a restaurant,
# typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve
# written a tip calculator for you, below!
#   def main():
#       dollars = dollars_to_float(input("How much was the meal? "))
#       percent = percent_to_float(input("What percentage would you like to tip? "))
#       tip = dollars * percent
#       print(f"Leave ${tip:.2f}")
#
#
#   def dollars_to_float(d):
#       todo
#
#
#   def percent_to_float(p):
#       todo
#
#
#   main()
# Need to write two functions:
# 1.- dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is
#     a decimal digit), remove the leading $, and return the amount as a float. For instance, given
#     $50.00 as input, it should return 50.0.
# 2.- percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a
#     decimal digit), remove the trailing %, and return the percentage as a float. For instance,
#     given 15% as input, it should return 0.15.
# 3.- Assume that the user will input values in the expected formats.
# 4.- Prompt the user with "How much was the meal?: "
# 5.- Prompt the user with "What percentage would you like to tip? "


# Extra work problem statement
# None defined

def dollars_to_float(lunchTotStr: str) -> float:
    '''
        Accepts a str formatted as $##.##, whereas each # is a number with two decimal places.

        It removes the leading $, and return the amount as a float.
        For instance, given $50.00 as input, it should return 50.0
    '''
    return float(lunchTotStr[1:])


def percent_to_float(tipPctStr: str) -> float:
    '''
        Accepts a str as input (formatted as ##%, whereas # is a number with two decimals
        places

        It removes the trailing %, and return the percentage as a float. For instance,
        given 15% as input, it should return 0.15.  The amount needs to be divided by 100
    '''
    return float(float(tipPctStr[:-1]) / 100)


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
#    print(f'Dollars {dollars:.2f}')
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
#    print(f'Percentage {percent:.2f}')
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()
