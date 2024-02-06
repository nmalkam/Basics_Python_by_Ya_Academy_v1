import unittest
from unittest import mock

from N import masterpiece


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [4,
                      'Яблоки',
                      'Хлеб',
                      'Варенье',
                      'Картошка',
                      3,
                      'Тосты',
                      2,
                      'Хлеб',
                      'Варенье',
                      'Яблочный Сок',
                      1,
                      'Яблоки',
                      'Яичница',
                      1,
                      'Яйца']

        expected_output = ['Тосты',
                           'Яблочный Сок']

        test_input2 = [1,
                       'хлеб',
                       1,
                       'бутерброд',
                       2,
                       'масло',
                       'хлеб']

        expected_output2 = ['Готовить нечего']

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = masterpiece()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = masterpiece()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
