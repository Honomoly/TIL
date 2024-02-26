a = 'aaa'
b = 'bbb'
print(a.join(b)) #  b 사이에 a를 삽입하여 연결 / 리스트 또한 가능하다

delim = '-'
print(delim.join('대한민국'))

ch = ', '
print(ch.join('1234'))

sep = '-'
names = ['홍길동', '이몽룡', '성춘향'] # number는 안됨!
print(sep.join(names))