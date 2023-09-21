class Counter:
    def set_count(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def get_count(self):
        return self.count
    
c1 = Counter() # 객체(인스턴스) 생성
c2 = Counter()

c1.set_count()
c2.set_count()

c1.increment()

print(c1.get_count())
print(c2.get_count())