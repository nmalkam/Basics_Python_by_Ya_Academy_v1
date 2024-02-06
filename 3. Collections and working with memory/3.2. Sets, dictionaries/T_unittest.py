import unittest
from unittest import mock

from T import simple_task_4


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ['2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16; 17; 18; 19; 20']

        expected_output = ['2 - 3, 5, 7, 9, 11, 13, 15, 17, 19',
                           '3 - 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20',
                           '4 - 3, 5, 7, 9, 11, 13, 15, 17, 19',
                           '5 - 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19',
                           '6 - 5, 7, 11, 13, 17, 19',
                           '7 - 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20',
                           '8 - 3, 5, 7, 9, 11, 13, 15, 17, 19',
                           '9 - 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20',
                           '10 - 3, 7, 9, 11, 13, 17, 19',
                           '11 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20',
                           '12 - 5, 7, 11, 13, 17, 19',
                           '13 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20',
                           '14 - 3, 5, 9, 11, 13, 15, 17, 19',
                           '15 - 2, 4, 7, 8, 11, 13, 14, 16, 17, 19',
                           '16 - 3, 5, 7, 9, 11, 13, 15, 17, 19',
                           '17 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20',
                           '18 - 5, 7, 11, 13, 17, 19',
                           '19 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20',
                           '20 - 3, 7, 9, 11, 13, 17, 19', ]

        test_input2 = ['7; 2; 2; 12; 14; 7; 2; 49']

        expected_output2 = ['2 - 7, 49',
                            '7 - 2, 12',
                            '12 - 7, 49',
                            '49 - 2, 12']

        # Выполнение функции
        # with unittest.mock.patch('builtins.input', side_effect=test_input):
        #     actual_output = simple_task_4()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = simple_task_4()

        # Проверка результата
        # self.assertEqual(actual_output, expected_output)
        # print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
