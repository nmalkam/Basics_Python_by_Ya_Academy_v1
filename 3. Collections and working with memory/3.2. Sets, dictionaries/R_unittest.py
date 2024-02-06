import unittest
from unittest import mock

from R import treasure_map


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [9,
                      '10 18',
                      '17 15',
                      '25 21',
                      '0 21',
                      '1 16',
                      '25 29',
                      '24 24',
                      '8 26',
                      '10 20']

        expected_output = 3

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
            actual_output = treasure_map()
        # with unittest.mock.patch('builtins.input', side_effect=test_input2):
        #     actual_output2 = treasure_map()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        # self.assertEqual(actual_output2, expected_output2)
        # print('2 passed')


if __name__ == '__main__':
    unittest.main()
