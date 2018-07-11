from django.test import TestCase
from guesses.models import Guess
from game.models import Game


class TestGuess(TestCase):
    """This is the test for the Guess model"""

    def setUp(self):
        new_game = Game.objects.create(codemaker="User 1",
                            codebreaker="User 2",
                            peg_1="R",
                            peg_2="R",
                            peg_3="R",
                            peg_4="R")

        self.game_id = new_game.id

        Guess.objects.create(game = new_game,
                            peg_1="R",
                            peg_2="Y",
                            peg_3="R",
                            peg_4="R")


    def test_game_info_creation(self):
        """Here we test the creation of a new guess, and we confirm the recommendation
        white_pegs and black_pegs must be saved with the guess object"""

        guess = Guess.objects.all()[0]
        self.assertEqual(guess.game_id, self.game_id )
        self.assertEqual(guess.peg_1, "R")
        self.assertEqual(guess.peg_2, "Y")
        self.assertEqual(guess.peg_3, "R")
        self.assertEqual(guess.peg_4, "R")
        self.assertEqual(guess.black_pegs, 3)
        self.assertEqual(guess.white_pegs, 0)
