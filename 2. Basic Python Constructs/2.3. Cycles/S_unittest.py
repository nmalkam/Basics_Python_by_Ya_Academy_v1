import unittest
from unittest import mock

from S_v2 import guessing_game


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ['Меньше', 'Меньше', 'Больше', 'Меньше', 'Больше', 'Меньше',
                      'Больше', 'Больше', 'Больше', 'Угадал!']
        expected_output = [250, 188, 172, 171, 170, 168, 164, 156, 125]

        test_input2 = [512, 499, 342.50, 0]
        expected_output2 = 1302.3

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = guessing_game()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = guessing_game()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        # self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
