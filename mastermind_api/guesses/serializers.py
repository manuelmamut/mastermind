from rest_framework import serializers
####FROM OUR APP
from guesses.models import Guess
from game.models import Game

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

    def validate(self, data):
        if self.context.get('request').method == 'POST':
            game = Game.objects.get(id = data['game'].id)
            max_tries = game.tries_number
            total_guesses = len(Guess.objects.filter(game_id = game.id))
            if total_guesses < max_tries:
                print(total_guesses, max_tries)
                print(total_guesses, max_tries-1)
                if total_guesses == (max_tries - 1):
                    print('limit')
                    game.open_game = False
                    game.save()
                return data
            raise serializers.ValidationError("Maximum number of tries reached")            
                
