import unittest
from unittest import mock

from L import namesakes_2


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [6,
                      'Иванов',
                      'Петров',
                      'Сидоров',
                      'Петров',
                      'Иванов',
                      'Петров']

        expected_output = ['Иванов - 2',
                           'Петров - 3']

        test_input2 = [3,
                       'Иванов',
                       'Петров',
                       'Сидоров']

        expected_output2 = ['Однофамильцев нет']

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = namesakes_2()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = namesakes_2()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
