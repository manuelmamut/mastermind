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
    COLOR = (
        (RED, 'Red'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (YELLOW, 'Yellow'),
    )


    created = models.DateTimeField(auto_now_add=True)
    codemaker = models.CharField(max_length=100, blank=False, null=False)
    codebreaker = models.CharField(max_length=100, blank=True, null=True)
    peg_1 = models.CharField(max_length=1, blank=True, null=True, choices = COLOR)
    peg_2 = models.CharField(max_length=1, blank=True, null=True, choices = COLOR)
    peg_3 = models.CharField(max_length=1, blank=True, null=True, choices = COLOR)
    peg_4 = models.CharField(max_length=1, blank=True, null=True, choices = COLOR)
    tries_number = models.IntegerField(choices = DIFICULTY, default = EASY)
    open_game = models.BooleanField(default = True)
 
    class Meta:
        ordering = ('created',)
