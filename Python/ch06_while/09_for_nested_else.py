count = 0

for i in range(5):
    for j in range(5):
        count += 1
        print(i, j, count)

        if j == 2 :
            print('break')
            break # 1. break가 안돌면 else 시행 / break가 되면 else 건너뜀 
    else:
        continue
    break # 2. 위의 else가 실행되면 실행 안됨 / 위의 else를 건너뛰면 실행

# 3. 전부 실행 / 전부 break