import unittest
from unittest import mock

from J import route


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ['СЕВЕР', 2, 'ВОСТОК', 2, 'СТОП']
        expected_output = f'{2}\n{2}'

        test_input2 = ['СЕВЕР', 2, 'ЮГ', 3, 'ЗАПАД', 4, 'СТОП']
        expected_output2 = f'{-1}\n{-4}'

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = route()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = route()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
