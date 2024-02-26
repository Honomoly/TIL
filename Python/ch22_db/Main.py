from Controller import *
class Main:
    def __init__(self):
        self.__control = Controller()
    def start(self):
        while True:
            num = input("\n1.전체도서조회 2.도서등록 3.도서수정 4.도서삭제 5.검색 6.종료\n실행할 번호입력 : ")
            if num == '1':
                self.__control.select()
            elif num == '2':
                self.__control.insert()
            elif num == '3':
                self.__control.update()
            elif num == '4':
                self.__control.delete()
            elif num == '5':
                self.__control.search()
            elif num == '6':
                print('\n종료합니다')
                break;
            else:
                print('\n잘못된 양식입니다. 1 ~ 6 사이의 숫자를 입력하세요.')


# 현재모듈부터 시작
if __name__ == "__main__":
    print('\n도서 관리 시스템입니다')
    Main().start()