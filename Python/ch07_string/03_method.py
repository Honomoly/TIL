string = 'programming'

# len()
print(len(string)) # 11

# count()
print(string.count('g')) # 2
print(string.count('ro')) # 1

# find() : 못찾으면 -1 반환
print(string.find('g')) # 3
print(string.find('ram')) # 4

# index() : find()와 동일하지만 못찾으면 오류남!
print(string.index('g')) # 3
print(string.index('ram')) # 4

