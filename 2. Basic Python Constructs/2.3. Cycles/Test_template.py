# t_room, t_cond = map(int, input().split())
import unittest
from unittest import mock

from A import elochka_gori


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ["Один!", "Два!", "Три!"]
        expected_output = "Ёлочка, гори!"

        test_input2 = ["Десять!", "Девять!", "Раз!", "Три!"]
        expected_output2 = "Ёлочка, гори!"
        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = elochka_gori()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = elochka_gori()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
