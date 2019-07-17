from django.shortcuts import render
from rest_framework import viewsets
from .models import Screen, Seat, avilable
from .serializers import Screenserializer, Seatserializer, Availableserializer
# Create your views here.


class ScreenViews(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    serializer_class = Screenserializer


class SeatViews(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = Seatserializer


class available(viewsets.ModelViewSet):
    queryset = Seat.objects.filter(status=True)
    serializer_class = Seatserializer