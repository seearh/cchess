import numpy as np

NEW_BOARD = {
    'R': {
        'General': (0,4),
        'Guard': [(0,3), (0,5)],
        'Elephant': [(0,2), (0,6)],
        'Horse': [(0,1), (0,7)],
        'Car': [(0,0), (0,8)],
        'Cannon': [(2,1), (2,7)],
        'Troop': [(3,0), (3,2), (3,4), (3,6), (3,8)]
    },
    'G': {
        'General': (9,4),
        'Guard': [(9,3), (9,5)],
        'Elephant': [(9,2), (9,6)],
        'Horse': [(9,1), (9,7)],
        'Car': [(9,0), (9,8)],
        'Cannon': [(7,1), (7,7)],
        'Troop': [(6,0), (6,2), (6,4), (6,6), (6,8)]
    }
}

PIECES_MAP = {
    'R': {
        'General': '帥',
        'Guard': '仕',
        'Elephant': '相',
        'Horse': '傌',
        'Car': '俥',
        'Cannon': '炮',
        'Troop': '兵'
    },
    'G': {
        'General': '將',
        'Guard': '士',
        'Elephant': '象',
        'Horse': '馬',
        'Car': '車',
        'Cannon': '砲',
        'Troop': '卒'
    }
}

class CChessBoardState():
    def __init__(self, pieces: dict = NEW_BOARD, turn: str = 'R'):
        for color in pieces.keys():
            for piece, coord in pieces[color].items():
                setattr(self, color + piece, coord)
        self.turn = turn

    def __repr__(self):
        return_str = ('{:^3}'*9 + '\n') * 5 \
            + '{:^32}\n'.format('楚河汉界') \
            + ('{:^3}'*9 + '\n') * 5
        format_tuple = np.full((10,9), '十')
        for attr, val in vars(self).items():
            if attr[0] in ('R', 'G'):
                if isinstance(val, list):
                    for coord in val:
                        format_tuple[coord] = PIECES_MAP[attr[0]][attr[1:]]
                else:
                    format_tuple[val] = PIECES_MAP[attr[0]][attr[1:]]
        return return_str.format(*format_tuple.ravel())

    def valid_moves(self):
        {attr, val for attr, val in vars(self).items() if attr[0] == self.turn}
        return {piece: moves}

    def general_moves(self):
        coord = self.getattr(self.turn + 'General', None)
        return [(x+1,y), (x-1,y), (x,y+1), (x,y-1) for x, y in coord]