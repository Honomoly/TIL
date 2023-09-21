class Donation:
    total = 0
    def __init__(self, name, donation):
        self.__name = name
        self.__donation = donation
        self.add_donation()
        
    def add_donation(self):
        Donation.total += self.__donation

    def show_donation_info(self):
        print('-------------')
        print('성명 : ', self.__name)
        print('기부금 : ', self.__donation)

    def show_total_donation(self):
        print('총 기부금 : ', Donation.total)
        

p1 = Donation('홍길동', 10000)
p1.show_donation_info()
p1.show_total_donation()

p2 = Donation('이몽룡', 20000)
p2.show_donation_info()
p2.show_total_donation()

p3 = Donation('성춘향', 30000)
p3.show_donation_info()
p3.show_total_donation()