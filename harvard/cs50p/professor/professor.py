"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/15"

# < Original Requirements:
# > In a file called professor.py, implement a program that:
# >   1.- Prompts the user for a level, If the user does not input 1, 2, or 3, the program
# >       should prompt again.
# >   2.- Randomly generates ten (10) math problems formatted as X + Y = , wherein each of
# >       X and Y is a non-negative integer with digits. No need to support operations other
# >       than addition(+).
# >   3.- Prompts the user to solve each of those problems. If an answer is not correct
# >       (or not even a number), the program should output EEE and prompt the user again,
# >       allowing the user up to three tries in total for that problem. If the user has still
# >       not answered correctly after three tries, the program should output the correct
# >       answer.
# >   4.- The program should ultimately output the user’s score: the number of correct answers
# >       out of 10.
# >
# > Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts)
# > the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly
# > generated non-negative integer with level digits or raises a ValueError if level is not
# > 1, 2, or 3:
# >
# >                 import random
# >
# >                 def main():
# >                     ...
# >
# >                 def get_level():
# >                     ...
# >
# >                 def generate_integer(level):
# >                     ...
# >
# >                 if __name__ == "__main__":
# >                     main()
# >


# < Hints:
# > 1.- Note that you can raise an exception like ValueError with code like:
# >             raise ValueError
# > 2.- Note that the random module comes with quite a few functions, per
# >     docs.python.org/3/library/random.html.


# < Extra work requirements:
# > None defined
# >


# < My pseudo code approach:
# > 1.- Import random
# > 2.- Prompt the user for a level, using get_level(). If the user does not input 1, 2,
# >     or 3, the program should prompt again.
# > 3.- Randomly generate 10 problems where you are adding a single digit integer to
# >     another integer single digit.
# > 4.- Prompt the user to solve all the problems.  If the user does not get a problem
# >     correct, output "EEE" and re-prompt, with the same problem.
# >   4.1.- If the user gets it wrong 3 times, display the right answer
# > 5.- When the 10 problems are resolved, output the score with the number of correct
# >     answers.
# >
# >

import random


def generate_integer(level: int) -> int:
    """
    generate_integer
        Function accepts an integer, that must be 1, 2 or 3 and uses that number to determine
        the number of digits that the random function will use to get the integer.  The levels
        define the numbers of digits x and y will have.  Example:
            level = 1 --> Returns any integer from 0 to 9
            level = 2 --> Returns any integer from 10 to 99
            level = 3 --> Returns any integer from 100 to 999

    Arguments:
        level -- Integer of value 1, 2 or 3
    Prerequisites:
        level -- Must be either number 1, 2 or 3

    Returns:
        An integer of either 1, 2 or 3 digits.
    """
    # * Validate that the passed string is an integer and it is either 1, 2 or 3.
    try:
        int(level)
    except ValueError:
        print('The level must be an integer')
    # * Determine the number of digits to use based on the level
    if not (1 <= level <= 3):
        raise ValueError('Level needs to be 1, 2 or 3')
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def get_level() -> int:
    """
    get_lvl
        Formula asks the user for an input that has to be a number from 1 to 3.  If it is not
        a number, keep asking.

    Returns:
        Returns an integer of 1, 2 or 3.
    """
    while True:
        try:
            lvl = int(input('Level: ').strip())
        except:
            continue
        if 1 <= lvl <= 3:
            return lvl


def get_guess(formula: str) -> int:
    """
    get_guess
        Formula asks the user for an input that has to be a positive integer.  It will continue to
        prompt until the user enters an integer.

    Arguments
        -- form needs to get a string that gets outputted to the user.

    Preconditions:
        -- form cannot be an empty string.

    Returns:
        Returns a positive integer.
    """
    while True:
        try:
            guess = int(input(formula).strip())
            return guess
        except:
            continue


def main():
    # * This is an inline code comment.
    lvl = get_level()
    # * print(lvl)

    # * Build the formula dictionary.  The dictionary key will be x and y will be the value
    my_xs = list()
    my_ys = list()
    i = 0
    for i in range(10):
        my_xs.append(generate_integer(lvl))
        my_ys.append(generate_integer(lvl))

    score = 0
    for i in range(10):
        formula = str(my_xs[i]) + ' + ' + str(my_ys[i]) + ' = '
        attempt = 1
        while True:
            ans = get_guess(formula)
            if ans == my_xs[i] + my_ys[i]:
                score = score + 1
                break
            else:
                print('EEE')
                attempt = attempt + 1

            if attempt == 4:
                print(formula, my_xs[i] + my_ys[i])
                break

    print('Score:', score)


# * Call main only when intended
if __name__ == "__main__":
    main()
