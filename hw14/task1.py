# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest. 

import unittest
import pytest
import doctest

def get_string_number(number: int, mod: int = 10) -> str:
    """
    Функция получает целое число, систему исчисления 
    и возвращает его  строковое представление.

    >>> get_string_number(33, 2)
    '100001'
    >>> get_string_number(33, 3)
    '1020'
    >>> get_string_number(33, 4)
    '201'
    >>> get_string_number(33, 5)
    '113'
    
    """
    result = ''
    while number != 0:
        result = str(number % mod) + result
        number //= mod
    return result


class TestCaseNumbers(unittest.TestCase):
    def test2(self):
        self.assertEqual(get_string_number(33, 2), '100001')

    def test3(self):
        self.assertEqual(get_string_number(33, 3), '1020')

    def test4(self):
        self.assertEqual(get_string_number(33, 4), '201')

    def test5(self):
        self.assertEqual(get_string_number(33, 5), '113')


def test2():
    assert get_string_number(33, 2) == '100001', 'Test 1'


def test3():
    assert get_string_number(33, 3) == '1020', 'Test 2'


def test4():
    assert get_string_number(33, 4) == '201', 'Test 3'


def test5():
    assert get_string_number(33, 5) == '113', 'Test 4'


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    unittest.main()
    pytest.main()