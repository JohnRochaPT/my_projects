"""
     Program tests numb3rs.py functions

"""
import pytest
import numb3rs


def test_validate():
    assert numb3rs.validate('192.168.1.1') == True
    assert numb3rs.validate('1.1.1.1') == True
    assert numb3rs.validate('0.168.1.1') == True
    assert numb3rs.validate('192.168.255.1') == True
    assert numb3rs.validate('192.168.256.1') == False
    assert numb3rs.validate('192.168') == False
    assert numb3rs.validate('abc') == False
    assert numb3rs.validate('192-168-0-1') == False
#     assert fuel.convert('1/2') == 50
#     assert fuel.convert('1/3') == 33


# def test_gauge():
#     assert fuel.gauge(1) == 'E'
#     assert fuel.gauge(99) == 'F'
#     assert fuel.gauge(2) == '2%'
#     assert fuel.gauge(50) == '50%'


# def test_raises_typeError():
#     with pytest.raises(ValueError):
#         fuel.convert('2/1')
#     with pytest.raises(ValueError):
#         fuel.convert('a/b')
#     with pytest.raises(ZeroDivisionError):
#         fuel.convert('1/0')
