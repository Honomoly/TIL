from library.dao import LibraryDAO

if __name__ == "__main__":
    dao = LibraryDAO()
    # dao.create(" CREATE TABLE users (id integer primary key, name text, age integer)")
    sql = "INSERT INTO users (name, age) VALUES (?, ?)"
    data = [
        ("JSH", 26),
        ("KSG", 22),
        ("HGD", 30)
    ]
    # dao.insert_many(sql, data)
    # print(dao.search())
