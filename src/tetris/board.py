import numpy as np

from tetris.coord import Coord
from tetris.pieces import Piece


class Board:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid: np.ndarray = self.empty()

    def empty(self):
        return np.full((self.rows, self.cols), '-')

    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid) + "\n"

    def __eq__(self, other):
        return np.array_equal(self.grid, other.grid) and self.rows == other.rows and self.cols == other.cols

    def check_free(self, coords: list[Coord]):
        return all(0 <= coord.col < self.cols and 0 <= coord.row < self.rows
                   and self.grid[coord.row][coord.col] == '-' for coord in coords)

    def insert_new(self, piece: Piece):
        coords = piece.get_coords()
        if not self.check_free(coords):
            return False
        self.position_piece(piece)
        return True

    def move_piece(self, piece: Piece, command: str):
        self.clear_piece(piece)
        piece.call_by_command(command)
        if not self.check_free(piece.get_coords()):
            piece.revert_command(command)
        self.position_piece(piece)
        piece.set_stuck(self.check_stuck(piece.get_coords()))
        return any(cell.row == 0 for cell in piece.get_coords())

    def position_piece(self, piece):
        for coord in piece.get_coords():
            self.grid[coord.row][coord.col] = '0'

    def clear_piece(self, piece):
        for coord in piece.get_coords():
            self.grid[coord.row][coord.col] = '-'

    def handle_break(self):
        while all(cell == '0' for cell in self.grid[-1]):
            self.grid = np.roll(self.grid, 1, axis=0)
            self.grid[0] = '-'

    def check_stuck(self, coords: list[Coord]):
        for coord in coords:
            if coord.row == self.rows - 1:
                return True
            if self.grid[coord.row + 1][coord.col] == '0' and Coord(coord.row + 1, coord.col) not in coords:
                return True
        return False
