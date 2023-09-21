s = set() # 공집합 생성

s1 = {1, 2, 3, 4, 5}
print(s1)

s3 = set((100, 200, 300)) # 튜플로 만들기

s4 = {1, 2, 3, 3, 4} # 중복이 되면 알아서 제거하고 생성
print(s4)

s5 = {1, 2, [3, 4]} # 변경 가능한 요소(리스트) 포함 불가
# 오류코드가 unhashable type이다
# hash : 각 객체가 가지고 있는 고유 식별키

s = {1, 2, 3}
s.add(4)
print(s)

s.update([5, 6])
print(s)

s.remove(3) # 없는거 지우려 하면 오류남
print(s)

s.discard(5) # 없는거 지우려 해도 오류 없음
print(s)

s.clear() # 공집합 됨
print(s)