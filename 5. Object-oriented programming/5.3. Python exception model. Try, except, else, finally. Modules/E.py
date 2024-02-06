def merge(sequence_1, sequence_2):
    if type(sequence_1) in [int, float, bool] or type(sequence_2) in [int, float, bool]:
        raise StopIteration
    # type_first_seq_1 = type(sequence_1[0])
    # type_first_seq_2 = type(sequence_2[0])
    if all(type(item) is not type(sequence_1[0]) for item in sequence_1):
        raise TypeError
    elif all(type(item) is not type(sequence_2[0]) for item in sequence_2):
        raise TypeError
    elif sequence_1 != sorted(sequence_1) and sequence_2 != sorted(sequence_2):
        raise ValueError
    else:
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
        return tuple(sequence)


# print(*merge(35, (1, 2, 3)))
# print(*merge(35, (1, 2, 3)))
# Вызвано исключение StopIteration
print(*merge([3, 2, 1], range(10)))
# Вызвано исключение ValueError
