# Реализуйте стек со следующими методами:
# 1. push(item), добавляющий элемент на вершину стека
# 2. pop(), удаляющий самый верхний элемент стека и возвращающий его.
# Если в стеке нет элементов, метод должен выбросить ошибку или вернуть null.
# Каждый метод должен иметь постоянную временную сложность.
"""---"""
# Ввод
# 7 2 3 * -   -> 2*3=6 -> 7-6=1
# Вывод
# 1
# Ввод
# 10 15 - 7 * -> 10-15=-5 -> -5*7=-35
# Вывод
# -35


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed


s = Stack()

s.push(1)
print(s)  #.pop())
