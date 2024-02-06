import unittest
from unittest import mock

from H import porridge_eater_4


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [5,
                      'Васильев манная',
                      'Петров манная',
                      'Васечкин манная',
                      'Иванов овсяная',
                      'Михайлов овсяная',
                      'манная']
        # 'Таких нет'
        expected_output = ['Васечкин',
                           'Васильев',
                           'Петров']

        test_input2 = [3,
                       'Иванов манная овсяная',
                       'Петров манная овсяная',
                       'Васечкин манная овсяная',
                       'манная']

        expected_output2 = 'Таких нет'

        # Выполнение функции
        # with unittest.mock.patch('builtins.input', side_effect=test_input):
        #     actual_output = porridge_eater_4()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = porridge_eater_4()

        # Проверка результата
        # self.assertEqual(actual_output, expected_output)
        # print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
