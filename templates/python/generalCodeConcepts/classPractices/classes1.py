"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/24'


import datetime

# < Classes need to be defined above main
# < Defining a class called "Employee"
# < Calling a class method requires "()".
# < Calling attributes, or variables, does not use "()"


class Employee:
    # < The following are class attributes.  These attributes belong to the class and not the instance
    # < However, if we ever update the value of an instance raise_amt, Python will make it a self
    # < variable.
    raise_amt = 0
    # < The following code is the constructor.  It reads the arguments passed when the class gets
    # < instantiated

    def __init__(self, first: str, last: str, pay: int):
        #: In the constructor, you can assign values to self variables.  You can even create
        #: new variables that you are not passing values to and set them yourself.
        self.first = first                              # >> Instance variable called first
        self.last = last
        self.pay = pay
        self.hair_color = 'White'

    # < 1.- The following code is a sample of implementing a instance method.  The method will be called
    # <     "full_name" and will return the employee's full name
    # < 2.- Every method, or function in a class, has to have self as the first parameter.  Now,
    # <     the passed self is an instantiation of itself. Since you are passing, self, you can change
    # <     any attributes of self.
    # < 3.- To call a function's method you must call object.method().
    def full_name(self):
        self.hair_color = 'Black'
        return f'{self.first} {self.last}'

    # < Another instance method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # <
    # < A class method, requires a decorator and accepts the "class", not "self", as the first argument
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # <
    # < Static methods don't automatically accept either the class or the instantiation of the class.  They
    # < do use the decorator @staticmethod
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        else:
            return True

    # < Special instance methods.  Special methods begin with "__something__" and serve a specific purpose
    # < Special method __repr__ is intended for other developers.  However, if you don't define a __str__
    # < method for your class, it will use __repr__ if it exists.
    # < A good idea may be to return what would create the object itself
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    # <
    # < Special methods can be used to overload an operator.  For example, if you wanted to add two
    # < Employees, you can do that.
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.first) + len(self.last)

    # <
    # < Getter and setters give us more control over attributes.  We can define a instance method that acts
    # < like an attribute but decorating the method with the keyword "property".  "property" decorators are
    # < the getter
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # < setter methods allows us to change instance variables
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # < An example of how to disallow a user from changing a incorrectly variable.  For example, the variable
    # < last should never be changed unless the string being passed is more than one character
    @property
    def last(self):
        # < While the user may be passing an empty string, Python will use this getter
        return self._last
        # < before the change takes place

    @last.setter
    def last(self, name):
        if len(name) < 1:
            raise ValueError('Need more characters')
        # < Here we are telling Python to overwrite the instance attribute called "last"
        self._last = name


def main():
    emp1 = Employee('John', 'Rocha', 10000)
    emp2 = Employee('Lucas', 'Rocha', 20000)

    # < Printing the employee's attributes
    # //print(emp1.first)
    # //print(emp1.last)
    # //print(emp1.email)
    # //print(emp1.pay)

    # < Seeing if by calling the method, the hair color changes.  Yes it did.
    # // print(emp1.hair_color)
    # // print(emp1.full_name())
    # // print(emp1.hair_color)

    # < Seeing if by calling the class itself, and passing the obj as a parameter, also changes the hair
    # < The result was that it did.
    # //print(emp1.hair_color)
    # //Employee.full_name(emp1)
    # //print(emp1.hair_color)

    # < Before adding getters and setters, I was able to change the hair color by calling the attribute.
    # //emp1.hair_color = 'Blue'
    # //print(emp1.hair_color)

    # < Checking all the class variables before we try to change them
    print('Emp1 raise amount: ', emp1.raise_amt)
    print('Emp2 raise amount: ', emp2.raise_amt)
    print()

    # < Changing the raise_amt for the instantiation of emp1
    emp1.raise_amt = 1
    print('Emp1 raise amount: ', emp1.raise_amt)
    # < Now, emp1 has a self variable called self.raise_amt and no longer gets its value from the class
    # < but from itself.
    print('Emp2 raise amount: ', emp2.raise_amt)
    print('Class raise amount: ', Employee.raise_amt)
    print()

    # < Changing the raise_amt for the instantiation of emp1
    emp2.raise_amt = 2
    emp3 = Employee('Joe', 'Brusatto', 30000)
    emp4 = Employee('Wonka', 'Rocha', 50000)
    print('Emp1 raise amount: ', emp1.raise_amt)
    print('Emp2 raise amount: ', emp2.raise_amt)
    print('Emp3 raise amount: ', emp3.raise_amt)
    print('Emp4 raise amount: ', emp4.raise_amt)
    print('Class raise amount: ', Employee.raise_amt)
    print()

    # < Now let's change the class.  Every instantiated object, whose class variable raise_amt has not
    # < been overwritten, it will continue to display the "class" value, and not the instance value.
    # < Therefore, emp3 and emp4 will both show "5" and emp1 and emp2 will show their implementation
    # < of their instance value for raise_amt
    Employee.raise_amt = 5
    print('Emp1 raise amount: ', emp1.raise_amt)
    print('Emp2 raise amount: ', emp2.raise_amt)
    print('Emp3 raise amount: ', emp3.raise_amt)
    print('Emp4 raise amount: ', emp4.raise_amt)
    print('Class raise amount: ', Employee.raise_amt)
    print()

    emp3.raise_amt = 3
    emp4.raise_amt = 4
    print('Emp1 raise amount: ', emp1.raise_amt)
    print('Emp2 raise amount: ', emp2.raise_amt)
    print('Emp3 raise amount: ', emp3.raise_amt)
    print('Emp4 raise amount: ', emp4.raise_amt)
    print('Class raise amount: ', Employee.raise_amt)
    print()

    # < If we change the class variable again, no instantiated objects will change.  But any new
    # < instantiations of the object, who has not had their value of raise_amt modified, will continue to
    # < get the value from the class
    Employee.raise_amt = 10
    print('Emp1 raise amount: ', emp1.raise_amt)
    print('Emp2 raise amount: ', emp2.raise_amt)
    print('Emp3 raise amount: ', emp3.raise_amt)
    print('Emp4 raise amount: ', emp4.raise_amt)
    print('Class raise amount: ', Employee.raise_amt)
    print()

    # < The set_raise_amt() method, is a class method and does not change instance variables.  Only affects
    # < class variables.
    Employee.set_raise_amt(15)
    print('Emp1 raise amount: ', emp1.raise_amt)
    print('Emp2 raise amount: ', emp2.raise_amt)
    print('Emp3 raise amount: ', emp3.raise_amt)
    print('Emp4 raise amount: ', emp4.raise_amt)
    print('Class raise amount: ', Employee.raise_amt)
    print()

    # < Even if you call a class method, from an instantiated object, only the class attributes will be
    # < modified
    emp1.set_raise_amt(20)
    print('Emp1 raise amount: ', emp1.raise_amt)
    print('Emp2 raise amount: ', emp2.raise_amt)
    print('Emp3 raise amount: ', emp3.raise_amt)
    print('Emp4 raise amount: ', emp4.raise_amt)
    print('Class raise amount: ', Employee.raise_amt)
    print()

    # < Sample of calling a static method
    if emp1.is_workday(datetime.date.today()):
        print('Workday')
    else:
        print('Weekend')

    print(emp1)

    # < Overloading operators
    # < Adding two employees to get the combined salary
    salaries = emp1 + emp2
    print(f'The salaries are {salaries}')

    # < Get the Employee class length, which would call its special method of __len__
    print(f'The names length is {len(emp1)}')

    print('')

    # < The code below is showing us how to call a method that is behaving like a variable.
    print(emp1.email)

    # < Example of a getter and setter.  In this example, we have a getter called "fullname"

    print(f'Before name change the fullname was {emp3.fullname}')
    emp3.fullname = ('Charlie Rocha')
    print(f'After name change the fullname was {emp3.fullname}')

    # < Attempting to set the last name to an empty string
    try:
        emp1.last = ''
    except:
        print('Trying to change the last name to an empty string')
    emp1.last = 'Rocha 2'
    print(emp1.last)


# < This calls main
if __name__ == '__main__':
    main()
