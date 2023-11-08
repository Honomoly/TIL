def doom_day(num):
    # 6이 3번 연속으로 나오는 숫자
    pass

def combi(n, r):
    pass

def dwarf(arr):
    length = len(arr)
    lier1 = 0
    lier2 = 1
    while True:
        sum = 0
        for l in range(length):
            if l not in [lier1, lier2]:
                sum += arr[l]
        if sum == 100:
            break
        if lier2+1 < length:
            lier2 += 1
        else:
            if lier1+1 < lier2:
                lier1 += 1
                lier2 = lier1+1
            else:
                break
        print([lier1, lier2])
    del arr[lier2]
    del arr[lier1]
    return arr