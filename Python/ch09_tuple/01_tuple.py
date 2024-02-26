# 추가, 수정, 변경이 불가능한 점을 이용해 리스트와는 다른 쓰임새가 존재한다
t1 = () # 빈 녀석
t2 = tuple()
t3 = (1, 2, 3)
t4 = 4, 5, 6 # 괄호 없으면 자동 튜플 생성
t5 = [1, 2], [3, 4] # 튜플은 리스트를 엔트리로 가질 수도 있음
t6 = t1, t4, (7, 8, 9) # 튜블을 엔트리로 가질 수도 있음
t7 = tuple([5, 6, 7, 8]) # 함수 사용

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)

t = (1,) # 하나만 가진 튜플은 이렇게 쉼표를 넣어야함 / 아니면 그냥 숫자가 된다

to_list1 = list(t3) # 리스트로 바꾸기
print(to_list1)
to_list2 = list(t6) # 근데 겉에 것만 가능
print(to_list2)

##########################

my_tuple = ()

companies_t = ('삼성', '엘지', '현대')
companies_l = list(companies_t)
print(companies_l)