from Cat import *

c = Cat()
c.show() # 부모클래스의 show()호출
c.sound() # 자식클래스의 오버라이딩 된 sound()호출

print(Cat.mro()) # 클래스의 상속 경로를 보여줌