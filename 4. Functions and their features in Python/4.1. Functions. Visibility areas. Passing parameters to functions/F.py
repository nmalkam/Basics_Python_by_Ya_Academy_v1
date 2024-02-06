lst_strngs = set()


def modern_print(string: str):
    global lst_strngs
    if string not in lst_strngs:
        print(string)
    lst_strngs.add(string)

modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")
