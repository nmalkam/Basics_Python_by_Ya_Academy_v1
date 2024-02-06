# ['A', 'C', 'E', 'G'], ['1', '3']
# ['B', 'D', 'F', 'H'], ['2']
# ['B', 'D', 'F', 'H'], ['8', '6']
# ['A', 'C', 'E', 'G'], ['7']
# from itertools import product
# print(list(product(['B', 'D', 'F', 'H'], ['2'])))


class Checkers:
    board = {}

    def __init__(self):
        for row in '87654321':
            for col in 'ABCDEFGH':
                # if tuple([col, row]) in product(['8', '3'], ['A', 'C', 'E', 'G']):
                # if ('A', '8') in [('A', '8'), ('A', '3'), ('C', '8'), ('C', '3'),
                #                   ('E', '8'), ('E', '3'), ('G', '8'), ('G', '3')]:
                # print(list(product(['A', 'C', 'E', 'G'], ['1', '3'])))
                # print(tuple([col, row]))
                # print(col + row)

                # print(list(product(['7'], ['A', 'C', 'E', 'G'])))
                if tuple([col, row]) in [('A', '1'), ('A', '3'), ('C', '1'), ('C', '3'),
                                         ('E', '1'), ('E', '3'), ('G', '1'), ('G', '3')]:
                    self.board[col + row] = 'W'
                elif tuple([col, row]) in [('B', '2'), ('D', '2'), ('F', '2'), ('H', '2')]:
                    self.board[col + row] = 'W'
                elif tuple([col, row]) in [('B', '8'), ('B', '6'), ('D', '8'), ('D', '6'),
                                           ('F', '8'), ('F', '6'), ('H', '8'), ('H', '6')]:
                    self.board[col + row] = 'B'
                elif tuple([col, row]) in [('A', '7'), ('C', '7'), ('E', '7'), ('G', '7')]:
                    self.board[col + row] = 'B'
                else:
                    self.board[col + row] = 'X'

    def move(self, f: str, t: str):  # from - to
        self.board[t] = self.board[f]
        self.board[f] = 'X'

    def get_cell(self, p: str) -> str:  # position
        # pass
        return self.board[p]


class Cell:
    def __init__(self):
        pass

    def status(self):
        # pass
        return Checkers.board


checkers = Checkers()
for row in '87654321':
    for col in 'ABCDEFGH':
        # print(checkers.get_cell(col + row), end='')
        print(checkers.get_cell(col + row).status(), end='')
    print()
# XBXBXBXB
# BXBXBXBX
# XBXBXBXB
# XXXXXXXX
# XXXXXXXX
# WXWXWXWX
# XWXWXWXW
# WXWXWXWX
print()
print()
checkers = Checkers()
checkers.move('C3', 'D4')
checkers.move('H6', 'G5')
for row in '87654321':
    for col in 'ABCDEFGH':
        # pass
        # print(checkers.get_cell(col + row), end='')
        print(checkers.get_cell(col + row).status(), end='')
    print()
# XBXBXBXB
# BXBXBXBX
# XBXBXBXX
# XXXXXXBX
# XXXWXXXX
# WXXXWXWX
# XWXWXWXW
# WXWXWXWX
