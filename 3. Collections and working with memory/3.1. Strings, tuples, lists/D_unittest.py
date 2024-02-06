import unittest
from unittest import mock

from D import data_cleaning


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        # test_input = ['Hello, world', 'Hello, @@@', '##Goodbye']
        # expected_output = ['Hello, world', 'Goodbye']

        test_input2 = ['First Message', '##Second Message',
                       '@@@Third Message##', '##Fourth Message@@@']
        expected_output2 = ['First Message', 'Second Message',
                            '@@@Third Message##']
        # Выполнение функции
        # with unittest.mock.patch('builtins.input', side_effect=test_input):
        #     actual_output = data_cleaning()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = data_cleaning()

        # Проверка результата
        # self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
