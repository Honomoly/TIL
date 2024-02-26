import sqlite3

class LibraryDAO:
    def create(self, sql):
        try:
            con = sqlite3.connect('DesignPattern/template_method.db')
            cur = con.cursor()
            cur.execute(sql)
        except Exception as e:
            print(e)
        finally:
            con.close()
            
    def insert_many(self, sql, data):
        try:
            con = sqlite3.connect('DesignPattern/template_method.db')
            cur = con.cursor()
            cur.executemany(sql, data)
            con.commit()
        except Exception as e:
            print(e)
            con.rollback()
        finally:
            con.close()
    
    def search(self):
        try:
            con = sqlite3.connect('DesignPattern/template_method.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM users")
            result = cur.fetchall()
        except Exception as e:
            print(e)
            result = []
        finally:
            con.close()
            return result
            