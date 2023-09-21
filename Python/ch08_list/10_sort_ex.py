scores = []
sum = 0
over_eighty = 0

nums = int(input('학생 수 입력 : '))

for i in range(nums):
    score = int(input('학생%d 점수 입력 : '%(i+1)))
    scores.append(score)
    sum += score
    if score >= 80:
        over_eighty += 1

avg = sum/nums
scores.sort(reverse=True)

print('총점 : ', sum)
print('평균 : %.2f'%avg)
print('80점 이상 학생 : %d명'%over_eighty)
print('점수 내림차순 정렬 : ', scores)