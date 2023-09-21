# 파일내용 전체를 리스트로 반환
f1 = open('test.txt', 'r')
lines = f1.readlines()
print(lines)
f1.close()

# 읽어보기
f2 = open('test.txt', 'r')
lines = f2.readlines()
for line in lines:
    print(line, end='')
f2.close()