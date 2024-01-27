from datetime import datetime, timedelta


class DatesBR:
    def __init__(self):
        self.register_moment = datetime.today()

    def __str__(self):
        return self.format_date()

    def register_month(self):

        months_year = [
            "january", "february", "march", "april",
            "may", "june", "july", "august", "september",
            "october", "november", "december"
        ]
        register_month = self.register_moment.month - 1
        return months_year[register_month]

    def week_day(self):

        days = [
            "monday", "tuesday", "wednesday", "thursday",
            "friday", "saturday", "sunday"
        ]
        week_day = self.register_moment.weekday()
        return days[week_day]

    def format_date(self):
        format_date = self.register_moment.strftime("%d/%m/%y %H:%M")
        return format_date

    def register_time(self):
        register_time = ((datetime.today() + timedelta(days=30))
                         - self.register_moment)
        return register_time
