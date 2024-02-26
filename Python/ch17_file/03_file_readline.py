# 파일 데이터를 읽기 위해서는 읽기모드(r)로 사용한다

# 파일내용을 실행마다 한 줄씩 출력
f1 = open('test.txt', 'r')
line = f1.readline() # 한 줄씩 읽기
print(line) # 한 번만 해서 첫 행만 나옴
f1.close()

# 읽어보기
f2 = open('test.txt', 'r')
while True:
    line = f2.readline()
    if not line: # 값이 없으면 while문 종료
        break
    print(line, end='') # 1행 출력하고 줄바꿈(\n)이 포함되어 있어서 end=''로 출력
f2.close()