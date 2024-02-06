import unittest
from unittest import mock

from K import everything_will_be_found


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ['8',
                      "учебник питона",
                      "сериал шерлок смотреть онлайн",
                      "мемы",
                      "социальная сеть",
                      "упражнения по питону",
                      "кормовые мыши для питонов",
                      "ответы егэ скачать бесплатно",
                      "компьютерные мыши",
                      "питон"]

        expected_output = ["учебник питона",
                           "упражнения по питону",
                           "кормовые мыши для питонов"]

        test_input2 = [3,
                       "Яндекс выпустил задачник по программированию",
                       "На соревнованиях по программированию победил любитель питона",
                       "Как заказать Яндекс.Такси?!",
                       "яндекс"]

        expected_output2 = ["Яндекс выпустил задачник по программированию",
                            "Как заказать Яндекс.Такси?!"]

        # test_input3 = ['аааабб', 'ииибб',
        #                'ФИНИШ']
        #
        # expected_output3 = 'а'

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = everything_will_be_found()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = everything_will_be_found()
        # with unittest.mock.patch('builtins.input', side_effect=test_input3):
        #     actual_output3 = everything_will_be_found()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')
        # self.assertEqual(actual_output3, expected_output3)
        # print('3 passed')


if __name__ == '__main__':
    unittest.main()
