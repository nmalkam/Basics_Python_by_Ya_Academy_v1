import unittest
from unittest import mock

from L import shopping_list_2


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [3,
                      'картина, корзина, картонка',
                      'мыло, манка',
                      'молоко, хлеб, сыр']

        expected_output = ['1. картина',
                           '2. картонка',
                           '3. корзина',
                           '4. манка',
                           '5. молоко',
                           '6. мыло',
                           '7. сыр',
                           '8. хлеб']

        test_input2 = [2,
                       'печенье, сушки',
                       'чай, кофе']

        expected_output2 = [123]

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = shopping_list_2()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = shopping_list_2()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
