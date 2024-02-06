# из задания не понятно должны ли быть отсортированы списки или нет
# в примере: 9 пик, король треф, туз червей -> 9 пик, король червей, туз бубен
# (по моему мнению должен быть сперва туз пик)
from itertools import chain, permutations, product, combinations
import re

suit = input().strip()
rank = input().strip()
last_hand = input()

# a = input()
# last_hand = re.split(' |, ', a)
# copy_last_hand = last_hand[::-1]
# set_1 = []
# set_2 = []
# for _ in range(len(last_hand)):
#     set_1.append(copy_last_hand.pop())
#     if len(set_1) == 2:
#         set_2.append(tuple(set_1))
#         set_1 = []

suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

ranks.remove(rank)
deck = product(ranks, suits.values())
triplets = combinations(deck, 3)
triplets = [triplet for triplet in triplets if suits[suit] in chain.from_iterable(triplet)]
sorted_combinations = sorted(triplets)
for index, combination in enumerate(triplets):
    if [', '.join(f'{rank} {suit}' for rank, suit in combination)] == [last_hand]:
        print(', '.join(f'{rank} {suit}' for rank, suit in triplets[index + 1]))
