"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/18'

# ▓ Original Requirements:
#: Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka
#: Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”
#:
#: Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu
#: too, per this CSV file of Sicilian pizzas, sicilian.csv, below:
#:
#:          Sicilian Pizza,Small,Large
#:          Cheese,$25.50,$39.95
#:          1 item,$27.50,$41.95
#:          2 items,$29.50,$43.95
#:          3 items,$31.50,$45.95
#:          Special,$33.50,$47.95
#:
#: See regular.csv for a CSV file of regular pizzas as well.
#:
#: Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a
#: table, formatted as ASCII art, like this one:
#:
#:              +------------------+---------+---------+
#:              | Sicilian Pizza   | Small   | Large   |
#:              +==================+=========+=========+
#:              | Cheese           | $25.50  | $39.95  |
#:              +------------------+---------+---------+
#:              | 1 item           | $27.50  | $41.95  |
#:              +------------------+---------+---------+
#:              | 2 items          | $29.50  | $43.95  |
#:              +------------------+---------+---------+
#:              | 3 items          | $31.50  | $45.95  |
#:              +------------------+---------+---------+
#:              | Special          | $33.50  | $47.95  |
#:              +------------------+---------+---------+
#:
#: Implement a program that expects exactly one command-line argument, the name (or path) of a
#: CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate,
#: a package on PyPI at pypi.org/project/tabulate.
#:
#: Format the table using the library’s grid format. If the user does not specify exactly one
#: command-line argument, or if the specified file’s name does not end in .csv, or if the
#: specified file does not exist, the program should instead exit via sys.exit.
#:
#:


# ▓ Hints:
#: 1.- Recall that the csv module comes with quite a few methods, per
#:     docs.python.org/3/library/csv.html, among which are reader, per
#:     docs.python.org/3/library/csv.html#csv.reader, and DictReader, per
#:     docs.python.org/3/library/csv.html#csv.DictReader.
#:
#: 2.- Note that open can raise a FileNotFoundError, per
#:     docs.python.org/3/library/exceptions.html#FileNotFoundError.
#:
#: 3.- Note that the tabulate package comes with just one function, per pypi.org/project/tabulate.
#:     You can install the package with:
#:              pip install tabulate
#:
#:


# ▓ Extra work requirements:
#: None defined
#:


# ▓ My pseudo code approach:
#: 1.- Use the last program, for a sample of how to control one argument, which is a valid file
#:     name, and adapt it to .csv
#:
#: 2.- Install the tabulate library from a package on PyPI at pypi.org/project/tabulate
#:
#: 3.- Open csv file and output its content formatted as ASCII art using tabulate where the form
#:     is "grid"
#:
#:

import sys
import csv
from tabulate import tabulate


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
    if (sys.argv[1][-3:]) not in ('csv', 'CSV'):
        sys.exit('Not a csv file')

    # > Now we need to determine if we can open the file
    try:
        file = open(sys.argv[1], 'r')
        file.close()
        return True
    except:
        sys.exit('File does not exists')
        return False


def output_tabular():
    """
    output_tabular
        Function is a simple function that reads a Pinocchio csv file and uses the tabulate
        function from library tabulate and outputs the file in grid format.

        Function does not accept any arguments or return anything.
    """
    with open(sys.argv[1], newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        # Now print with the correct arguments.
        print(tabulate(reader, headers="keys", tablefmt="grid"))


def main():
    # ? This is an inline code comment.
    check_args()
    output_tabular()


# ? Call main ONLY when intended
if __name__ == '__main__':
    main()
