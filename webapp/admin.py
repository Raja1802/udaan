from django.contrib import admin
from .models import Screen, Seat, avilable
# Register your models here.
myModels = [Screen, Seat, avilable]
admin.site.register(myModels)