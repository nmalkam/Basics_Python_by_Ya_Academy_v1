import unittest
from unittest import mock

from F import porridge_eater_3


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [3,
                      2,
                      'Васильев',
                      'Петров',
                      'Васечкин',
                      'Иванов',
                      'Михайлов']
# 'Таких нет'
        expected_output = ['Васечкин',
                           'Васильев',
                           'Иванов',
                           'Михайлов',
                           'Петров']

        test_input2 = [3,
                       3,
                       'Иванов',
                       'Петров',
                       'Васечкин',
                       'Иванов',
                       'Петров',
                       'Васечкин',
                       ]

        expected_output2 = 'Таких нет'

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = porridge_eater_3()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = porridge_eater_3()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
