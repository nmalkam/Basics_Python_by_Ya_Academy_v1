import unittest
from unittest import mock

from P import news_announcement_2


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = [144, 5,
                      'Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана',
                      'Благодаря ей он может регулировать громкость,',
                      'показывая расстояние между большим и указательным пальцами.',
                      'Для этого ему понадобилась веб-камера, знания Python и',
                      'библиотека для работы с компьютерным зрением.']

        expected_output = [
            'Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана',
            'Благодаря ей он может регулировать громкость...']

        test_input2 = [121, 5,
                       'Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана',
                       'Благодаря ей он может регулировать громкость,',
                       'показывая расстояние между большим и указательным пальцами.',
                       'Для этого ему понадобилась веб-камера, знания Python и',
                       'библиотека для работы с компьютерным зрением.']

        expected_output2 = ['Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана',
                            'Благодаря ей он может...']

        test_input3 = [10,
                       2,
                       12345,
                       123]

        expected_output3 = [12345,
                            123]  # 12345, 12...

        # test_input4 = ['аааабб', 'ииибб',
        #                'ФИНИШ']
        #
        # expected_output4 = 'а'

        # Выполнение функции
        # with unittest.mock.patch('builtins.input', side_effect=test_input):
        #     actual_output = news_announcement_2()
        # with unittest.mock.patch('builtins.input', side_effect=test_input2):
        #     actual_output2 = news_announcement_2()
        with unittest.mock.patch('builtins.input', side_effect=test_input3):
            actual_output3 = news_announcement_2()

        # Проверка результата
        # self.assertEqual(actual_output, expected_output)
        # print('1 passed')
        # self.assertEqual(actual_output2, expected_output2)
        # print('2 passed')
        self.assertEqual(actual_output3, expected_output3)
        print('3 passed')


if __name__ == '__main__':
    unittest.main()
