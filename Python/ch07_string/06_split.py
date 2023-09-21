string = "Python Programming"
string_split = string.split() # 구분자는 띄어쓰기 기준
print(string_split) # 리스트로 변환

names = '홍길동, 이몽룡, 성춘향, 변학도'
names_split = names.split(',') # 구분자는 ,(쉼표)지만 띄어쓰기 한칸도 포함한다 추가
print(names_split)

colors = 'red:blue:yellow:green'
colors_split = colors.split(':') # 구분자를 :(콜론)으로만 
print(colors_split)

# 알파벳 수준으로 분리된다
for color in colors:
    print(color)

# 그래서 split()을 쓴다
for color in colors_split:
    print(color)