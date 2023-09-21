# remove(entry)
n = [1, 3, 3, 2, 6, 4, 5, 4, 3]
n.remove(4) # 첫 번째 4 제거
print(n)

# 전부 제거하기
n = [1, 3, 3, 2, 6, 4, 5, 4, 3]
num = n.count(3)
for i in range(num):
    n.remove(3)
print(n)

# pop()
x = ['a', 'b', 'c', 'd']
y = x.pop() # x의 마지막 엔트리 반환하고 x에서 삭제
print(x, y)

# pop(index)
heros = ['슈퍼맨', '스파이더맨', '헐크', '아이언맨', '배트맨']
heros.pop(2)
print(heros)

# clear()
n = [1, 3, 3, 2, 6, 4, 5, 4, 3]
n.clear()
print(n)

# del
n = [1, 3, 3, 2, 6, 4, 5, 4, 3]
del n[2]
print(n)

n = [1, 2, 3, 4, 5, 6, 7, 8]
del n[2:5] # 인덱스 2 ~ 4 엔트리 삭제
print(n)

n = [1, 2, 3, 4, 5, 6, 7, 8]
del n[2:] # 인덱스 2부터 전부 삭제
print(n)

n = [1, 2, 3, 4, 5, 6, 7, 8]
del n[2:6:2] # 인덱스 2 ~ 5에서 한 칸씩 띄워 삭제
print(n)

n = [1, 2, 3, 4, 5, 6, 7, 8]
del n # 전부 삭제
print(n)