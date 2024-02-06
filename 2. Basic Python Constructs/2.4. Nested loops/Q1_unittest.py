# почему то не работает
# пишет такую ошибку
# Error running 'Python tests for Q_unittest.MyFuncTest.test_palindrome': Can't get an importable name for PyFile:Q1_unittest.py. Is it a Python file in project?
# копировал файл удалил старый НО не могу переименовать копию тоже начинает ругаться,
# всё по причине тоо что я вырезал старый оригинальный файл(ctrl + X)

import unittest
from unittest.mock import patch

from Q import palindrome

class MyFuncTest(unittest.TestCase):
    def test_palindrome(self):
        # Подготовка данных
        test_input1 = [5, 1, 2, 3, 4, 5]
        expected_output = 5

        test_input2 = [3, 123, 454, 321]
        expected_output2 = 1
        # Выполнение функции
        with patch('builtins.input', side_effect=test_input1):
            actual_output = palindrome()
        with patch('builtins.input', side_effect=test_input2):
            actual_output2 = palindrome()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')

if __name__ == '__main__':
    unittest.main()
