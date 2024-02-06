import unittest
from unittest import mock

from S_v2 import private_property


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [3,
                      'Аня: кукла, машинка, кукла, домик',
                      'Боря: машинка, зайчик',
                      'Вова: кубики, машинка']

        expected_output = ['домик',
                           'зайчик',
                           'кубики',
                           'кукла']

        # test_input2 = ['Николай Фёдор',
        #                'Николай Женя',
        #                'Фёдор Женя',
        #                'Фёдор Илья',
        #                'Илья Фёдор',
        #                '']
        #
        # expected_output2 = ['Женя: Илья',
        #                     'Илья: Женя, Николай',
        #                     'Николай: Илья',
        #                     'Фёдор: ']

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = private_property()
        # with unittest.mock.patch('builtins.input', side_effect=test_input2):
        #     actual_output2 = private_property()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        # self.assertEqual(actual_output2, expected_output2)
        # print('2 passed')


if __name__ == '__main__':
    unittest.main()
