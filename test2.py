import datetime

def todayAt (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now()
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)    

# time = datetime.datetime.now()
# min = time.minute

hours = todayAt(11, 30)
delta = datetime.timedelta(minutes=15)
now = datetime.datetime.now() + delta
hasil = now.time()
print(hasil > hours.time())
# print(hasil.minute <= hours.minute)
# left = 15-(min%5)
# if now == hours:
#     print(left)
    
