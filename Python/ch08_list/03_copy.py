# Shallow Copy
scores = [10, 20, 30, 40]
copies = scores # 리스트 요소(객체)의 주소(참조값)만 복사하게 된다 

copies[0] = 50
print(scores, copies) # 그러므로 복사본에서 변경하면 원본도 변경된다

# Deep Copy
scores = [10, 20, 30, 40]
copies = list(scores) # 똑같은 리스트를 완전히 새로 만든다.

copies[0] = 50
print(scores, copies) # 그러므로 복사본에서 변경해도 원본은 그대로다

# Deep Copy / deepcopy() 사용
scores = [10, 20, 30, 40]
import copy
copies = copy.deepcopy(scores)

copies[0] = 50
print(scores, copies)