from calendar import HTMLCalendar
from api.models import TruckBooking


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, user=None):
        self.year = year
        self.month = month
        self.user = user
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter booking by day
    def formatday(self, day, bookings):
        bookings_per_day = bookings.filter(Date__day=day)
        d = ""
        for booking in bookings_per_day:
            d += "<li>" + booking.get_html_url + "</li>"
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"


    # formats a week as a tr
    def formatweek(self, theweek, bookings):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, bookings)
        return f"<tr> {week} </tr>"

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):

        if self.user.is_staff:
            bookings = TruckBooking.objects.filter(Date__year=self.year, Date__month=self.month)
        else:
            bookings = TruckBooking.objects.filter(Date__year=self.year, Date__month=self.month, User=self.user)

        
        cal = (
            '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        )  # noqa
        cal += (
            f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        )  # noqa
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, bookings)}\n"
        return cal
