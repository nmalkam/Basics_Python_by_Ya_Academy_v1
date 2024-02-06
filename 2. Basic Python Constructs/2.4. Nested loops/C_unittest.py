# Оказывается просто забыл строку "Приехали!"..... ппц

import unittest
from unittest import mock

from C_v3_SK import christmas_mood


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = 14
        expected_output = ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14']

        test_input2 = 6
        expected_output2 = ['1', '2 3', '4 5 6']

        # test_input3 = 10
        # expected_output2 = ['1', '2 3', '4 5 6']
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = christmas_mood()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = christmas_mood()

        # Проверка результата
        # self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
