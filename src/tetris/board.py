import numpy as np

from tetris.pieces import Piece


class Board:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid: np.ndarray = self.empty()

    def empty(self):
        return np.full((self.rows, self.cols), '-')

    def __str__(self):
        return "\n" + "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)

    def __eq__(self, other):
        return np.array_equal(self.grid, other.grid) and self.rows == other.rows and self.cols == other.cols

    def correct_boundaries(self, piece: Piece):
        coords = piece.get_coords()
        if any(coord.col < 0 for coord in coords):  # left
            piece.shift_horizontal(abs(min(coord.col for coord in coords)))
        elif any(coord.col >= self.cols for coord in coords):  # right
            piece.shift_horizontal(min(self.rows - 1 - coord.col for coord in coords))
        if any(coord.row == self.rows - 1 for coord in coords):  # bottom
            piece.set_hit_bottom()
            below_bottom = max(coord.row for coord in piece.get_coords()) - self.rows + 1
            piece.shift_vertical(below_bottom)  # necessary, if piece is rotated and goes through bottom

    def position(self, piece: Piece):
        self.grid = self.empty()
        self.correct_boundaries(piece)
        for coord in piece.get_coords():
            self.grid[coord.row][coord.col] = '0'
