list1 = list()
list2 = []

print(list1)
print(list2)

integers = [32, 56, 64, 72, 12]
floats = [1.32, 5.112, 0.862]
strings = ['홍길동', '이몽룡', '성춘향']

numbers = [1, 2, [3, 4]]

for i in range(len(integers)):
    print(integers[i])

for i in strings:
    print(i)

# 합 구하는 내장 함수 / 근데 하위리스트가 있는건 오류남
print(sum(integers))
print(sum(floats))