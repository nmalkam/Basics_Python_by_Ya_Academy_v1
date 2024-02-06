import unittest
from unittest import mock

from E import promotion


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [100, 500, 333, 0]
        expected_output = 883.0

        test_input2 = [512, 499, 342.50, 0]
        expected_output2 = 1302.3

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = promotion()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = promotion()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
