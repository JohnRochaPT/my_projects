"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/09/24'


# .Original Requirements:
#: 1.- Suppose that you’d like to implement a cookie jar in which to store cookies. In a file
#:     called jar.py, implement a class called Jar with these methods:
#:
#:     1.1.- "__init__" should initialize a cookie jar with the given capacity, which represents
#:           the maximum number of cookies that can fit in the cookie jar. If capacity is not a
#:           non-negative int, though, __init__ should instead raise a ValueError.
#:
#:     1.2.- "__str__" should return a str with 🍪, where is the number of cookies in the cookie
#:           jar. For instance, if there are 3 cookies in the cookie jar, then str should
#:           return "🍪🍪🍪"
#:
#:     1.3.- "deposit" should add n cookies to the cookie jar. If adding that many would exceed
#:           the cookie jar’s capacity, though, deposit should instead raise a ValueError.
#:
#:     1.4.- "withdraw" should remove n cookies from the cookie jar. Nom nom nom. If there aren’t
#:           that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
#:
#:     1.5.- "capacity" should return the cookie jar’s capacity.
#:
#:     1.6.- "size" should return the number of cookies actually in the cookie jar, initially 0.
#:
#: 2.- Structure your class per the below. You may not alter these methods’ parameters, but you may
#:     add your own methods.
#:
#:                     class Jar:
#:                         def __init__(self, capacity=12):
#:                             ...
#:
#:                         def __str__(self):
#:                             ...
#:
#:                         def deposit(self, n):
#:                             ...
#:
#:                         def withdraw(self, n):
#:                             ...
#:
#:                         @property
#:                         def capacity(self):
#:                             ...
#:
#:                         @property
#:                         def size(self):
#:                             ...
#:
#: 3.- Either before or after you implement jar.py, additionally implement, in a file called
#:     test_jar.py, four or more functions that collectively test your implementation of Jar
#:     thoroughly, each of whose names should begin with test_ so that you can execute your tests
#:     with:
#:
#:                     pytest test_jar.py
#:
#: 4.- Note that it’s not as easy to test instance methods as it is to test functions alone, since
#:     instance methods sometimes manipulate the same “state” (i.e., instance variables). To test
#:     one method (e.g., withdraw), then, you might need to call another method first
#:     (e.g., deposit). But the method you call first might itself not be correct!
#:
#: 5.- And so programmers sometimes mock (i.e., simulate) state when testing methods, as with
#:     Python’s own mock object library, so that you can call just the one method but modify the
#:     underlying state first, without calling the other method to do so.
#:
#: 6.- For simplicity, though, no need to mock any state. Implement your tests as you normally
#:     would!
#:
#:


# .Hints:
#: 1.- No verbal instructions.  Just the code below
#:
#:                     from jar import Jar
#:
#:
#:                     def test_init():
#:                         ...
#:
#:
#:                     def test_str():
#:                         jar = Jar()
#:                         assert str(jar) == ""
#:                         jar.deposit(1)
#:                         assert str(jar) == "🍪"
#:                         jar.deposit(11)
#:                         assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
#:
#:
#:                     def test_deposit():
#:                         ...
#:
#:
#:                     def test_withdraw():
#:                         ...
#:


# .How to test:
#: 1.- Open your test_jar.py file and import your Jar class with from jar import Jar. Create a
#:     function called test_init, wherein you create a new instance of Jar with jar = Jar().
#:     Assert that this jar has the capacity it should, then run your tests with pytest
#:     test_jar.py.
#:
#: 2.- Add another function to your test_jar.py file called test_str. In test_str, create a new
#:     instance of your Jar class and deposit a few cookies. assert that str(jar) prints out as
#:     many cookies as have been deposited, then run your tests with pytest test_jar.py.
#:
#: 3.- Add another function to your test_jar.py file called test_deposit. In test_deposit, create
#:     a new instance of your Jar class and deposit a few cookies. assert that the jar’s size
#:     attribute is as large as the number of cookies that have been deposited. Also assert
#:     that, if you deposit more than the jar’s capacity, deposit should raise a ValueError. Run
#:     your tests with pytest test_jar.py.
#:
#: 4.- Add another function to your test_jar.py file called test_withdraw. In test_withdraw,
#:     create a new instance of your Jar class and first deposit a few cookies. assert that
#:     withdrawing from the jar leaves the appropriate number of cookies in the jar’s size
#:     attribute. Also assert that, if you withdraw more than the jar’s size, withdraw should
#:     raise a ValueError. Run your tests with pytest test_jar.py.
#:
#:


# .My pseudo code approach:
#: 1.- Create a class as defined above.
#:
#: 2.- Implement the functionality the way the specs say above.
#:
#: 3.- Use the "How to test" section to test every case they want us to test.  Working backwards
#:     from the test file
#:
#:


import sys


# | ***********************************************************************************************
# | **********************           C L A S S    S E C T I O N            ************************
# | ***********************************************************************************************

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Capacity needs to be positive')
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError('Not enough room')
        self.size = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError('Not enough funds')
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError('Positive numbers only')
        self._capacity = n

    # @property
    # def size(self):
    #     return self._size

    # @size.setter
    # def size(self, n):
    #     self.size = n


# | ***********************************************************************************************
# | **********************    M A I N    P R O G R A M    S E C T I O N    ************************
# | ***********************************************************************************************

def main():
    jar = Jar(20)
    capacity = jar.capacity
    # // print(capacity)

    # // jar.size = 20
    # < Adding cookies
    jar.deposit(20)
    print(jar)

    jar.withdraw(10)
    print(jar)
    print(jar.capacity)


#
#
#
# | ***********************************************************************************************
# | **************************    F U N C T I O N     S E C T I O N    ****************************
# | ***********************************************************************************************
#
#
#
#
# | ***********************************************************************************************
# | **********************           C A L L   S E L F   M A I N           ************************
# | ***********************************************************************************************
# # > Call main ONLY when intended
if __name__ == '__main__':
    main()
