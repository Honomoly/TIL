from BookDAO import *
from BookVO import *
class Controller:
    def __init__(self):
        self.__DAO = BookDAO(None, None, None)
        self.__vars = BookVO(None, None, None, None, None, None, None)
    
    def select(self):
        self.__DAO.select()
    
    def insert(self):
        self.__vars.set_bNo(input('도서번호 입력 (!을 입력하여 취소) : '))
        if self.__vars.get_bNo() == '!':
            pass
        else:
            self.__vars.set_bName(input('도서명 입력 : '))
            self.__vars.set_bAuthor(input('저자 입력 : '))
            self.__vars.set_bPrice(input('가격 입력 : '))
            self.__vars.set_bDate(input('출판일 입력 : '))
            self.__vars.set_bStock(input('재고 입력 : '))
            self.__vars.set_pubNo(input('출판사번호 입력 : '))
            self.__DAO.insert(self.__vars)
    
    def update(self):
        self.__vars.set_bNo(input('정보수정할 도서번호 입력 (!을 입력하여 취소) : '))
        if self.__vars.get_bNo() == '!':
            pass
        else:
            self.__vars.set_bName(input('도서명 수정 (!을 입력하여 스킵) : '))
            self.__vars.set_bAuthor(input('저자 수정 (!을 입력하여 스킵) : '))
            self.__vars.set_bPrice(input('가격 수정 (!을 입력하여 스킵) : '))
            self.__vars.set_bDate(input('출판일 수정 (!을 입력하여 스킵) : '))
            self.__vars.set_bStock(input('재고 수정 (!을 입력하여 스킵) : '))
            self.__vars.set_pubNo(input('출판사번호 수정 (!을 입력하여 스킵) : '))
            self.__DAO.update(self.__vars)
    
    def delete(self):
        self.__vars.set_bNo(input('삭제할 도서번호 입력 (!을 입력하여 취소) : '))
        if self.__vars.get_bNo == '!':
            pass
        else:
            self.__DAO.delete(self.__vars)
    
    def search(self):
        self.__vars.set_bName(input('검색할 도서명 입력 (!을 입력하여 취소) : '))
        if self.__vars.get_bName == '!':
            pass
        else:
            self.__DAO.search(self.__vars)