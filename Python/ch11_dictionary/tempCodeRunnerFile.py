icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# (1) icecream 딕셔너리에서 key 값만 출력
print(' '.join(list(icecream.keys())))


# (2) key 값으로만 구성된 리스트 생성
print(list(icecream.keys()))



# 12.
# (1) icecream 딕셔너리에서 가격만 출력
for i in list(icecream.values()):
    print(i, end=' ')
print()