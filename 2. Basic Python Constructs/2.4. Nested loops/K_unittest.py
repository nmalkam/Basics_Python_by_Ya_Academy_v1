# оказывается просто забыл строку "Приехали!"..... ппц
import unittest
from unittest import mock

from K import simple_num_3


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [5, 1, 2, 3, 4, 5]

        expected_output = 3

        test_input2 = [6, 11, 13, 15, 63, 71, 51]

        expected_output2 = 3

        # test_input3 = [5, 19683, 39, 768, 96, 102]

        # expected_output3 = 3
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = simple_num_3()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = simple_num_3()
        # with unittest.mock.patch('builtins.input', side_effect=test_input3):
        #     actual_output3 = simple_num_3()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')
        # self.assertEqual(actual_output3, expected_output3)
        # print('3 passed')


if __name__ == '__main__':
    unittest.main()
