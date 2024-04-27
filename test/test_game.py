import unittest
from unittest.mock import patch

from tetris.game import Tetris


class TestGame(unittest.TestCase):

    @patch("builtins.print")
    def test_game(self, mock_print):
        game = Tetris()
        self.assertEqual(str(game), "\n- - - -\n- - - -\n- - - -\n- - - -")
        game.rotate("I")
        self.assertEqual(str(game), "\n- 0 - -\n- 0 - -\n- 0 - -\n- 0 - -")
        mock_print.assert_called_with(game)
        self.assertEqual(5, mock_print.call_count)
