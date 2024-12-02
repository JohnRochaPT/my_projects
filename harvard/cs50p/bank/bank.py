"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/10"


# Original Requirements
# Implement a program that prompts the user for a greeting. If the greeting starts with “hello”,
# output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise,
# output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s
# greeting case-insensitively.

# Extra work problem statement
# None offered

# My pseudo code approach:
#  1.- With a str variable, and using the "input()" function, ask the user to type a response to
#      the program's "Greeting:" message.
#  2.- Evaluate what the user entered not case sensitive.
#     2.1.- If the user enters "hello" send "$0" to the screen
#     2.2.- If the user enters a word that begins with letter "h", output "$20"
#     2.3.- If the user enters a a word or words that do not contain the letter "H", then
#           output "$100" to the screen.

def main():
    myStr = 'Greeting: '
    resStr = input(myStr).lower()

    if not ('hello' in resStr or 'h' == resStr[0]):
        print('$100')
    elif 'hello' in resStr:
        print('$0')
    else:
        print('$20')


main()
