from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Songs
from music.serializers import SongSerializer


class ListSongsView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongSerializer