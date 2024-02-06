# ne robit

# import unittest
# from unittest.mock import MagicMock, patch
# from B import zaika4


# class MyFuncTest(unittest.TestCase):
#     def test_zaika4(self):
#         mock_input = MagicMock(input_value=["березка елочка зайка волк березка",
#                                             "сосна сосна сосна елочка грибочки медведь",
#                                             "сосна сосна сосна белочка сосна белочка"])
#         with patch("builtins.input", mock_input):
#             assert zaika4() == 12


import unittest
from unittest.mock import patch

from O import zaika4


class MyFuncTest(unittest.TestCase):
    def test_zaika4(self):
        # Подготовка данных
        test_input1 = [3,
                       'березка елочка зайка волк березка',
                       'сосна сосна сосна елочка грибочки медведь',
                       'сосна сосна сосна белочка сосна белочка']
        expected_output = 1

        test_input2 = [4,
                       'зайка березка',
                       'березка зайка',
                       'березка елочка березка',
                       'елочка елочка елочка']
        expected_output2 = 2
        # Выполнение функции
        with patch('builtins.input', side_effect=test_input1):
            actual_output = zaika4()
        with patch('builtins.input', side_effect=test_input2):
            actual_output2 = zaika4()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        self.assertEqual(actual_output2, expected_output2)


if __name__ == '__main__':
    unittest.main()
