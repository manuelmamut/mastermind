from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
####FROM OUR APP
from guesses.models import Guess
from guesses.serializers import GuessesSerializer


@authentication_classes([])
@permission_classes([])
class GuessesList(generics.ListCreateAPIView):
    """Class used to handle Guess models listing and creation"""
    queryset = Guess.objects.all()
    serializer_class = GuessesSerializer

