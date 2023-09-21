num = input("숫자 입력 : ") # 문자열로 받음
print(num + str(5))
print(int(num) + 5) # 또는 float(), eval()

# eval()함수의 유용성
long = '10*3+2'
print(eval(long)) # 문자열로 수식을 입력하면 계산해줌 ㄷㄷ