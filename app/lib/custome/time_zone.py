import pytz
import datetime

def utc_makassar():
    utc = pytz.timezone('Asia/Makassar')
    datetime_utc = datetime.datetime.now(utc)

    return datetime_utc

def todayAt (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now()
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)    

