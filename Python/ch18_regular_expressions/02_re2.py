import re # 정규표현식(Regular Expressions) 사용

string = "ID seoul_777 lived in Seoul in 2015"

# [\d] : [0-9]와 동일한 효과
result = re.findall('[\d]+', string)
print(result)

# [\D] : [^0-9]와 동일한 효과
result = re.findall('[\D]+', string)
print(result)

# [\s] : 스페이스
result = re.findall('[\s]', string)
print(result)

# [\w] : 문자, 숫자
result = re.findall('[\w]+', string)
print(result)

# [\W] : 문자, 숫자가 아닌 것
result = re.findall('[\W]+', string)
print(result)


# seoul_777만 뽑기
result = re.findall('[a-z]+[\w][\d]+', string)
# [a-z]+    : seoul
# [\w]      : _
# [\d]+     : 777
print(result)