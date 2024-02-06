# Класс Node представляет из себя объект,
# содержащий значение текущего элемента очереди и ссылку на следующий объект.
# В момент создания объекта ссылка на следующий объект определяется
# как пустое значение (None)
class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = self.tail = None

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.item
        self.head = self.head.next
        return temp

    def is_empty(self):
        return self.head is None


queue = Queue()
for item in range(10):
    queue.push(item)
    print('ы')
for item in range(5):
    print(queue.pop(), end=" ")
for item in range(20, 25):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")
# 0 1 2 3 4 5 6 7 8 9
# queue = Queue()
# for item in ("Hello,", "world!"):
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop())
# # Hello,
# # world!
