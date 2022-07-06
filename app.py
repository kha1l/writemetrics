import time
import schedule
from schedule import repeat
from writer import writer
from datetime import date, timedelta


@repeat(schedule.every().day.at('10:54'))
def write_metrics():
    writer('korsakov', 'day')


@repeat(schedule.every().day.at('10:55'))
def write_metrics():
    writer('zelen', 'day')


@repeat(schedule.every().day.at('01:35'))
def write_metrics():
    writer('omsk', 'day')


@repeat(schedule.every().day.at('06:20'))
def write_metrics():
    writer('veris', 'day')


@repeat(schedule.every().day.at('07:20'))
def write_metrics():
    writer('vkz', 'day')


@repeat(schedule.every().day.at('04:35'))
def write_metrics():
    writer('south', 'day')


@repeat(schedule.every().day.at('02:30'))
def write_metrics():
    writer('vkus', 'day')


@repeat(schedule.every().day.at('03:35'))
def write_metrics():
    writer('msk-sch', 'day')


@repeat(schedule.every().day.at('05:20'))
def write_metrics():
    writer('sergpas', 'day')


@repeat(schedule.every().monday.at('01:40'))
def write_metrics():
    writer('omsk', 'week')


@repeat(schedule.every().monday.at('13:01'))
def write_metrics():
    writer('korsakov', 'week')


@repeat(schedule.every().monday.at('06:25'))
def write_metrics():
    writer('veris', 'week')


@repeat(schedule.every().monday.at('14:27'))
def write_metrics():
    writer('vkus', 'week')


@repeat(schedule.every().monday.at('03:40'))
def write_metrics():
    writer('msk-sch', 'week')


@repeat(schedule.every().day.at('12:41'))
def write_metrics():
    writer('vkz', 'week')


@repeat(schedule.every().monday.at('04:40'))
def write_metrics():
    writer('south', 'week')


@repeat(schedule.every().monday.at('05:25'))
def write_metrics():
    writer('sergpas', 'week')


@repeat(schedule.every().day.at('14:22'))
def write_metrics():
    writer('zelen', 'week')


@repeat(schedule.every().thursday.at('01:40'))
def write_metrics():
    writer('omsk', 'week2')


@repeat(schedule.every().thursday.at('06:25'))
def write_metrics():
    writer('veris', 'week2')


@repeat(schedule.every().thursday.at('00:35'))
def write_metrics():
    writer('korsakov', 'week2')


@repeat(schedule.every().thursday.at('12:49'))
def write_metrics():
    writer('vkus', 'week2')


@repeat(schedule.every().thursday.at('03:40'))
def write_metrics():
    writer('msk-sch', 'week2')


@repeat(schedule.every().thursday.at('07:25'))
def write_metrics():
    writer('vkz', 'week2')


@repeat(schedule.every().thursday.at('04:40'))
def write_metrics():
    writer('south', 'week2')


@repeat(schedule.every().thursday.at('05:25'))
def write_metrics():
    writer('sergpas', 'week2')


@repeat(schedule.every().day.at('16:55'))
def write_metrics():
    writer('omsk', 'month')


@repeat(schedule.every().day.at('16:57'))
def write_metrics():
    writer('veris', 'month')


@repeat(schedule.every().day.at('13:04'))
def write_metrics():
    writer('korsakov', 'month')


@repeat(schedule.every().day.at('17:10'))
def write_metrics():
    writer('vkus', 'month')


@repeat(schedule.every().day.at('17:02'))
def write_metrics():
    writer('msk-sch', 'month')


@repeat(schedule.every().day.at('17:04'))
def write_metrics():
    writer('vkz', 'month')


@repeat(schedule.every().day.at('17:05'))
def write_metrics():
    writer('south', 'month')


@repeat(schedule.every().day.at('17:07'))
def write_metrics():
    writer('sergpas', 'month')


@repeat(schedule.every().day.at('13:16'))
def write_metrics():
    writer('zelen', 'month')


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
