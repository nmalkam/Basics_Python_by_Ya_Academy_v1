def ORANGE(segment):
    import time
    # import resource
    time_start = time.perf_counter()

    print('А Б В')
    n_list = []
    for a in range(1, segment):
        for b in range(1, segment):
            for v in range(1, segment):
                if a + b + v == segment:
                    n_list.append([a, b, v])
                    # n_list.append(str(a) + ' ' + str(b) + ' ' + str(v))
    # print(sorted(n_list))
    # return sorted(n_list)
    result = ''
    for item in sorted(n_list):
        for num in item:
            result += str(num) + ' '
        print(result[:-1])
        result = ''

    time_elapsed = (time.perf_counter() - time_start)
    # memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
    print("%5.1f secs " % time_elapsed)  # , memMb))   %5.1f MByte


#     # while a != segment - 1:
#     if sum(map(int, str(i))) == segment:
#         n_list.append(str(a)+' '+str(b))
#
#     # for num in range(1, segment + 1):
#     #     v = segment - 2
#     #     print(f'{a} {b} {v}')
# # else:
#     for item in n_list:
#         answer.append(item)
#         # print(item)
#     print(answer)

print()
# assert ORANGE(600) == ["1 1 1"]
assert ORANGE(100) == ["1 1 1"]
assert ORANGE(3) == ["1 1 1"]
assert ORANGE(5) == ["1 1 3", "1 2 2", "1 3 1", "2 1 2", "2 2 1", "3 1 1"]
print("У! ЗАКОММЕНТИРУЙ СТРОКУ!!")


def main():
    segment = int(input())
    ORANGE(segment)


if __name__ == '__main__':
    main()

# Примечания            СДЕЛАЙ ТЕСТЫ ДЛЯ ЭТИХ СЛУЧАЕВ
# Каждому ребёнку должна достаться хотя бы одна долька апельсина.
# Ни одной дольки не должно остаться.
# Выводить варианты в порядке увеличения количества долек у Ани, затем Бори и затем уже Вовы.
