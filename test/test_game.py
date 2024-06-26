import unittest
from unittest.mock import patch

from tetris.board import Board
from tetris.game import Tetris
from tetris.pieces import Piece


class TestGame(unittest.TestCase):

    @patch("builtins.print")
    @patch("builtins.input")
    def test_immediate_exit(self, mock_input, mock_print):
        mock_input.side_effect =  ["6 6", "piece", "i", "exit"]
        game = Tetris()
        game.run()
        self.assertEqual("I", game.active_piece.key)
        self.assertEqual(2, mock_print.call_count)
        expected_board_at_end = Board(6, 6)
        expected_board_at_end.insert_new(Piece("I"))
        mock_print.assert_called_with(expected_board_at_end)

    @patch("builtins.print", wraps=print)  # spy on print
    @patch("builtins.input")
    def test_real_moves(self, mock_input, mock_print):
        mock_input.side_effect = ["6 6", "piece", "t", "left", "down", "rotate", "right", "exit"]
        game = Tetris()
        game.run()
        self.assertEqual("T", game.active_piece.key)
        self.assertEqual(6, mock_print.call_count)
        expected_board_at_end = Board(6, 6)
        expected_board_at_end.grid[4][4] = "0"
        expected_board_at_end.grid[5][3] = "0"
        expected_board_at_end.grid[5][4] = "0"
        expected_board_at_end.grid[5][5] = "0"
        mock_print.assert_called_with(expected_board_at_end)
