"""
A eDX assignment.

This file shows how modules work

"""
__author__ = "John Rocha"
__date__ = "2024/09/13"


# Original Requirements:
# Implement a program that prompts the user for items, one per line, until the user inputs
# control-d (which is a common way of ending one’s input to a program). Then output the
# user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each
# line with the number of times the user inputted that item. No need to pluralize the
# items. Treat the user’s input case-insensitively.
#
# Hints:
#   1.- Note that you can detect when the user has inputted control-d by catching an
#       EOFError with code like:
#           try:
#               item = input()
#           except EOFError:
#               ...
#   2.- Note that a dict comes with quite a few methods, per
#       docs.python.org/3/library/stdtypes.html#mapping-types-dict, among them get, and
#       supports operations like:
#           d[key]
#       and
#
#           if key in d:
#               ...
#       wherein d is a dict and key is a str.
#   3.- Be sure to avoid or catch any KeyError.
#   4.- Note that you can sort a dictionary’s keys alphabetically by passing that
#       dictionary as an argument to sorted.
#


# Extra work requirements:
# None defined
#
#


# My pseudo code approach:
#   1.- Get all the grocery items from the user. The user finishes entering the grocery
#       items when they hit "control-c" and load them into a dictionary.
#       1.1.- The dictionary key is the item and the value is the number of times the
#             item has been mentioned
#       1.2.- Each item name needs to be inserted into the dictionary in CAPs
#   2.- When the user stops entering items:
#       2.1.- Sort the array in alphabetical order
#       2.2.- Output the dictionary to the user as "Value" " " "Key"
#


def main():
    my_dict = dict()
    resp = str()
    freq: int = 0
    while True:
        try:
            resp = input().upper()
        except EOFError:
            break
        except KeyboardInterrupt:
            break

        # Get the price now
        try:
            freq = my_dict.get(resp, 0)
        except KeyError:
            continue
        else:
            if freq == 0:
                # This means that it did not find the key so we need to insert it
                my_dict.update({resp: 1})
            else:
                # This means that it did find an entry and we need to up it by 1
                my_dict[resp] = freq + 1

    # Now print the dictionary value first then key.
    for k, v in sorted(my_dict.items()):
        print(v, k)


# Call main only when intended
if __name__ == '__main__':
    main()
