scores = [90, 78, 81, 64, 89]
scores.sort() # 기본 오름차순 정렬 / 원본 변경
print(scores)

scores = [90, 78, 81, 64, 89]
scores.sort(reverse=True) # 내림차순 정렬 / 원본 변경
print(scores)

scores = [90, 78, 81, 64, 89]
scores.reverse() # 역순으로 변경 / 원본 변경
print(scores)

char = ['b', 'A', 'd', 'C']
char.sort() # 대문자 먼저 알파벳 순서로 정렬
print(char)

char = ['b', 'A', 'd', 'C']
char.sort(key=str.lower) # 그냥 알파벳 순서로 정렬
print(char)

char = ['b', 'A', 'd', 'C']
char.sort(key=str.lower, reverse=True) # 그냥 알파벳 역순으로 정렬
print(char)

ids = ['SKY', 'Blue', 'red', 'eBook', 'GREEN', 'blue']
ids.sort() # 첫 문자는 대문자 소문자 구별하면서 정렬
print(ids)

ids = ['SKY', 'Blue', 'red', 'eBook', 'GREEN', 'blue']
ids.sort(key=str.lower) # 그냥 대문자 소문자 구별없이 정렬
print(ids)


a = [3, 5, 2, 1, 4]
b = sorted(a) # 원본 유지하면서 정렬된 리스트를 새로 반환
print(a, b)