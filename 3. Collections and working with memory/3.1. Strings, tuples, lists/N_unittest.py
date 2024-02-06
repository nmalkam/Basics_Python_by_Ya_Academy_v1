import unittest
from unittest import mock

from M import mass_exponentiation


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [2, 3, 4]

        expected_output = [8, 27, 64]

        test_input2 = [5, 222222, 22222, 2222, 222, 22, 2]

        expected_output2 = [49382617284, 493817284, 4937284, 49284, 484]

        # test_input3 = ['аааабб', 'ииибб',
        #                'ФИНИШ']
        #
        # expected_output3 = 'а'

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = mass_exponentiation()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = mass_exponentiation()
        # with unittest.mock.patch('builtins.input', side_effect=test_input3):
        #     actual_output3 = mass_exponentiation()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')
        # self.assertEqual(actual_output3, expected_output3)
        # print('3 passed')


if __name__ == '__main__':
    unittest.main()
