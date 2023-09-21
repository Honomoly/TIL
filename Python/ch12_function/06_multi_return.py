def multi_return() :
    return 1, 2, 3

a, b, c = multi_return() # 하나씩 받기
print(a, b, c)

d = multi_return() # 튜플로 받음
print(d)

t = 4, 5, 6
p, q, r = t
print(p, q, r)