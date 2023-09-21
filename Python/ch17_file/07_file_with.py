# with문이 끝나면 파일이 자동으로 닫히므로 close()을 안 써도 된다
with open('file7.txt', 'w') as f:
    f.write('with문으로 파일 쓰기')


# 변수 미리 저장
file = 'file8.txt'
data = '''--Python Programming
Database
Django--'''

# 쓰기모드
with open(file, 'w') as f:
    f.write(data)

# 읽기모드
with open(file, 'r') as f:
    print(f.read())