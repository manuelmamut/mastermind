from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
####FROM OUR APP
from game.models import Game
from game.serializers import GameSerializer


@authentication_classes([])
@permission_classes([])
class GameList(generics.ListCreateAPIView):
    """Class used to handle Game models listing and creation"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
 

@authentication_classes([])
@permission_classes([])
class GameDetail(generics.RetrieveAPIView):
    """Class used to handle Game models details"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
