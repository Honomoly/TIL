# 반복문 바깥의 반복문 중단하기
flag = False
count = 0
for i in range(5):
    for j in range(5):
        count += 1
        print(i, j, count)

        if j==2:
            print('break')
            break # 안쪽의 j 만 break

count = 0
for i in range(5):
    for j in range(5):
        count += 1
        print(i, j, count)

        if j==2:
            print('break')
            flag = True
            break # 안쪽의 j 만 break
    if flag:
        break # 안쪽이 break될 때 같이 break
    