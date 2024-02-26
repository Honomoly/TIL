a = [1, 2, 3, 4 ,5]
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])

b = [1, 2, 3, [10, 20]]
print(b[-1][0])

c = [1, 2, 3, [10, 20], 4, 5]
print(c[3][0])

# 리스트 합치기
all_list = [a, b, c]
print(all_list)

print(all_list[0][2])
print(all_list[-1][3][0])

# 리스트 변경
a = [1, 2, 3, 4 ,5]

a[2] = 30
print(a)

a[1:3] = [10, 20]
print(a)

a[0] = [100, 200, 300]
print(a)

a[1:3] = []
print(a)