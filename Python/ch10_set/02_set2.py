A = {1, 2, 3}
B = {3, 4, 5}

# 합집합
C = A|B
print(C)

C = A.union(B)
print(C)

# 교집합
C = A&B
print(C)

C = A.intersection(B)
print(C)

# 차집합
C = A-B
print(C)

C = A.difference(B)
print(C)