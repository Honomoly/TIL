class Animal:
    def show(self):
        print('동물입니다')

    def sound(self):
        print('동물 사운드')
        super().sound() # 부모것 호출