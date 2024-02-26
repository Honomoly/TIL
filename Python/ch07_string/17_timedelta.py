from datetime import date, datetime, timedelta

today = date.today()

# 날짜 차이
print('오늘 : ', today)
print('어제 : ', today - timedelta(days=1))
print('내일 : ', today + timedelta(days=1))

# 시간 차이
current_time = datetime.now()
print('현재시간 : ', current_time)
print('1시간 15분 10초전 : ', current_time - timedelta(hours=1, minutes=15, seconds=10))

print('***************//***************')

# 날짜 형식으로 문자로 변환하는 strftime() / STRing Format TIME
current_time = datetime.now()
print(current_time.strftime('%Y-%m-%d %H:%M:%S'))
print(current_time.strftime('%y-%m-%d %I:%M:%S %p'))

print('***************//***************')

# 문자를 날짜 형식으로 변환하는 strptime() / STRing P TIME
str_b_datetime = '1997-08-14 05:30:00'
b_datetime = datetime.strptime(str_b_datetime, '%Y-%m-%d %H:%M:%S')
current_time = datetime.now()
print('나의 생일 : ', b_datetime)
print('경과 시간 : ', current_time - b_datetime)