import unittest
from unittest import mock

from B import twist_turn


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = 'Привет'
        expected_output = ['П', 'р', 'и', 'в', 'е', 'т']

        test_input2 = 'Питон'
        expected_output2 = ['П', 'и', 'т', 'о', 'н']
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = twist_turn()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = twist_turn()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
