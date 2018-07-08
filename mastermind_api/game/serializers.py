from rest_framework import serializers
####FROM OUR APP
from game.models import Game
from guesses.serializers import GuessesSerializer

class GameSerializer(serializers.ModelSerializer):
 
    guesses = GuessesSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('id', 
               'created', 
               'codemaker', 
               'codebreaker',
               'tries_number',
               'peg_1',
               'peg_2',
               'peg_3',
               'peg_4',
               'guesses',
               'open_game')
