"""
A eDX assignment.

This file shows how modules work

"""

__author__ = 'John Rocha'
__date__ = '2024/##/##'

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


import pytest
from jar import Jar


def main():
    test_init()
    # < test_jar()


def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar2 = Jar(11)
    assert jar2.capacity == 11


def test_jar():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'

    jar.deposit(5)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'


def test_raises_initiate():
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_raises_deposit():
    with pytest.raises(ValueError):
        jar = Jar(10)
        jar.deposit(100)
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


# def test_get_input():
#     assert type(seasons3.get_input('1964-07-04')) is date

# def test_validate_date():
#     assert seasons3.validate_date('1964-07-04') == True
#     assert seasons3.validate_date('1966-07-04') == True
#     assert seasons3.validate_date('1966-074-10') == False

# def test_exception():
#     with pytest.raises(ValueError):
#         working.convert("09:00 AM - 17:00 PM")
#     with pytest.raises(ValueError):
#         working.convert("9:00 AM 5:00 PM")
#     with pytest.raises(ValueError):
#         working.convert("9:60 AM to 5:60 PM")
#     with pytest.raises(ValueError):
#         working.convert("9 AM - 5 PM")
#     with pytest.raises(ValueError):
#         working.convert("9 AM5 PM")
#     with pytest.raises(ValueError):
#         working.convert("9 AM 5 PM")
#     with pytest.raises(ValueError):
#         working.convert("9:72 to 6:30")

# def test_raises_typeError():
#     with pytest.raises(ValueError):
#         fuel.convert('2/1')
#     with pytest.raises(ValueError):
#         fuel.convert('a/b')
#     with pytest.raises(ZeroDivisionError):
#         fuel.convert('1/0')


# def test_get_the_words():
#     date1 = date(1964, 7, 4)
#     date2 = date(1964, 7, 5)
#     difference = date2 - date1
#     assert type(seasons.get_the_words(difference)) is str
# # > Call main ONLY when intended
if __name__ == '__main__':
    main()
