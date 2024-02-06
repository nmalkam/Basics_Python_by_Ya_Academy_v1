import itertools

suit_main = input()
# suit_main = 'трефы'
suits = ['пик', 'бубен', 'треф', 'червей']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
if suit_main == 'трефы':
    suits.remove('червей')
    suit_main = 'треф'
elif suit_main == 'черви':
    suits.remove('треф')
    suit_main = 'червей'
elif suit_main == 'пики':
    suit_main = 'пик'
else:
    suit_main = 'бубен'
cards.remove(input())
# cards.remove('король')
count = 0
lst_deck = []
res = []
values = list(itertools.product(sorted(cards), sorted(suits)))
for card, suit in itertools.product(sorted(cards), sorted(suits)):
    lst_deck.append(' '.join([card, suit]))
for i in itertools.permutations(lst_deck, 3):
    for j in i:
        if suit_main in j:
            res.append(i)
            break

while count != 10:
    print(', '.join(res[count]))
    count += 1


suit = input().strip()
