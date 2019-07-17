from rest_framework import serializers
from .models import Screen, Seat, avilable

class Screenserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Screen
        fields = ('id', 'screenname', 'numberOfSeats', 'aisleSeats')


class Seatserializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('screen', 'number')


class Availableserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = avilable
        fields = ('status')
