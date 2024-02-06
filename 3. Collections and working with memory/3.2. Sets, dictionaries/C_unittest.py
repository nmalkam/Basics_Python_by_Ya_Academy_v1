import unittest
from unittest import mock

from C import zaika8


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [3, 'березка елочка зайка волк березка',
                      'сосна зайка сосна елочка зайка медведь',
                      'сосна сосна сосна белочка сосна белочка']

        expected_output = ['сосна',
                           'березка',
                           'волк',
                           'елочка',
                           'медведь',
                           'белочка',
                           'зайка']

        test_input2 = [4,
                       'зайка березка',
                       'березка зайка',
                       'березка елочка березка',
                       'елочка елочка елочка']

        expected_output2 = ['березка',
                            'елочка',
                            'зайка']

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = zaika8()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = zaika8()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
