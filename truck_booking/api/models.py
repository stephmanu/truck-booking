from django.db import models
from .enum import StatusEnum 
from django_enumfield import enum

from django.contrib.auth.models import User



class Truck(models.Model):
    Truck_ID = models.CharField(max_length=50)

    Asset_Tag = models.CharField(max_length=50)
    
    Truck_Model = models.CharField(max_length=50)
    
    ECM_Type = models.CharField(max_length=50)
    
    status = enum.EnumField(
        StatusEnum,
        default=StatusEnum.AVAILABLE
    )
    
    comment = models.TextField()


class TruckBooking(models.Model):

    User = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    Truck_ID = models.ForeignKey(Truck, on_delete=models.CASCADE)

    Date = models.DateField(default='some_value', blank=False, null=True)

    From_Time = models.TimeField(default='')
    
    To_Time = models.TimeField(default='')



