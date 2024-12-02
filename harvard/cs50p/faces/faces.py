"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/10"

# Original Requirements
# Implement a function called convert that accepts a str as input and returns that same input
# with any :) converted to emoji "🙂" and any :( converted to "🙁". All other text should be
# returned unchanged.  Then, in the same program, implement a function called main that
# prompts the user for input, calls convert on that input, and prints the result.


# Extra work problem statement
# You’re welcome, but not required, to prompt the user explicitly, as by passing a str of
# your own as an argument to input. Be sure to call main at the bottom of your file.

# My pseudo code is:
#   1.- Create a function called "convert".
#       1.1.- Function accepts only one parameter of type string
#       1.2.- Function should return a string
#       1.3.- The function needs to look for any character combination of ":)" and replace
#             it with "🙂"
#       1.4.- The function needs to look for any character combination of ":(" and replace
#             it with "🙁"
#   2.- Create a function called "main":
#       2.1.- Creates a string parameter to enter the message to be displayed in the screen.
#       2.1.- Function needs to prompt the user for an input.
#       2.2.- Function needs to call "convert" passing the input
#       2.3.- Function needs to print the converted text


def convert(what: str) -> str:
    '''
        Function accepts a string, looks for :) and :( and turns them into 🙂 and 🙁
    '''
    return what.replace(':)', '🙂').replace(':(', '🙁')


def main():
    myStr = 'Hi.  Tell me something: '
    getStr = input(myStr)

    getStr = convert(getStr)
    print(getStr)


main()
