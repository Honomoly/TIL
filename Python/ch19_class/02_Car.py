class Car:
    def set_car(self):
        self.no = '01가1234'
        self.model = '아반떼'
        self.maker = '현대'
        self.year = 2023
        self.cc = 1600

    def show_car_info(self):
        print('차량번호 : ', self.no)
        print('차종 : ', self.model)
        print('제조사 : ', self.maker)
        print('연식 : ', self.year)
        print('배기량 : ', self.cc)

car1 = Car()

car1.set_car()
car1.show_car_info()