from django.db import models
from datetime import datetime

# Create your models here.


class Game(models.Model):
    EASY = 12
    MEDIUM = 10
    HARD = 8
    PRO = 6
    DIFICULTY = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
        (PRO, 'Pro'),
    )

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


    created = models.DateTimeField(auto_now_add=True)
    codemaker = models.CharField(max_length=100, blank=False, null=False, 
                                 help_text=("The name of the person running the game"))
    codebreaker = models.CharField(max_length=100, blank=True, null=True, 
                                 help_text=("The name of the person solving the riddle"))
    peg_1 = models.CharField(max_length=1, blank=True, null=True, choices = COLOR, 
                                 help_text=("In mastermind you use color pegs, here we use the initial of the color \
                                            Red, Green, Blue, Yellow, Purple, Organge "))
    peg_2 = models.CharField(max_length=1, blank=True, null=True, choices = COLOR,
                                 help_text=("In mastermind you use color pegs, here we use the initial of the color \
                                            Red, Green, Blue, Yellow, Purple, Organge "))
    peg_3 = models.CharField(max_length=1, blank=True, null=True, choices = COLOR,
                                 help_text=("In mastermind you use color pegs, here we use the initial of the color \
                                            Red, Green, Blue, Yellow, Purple, Organge "))
    peg_4 = models.CharField(max_length=1, blank=True, null=True, choices = COLOR,
                                 help_text=("In mastermind you use color pegs, here we use the initial of the color \
                                            Red, Green, Blue, Yellow, Purple, Organge "))
    tries_number = models.IntegerField(choices = DIFICULTY, default = EASY,
                                 help_text=("Here we define how is it going to be for the codebreaker, 12, 10, 8 or 6 tries "))
    open_game = models.BooleanField(default = True, 
                                    help_text=("Is the game open for play? True or False"))
 
    class Meta:
        ordering = ('created',)
