from django.test import TestCase, Client
from game.models import Game
from django.urls import reverse

class TestGameViews(TestCase):
    """Test for the game app endpoints"""

    def setUp(self):
    
        self.client = Client()
        self.game_data = {
            "codemaker": "User 1",
            "codebreaker": "User 2",
            "peg_1": "R",
            "peg_2": "R",
            "peg_3": "R",
            "peg_4": "R",
        }

        self.first_game = Game.objects.create(
                            codemaker="User 1",
                            codebreaker="User 2",
                            peg_1="R",
                            peg_2="R",
                            peg_3="R",
                            peg_4="R")

    def test_can_get_game_list(self):
        """We check if the setUp game is in the list returned"""
    
        url = reverse("game:game-list")
        response = self.client.get(url)
        assert response.status_code == 200, \
            "Wanted 200 got: {}" . format(
                response.status_code)
        assert len(response.json()) == 1, \
            "We must have one game {} found". format( #here we confirm the number of games available 
            len(response.json()))
     

    def test_can_get_game_list(self):
        """We check if the setUp game is returned when calling to the list endpoint 
        and validating the fields in the JSON response"""

        url = reverse("game:game-detail", args=[self.first_game.id])
        response = self.client.get(url)
        assert response.status_code == 200, \
            "Wanted 200 got: {}" . format(
                response.status_code)
        assert response.json()['codemaker'] == 'User 1'
        assert response.json()['codebreaker'] == 'User 2'
        assert response.json()['peg_1'] == 'R'
        assert response.json()['peg_2'] == 'R'
        assert response.json()['peg_3'] == 'R'
        assert response.json()['peg_4'] == 'R'
     
    def test_create_new_game(self):
        """ Here we check if the new game is created, since we already created one in the setUP
        we compare with a second game being created"""
    
        url = reverse("game:game-list")
        response = self.client.post(url, self.game_data)
        assert response.status_code == 201, \
            "Wanted 201 got: {}" . format(
                response.status_code)
        assert Game.objects.count() == 2, \
            "Created new game, we must have two games"
