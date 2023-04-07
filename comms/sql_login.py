import sqlite3


class SQL():


    def __init__(self) -> None:
        self.con = sqlite3.connect("db.sqlite", check_same_thread=False)
        self.QUERY = "SELECT * FROM user WHERE username='{username}' AND password='{password}'"
    

    def login(self, username, password):
        q = self.QUERY.format(username=username, password=password)
        print(q)
        cur = self.con.cursor()
        res = cur.execute(q).fetchone()
        if res is None:
            return None
        return res[1]
