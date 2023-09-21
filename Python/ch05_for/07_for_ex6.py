score = [90, 57, 88, 45, 78]
for i in range(5):
    if score[i] < 60:
        result = '불합격'
    else:
        result = '합격'
    print('%d번 %d점 %s'%(i+1, score[i], result))