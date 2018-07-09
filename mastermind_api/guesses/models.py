from django.db import models
from game.models import Game
from utils.functions import mastermindAlgorithm

# Create your models here.
class Guess(models.Model):

    RED = 'R'
    GREEN = 'G'
    YELLOW = 'Y'
    BLUE = 'B'
    COLOR = (
        (RED, 'Red'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (YELLOW, 'Yellow'),
    )


    game = models.ForeignKey(Game, related_name = 'guesses', on_delete=models.CASCADE)
    peg_1 = models.CharField(max_length=1, blank=True, null=False, choices = COLOR)
    peg_2 = models.CharField(max_length=1, blank=True, null=False, choices = COLOR)
    peg_3 = models.CharField(max_length=1, blank=True, null=False, choices = COLOR)
    peg_4 = models.CharField(max_length=1, blank=True, null=False, choices = COLOR)
    black_pegs = models.IntegerField(default = 0)
    white_pegs = models.IntegerField(default = 0)
    created = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return '%d' %peg_1
        #return '%s %s %s %s' % (self.peg_1, self.peg_2, self.peg_3, self.peg_4)

    def save(self, *args, **kwargs):
        game_active = Game.objects.filter(id = self.game.id)
        riddle_list = game_active.values_list('peg_1', 'peg_2', 'peg_3', 'peg_4')
        riddle_list = [i for i in riddle_list[0]]
        guess_list = [self.peg_1, self.peg_2, self.peg_3, self.peg_4]
        self.white_pegs, self.black_pegs = mastermindAlgorithm(riddle_list, guess_list)
        super().save(*args, **kwargs)	
