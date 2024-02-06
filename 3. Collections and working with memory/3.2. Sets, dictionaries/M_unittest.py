import unittest
from unittest import mock

from M import menu_blocks


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [5,
                      'Овсянка',
                      'Рис',
                      'Суп',
                      'Манная каша',
                      'Рыба',
                      '2',
                      '3',
                      'Рис',
                      'Суп',
                      'Рыба',
                      2,
                      'Рис',
                      'Рыба']

        expected_output = ['Манная каша',
                           'Овсянка']

        test_input2 = [3,
                       'Иванов',
                       'Петров',
                       'Сидоров']

        expected_output2 = ['Однофамильцев нет']

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = menu_blocks()
        # with unittest.mock.patch('builtins.input', side_effect=test_input2):
        #     actual_output2 = menu_blocks()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        # self.assertEqual(actual_output2, expected_output2)
        # print('2 passed')


if __name__ == '__main__':
    unittest.main()
