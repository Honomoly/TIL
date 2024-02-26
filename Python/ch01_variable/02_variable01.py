result = 10
print(result)

result = 20
print(result)

# 한 번에 저장하기
a, b, c = 1, 2, 3
print(a, b, c)

a = b = c = 10
print(a, b, c)

# 서로 교환하기
a, b = 10, 20
a, b = b, a
print(a, b)

# 변수 삭제
a = 10
del a
print(a) # 오류