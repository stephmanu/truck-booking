from django.urls import path

from . import views

app_name = "calendarapp"


urlpatterns = [
    
    path("api/user/calendar/", views.CalendarView.as_view(), name="calendar")
    
]