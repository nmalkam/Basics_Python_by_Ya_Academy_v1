# оказывается просто забыл строку "Приехали!"..... ппц

import unittest
from unittest import mock

from B import main


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = 3
        expected_output = ['''1 2 3
                           2 4 6
                           3 6 9''']

        test_input2 = 5
        expected_output2 = ['''1 2 3 4 5
                            2 4 6 8 10
                            3 6 9 12 15
                            4 8 12 16 20
                            5 10 15 20 25''']

        # print("a", "b", "c", sep="\n")

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = main()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = main()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
