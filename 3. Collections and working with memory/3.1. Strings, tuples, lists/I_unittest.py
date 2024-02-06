import unittest
from unittest import mock

from I import no_comments


class MyFuncTest(unittest.TestCase):
    def test_my_func(self):
        # Подготовка данных
        test_input = ['# Моя первая супер-пупер программа',
                      'print("What is your name?") #  Как тебя зовут?',
                      'name = input() #  Сохраняем имя',
                      'print(f"Hello, {name}!") #  Здороваемся# Конец моей супер-пупер программы']

        expected_output = ['print("What is your name?")', 'name = input()',
                           'print(f"Hello, {name}!")']

        test_input2 = ['# Мой первый цикл',
                       'for i in range(10): # Считаем до 10',
                       '    print(i) # выводим число']

        expected_output2 = ['for i in range(10):', '    print(i)']

        # Выполнение функции
        with unittest.mock.patch('builtins.input', side_effect=test_input):
            actual_output = no_comments()
        with unittest.mock.patch('builtins.input', side_effect=test_input2):
            actual_output2 = no_comments()

        # Проверка результата
        self.assertEqual(actual_output, expected_output)
        print('1 passed')
        self.assertEqual(actual_output2, expected_output2)
        print('2 passed')


if __name__ == '__main__':
    unittest.main()
