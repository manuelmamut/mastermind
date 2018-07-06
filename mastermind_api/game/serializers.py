from rest_framework import serializers
####FROM OUR APP
from game.models import Game

class GameSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Game
        fields = ('id', 
               'created', 
               'codemaker', 
               'codebreaker',
               'tries_number',
               'open_game')
