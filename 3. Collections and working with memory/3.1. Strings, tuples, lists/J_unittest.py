import unittest
from unittest import mock

from J import frequency_analysis_at_minimum_prices


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ['Баобаб', 'Белка', 'Бобы', 'ФИНИШ']

        expected_output = 'б'

        test_input2 = ['Финики Фокачча Зайка', 'Филин Фосфор Светофор',
                       'Фехтовальщик Форма', 'ФИНИШ']

        expected_output2 = 'ф'

        test_input3 = ['аааабб', 'ииибб',
                       'ФИНИШ']

        expected_output3 = 'а'

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = frequency_analysis_at_minimum_prices()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = frequency_analysis_at_minimum_prices()
        with unittest.mock.patch('builtins.input', side_effect=test_input3):
            actual_output3 = frequency_analysis_at_minimum_prices()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')
        self.assertEqual(actual_output3, expected_output3)
        print('3 passed')

if __name__ == '__main__':
    unittest.main()
