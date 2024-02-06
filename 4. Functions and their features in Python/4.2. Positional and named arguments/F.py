def order(*args: str) -> str | dict:
    RECIPES = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1}
    }
    global in_stock
    is_in_stock = False
    for arg in args:
        reserved_in_stock = dict(in_stock).copy()
        for key, value in RECIPES[arg].items():
            if in_stock[key] < value:
                is_in_stock = False
                break
            else:
                reserved_in_stock[key] -= value
                is_in_stock = True
        if is_in_stock:
            in_stock = reserved_in_stock
            return arg
    return 'К сожалению, не можем предложить Вам напиток'


# in_stock = {}
# in_stock = {"coffee": 1, "milk": 2, "cream": 3}
# print(order("Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
# Кофе по-венски
in_stock = {"coffee": 1, "milk": 2, "cream": 3}
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
# Эспрессо
# К сожалению, не можем предложить Вам напиток

in_stock = {"coffee": 4, "milk": 4, "cream": 0}
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))  #, end="2\n")
print(order("Капучино", "Макиато", "Эспрессо"))  #, end="3\n")
# Капучино
# Макиато
# Эспрессо
