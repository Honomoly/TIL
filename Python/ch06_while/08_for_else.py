# for문이 끝나면 else문 실행

for i in range(5):
    print(i, end=" ")
    break # for가 완벽히 수행되지 않으면 else도 출력되지 않음!
else:
    print('for문 종료후 실행')