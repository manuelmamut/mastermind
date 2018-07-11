from django.test import TestCase, Client
from game.models import Game
from guesses.models import Guess
from django.urls import reverse

class TestGameViews(TestCase):
    """Test for the app endpoints"""

    def setUp(self):
        self.client = Client()

        self.first_game = Game.objects.create(
                            codemaker="User 1",
                            codebreaker="User 2",
                            peg_1="R",
                            peg_2="R",
                            peg_3="R",
                            peg_4="R")

        self.first_guess = Guess.objects.create(
                            game = self.first_game,
                            peg_1="R",
                            peg_2="R",
                            peg_3="R",
                            peg_4="Y")

        self.guess_data ={ 
            "game": self.first_game.id,
            "peg_1": "R",
            "peg_2": "Y",
            "peg_3": "Y",
            "peg_4": "R",
        }

        self.right_guess_data ={ 
            "game": self.first_game.id,
            "peg_1": "R",
            "peg_2": "R",
            "peg_3": "R",
            "peg_4": "R",
        }

    def test_can_get_guess_list(self):
        """We check if the setUp guess is in the list returned"""

        url = reverse("guesses:guesses-list")
        response = self.client.get(url)
        assert response.status_code == 200, \
            "Wanted 200 got: {}" . format(
                response.status_code)
        assert Guess.objects.count() == 1, \
            "We must have one guess"
     

    def test_create_new_guess(self):
        """ Here we check if the new guess is created, since we already created one in the setUP
        we compare with a second game being created, also check if the guesses list for the specific
        game grows to two also"""

        url = reverse("guesses:guesses-list")
        response = self.client.post(url, self.guess_data)
        assert response.status_code == 201, \
            "Wanted 201 got: {}" . format(
                response.status_code)
        assert Guess.objects.count() == 2, \
            "Created new guess, we must have two guesses, got {}".format(
                Guess.objects.count())


    def test_game_gets_closed_right_guess(self):
        """After a right guess the open_game attribute should change to False"""

        url = reverse("guesses:guesses-list")
        response = self.client.post(url, self.right_guess_data)
        assert response.status_code == 201, \
            "Wanted 201 got: {}" . format(
                response.status_code)
        self.first_game.refresh_from_db() #We need a fresh object that has been 
                                          #changed by the save method of a right new guess
        assert self.first_game.open_game == False, \
            "Wanted False after right guess, got: {}" . format(
                self.first_game.open_game)


    def test_game_gets_closed_after_maximum_tries(self):
        """After a right guess the open_game attribute should change to False"""

        url = reverse("guesses:guesses-list")
        max_tries = self.first_game.tries_number
        for i in range(max_tries):
            response = self.client.post(url, self.guess_data)
        self.first_game.refresh_from_db() #We need a fresh object that has been 
                                          #changed by the save method of a new guess 
                                          #when maximum_tries is reached
        assert Guess.objects.filter(game = self.first_game).count() == 12, \
            "Max tries number is 12, got: {}" . format(
                Guess.objects.filter(game = self.first_game).count()) 
        assert self.first_game.open_game == False, \
            "Wanted False after right guess, got: {}" . format(
                self.first_game.open_game)
