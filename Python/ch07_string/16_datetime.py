from datetime import date, datetime

today = date.today() # 날짜만 출력
# datetime.today()도 같은 기능이지만 이건 시간도 나옴
year = today.year
month = today.month
day = today.day

print('날짜 : ', today)
print('연도 : ', year)
print('월 : ', month)
print('일 : ', day)

print('***************//***************')

now = datetime.now()
# 날짜 파트는 위의 date와 동일 속성
year = now.year
month = now.month
day = now.day
currnet_time = now.time()
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond
print('현재 : ', now)
print('현재 시간 :', currnet_time)
print('***************//***************')
print('날짜 : ', today)
print('연도 : ', year)
print('월 : ', month)
print('일 : ', day)
print('시 : ', hour)
print('분 : ', minute)
print('초 : ', second)
print('micro초 : ', microsecond)
