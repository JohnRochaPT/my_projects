"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/15"

# < Original Requirements:
# > Implement a program that:
# >  1.- Prompts the user for a level "n" number. If the user does not input a positive integer, the
# >      program should prompt again.
# >  2.- Randomly generates an integer between 1 and "n", inclusive of "n", using the random module.
# >  3.- Prompts the user to guess that integer. If the guess is not a positive integer, the program
# >      should prompt the user again.
# >    3.1.- If the guess is smaller than that integer, the program should output Too small! and
# >          prompt the user again.
# >    3.2.- If the guess is larger than that integer, the program should output Too large! and
# >          prompt the user again.
# >    3.3.- If the guess is the same as that integer, the program should output Just right! and exit.
# >

# < Hints:
# > Use the random function from random.
# >

# < Extra work requirements:
# > None specified

# < My pseudo code approach:
# > 1.- Import library "random"
# > 2.- Prompt, with "Level: ", to obtain an integer. If the user does not input an integer, keep
# >     asking.  The response needs to a positive integer greater than zero:
# > 3.- Using the random.random function, get a random number from 1 to the level "n"
# > 4.- Prompt the user again, with "Guess: " and get the user to enter an integer.  If the number is
# >     not an integer, keep asking.
# >   4.1.- If the answer is greater than the random number, output "Too Large!" and prompt again
# >   4.2.- If the answer is lower than the random number, output "Too small!" and prompt again
# >   4.3.- If the answer is the random number, output "Just right!" and exit the game.

import random


def get_num(msg: str) -> int:
    """
    get_num
    Function accepts a string and prompts the user for a number.

    When prompting the user, the function will use "msg" as a message to the user.  The function will
    concatenate ": " to the message so the developer using this function does not need to remember
    to add a space.  The function then will accept an input from the user.  The input must:
      1.- Be an positive integer from 1 to infinite

    The function will continue to ask the user for an input until the input value passes the input
    requirements.  Once the input is accepted, it will return a string with the inputted integer.

    Arguments:
        msg -- String type
    Preconditions:
        msg -- Must not be an empty string

    Returns:
        Returns the user's validated integer
    """
    while True:
        try:
            lvl = int(input(msg + ': ').strip())
        except:
            continue
        if lvl > 0:
            return lvl


def main():
    # * This is an inline code comment.
    lvl = get_num('Level')
    my_num = random.randint(1, lvl)
    while True:
        guess = get_num('Guess')
        if guess < my_num:
            print('Too small!')
        elif guess > my_num:
            print('Too large!')
        else:
            print('Just right!')
            break


# * Call main only when intended
if __name__ == "__main__":
    main()
