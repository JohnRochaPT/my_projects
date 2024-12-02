"""
A eDX assignment.

This file shows how modules work

"""

__author__ = "John Rocha"
__date__ = "2024/09/16"


# ▓Original Requirements
# ░ Reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the
# ░ below, wherein value expects a str as input and returns an int, namely 0 if that str starts
# ░ with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise,
# ░ treating the str case-insensitively.
# ░
# ░ You can assume that the string passed to the value function will not contain any leading
# ░ spaces. Only main should call print.
# ░
# ░       def main():
# ░           ...
# ░
# ░       def value(greeting):
# ░           ...
# ░
# ░       if __name__ == "__main__":
# ░           main()
# ░


# ▓Extra work problem statement
# ░
# ░
# ░

# ▓My pseudo code approach:
# ░ 1.- Create a function called "value()" which accepts a string as the input and returns
# ░     an integer as follows:
# ░   1.1.- If the string starts with "hello" return int 0
# ░   1.2.- If the string starts with an "h" but it is not part of "hello", return 20
# ░   1.3.- Otherwise return 100.


def value(greeting: str) -> int:
    """
    value
    Function accepts and evaluates a string returning an integer of value 0, 20 or 100

    As follows:
       1.- If the string starts with the word "hello", case insensitively, it returns 0.
       2.- If the string starts with the letter "h", case insensitively, but it is not part of
    "hello", return 20.
       3.- All other strings return 100

    Arguments:
        greeting -- String of at least 1 character long
    Preconditions:
        greeting -- String cannot be empty

    Returns:
        Will return an integer with value zero, 20 or 100 depending on the evaluation
    """
    if not ("hello" in greeting.lower() or "h" == greeting[0].lower()):
        return 100
    elif "hello" in greeting.lower():
        return 0
    else:
        return 20


def main():
    myStr = "Greeting: "
    resStr = input(myStr).strip().lower()

    resp = value(resStr)
    print(f"The function returned: {resp}")


# Call main only when intended
if __name__ == "__main__":
    main()
