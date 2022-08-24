import time
WEEKDAYS = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

now = time.localtime()
weekday_index = now.tm_wday
print(WEEKDAYS[weekday_index])