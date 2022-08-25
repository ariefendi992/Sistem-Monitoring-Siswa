import time

def today_():
    week_days = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
    local_time = time.localtime()
    today = local_time.tm_wday
    return week_days[today] 


def tomorrow_():
    week_days = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
    local_time = time.localtime()
    tomorrow = local_time.tm_wday
    return week_days[tomorrow + 1]

