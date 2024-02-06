# from itertools import product
#
# mst = ['пик', 'бубен', 'треф', 'червей']
#
# mst.remove(input())
#
# nom = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
#
# for n, m in product(nom, mst):
#     print(n, m)
from itertools import product

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']

suits.remove(input())

for card, suit in product(cards, suits):
    print(card, suit)
