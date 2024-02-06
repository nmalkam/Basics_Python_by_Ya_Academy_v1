import unittest
from unittest import mock

from A import alphabet


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [3, 'арбуз', 'барабан', 'ворона']
        expected_output = 'YES'

        test_input2 = [4, 'аист', 'вареник', 'кузнечик', 'алыча']
        expected_output2 = 'NO'
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = alphabet()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = alphabet()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
