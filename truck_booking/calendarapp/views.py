import calendar
from datetime import date, datetime, timedelta

from django.views import generic 

from django.utils.safestring import mark_safe
from api.models import TruckBooking
from calendarapp.utils import Calendar
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


class AllBookingsListView(generic.ListView):
    """ All event list views """

    template_name = "calendarapp/events_list.html"
    model = TruckBooking

    def get_queryset(self):
        return TruckBooking.objects.get_all_events(user=self.request.user)
    


class CalendarView(LoginRequiredMixin, generic.ListView):
    model = TruckBooking
    template_name = "calendar.html"
    permission_classes = [IsAuthenticated]
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        user = self.request.user
        cal = Calendar(d.year, d.month, user)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context
