import datetime

now = datetime.datetime.now()
nowutc = datetime.datetime.utcnow()
today = datetime.date.today()
time = datetime.datetime.now()

print(now)
print(nowutc)
print(today) #.year, .month, .day
print(time.strftime('%H:%M%p'))
print(time.strftime('%I:%M'))
print(time.strftime('%d-%m-%Y'))