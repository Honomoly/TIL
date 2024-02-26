# append()와 insert()는 한 개씩 넣었지만 extend()는 다르다!

a = [1, 2, 3]
a.extend([4, 5])
print(a)

a = [1, 2, 3]
a.append([4, 5]) # 이건 하위 리스트로 포함됨
print(a)

a = [1, 2, 3]
a.insert(len(a), [4, 5]) # 이것도 하위 리스트로 포함됨
print(a)

x = [1, 2, 3]
y = [4, 5]
print(x+y) # 더하기도 같은 효과