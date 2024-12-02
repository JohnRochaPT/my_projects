"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/17'

# ▓ Original Requirements:
#: 1.- One way to measure the complexity of a program is to count its number of lines of code
#:     (LOC), excluding blank lines and comments. For instance, a program like
#:
#:             # Say hello
#:
#:             name = input("What's your name? ")
#:             print(f"hello, {name}")
#:
#:     Has just two lines of code, not four, since its first line is a comment, and its second
#:     line is blank (i.e., just whitespace). That’s not that many, so odds are the program
#:     isn’t that complex. Of course, just because a program (or even function) has more lines
#:     of code than another doesn’t necessarily mean it’s more complex. For instance, a
#:     function like
#:
#:             def is_even(n):
#:                 if n % 2 == 0:
#:                     return True
#:                 else:
#:                     return False
#:     isn’t really twice as complex as a function like
#:
#:             def is_even(n):
#:                 return n % 2 == 0
#:
#:     Even though the former has (more than) twice as many lines of code. In fact, the former
#:     might arguably be simpler if it’s easier to read! So lines of code should be taken with
#:     a grain of salt.
#:
#: 2.- Even so, implement a program that expects exactly one command-line argument, the name
#:     (or path) of a Python file, and outputs the number of lines of code in that file,
#:     excluding comments and blank lines. If the user does not specify exactly one
#:     command-line argument, or if the specified file’s name does not end in .py, or if the
#:     specified file does not exist, the program should instead exit via sys.exit.
#:
#: 3.- Assume that any line that starts with #, optionally preceded by whitespace, is a
#:     comment. (A docstring should not be considered a comment.) Assume that any line that
#:     only contains whitespace is blank.
#:

# ▓ Hints:
#: 1.- Recall that a str comes with quite a few methods, per
#:     docs.python.org/3/library/stdtypes.html#string-methods, including lstrip and startswith.
#: 2.- Note that open can raise a FileNotFoundError, per
#:     docs.python.org/3/library/exceptions.html#FileNotFoundError.
#: 3.- You might find it helpful to test your program on, e.g., some of Week 6’s source code
#:     as well as on programs of your own.
#:

# ▓ Extra work requirements:
#: None defined
#:
#:

# ▓ My pseudo code approach:
#: 1.- Program needs to be able to read sys.args variables.  The program expects the name, and
#:     path of a file.  Handle argument validation as follows:
#:     1.1.- Exit the program with sys.exit() if:
#:           1.1.1.- If the user does not pass any parameter.  Output a message that says "Too
#:                   few command-line arguments"
#:           1.1.2.- If the user passes more than one parameter.  Output a message that says
#:                   "Too many command-line arguments"
#:           1.1.2.- If the user's file name does not end with ".py".  Output a message that
#:                   says "Not a Python file"
#:           1.1.3.- If the file does not exist.  Output a message that says "File does not
#:                   exists"
#:
#: 2.- The program should then read the file and count the number of lines.  Do not include:
#:     2.1.- Lines that are empty
#:     2.2.- Lines that are comments
#:
#: 3.- Output, in a new line, the number of lines.  No additional text.  Just the number.
#:


import sys


def check_args() -> bool:
    """
    check_args
        Function checks that the user passed a valid file name when launching this program

        Conditions:
            1.- There can only be one argument.  If there are no arguments or more than one
                argument, function exits with sys.exit()
            2.- If the file name does not end with "*.py", exist with sys.exit()
            3.- If the file does not exist, end with sys.exit()

    Returns:
        Returns True if all conditions are met.
    """
    # > Use the file "SampleProgram.py" as a test file.
    # > If there is only one argument, no file name is available
    if len(sys.argv) == 1:
        sys.exit('Too few command-line arguments')

    # > If there are more than 2 arguments, there are too many
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')

    # > Check the extension of the file.
    if (sys.argv[1][-2:]) not in ('py', 'PY'):
        sys.exit('Not a Python file')

    # > Now we need to determine if we can open the file
    try:
        file = open(sys.argv[1], 'r')
        file.close()
        return True
    except:
        sys.exit('File does not exists')
        return False


def get_count() -> int:
    """
    get_count
        Function will open the file and count lines of code.

        Should not include empty (blank) or comment lines.

    Returns:
        Returns the number of lines
    """
    count = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
            x = len(line.strip().rstrip('\n'))
            if not (len(line.strip().rstrip('\n')) == 0):
                if not line.strip()[0] == '#':
                    count += 1

    return count


def main():
    # > This is an inline code comment.
    check_args()

    # > Now count the lines, since we have a good file.
    count = get_count()
    print(count)


# > Call main ONLY when intended
if __name__ == '__main__':
    main()
