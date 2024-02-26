class Book:
    nation = 'korea'

    def __init__(self, no, name, author):
        self.__no = no
        self.__name = name
        self.__author = author
        self.__price = 10000
        self.__inventory = 100
        self.__publisher = '파이'

        self.get_book_no()
        self.get_book_name()
        self.get_book_author()
        print('출간된 나라 : ', Book.nation)
    
    def get_book_no(self):
        print('도서번호 : ', self.__no)

    def get_book_name(self):
        print('도서명 : ', self.__name)

    def get_book_author(self):
        print('저자 : ', self.__author)