def func():
    x = int('Hello, world!')
# ValueError


def func():
    x = int(input('Введи: '))


def func():
    x = '2' + 2


try:
    func()
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except SystemError:
    print('SystemError')
else:
    print('No Exceptions')
