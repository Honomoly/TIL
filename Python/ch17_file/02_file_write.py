# 파일에 데이터를 쓰기 위해선 쓰기모드(w)로 사용한다
# 정확히는 덮어쓰기 모드다
# 파일 객체의 write() 메소드 쓰기


f = open('file4.txt', 'w')
f.write('안녕')
# 원래 인코딩 설정 없이 한글 쓰면 깨짐
# 근데 맥에선 안깨지네? 개꿀
f.close()

data = '안녕하세요'
f = open('file5.txt', 'w')
f.write(data)
f.close()

# 여러 행 쓰기
f = open('file6.txt', 'w')
for i in range(1, 11):
    data = '%d행\n'%i
    f.write(data)
f.close()

