# оказывается просто забыл строку "Приехали!"..... ппц

import unittest
from unittest import mock

from D import total_amount


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [5, 1, 2, 3, 4, 5]

        expected_output = 15

        test_input2 = [3, 123, 654, 789]
        expected_output2 = 45
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = total_amount()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = total_amount()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
