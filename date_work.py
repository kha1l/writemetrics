from datetime import date, timedelta, datetime
import math


class DataWork:

    def __init__(self, date_end=None):
        self.date_end = date_end

    def set_date(self):
        if self.date_end is None:
            self.date_end = date.today() - timedelta(days=1)
            # self.date_end = date.today()
            return self.date_end
        else:
            return self.date_end

    @staticmethod
    def change_timedelta(t):
        h = t.days * 24 + t.seconds // 3600
        m = t.seconds % 3600 // 60
        s = t.seconds % 3600 % 60
        st_time = f'{h}:{m}:{s}'
        return st_time

    @staticmethod
    def change_date(t):
        dt = datetime.strftime(t, '%d.%m.%Y')
        return dt

    @staticmethod
    def change_time(t):
        x = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second, microseconds=t.microsecond)
        tm = timedelta(seconds=math.ceil(x.total_seconds()))
        h = tm.days * 24 + tm.seconds // 3600
        m = tm.seconds % 3600 // 60
        s = tm.seconds % 3600 % 60
        st_time = f'{h}:{m}:{s}'
        return st_time
