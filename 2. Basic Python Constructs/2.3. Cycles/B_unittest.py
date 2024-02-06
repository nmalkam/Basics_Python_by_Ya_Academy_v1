# оказывается просто забыл строку "Приехали!"..... ппц

import unittest
from unittest import mock

from B import zaika3


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ["березка елочка зайка волк березка",
                      "сосна сосна сосна елочка грибочки медведь",
                      "сосна сосна сосна белочка сосна белочка",
                      "Приехали!"]
        expected_output = 1

        test_input2 = ["зайка березка",
                       "березка зайка",
                       "березка елочка березка",
                       "Приехали!"]
        expected_output2 = 2
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = zaika3()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = zaika3()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
