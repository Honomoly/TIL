def q1(arr):
    sum = 0
    max = 0
    itv = [0, 0]
    for i in range(len(arr)):
        sum += arr[i]
        if max < sum:
            itv[1] = i
            max = sum
        if sum <= 0:
            itv[0] = i+1
            print(max)
            sum = 0
    print(itv)
    return max


print(q1([10, -4, 3, 1, 5, 6, -35, 12, 21, -1]))