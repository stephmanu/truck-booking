from django.db import models
from django.urls import reverse

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



class BookingAbstract(models.Model):
    """ Booking abstract model """

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        abstract = True



class BookingManager(models.Manager):
    """ Booking manager """

    def get_all_bookings(self, request, user):
        bookings = TruckBooking.objects.filter(user=user, is_active=True, is_deleted=False)
        return bookings
    

class TruckBooking(BookingAbstract):

    User = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='bookings')

    Truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

    Date = models.DateField(default='some_value', blank=False, null=True)

    From_Time = models.TimeField(default='')
    
    To_Time = models.TimeField(default='')

 
    objects = BookingManager()

    def __str__(self):
        return f"{self.Truck.Truck_ID} - {self.From_Time} to {self.To_Time}"
    
    def get_absolute_url(self):
        return reverse("calendarapp:calendar", args=(self.id,))

    
    @property
    def get_html_url(self):
        return self.__str__()

