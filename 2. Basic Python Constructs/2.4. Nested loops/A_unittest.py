#  не работает
import unittest
from unittest import mock

from A import multiplication_table


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = 3
        expected_output = '1 2 3\n2 4 6\n3 6 9'

        test_input2 = 5
        expected_output2 = "Ёлочка, гори!"
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = multiplication_table()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = multiplication_table()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        # self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
