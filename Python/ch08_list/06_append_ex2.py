scores = []
for i in range(5):
    scores.append(int(input('학생%d 점수 입력 : '%(i+1))))

sum = 0
over_eighty = 0
for score in scores:
    sum += score
    if score >= 80:
        over_eighty += 1
avg = sum/len(scores)

print('총점 : ', sum)
print('평균 : %.2f'%avg)
print('80점 이상 학생 : %d명'%over_eighty)