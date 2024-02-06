import unittest
from unittest import mock

from Q_SK import friends_of_friends


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ['Иванов Петров',
                      'Иванов Сергеев',
                      'Васильев Петров',
                      'Сергеев Яковлев',
                      'Петров Кириллов',
                      'Петров Яковлев',
                      '']

        expected_output = ['Васильев: Иванов, Кириллов, Яковлев',
                           'Иванов: Васильев, Кириллов, Яковлев',
                           'Кириллов: Васильев, Иванов, Яковлев',
                           'Петров: Сергеев',
                           'Сергеев: Петров',
                           'Яковлев: Васильев, Иванов, Кириллов']

        test_input2 = ['Николай Фёдор',
                       'Николай Женя',
                       'Фёдор Женя',
                       'Фёдор Илья',
                       'Илья Фёдор',
                       '']

        expected_output2 = ['Женя: Илья',
                            'Илья: Женя, Николай',
                            'Николай: Илья',
                            'Фёдор: ']

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = friends_of_friends()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = friends_of_friends()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
