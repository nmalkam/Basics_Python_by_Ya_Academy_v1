def can_eat(p_horse: tuple, p_eat: tuple) -> bool:
    p_eat = (p_eat[0], p_eat[1])
    p_horse = (p_horse[0], p_horse[1])
    diff_pos = set()
    diff_pos.add(abs(p_eat[0] - p_horse[0]))
    diff_pos.add(abs(p_eat[1] - p_horse[1]))
    true = {2, 1}
    if true == diff_pos:
        return True
    return False


assert can_eat((2, 1), (4, 2)) == True
assert can_eat((5, 5), (6, 6)) == False
