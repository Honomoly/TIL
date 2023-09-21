# 여러줄 가능
naver = {
    'name' : 'naver',
    'url' : 'www.naver.com',
    'userid' : 'nv',
    'password' : '1234'
}

google = {
    'name' : 'google',
    'url' : 'www.google.com',
    'userid' : 'gg',
    'password' : '5678'
}

print(naver.keys()) # key 리스트
print(naver.values()) # value 리스트
print(naver.items()) # (key, value) 리스트

print(type(naver.keys())) # 근데 타입들이 이상하네?
print(type(naver.values()))
print(type(naver.items()))

print(list(naver.keys())) # 리스트로 쓸려면 리스트로 만들면 된다

print(tuple(naver.values())) # 튜플을 원하면 튜플도 가능

print()

for value in naver.keys():
    print(value)
for value in naver.values():
    print(value)
for value in naver.items():
    print(value)

print()

# key를 사용하여 찾기
print(naver['userid']) # 근데 이건 존재하지 않으면 오류남
print(naver.get('password')) # 존재하지 않아도 오류 안남 / 존재하지 않으면 None

print()

# 위에서 반환값이 None인 경우 사용예시
insert_key = 'link'
if naver.get(insert_key) is None:
    print(insert_key + '에 대한 정보가 없습니다')

# 존재하는지만 판단
print('link' in google)
print('link' not in google)

print()


# 딕셔너리 합치기
# 1. update()
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
dict1.update(dict2) # dict1에 dict2 추가
print(dict1)
print(dict2)
#2. **
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
dict3 = {**dict1, **dict2}
print(dict3)

