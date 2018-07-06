from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
####FROM OUR APP
from guesses.models import Guess
from guesses.serializers import GuessesSerializer


class GuessesList(generics.ListCreateAPIView):
    """\brief, Class used to handle Game models listing and creation"""
    queryset = Guess.objects.all()
    serializer_class = GuessesSerializer

