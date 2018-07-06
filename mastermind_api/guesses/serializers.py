from rest_framework import serializers
####FROM OUR APP
from guesses.models import Guess

class GuessesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Guess
        fields = ('game', 
               'created', 
               'peg_1',
               'peg_2',
               'peg_3',
               'peg_4',
               'black_pegs',
               'white_pegs')
