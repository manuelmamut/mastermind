from django.test import TestCase
from ..models import Game


class TestGame(TestCase):
    """This is the test for the Game model"""

    def setUp(self):
        Game.objects.create(codemaker="User 1",
                            codebreaker="User 2",
                            peg_1="R",
                            peg_2="R",
                            peg_3="R",
                            peg_4="R")

    def test_game_info_creation(self):
        game = Game.objects.get(codemaker="User 1")
        self.assertEqual(game.codebreaker, "User 2")
        self.assertEqual(game.peg_1, "R")
        self.assertEqual(game.peg_2, "R")
        self.assertEqual(game.peg_3, "R")
        self.assertEqual(game.peg_4, "R")
        self.assertEqual(game.tries_number, 12)
        self.assertEqual(game.open_game, True)
