str = input('문자를 입력하세요 : ')
alp = 0
num = 0
sps = 0
oth = 0

for txt in str:
    if txt.isalpha():
        alp += 1
    elif txt.isdigit():
        num += 1
    elif txt.isspace():
        sps += 1
    else:
        oth += 1

print('알파벳 : %d개'%alp)
print('숫자 : %d개'%num)
print('스페이스 : %d개'%sps)
print('기타 : %d개'%oth)