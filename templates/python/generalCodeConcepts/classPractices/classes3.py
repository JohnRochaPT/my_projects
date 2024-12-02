"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/24'


# < This sample program shows how you should always name instance variables with the an
# < underscore before the name.  That will be an indicator to the person using the class
# < that they should never attempt to change a variable if the name begins with an "_".

class Cao:
    VAR = 1

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


def main():
    perro = Cao('Willy')
    print(f'The name is {perro.name}')

    perro.name = 'Charlie'
    print(f'The name is {perro.name}')

    perro._name = 'Tino'
    print(f'The name is {perro.name}')

    balance = 100


# < This calls main
if __name__ == '__main__':
    main()
