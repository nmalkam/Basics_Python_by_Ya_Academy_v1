# оказывается просто забыл строку "Приехали!"..... ппц
import unittest
from unittest import mock

from H import maximum_amount


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        # test_input = [2, 'Аня', 123, 'Боря', 234]

        # expected_output = 'Боря'

        test_input2 = [3, 'Аня', 1234, 'Боря', 234, 'Ваня', 2323]

        expected_output2 = 'Ваня'

        # test_input3 = [5, 19683, 39, 768, 96, 102]
        # expected_output3 = 3
        # Выполнение функции
        # with unittest.mock.patch('builtins.input', side_effect=test_input):
        #     actual_output = maximum_amount()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = maximum_amount()
        # with unittest.mock.patch('builtins.input', side_effect=test_input3):
        #     actual_output3 = maximum_amount()

        # Проверка результата
        # self.assertEqual(actual_output, expected_output)
        # print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')
        # self.assertEqual(actual_output3, expected_output3)
        # print('3 passed')


if __name__ == '__main__':
    unittest.main()
