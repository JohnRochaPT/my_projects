"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/14"


# Original Requirements:
# Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs
# support “codes,” whereby you can type, for instance, :thumbs_up:, which will be automatically
# converted to 👍. Some programs additionally support aliases, whereby you can more succinctly type,
# for instance, :thumbsup:, which will also be automatically converted to 👍.
#
# See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with
# aliases.
#
# Implement a program that prompts the user for a str, in English, and then outputs the “emojized”
# version of that str, converting any codes (or aliases) therein to their corresponding emoji. The
# input message needs to be "Input: " and the output message needs to be "Output: "
#
#
# Hints:
# Note that the emoji module comes with two functions, per pypi.org/project/emoji, one of which is
# emojize, which takes an optional, named parameter called language. You can install it with:
#          pip install emoji
#
#
# Extra work requirements:
# None defined
#
#
# My pseudo code approach:
#   1.- Using "pip", install emoji into "train1" Anaconda environment.
#   2.- Prompt the user for an input which includes the code for an emoji, as defined in the emoji
#       library included with the emoji package.
#   3.- Output the same message where the code is converted.  Sample code is
#           import emoji
#           print(emoji.emojize('Python is :thumbs_up:'))
#

import emoji


def main():
    # Get user's input
    resp = input("Input: ").strip()
    # resp = "Hello :1st_place_medal:"
    # Get the position for all codes.
    print(f"Output: {emoji.emojize(resp, language="alias")}")


# Call main only when intended
if __name__ == "__main__":
    main()
