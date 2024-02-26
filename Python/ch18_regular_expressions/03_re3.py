import re # 정규표현식(Regular Expressions) 사용

string = "Those are my books written by Mr. Koooook."

# * : 최소 0번 이상
result = re.findall('o*', string)
print(result)

# {1, 5} : 1 ~ 5회 반복
result = re.findall('o{1, 5}', string)
print(result)

# {1, } : 최소 1회 반복
result = re.findall('o{1, }', string)
print(result)