# оказывается просто забыл строку "Приехали!"..... ппц
import unittest
from unittest import mock

from F_v2 import NOD_2_0


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [2, 12, 42]
        expected_output = 6

        test_input2 = [3, 102, 39, 768]
        expected_output2 = 3

        test_input3 = [3, 855, 255, 306]
        expected_output3 = 3

        test_input4 = [3, 126, 3724, 266]
        expected_output4 = 14

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = NOD_2_0()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = NOD_2_0()
        with unittest.mock.patch('builtins.input', side_effect=test_input3):
            actual_output3 = NOD_2_0()
        with unittest.mock.patch('builtins.input', side_effect=test_input4):
            actual_output4 = NOD_2_0()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')
        self.assertEqual(actual_output3, expected_output3)
        print('3 passed')
        self.assertEqual(actual_output4, expected_output4)
        print('4 passed')


if __name__ == '__main__':
    unittest.main()
