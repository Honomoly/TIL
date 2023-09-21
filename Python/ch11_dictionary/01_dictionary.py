# 중괄호 안에 키:값 형식으로 저장
# 집합처럼 인덱스로 접근이 안됨

scores = {'kor':90, 'eng':88, 'math':95}
print(scores)
print(type(scores))

student = {} # 빈 딕셔너리 / 공집합 아님
student['name'] = '홍길동' # 추가법 : 딕셔너리[키] = 값
student['age'] = 23
print(student)

nums = {}
nums[1] = 10
nums[2] = 20
nums[3] = 30
print(nums)

person = dict() # 빈 딕셔너리
person['이름'] = '홍길동'
person['키'] = 170
person['몸무게'] = 75
print(person)

person2 = dict(이름='이몽룡', 키=175, 몸무게=80)
print(person2)

# zip()
person3 = dict(zip(['이름', '키', '몸무게'], ['성춘향', 160, 60]))
print(person3)
# 근데 zip()이 뭐임?
numbers = [1, 2, 3]
names = ['홍길동', '이몽룡', '성춘향']
items = zip(numbers, names) # 동일 갯수의 iterable object를 각각 순서대로 묶어서 한 튜플로 만드는 것 
for i in items:
    print(i)

###########################

d = {1:'a'}
d[2] = 'b'

