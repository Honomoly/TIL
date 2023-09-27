import pymysql
class BookDAO:
    def __init__(self, sql, conn, cursor):
        self.__sql = sql
        self.__conn = conn
        self.__cursor = cursor
    
    def connect(self):
        self.__conn = pymysql.connect(host='localhost', port=3306, db='sqldb3', user='root', passwd='Wk0qbfmt!', charset='utf8')
        self.__cursor = self.__conn.cursor()
    
    def disconnect(self):
        self.__cursor.close()
        self.__conn.close()
    
    # 연결, 실행(결과출력), 접속종료
    def select(self):
        self.connect()
        self.__sql = "SELECT * FROM book"
        self.__cursor.execute(self.__sql)
        print('\n도서번호 / 도서명 / 저자 / 가격 / 출판일 / 재고 / 출판사번호')
        for row in self.__cursor.fetchall():
            for item in row:
                print(item, end=' / ')
            print()
        self.disconnect()
    
    def insert(self, values):
        self.connect()
        self.__sql = "INSERT INTO book VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            self.__cursor.execute(self.__sql, values.get_all())
            self.__conn.commit()
        except Exception as e:
            print('\n추가에 실패했습니다')
            print(e)
        else:
            print('\n해당 도서가 정상적으로 추가되었습니다')
        self.disconnect()
    
    def update(self, values):
        self.connect()
        self.__sql = "UPDATE book SET "
        names = ("bookName=", "bookAuthor=", "bookPrice=", "bookDate=", "bookStock=", "pubNo=")
        print(values.get_all())
        for i in range(len(names)):
            if values.get_all()[i+1] == '!':
                continue
            else:
                self.__sql += names[i] + values.get_all()[i+1] + ', '
        self.__sql = self.__sql[:-2] + " WHERE bookNo=" + values.get_all()[0]
        try:
            self.__cursor.execute(self.__sql)
            self.__conn.commit()
        except Exception as e:
            print('\n정보 수정에 실패했습니다')
            print(e)
        else:
            print('\n해당 도서의 정보가 정상적으로 수정되었습니다')
        self.disconnect()
    
    def delete(self, values):
        self.connect()
        self.__sql = "DELETE FROM book WHERE bookNo=" + values.get_bNo()
        try:
            self.__cursor.execute(self.__sql)
            self.__conn.commit()
        except Exception as e:
            print('\n해당 도서정보 삭제에 실패했습니다')
            print(e)
        else:
            print('\n해당 도서정보가 정상적으로 삭제되었습니다')
        self.disconnect()
    
    def search(self, values):
        self.connect()
        self.__sql = "SELECT * FROM book WHERE bookName LIKE '%" + values.get_bName() + "%'"
        self.__cursor.execute(self.__sql)
        print('--검색결과--')
        print('도서번호 / 도서명 / 저자 / 가격 / 출판일 / 재고 / 출판사번호')
        for row in self.__cursor.fetchall():
            for item in row:
                print(item, end=' / ')
            print()
        self.disconnect()