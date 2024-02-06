import unittest
from unittest import mock

from M import smallest_name


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [3, 'Вова', 'Аня', 'Боря']
        expected_output = 'Аня'

        test_input2 = [4, 'Толя', 'Коля', 'Вася', 'Юля']
        expected_output2 = 'Вася'

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = smallest_name()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = smallest_name()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
