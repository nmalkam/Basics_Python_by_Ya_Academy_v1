from itertools import chain, permutations, product, combinations
# трефы
# король
suit = input()
rank = input()

suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

ranks.remove(rank)

deck = list(product(ranks, suits.values()))

triplets = list(permutations(deck, 3))
new_triplets = list(combinations(deck, 3))
# что значит не меняет последовательности элементов
# a = list(chain.from_iterable(new_triplets[0]))
# b = list(chain.from_iterable('бубен'))
triplets = [triplet for triplet in new_triplets if suits[suit] in chain.from_iterable(triplet)]
# triplets.sort()

sorted_combinations = sorted(new_triplets)
for combination in sorted_combinations[:10]:
    print(', '.join(f'{rank} {suit}' for rank, suit in combination))
# почему rank, suit обращается к значениям множества внутри множества?? ведь combination это (('2', 'пик'), ('2', 'треф'), ('2', 'червей'))
