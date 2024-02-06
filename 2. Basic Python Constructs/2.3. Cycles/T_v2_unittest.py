# перепутал с другим заданием


import unittest
from unittest import mock

from T_v2 import Blockchain


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [5, 6122802, 14406496, 15230209, 2541121, 1758741]
        expected_output = -1

        test_input2 = [5, 1865535, 13479687, 16689153, 1839958, 5214020]
        expected_output2 = 3

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = Blockchain()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = Blockchain()

        # Проверка результата
        # self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
