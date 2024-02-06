import unittest
from unittest import mock

from E import pali_6


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ['Анна Боря Вова',
                      'Я последняя буква алфавита',
                      'Дед строит шалаш',
                      'Шалаш был хорош',
                      'Дед слышит топот',
                      'Ара залетел в шалаш']

        expected_output = ['Анна',
                           'Дед',
                           'шалаш']

        test_input2 = [2,
                       'печенье, сушки',
                       'чай, кофе']

        expected_output2 = [123]

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = pali_6()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = pali_6()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
