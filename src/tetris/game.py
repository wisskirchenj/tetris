from tetris.board import Board
from tetris.pieces import Piece


class Tetris:

    def __init__(self):
        self.board = None
        self.piece = None

    def user_init_game(self):
        key = input().upper()
        self.piece = Piece(key)
        board_dim = input().split()
        self.board = Board(int(board_dim[1]), int(board_dim[0]))

    def command_loop(self):
        while (command := input().lower()) != "exit":
            if not self.piece.has_hit_bottom():
                self.piece.call_by_command(command)
                self.board.position(self.piece)
            print(self.board)

    def run(self):
        self.user_init_game()
        print(self.board)  # empty board
        self.board.position(self.piece)
        print(self.board)  # board with piece
        self.command_loop()


if __name__ == "__main__":
    Tetris().run()
