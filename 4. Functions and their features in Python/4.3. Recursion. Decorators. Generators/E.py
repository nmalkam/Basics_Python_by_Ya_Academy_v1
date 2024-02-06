# """Накопление результата"""  plus_list = []


def result_accumulator(func):
    # global plus_list
    plus_list = []

    def code(*args, method="accumulate"):
        if "accumulate" == method:
            plus_list.append(func(*args))
            return
        elif "drop" == method:
            plus_list.append(func(*args))
            res = plus_list.copy()
            plus_list.clear()
            return res  # code(*args)

    return code


@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))
