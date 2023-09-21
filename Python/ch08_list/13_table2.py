kim = [90, 85, 70]
lee = [88, 79, 92]
park = [100, 100, 100]
kang = [90, 60, 70]

students = [kim, lee, park, kang]

print('---성적표 (점수, 총범, 평균)---')
for scores in students:
    print(scores, end=" , ")
    print(sum(scores), end=" , ")
    print(format(sum(scores)/3, '.2f'))