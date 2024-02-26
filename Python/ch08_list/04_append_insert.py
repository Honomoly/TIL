a = [1, 2, 3, 3, 4]
print('원소의 갯수 : ', len(a))
print('3의 갯수 : ', a.count(3))

# 뒤에 붙이기
a = [1, 2, 3, 3, 4]

a.append(5)
print(a)

a.append([6, 7])
# 두 개씩 넣으려다 하위 리스트로 들어갈 수 있다!
# 그냥 하나씩 넣어라!
# 두 개는 동시에 안 들어간다!
print(a)

# for문으로 리스트 만들기
x = list()
for i in range(5):
    x.append(i)
print(x)

# 특정 위치에 넣기
nums = [1, 2, 3, 4, 5]
nums.insert(1, 200) # 1의 위치에 200을 넣고 나머지 원소는 밀려난다
print(nums)

nums.append('홍길동')
nums.append(12.3)
nums.insert(-1, [10, 20])

print(nums)