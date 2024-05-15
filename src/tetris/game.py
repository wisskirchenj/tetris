from tetris.board import Board
from tetris.pieces import Piece


class Tetris:

    def __init__(self):
        self.board = None
        self.active_piece = None

    def user_init_game(self):
        board_dim = input().split()
        self.board = Board(int(board_dim[1]), int(board_dim[0]))
        print(self.board)  # empty board

    def request_piece(self):
        if not self.active_piece or self.active_piece.is_stuck():
            key = input().upper()
            self.active_piece = Piece(key)
            return self.board.insert_new(self.active_piece)

    def command_loop(self):
        while (command := input().lower()) != "exit":
            if command == "piece":
                if not self.request_piece():
                    print("\nGame Over!")
                    break
            elif command == "break":
                self.board.handle_break()
            elif self.active_piece and not self.active_piece.is_stuck():
                if self.board.move_piece(self.active_piece, command=command):
                    print(self.board)
                    print("\nGame Over!")
                    break
            print(self.board)

    def run(self):
        self.user_init_game()
        self.command_loop()


if __name__ == "__main__":
    Tetris().run()
