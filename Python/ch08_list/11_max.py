n = [100, 7, -2, 99, 30]
print(max(n))
print(min(n))

# 문자는 ASCII 코드 기준으로 찾음
ch = ['c', 'a', 'D', 'A', 'b']
print(max(ch))
print(min(ch))
# A, B, C, ... : 65, 66, 67, ...
# a, b, c, ... : 97, 98, 99, ...

names = ['홍길동', '이몽룡', '성춘향']
print(names.index('성춘향'))
print(names.index('강길동')) # 없으면 오류

print(dir(list)) # list class 파해치기
help(list)

# join() / ch07의 10_join.py에서 다루었음
names_list = ['홍길동', '이몽룡', '성춘향']
names_str = ' '.join(names_list)
print(names_str)
print(type(names_str))