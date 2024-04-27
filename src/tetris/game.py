import numpy as np
from tetris.pieces import pieces


class Tetris:
    empty: np.ndarray = np.full((4, 4), '-')

    def __init__(self):
        self.board: np.ndarray = self.empty

    def __str__(self):
        return "\n" + "\n".join(" ".join(str(cell) for cell in row) for row in self.board)

    def rotate(self, key: str):
        for i in range(5):
            self.fill_board(pieces[key][i % len(pieces[key])])
            print(self)

    def fill_board(self, coords: list[int]):
        self.board = self.empty.copy()
        for coord in coords:
            self.board[coord // 4][coord % 4] = '0'

    def run(self):
        key = input().upper()
        print(self)
        self.rotate(key)


if __name__ == "__main__":
    Tetris().run()
