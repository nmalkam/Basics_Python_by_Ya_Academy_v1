def merge_sort(nums: list):
    """В части функции merge_sort – да, вспомогательная функция merge нерекурсивна"""

    def merge(sequence_1, sequence_2):
        pos1 = 0
        pos2 = 0
        sequence = []
        while pos1 < len(sequence_1) and pos2 < len(sequence_2):
            if sequence_1[pos1] > sequence_2[pos2]:
                sequence.append(sequence_2[pos2])
                pos2 += 1
            else:
                sequence.append(sequence_1[pos1])
                pos1 += 1
        sequence.extend(sequence_1[pos1:])
        sequence.extend(sequence_2[pos2:])
        return sequence
    first = nums[:1]
    last = nums[1:]
    if len(last) > 1:
        last = merge_sort(last)
    return merge(first, last)


# assert merge_sort([]) == []
assert merge_sort([2, 1]) == [1, 2]
# assert merge_sort([1, 2, 3]) == [1, 2, 3]
# assert merge_sort([1, 1, 1]) == [1, 1, 1]
# assert merge_sort([-3, -2, -1]) == [-3, -2, -1]
# assert merge_sort([-3, -1, -2]) == [-3, -2, -1]
# assert merge_sort([3]) == [3]
# assert merge_sort([-2, 0, 3, 1, 0, 5, 3, -10]) == [-10, -2, 0, 0, 1, 3, 3, 5]
# assert merge_sort([3, 2, 1]) == [1, 2, 3]
assert merge_sort([3, 1, 5, 3]) == [1, 3, 3, 5]
print('OKAY')

# слияние вынесено в отдельную функцию.
# потому что это лучшая практика по сравнению с пихаем все в одно место.
# если не говорить только про пайтон то выделение логически обособленных кусков кода
# в функции это очень правильная практика.
# но в пайтона вызов функции очень дорогая процедура и поэтому,
# если наужна скорость, то надо все пихать в один код
# с этой точки зрения сортировка именно на пайтоне
# миллиарда элементов будет куда быстрее если все будет в одной функции
# если бы мы говорили про c++ например
# то там решение с отдельной функцией не будет заметно медленнее
