# 밖에 있는 모듈 파일 불러오기
# 1-1. 모듈 전체 참조
import new_calculator1
print(new_calculator1.add(6, 3)) # 앞에 모듈명 붙여야 함

# 1-2. 별칭 쓰기
import new_calculator1 as nc1
print(nc1.sub(6, 3))

# 2-1. 모듈내 함수 전체 참조
from new_calculator1 import *
print(mul(6, 3)) #앞에 모듈명 안붙여도 됨

# 2-2. 일부 참조
from new_calculator1 import div
print(div(6, 3))

# 모듈내 함수 직접 참조가 코드 작성에는 편하지만
# 여러 모듈을 참조하면 함수 이름이 겹쳐서 오류날 수도 있다