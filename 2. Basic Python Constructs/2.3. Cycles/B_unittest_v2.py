# ne robit

# import unittest
# from unittest.mock import MagicMock, patch
# from B import zaika3


# class MyFuncTest(unittest.TestCase):
#     def test_zaika3(self):
#         mock_input = MagicMock(input_value=["березка елочка зайка волк березка",
#                                             "сосна сосна сосна елочка грибочки медведь",
#                                             "сосна сосна сосна белочка сосна белочка"])
#         with patch("builtins.input", mock_input):
#             assert zaika3() == 12


import unittest
from unittest.mock import MagicMock, patch

from B import zaika3


class MyFuncTest(unittest.TestCase):
    def test_zaika3(self):
        # Подготовка данных
        mock_input = MagicMock(input_value=["березка елочка зайка волк березка",
                                            "сосна сосна сосна елочка грибочки медведь",
                                            "сосна сосна сосна белочка сосна белочка"])
        expected_output = 1

        # test_input2 = ["зайка березка"]
        # expected_output2 = 1
        # Выполнение функции
        with patch('builtins.input', side_effect=mock_input):
            actual_output = zaika3()
        # with unittest.mock.patch('builtins.input', side_effect=test_input2):
        #     actual_output2 = zaika3()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        # self.assertEqual(actual_output2, expected_output2)


#
if __name__ == '__main__':
    unittest.main()
