from django.contrib import admin
from .models import Truck, TruckBooking
from schedule.models import Calendar


# Register your models here.


admin.site.register(Truck)
admin.site.register(TruckBooking)
#admin.site.register(Calendar)

