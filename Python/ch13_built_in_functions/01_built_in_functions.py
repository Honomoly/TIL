# 내장 함수
print("-----abs()-----")
print(abs(-10)) # 절댓값 / absolute


print("-----chr()-----")
# ASCII 코드값에 따라 문자 출력
print(chr(97)) # a
print(chr(65)) # A
print(chr(13)) # Enter


print("-----ord()-----")
# 문자에 따른 ASCII 코드값 출력
print(ord('a')) # 97
print(ord('0')) # 48
print(ord('\n')) # 10
print(ord(' ')) # 32
print(ord('\r')) # 13


print("-----filter()-----")
# filter(function, iterable) function에 iterable을 계속 넣었을 때 반환값이 True인 것만 반환
def positive(x):
    return x > 0 # 양수일때만 참으로 반환
print(list(filter(positive, [0, 1, 3, -4, 2, -7, 10]))) # filter object라서 리스트로 변환

nums = [1, 2, 3, 4, 5, 6, 7, 8]
def even_number(x):
    return x%2==0
print(filter(even_number, nums))
print(list(filter(even_number, nums)))


print("-----map()-----")
# map(function, iterable) function에 iterable을 넣은 값들을 반환

def increase(x):
    return x+1

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(map(increase, nums))
print(list(map(increase, nums)))

def power(x):
    return x**2
print(list(map(power, [1, 2, 3, 4, 5])))


print("-----pow()-----")
# pow(x, y) : x^y
print(pow(2, 3))


print("-----round()-----")
# 실수 반올림
print(round(3.14))
print(round(3.141592, 4))


print("-----zip()-----")
# zip(*iterable) : 각 iterable에서 동일 인덱스 요소를 추출하고 튜플로 묶어서 반환
print(zip([1, 2, 3, 4],(10, 20, 30, 40))) # 리스트, 튜플 혼용 가능
print(list(zip([1, 2, 3, 4],(10, 20, 30, 40))))


print("-----lambda 식-----") 
# 실행 시 생성해서 사용하는 익명 함수
# def 보다 간결하게 함수 만들기 가능
# (lambda 변수들 : 반환식)(입력값들)
print((lambda a, b : a + b)(3, 5))
# 람다식을 변수에 할당해서 재사용 가능
lambda_add = lambda a, b : a+b
print(lambda_add(4, 7))

print(list(map(lambda x : x**3, [1, 2, 3])))