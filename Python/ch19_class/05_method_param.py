
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
p1 = Person('장승헌', 26)
p2 = Person('홍길동', 30)

print(p1.name)
print(p1.get_name())

p2.set_age(26)
p2.name = '성춘향'

print(p2.age, p2.name)