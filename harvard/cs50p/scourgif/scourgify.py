"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/18'

# .Original Requirements:
#: “Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in. That could do with
#: a bit of cleaning, too.” She pointed her wand at Hedwig’s cage. “Scourgify.” A few feathers and
#: droppings vanished.
#:
#:      — Harry Potter and the Order of the Phoenix
#:
#: Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent,
#: if not more convenient, format. Consider, for instance, this CSV file of students, before.csv,
#: below:
#:      Source: en.wikipedia.org/wiki/List_of_Harry_Potter_characters
#:
#: Even though each “row” in the file has three values (last name, first name, and house), the first
#: two are combined into one “column” (name), escaped with double quotes, with last name and first
#: name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter to each
#: student, as via mail merge, since it’d be strange to start a letter with:
#:
#:      Dear Potter, Harry,
#:
#:      Rather than with, for instance:
#:
#:      Dear Harry,
#:
#: Implement a program that:
#: 1.- Expects the user to provide two command-line arguments:
#:   1.1.- The name of an existing CSV file to read as input, whose columns are assumed to be, in
#:         order, name and house, and
#:   1.2.- The name of a new CSV to write as output, whose columns should be, in order, first,
#:         last, and house.
#:
#: 2.- Converts that input to that output, splitting each name into a first name and last name.
#:     Assume that each student will have both a first name and last name.
#:
#: 3.- If the user does not provide exactly two command-line arguments, or if the first cannot
#:     be read, the program should exit via sys.exit with an error message.
#:


# .Hints:
#: 1.- Note that csv module comes with quite a few methods, per docs.python.org/3/library/csv.html,
#:     among which are DictReader, per docs.python.org/3/library/csv.html#csv.DictReader
#:     nd DictWriter, per docs.python.org/3/library/csv.html#csv.DictWriter.
#:
#: 2.- Note that you can tell a DictWriter to write its fieldnames to a file using writeheader with
#:     no arguments, per docs.python.org/3/library/csv.html#csv.DictWriter.writeheader.
#:


# .Extra work requirements:
#: None defined
#:


# .My pseudo code approach:
#: 1.- Import csv and sys library
#:
#: 2.- Reimplement old code, from pizza, to read the new csv file.
#:    2.1.- If the file cannot be read, issue message "Could not read " and file name.
#:    2.2.- User has to pass two arguments.  The first argument is supposed to be "before.csv" and
#:          "after.csv" which contains the reformatted names.
#:
#: 3.- Reading, row by row, the first file, slipt the first column into two columns and write
#:     into the new file.  Columns should be first, last and house.
#:
#:


import sys
import csv


def check_args() -> bool:
    """
    check_args
        Function checks that the user passed valid file names when launching this program

        Conditions:
            1.- There can only be three arguments. The program name, the first file name and
                the second file name.  If there are less than three arguments or more than
                three, exist with sys.exit()
            2.- If the file names does not end with "*.csv", exist with sys.exit()
            3.- If the second file does not exist end with sys.exit()

    Returns:
        Returns True if all conditions are met.
    """
    # > If there is less than 3 argument
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    # > If there are more than 3 arguments, there are too many
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    # > Check the extension of the file.
    if (sys.argv[1][-3:]) not in ('csv', 'CSV'):
        sys.exit(f'Could not read {sys.argv[1][-3:]}')

    if (sys.argv[2][-3:]) not in ('csv', 'CSV'):
        sys.exit('Not a csv file')

    # > Now we need to determine if we can open the file
    try:
        file = open(sys.argv[1], 'r')
        file.close()
        return True
    except:
        sys.exit('File does not exists')
        return False


def read_source_file() -> list:
    """
    read_source_file
        Function will open and populate a file that contains the entire before.cvs file.

    Returns:
        Returns a populated variable of type cvs.DictReader
    """
    with open(sys.argv[1]) as csv_file:
        reader = csv.DictReader(csv_file)
        people = list()
        for row in reader:
            people.append(row)

    return people


def after_file(people: list) -> bool:
    """
    after_file
        Function accepts a csv.DictReader file and uses that file to write to another file.

    Arguments:
        reader -- Non empty csv.DictReader variable.

    Returns:
        Returns True if it was able to read and write to the "after.csv" file.
    """
    # > Open the after file
    with open(sys.argv[2], 'w', newline='') as csv_after:
        col_names = ['first', 'last', 'house']
        writer = csv.DictWriter(csv_after, fieldnames=col_names)
        writer.writeheader()

        # > Now we can write every line but splitting the original name.
        for row in people:
            last, first = row.get('name').split(',')
            last = last.strip()
            first = first.strip()
            # print(f'First name = {first} and last name = {last}')
            writer.writerow(
                {'first': first, 'last': last, 'house': row.get('house')})


def main():
    # > This is an inline code comment.
    check_args()
    people = list()
    people = read_source_file()
    if after_file(people):
        pass


# > Call main ONLY when intended
if __name__ == '__main__':
    main()
