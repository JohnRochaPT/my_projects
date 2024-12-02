"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/14"


# Original Requirements:
# Implement a program that:
#   1.- Expects zero or two command-line arguments:
#      1.1.- Zero if the user would like to output text in a random font.
#      1.2.- Two if the user would like to output text in a specific font, in which case the
#            first of the two should be -f or --font, and the second of the two should be the
#            name of the font.
#   2.- Prompts the user for a str of text.
#   3.- Outputs that text in the desired font.
#
# If the user provides two command-line arguments and the first is not -f or --font or
# the second is not the name of a font, the program should exit via sys.exit with an error
# message.
#
#
# Hints:
#   1.- You can install pyfiglet with:
#       pip install pyfiglet
#   2.- The documentation for pyfiglet isn’t very clear, but you can use the module as
#       follows:
#               from pyfiglet import Figlet
#
#               figlet = Figlet()
#
#       You can then get a list of available fonts with code like this:
#               figlet.getFonts()
#
#       You can set the font with code like this, wherein f is the font’s name as a str:
#               figlet.setFont(font=f)
#
#       And you can output text in that font with code like this, wherein s is that text
#       as a str:
#               print(figlet.renderText(s))
#
# Note that the random module comes with quite a few functions, per
# docs.python.org/3/library/random.html.
#
#
# Extra work requirements:
# None defined
#
#
#
# My pseudo code approach:
#   1.- Build a list of fonts, from figlet library using:
#           figlet.getFonts()
#   2.- Set checks to make sure that there are two parameters passed when the program
#       opens.  Reject with sys.exit() and message "Invalid usage" if:
#     2.1.- If parameters are passed, there must be two.  Reject if there is only one
#     2.2.- The first parameter must be "-f" or "--f".
#     2.3.- The second parameter must be a valid font name
#   3.- Accept an input from the user, passing message "Input: "
#   4.- If the input if more than 1 character:
#     4.1.- If no parameters where passed, use the random function to get a random picked
#           font.
#     4.2.- If the user passed a font, then output using that font.
#

import random
from pyfiglet import Figlet
import sys


def main():
    # Load the fonts
    figlet = Figlet()
    my_fonts = figlet.getFonts()
    # print(my_fonts)

    # print(f'Zero argument {sys.argv[0]}')
    # try:
    #     print(f'First argument {str(sys.argv[1])}')
    # except:
    #     print('There is no first argument')

    # try:
    #     print(f'Second argument {sys.argv[2]}')
    # except:
    #     print('There is no second argument')

    # Check the number of parameters.
    # If len is 1, there were no parameters passed.
    if len(sys.argv) == 1:
        # Random select the font
        my_font = random.choice(my_fonts)
    else:

        # Means that there are parameters
        if len(sys.argv) == 2:
            sys.exit('Invalid usage')

        if ('-f' in str(sys.argv[1]) and len(str(sys.argv[1])) == 2) or ('--font' in str(sys.argv[1]) and len(str(sys.argv[1])) == 6):
            pass
        else:
            # print('Not matched with --font')
            sys.exit('Invalid usage')

        # If we are here, the first parameter is a valid "-" or "--font"
        if sys.argv[2] not in my_fonts:
            sys.exit('Invalid usage no found font')
        else:
            figlet.setFont(font=sys.argv[2])

    # Now print if you are still here
    resp = input('Input: ').strip()
    if len(resp) < 1:
        sys.exit('No input')

    print('Output: \n' + figlet.renderText(resp))


# Call main only when intended
if __name__ == '__main__':
    main()
