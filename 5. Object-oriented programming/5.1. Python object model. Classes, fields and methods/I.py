class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            return 'List is empty'

    def is_empty(self):
        return len(self.queue) == 0


# queue = Queue()
# for item in range(10):
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop(), end=" ")
# 0 1 2 3 4 5 6 7 8 9
queue = Queue()
for item in ("Hello,", "world!"):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop())
print(queue.pop())
# Hello,
# world!
