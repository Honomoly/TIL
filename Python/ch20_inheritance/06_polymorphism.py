class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def show_item(self):
        print(self.__name, self.__price)

class Book:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def show_item(self):
        print(self.__name, self.__price)


# polymorphism(다형성) : 하나의 객체에 2개의 다른 타입을 대입 가능
# Product 클래스 객체, Book 클래스 객체 모두 대입 가능
def show_items(item):
    item.show_item()

prd = Product('노트북', 1000000)
book = Book('파이썬', 20000)

show_items(prd)
show_items(book)