def my_func(s_P, s_V, s_T):
    # i = 0
    # count = 1
    winner = {s_P: "Петя", s_V: "Вася", s_T: "Толя"}
    a = sorted(list(winner.keys()), reverse=True)
    # print(a)
    # print(f"{count}. {winner[_]}")
    print(f"          {winner[a[0]]}        ")
    print(f"  {winner[a[1]]}               ")
    print(f"                  {winner[a[2]]}")
    print("   II      I      III")


assert my_func(10, 5, 7) ==  "Петя, Толя, Вася"
# assert my_func(5, 7, 10) == 115
# print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    s_P = int(input())
    s_V = int(input())
    s_T = int(input())
    my_func(s_P, s_V, s_T)


if __name__ == '__main__':
    main()

#         Петя
# Толя
#                 Вася
#  II      I      III
