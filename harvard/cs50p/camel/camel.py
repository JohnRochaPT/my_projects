"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/11"


# Original requirements
# Implement a program that prompts the user for the name of a variable in camel case and outputs
# the corresponding name in snake case. Assume that the user’s input will indeed be in camel
# case.
#
# Hints
#   * Recall that a str comes with quite a few methods, per
#     docs.python.org/3/library/stdtypes.html#string-methods.
#   * Much like a list, a str is “iterable,” which means you can iterate over each of its
#     characters in a loop. For instance, if s is a str, you could print each of its characters,
#     one at a time, with code like:
#           for c in s:
#               print(c, end="")
#
# Extra work problem statement
# None defined

# My pseudo code approach:
#   1.- Accept an input, from the user, that contains a string.
#   2.- Iterate through the string examining each letter.
#     2.1.- If the letter is NOT capitalized, print the character
#     2.2.- If the letter is capitalized, print an underscore and then the character in
#           lowercase

def main():
    my_str = 'CamelCase: '
    resp_str = input(my_str)

    for letter in resp_str:
        if letter.islower():
            print(letter, end='')
        else:
            print(f'_{letter.lower()}', end='')

    print()


# Call main only when intended
if __name__ == '__main__':
    main()
