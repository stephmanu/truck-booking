from django.db import models
from .enum import StatusEnum 
from django_enumfield import enum


#class BeerStyle(enum.Enum):
#    LAGER = 0
#    STOUT = 1
#    WEISSBIER = 2
# Create your models here.

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