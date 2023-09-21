
import re # 정규표현식(Regular Expressions) 사용

string = "ID seoul_777 lived in Seoul in 2015"

# findall(검색어, 문자열) : 문자열에서 검색어와 일치하는 모든 내용을 리스트로 반환
result = re.findall('seoul', string)
print(result)

result = re.findall('e', string)
print(result)

# 소문자 a ~ z
result = re.findall('[a-z]', string) 
print(result)

# 소문자 a ~ z
# + : 스페이스 기준으로 최소 1번 이상 연속되는 형태 (단어 단위))
result = re.findall('[a-z]+', string)
print(result)

# 대문자 A ~ Z
result = re.findall('[A-Z]+', string)
print(result)

# 대소문자 전부
result = re.findall('[a-zA-Z]+', string)
print(result)

# 숫자 전부
result = re.findall('[0-9]+', string)
print(result)

# 숫자가 포함되지 않은
result = re.findall('[^0-9]+', string)
print(result)