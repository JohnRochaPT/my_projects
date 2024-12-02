"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/14"


# Original requirements
# This is a reimplimentation of the original program in "D:\Dropbox\Learn\edX\CS50P\twttr". Now
# we need to reimplement by restructuring your code per the below, wherein shorten expects a
# str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.
#
#           def main():
#               ...
#
#           def shorten(word):
#               ...
#
#           if __name__ == "__main__":
#               main()
#
# Hints
# None defined for this program
#
# Extra work problem statement
# None defined for this program
#
# My pseudo code approach:
#   1.- Create a function called "shorten()" which accepts a string and returns a string
#       where all the vowels have been removed.  Regardless of the case but preserve the
#       case.


def shorten(old_str: str) -> str:
    """
    shorten:
        Function accepts a string and returns the same string without vowels.

        Removes vowels regardless of the case but preserves the case of all the letters.

    Arguments:
        old_str -- A string variable
    Preconditions:
        old_str -- The string cannot be empty and must contain at least 1 character

    Returns:
        Returns a converted string where the vowels have been removed
    """
    new_str: str = ""
    for letter in old_str:
        if letter not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            new_str = str(new_str) + letter
    return new_str


def main():
    inp_msg = "Input: "
    resp_msg = input(inp_msg)

    resp_msg = shorten(resp_msg)

    # Read the string, one character at a time, and print the string back without vowels.
    print(f"Output: {resp_msg}")
    print()


# Call main only when intended
if __name__ == "__main__":
    main()
