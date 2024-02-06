def can_eat(p_horse: tuple, p_eat: tuple) -> bool:
    from itertools import combinations_with_replacement, product
    """для решения задачи можно создать множество значений возможных
    позиций коня, если p_eat есть в данном множестве то True """
    p_horse = ("2", "1")
    horse_step = ['+2', '+1', '-2', '-1']
    POSITIONS = list(product(p_horse, horse_step, repeat=2))
    numbers_right_positions_horse = [5, 7, 21, 23,
                                     12, 14, 28, 30]
    p_p_h = []
    for index in numbers_right_positions_horse:
        p_p_h.append(POSITIONS[index])
    possible_positions_horse = []
    for a, b, c, d in p_p_h:
        pos = [eval(a + b), eval(c + d)]
        if pos[0] in range(1, 9) and pos[1] in range(1, 9):
            possible_positions_horse.append(pos)
        # for a, b, c, d, in p_p_h if eval(a + b) in range (1, 9) and eval(c + d) in range (1, 9)
        # if x, y in pos
    # for p in POSITIONS:
    if p_eat in possible_positions_horse:
        return True
    return False
    # horse_step = [('+2', '+1'), ('+2', '-1'), ('-2', '+1'), ('-2', '+1'),
    #               ('+1', '+2'), ('+1', '-2'), ('-1', '+2'), ('-1', '-2')]
    # all_positions = list(combinations_with_replacement(range(1, 9), 2))

    # if (p_horse[1] + 2 in range(1, 9) and p_horse[2] + 1 in range(1, 9)) or (
    #     p_horse[1] + 2 in range(1, 9) and p_horse[2] - 1 in range(1, 9)) or (
    #     p_horse[1] - 2 in range(1, 9) and p_horse[2] + 1 in range(1, 9)) or (
    #     p_horse[1] - 2 in range(1, 9) and p_horse[2] - 1 in range(1, 9)) or (
    #     p_horse[1] + 1 in range(1, 9) and p_horse[2] + 2 in range(1, 9)) or (
    #     p_horse[1] + 1 in range(1, 9) and p_horse[2] - 2 in range(1, 9)) or (
    #     p_horse[1] - 1 in range(1, 9) and p_horse[2] + 2 in range(1, 9)) or (
    #     p_horse[1] - 1 in range(1, 9) and p_horse[2] - 2 in range(1, 9)):
    #     possible_positions_horse.append(1)



assert can_eat((2, 1), (4, 2)) == True
assert can_eat((5, 5), (6, 6)) == False
