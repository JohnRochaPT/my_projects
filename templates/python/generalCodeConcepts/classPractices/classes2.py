"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/24'

# < The following is an example of the class variable and how, if you change the variable in
# < one of the instance, it becomes a local variable.


def main1():
    class Person():
        name = 'God'

    son1 = Person()
    son2 = Person()

    # < At this point, both son1 and son2 have the same name.  They are both using the same
    # < memory location where name is for the class.  All of them, at least in this execution
    # < had a memory address of "1932544662896"
    print(f'Class attribute name is[{Person.name}] and is located in [{id(Person.name)}]')
    print(f'Son1 object attribute name is [{son1.name}] and is located in [{id(son1.name)}]')
    print(f'Son2 object attribute name is [{son2.name}] and is located in [{id(son2.name)}]')
    print('-' * 100)
    print()

    # < Now, if I change son1 name, although it is a class attribute and not a object attribute,
    # < it will get a different address than the parent.
    print(f'Class attribute name is [{Person.name}] and is located in [{id(Person.name)}]')
    print(f'Son1 object attribute name is [{son1.name}] and is located in [{id(son1.name)}]')
    # < The following command, made name an instance variable, as opposed to a class variable
    son1.name = 'Son of God'
    print(f'Son1 object attribute name is [{son1.name}] and is located in [{id(son1.name)}]')


def main2():
    class Person():
        def __init__(self, first, last, age):
            self.first_name = first
            self.last_name = last
            self.age = age

    # < Here we are instantiating an object of Person, but passed a color to age as opposed to an integer.
    print('Using class Person')
    per = Person('John', 'Rocha', 'Blue')
    print(f'Person\'s first name is [{per.first_name}] and last name is [{per.last_name}] and is [{per.age} old]')
    print('-'*100)
    print()
    # < You can add controls to variables by adding methods that act as properties.

    class Person2():
        def __init__(self, first, last, age):
            self.first_name = first
            self.last_name = last
            self.age = age

        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, age):
            try:
                int(age)
            except:
                print('Age is not an integer')
            self._age = age

    # < When attempting to create per2, passing "blue" as the age, the class rejects the parameter and does not create
    # < the object.  This is because the __init__ called the setter method and the setter method raised an error
    per2 = Person2('John', 'Rocha', 'Blue')

    # < The setter method, in the call below, allowed the integer to pass and the object is therefore created.
    per2 = Person2('John', 'Rocha', 60)
    print('Using class Person2 (TWO)')
    print(f'Person\'s first name is [{per2.first_name}] and last name is [{per2.last_name}] and is [{per2.age} old]')

#
#
#
#
#
#
#
#
#
#


def main():
    # // main1()
    main2()


# < This calls main
if __name__ == '__main__':
    main()
