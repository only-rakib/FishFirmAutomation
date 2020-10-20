from . serializers import SWITCHESSerializer
from fishCultureApp.models import SWITCHES
from rest_framework import generics
from django.shortcuts import render
# Create your views here.

class StatesViews(generics.ListCreateAPIView):
    queryset = SWITCHES.objects.all()
    serializer_class = SWITCHESSerializer