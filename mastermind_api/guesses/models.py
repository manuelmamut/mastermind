from django.db import models
from game.models import Game
from utils.functions import mastermindAlgorithm

# Create your models here.
class Guess(models.Model):

    RED = 'R'
    GREEN = 'G'
    YELLOW = 'Y'
    BLUE = 'B'
    PURPLE = 'P'
    ORANGE = 'O'
    COLOR = (
        (RED, 'Red'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (YELLOW, 'Yellow'),
        (PURPLE, 'Purple'),
        (ORANGE, 'Orange'),
    )


    game = models.ForeignKey(Game, related_name = 'guesses', on_delete=models.CASCADE,
                                 help_text=("This is the id of the game we want to play"))
    peg_1 = models.CharField(max_length=1, blank=True, null=False, choices = COLOR,
                                 help_text=("In mastermind you use color pegs, here we use the initial of the color \
                                            Red, Green, Blue, Yellow, Purple, Organge "))
    peg_2 = models.CharField(max_length=1, blank=True, null=False, choices = COLOR,
                                 help_text=("In mastermind you use color pegs, here we use the initial of the color \
                                            Red, Green, Blue, Yellow, Purple, Organge "))
    peg_3 = models.CharField(max_length=1, blank=True, null=False, choices = COLOR,
                                 help_text=("In mastermind you use color pegs, here we use the initial of the color \
                                            Red, Green, Blue, Yellow, Purple, Organge "))
    peg_4 = models.CharField(max_length=1, blank=True, null=False, choices = COLOR,
                                 help_text=("In mastermind you use color pegs, here we use the initial of the color \
                                            Red, Green, Blue, Yellow, Purple, Organge "))
    black_pegs = models.IntegerField(default = 0,
                                 help_text=("When we make a guess these fields are filled automatically with the tip \
                                            or reccomendations from the mastermind rules according black pegs"))
    white_pegs = models.IntegerField(default = 0,
                                 help_text=("When we make a guess these fields are filled automatically with the tip \
                                            or reccomendations from the mastermind rules according white pegs"))
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return '%s %s %s %s' % (self.peg_1, self.peg_2, self.peg_3, self.peg_4)

    def save(self, *args, **kwargs):
        """Here we make the calculation of the white and black pegs using the mastermind algorithm 
        and save those results in the model for future reference"""
        game_active = Game.objects.filter(id = self.game.id)
        riddle_list = game_active.values_list('peg_1', 'peg_2', 'peg_3', 'peg_4')
        riddle_list = [i for i in riddle_list[0]]
        guess_list = [self.peg_1, self.peg_2, self.peg_3, self.peg_4]
        self.white_pegs, self.black_pegs = mastermindAlgorithm(riddle_list, guess_list)
        if self.black_pegs == 4:
            game_closed = game_active[0]
            game_closed.open_game = False
            game_closed.save()
        super().save(*args, **kwargs)	
