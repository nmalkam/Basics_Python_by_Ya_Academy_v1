def can_eat(horse, cell):
    x = abs(horse[0] - cell[0])
    y = abs(horse[1] - cell[1])
    return sorted([x, y]) == [1, 2]
