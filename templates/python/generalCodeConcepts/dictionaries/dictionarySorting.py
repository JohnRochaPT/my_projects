"""
A function to roll two dice

Author: John Rocha
Date: 09/06/2024
"""


def load_students() -> list:
    # > Function loads a list where each element is a dictionary
    students = []

    std1 = {'name': 'John', 'location': '1st Floor'}
    std2 = {'name': 'Joe', 'location': '2st Floor'}
    std3 = {'name': 'Lucas', 'location': 'Space'}
    std4 = {'name': 'Trump', 'location': 'Hell'}
    std5 = {'name': 'Rocky', 'location': 'Heaven'}
    students.append(std1)
    students.append(std2)
    students.append(std3)
    students.append(std4)
    students.append(std5)
    return students


def get_name(student: dict) -> str:
    # > Takes a student dictionary and returns the value for key 'name'
    return student['name']


def main():

    # > Load the student list with dictionary entries.
    students = load_students()

    # > Python allows us to call functions from within functions and to use
    # > functions as arguments.  There is a specific coding condition in Python
    # > that allows you to sort a list that contains dictionaries and that the
    # > sorting is done by one of the key values in that dictionary.  The syntax
    # > below reads as follows:

    # > For each student(type=dict()) in the "sorted" list of students, use the
    # > key argument, which in this case is the value for key 'name' and use that
    # > to sort the entire result set.
    for student in sorted(students, key=get_name):
        print(f'{student['name']} in in location {student['location']}')


# > Call main ONLY when intended
if __name__ == '__main__':
    main()
