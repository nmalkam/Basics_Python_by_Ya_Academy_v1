# Вариант с удалением элементов из списков

def merge(sequence_1, sequence_2):
    queue_1 = list(sequence_1)
    queue_2 = list(sequence_2)
    sequence = []
    while queue_1 and queue_2:
        if queue_1[0] > queue_2[0]:
            sequence.append(queue_2.pop(0))
        else:
            sequence.append(queue_1.pop(0))
    sequence.extend(queue_2)
    sequence.extend(queue_1)
    return tuple(sequence)
# Вариант с индексами элементов списков


# def merge(sequence_1, sequence_2):
#     pos1 = 0
#     pos2 = 0
#     sequence = []
#     while pos1 < len(sequence_1) and pos2 < len(sequence_2):
#         if sequence_1[pos1] > sequence_2[pos2]:
#             sequence.append(sequence_2[pos2])
#             pos2 += 1
#         else:
#             sequence.append(sequence_1[pos1])
#             pos1 += 1
#     sequence.extend(sequence_1[pos1:])
#     sequence.extend(sequence_2[pos2:])
#     return tuple(sequence)


assert merge((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)
assert merge((1, 91), (3, 4, 90)) == (1, 3, 4, 90, 91)
assert merge((7, 12), (1, 9, 50)) == (1, 7, 9, 12, 50)
print('OKAY')
