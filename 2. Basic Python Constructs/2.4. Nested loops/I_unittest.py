# оказывается просто забыл строку "Приехали!"..... ппц
import unittest
from unittest import mock

from I import big_number


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [2, 123, 234]

        expected_output = 34

        test_input2 = [3, 1234, 7234, 2323]

        expected_output2 = 473

        # test_input3 = [5, 19683, 39, 768, 96, 102]

        # expected_output3 = 3
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = big_number()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = big_number()
        # with unittest.mock.patch('builtins.input', side_effect=test_input3):
        #     actual_output3 = big_number()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')
        # self.assertEqual(actual_output3, expected_output3)
        # print('3 passed')


if __name__ == '__main__':
    unittest.main()
