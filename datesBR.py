from datetime import datetime


class DatesBR:
    def __init__(self):
        self.register_moment = datetime.today()

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
