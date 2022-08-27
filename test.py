import datetime

def todayAt (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now()
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)    

# time = datetime.datetime.now()
# min = time.minute

hours = todayAt(10, 30)
min = hours.minute
left = 15-(min%5)
print(left)


# dt = todayAt(10, 50)
# index = [15, 10, 5]
# now = datetime.datetime.now().minute + index
# if dt.minute == now:
#     print('lagi 15 menit')
# if (dt.minute - 15) == left:
#     print('lg 15')
# delta  = datetime.timedelta(minutes=15)

# print(dt - delta)

# if (dt - delta) <= dt:
#     print('lagi 15 menit')






# def day_now_indo():
#     WEEKDAYSLIST = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
#     MONTHLIST= ['Januari', 'Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
    
#     now = time.localtime()
#     hari = WEEKDAYSLIST[now.tm_wday]
#     tgl = now.tm_mday
#     bulan = MONTHLIST[now.tm_mon]
#     tahun = now.tm_year
#     format_indo = hari, tgl, bulan, tahun
#     return format_indo


# print(day_now_indo()[0])


# WEEKDAYS = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
# MonthList = ['Januari', 'Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']

# print(WEEKDAYS[0].lower() == 'senin')

# now = time.localtime()
# hari = now.tm_wday
# tgl = now.tm_mday
# bulan =  now.tm_mon -1
# thn = now.tm_year
# nama_hari = WEEKDAYS[hari]
# nama_bulan = MonthList[bulan]


# # # custom = n
# # print(now)
# print(type(bulan))
# print(nama_hari,tgl, nama_bulan, thn)
# weekday_index = now.hour
# print(WEEKDAYS[weekday_index])

# import datetime
# def todayAt (hr, min=0, sec=0, micros=0):
#    now = datetime.datetime.now()
#    return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)    

# print(todayAt(14))
# # Usage demo1:
# td= todayAt (17), todayAt (17, 15)
# # Usage demo2:    
# timeNow = datetime.datetime.now()
# print(timeNow)
# if timeNow >= todayAt(15, 57):
#     print("Too Early")

# delta = timedelta(minutes=10)
# before = todayAt(15, 40) - delta

# print(before)

# mulai = '09:40'
# str_todate = datetime.datetime.strptime(mulai, '%H:%M').time()
# print(str_todate.minute)