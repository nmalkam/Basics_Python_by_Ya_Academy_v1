def can_eat(p_horse: tuple, p_eat: tuple) -> bool:
    from itertools import product
    p_eat = list(p_eat)
    p_horse = (str(p_horse[0])), str(p_horse[1])
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
    if p_eat in possible_positions_horse:
        return True
    return False


assert can_eat((2, 1), (4, 2)) == True
assert can_eat((5, 5), (6, 6)) == False
