# 파일에 데이터를 덮어쓰기 않고 추가하기 위해선 추가모드(a)로 사용한다

f = open('test2.txt', 'a')
append_data = '\nPython Programming'
f.write(append_data)
f.close()

f1 = open('test2.txt', 'r')
print(f1.read())
f1.close()
