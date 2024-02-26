import re
email = input('이메일 입력 : ')
# ^ : 시작
# $ : 끝
# \. : 특수문자(.)

pattern = re.findall('^[a-zA-Z0-9]{2,}@[a-zA-Z0-9]{2,}\.[a-z]{2,}$', email)

if len(pattern) == 0:
    print('잘못된 이메일 형식')
else:
    print('올바른 이메일 형식')

print(pattern)