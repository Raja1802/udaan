from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class Screen(models.Model):
    screenname = models.CharField(max_length=10)
    numberOfSeats = models.IntegerField()
    aisleSeats = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True, null=True,default='')


    def __str__(self):
        return self.screenname


class Seat(models.Model):
    number = models.CharField(max_length=3, null=True,blank=False)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.number

class avilable(models.Model):
    available = models.ForeignKey(Seat, on_delete=models.CASCADE)