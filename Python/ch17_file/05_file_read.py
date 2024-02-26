# 파일내용 전체를 하나의 문자열로 출력
f1 = open('test2.txt', 'r')
data = f1.read()
print(data)
print(type(data))
print(len(data))
for ch in data:
    print(ch)
f1.close()
