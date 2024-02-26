string = 'python'
print("{0:<12}".format(string)) # 12칸중 왼쪽 정렬
print("{0:>12}".format(string)) # 12칸중 오른쪽 정렬
print("{0:^12}".format(string)) # 12칸중 가운데 정렬
print("{0:-^12}".format(string)) # 12칸중 공백문자(-) 지정 가운데 정렬

# 위와 동일한 효과를 내는 메소드
string = 'python'
print(string.ljust(12))
print(string.rjust(12))
print(string.center(12))
print(string.center(12, '-'))

# f-string의 경우
string = 'python'
print(f'{string:<12}')
print(f'{string:>12}')
print(f'{string:^12}')
print(f'{string:-^12}')