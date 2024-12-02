"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/10"


# Original Requirements
# Implement a program that prompts the user for mass as an integer (in kilograms) and then
# outputs the equivalent number of Joules as an integer. Assume that the user will input
# an integer.  Formula is E = mc2 wherein "E" represents energy (measured in Joules),
# "m" represents mass (measured in kilograms), and "c" represents the speed of light
# (measured approximately as 300000000 meters per second).

# Extra work problem statement
# None defined.

# My pseudo code approach:
#  1.- Accept an input, from the user, that receives the number of kilograms
#  2.- Use the E=mc2 using the pow, Python included, function to squaring a number

myStr = 'm: '
kiloAmt = int(input(myStr))

joules = kiloAmt * pow(300000000, 2)
print(f'E: {joules}')
