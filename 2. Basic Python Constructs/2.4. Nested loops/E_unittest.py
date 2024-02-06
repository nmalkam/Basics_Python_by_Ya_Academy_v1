# оказывается просто забыл строку "Приехали!"..... ппц
import unittest
from unittest import mock

from E import zaika5


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [3,
                      'березка', 'елочка', 'зайка', 'волк', 'березка', 'ВСЁ',
                      'сосна', 'сосна', 'сосна', 'елочка', 'грибочки', 'медведь', 'ВСЁ',
                      'сосна', 'сосна', 'сосна', 'белочка', 'сосна', 'белочка', 'ВСЁ']

        expected_output = 1

        test_input2 = [4,
                       'зайка', 'березка', 'ВСЁ',
                       'зайка', 'зайка', 'ВСЁ',
                       'березка', 'елочка', 'березка', 'ВСЁ',
                       'елочка', 'елочка', 'елочка', 'ВСЁ']
        expected_output2 = 2
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = zaika5()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = zaika5()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
