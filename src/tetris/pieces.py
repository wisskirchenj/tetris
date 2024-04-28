from tetris.coord import Coord

pieces = {
    "O": [[4, 14, 15, 5]],
    "I": [[4, 14, 24, 34], [3, 4, 5, 6]],
    "S": [[5, 4, 14, 13], [4, 14, 15, 25]],
    "Z": [[4, 5, 15, 16], [5, 15, 14, 24]],
    "L": [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
    "J": [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
    "T": [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
}


class Piece:

    def __init__(self, key: str):
        self.key = key
        self.rotation = 0
        self.col_offset = 0
        self.row_offset = 0
        self.hit_bottom = False

    def rotate(self):
        self.down()
        self.rotation = (self.rotation + 1) % len(pieces[self.key])

    def right(self):
        self.down()
        self.col_offset += 1

    def left(self):
        self.down()
        self.col_offset -= 1

    def shift_horizontal(self, offset: int):
        self.col_offset += offset

    def down(self):
        self.row_offset += 1

    def shift_vertical(self, rows: int):
        self.row_offset -= rows

    def call_by_command(self, command: str):
        getattr(self, command)()

    def get_coords(self) -> list[Coord]:
        return [Coord(index // 10 + self.row_offset, index % 10 + self.col_offset)
                for index in pieces[self.key][self.rotation]]

    def set_hit_bottom(self):
        self.hit_bottom = True

    def has_hit_bottom(self) -> bool:
        return self.hit_bottom
