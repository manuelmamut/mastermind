from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
####FROM OUR APP
from game.models import Game
from game.serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    """\brief, Class used to handle Game models listing and creation"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
 
#    def perform_create(self, serializer):
#        serializer.save(user=self.request.user)

class GameDetail(generics.RetrieveAPIView):
    """\brief, Class used to handle Game models details"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
