"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/10"


# Original Requirements
# In this program, prompt the user for the answer to "What is the answer to The Great Question of
# Life, the Universe and Everything?", then outputting "Yes" if the user inputs number 42 or
# (case-insensitively) forty-two or forty two. Otherwise output "No".

# Extra work problem statement
# None defined

# My pseudo code approach:
#  1.- Create a string variable to pass the string for the question.
#  2.- Using the "input" function, get the user's answer.
#     2.1.- Loop the program if the user does not enter at least 1 character.
#  3.- Inspect the value of the input.
#     3.1.- If number 42, text "42", word "forty-two" or word "forty two"
#           then output "Yes"
#     3.2.- If the input value does not math 3.1, then output "No"

def main():
    myStr = 'What is the answer to The Great Question of Life, the Universe and Everything? '
    resp = input(myStr).lower()

    if '42' in resp or 'forty-two' in resp or 'forty two' in resp:
        print('Yes')
    else:
        print('No')


main()
