import sqlite3

class dataBD():
    def __init__(self):
        self.con = sqlite3.connect("./BaseDate/LMSDataBase.db")
        self.cur = self.con.cursor()


    def searchUser(self, userName):
        result = self.cur.execute("""SELECT * FROM users_date
                    WHERE user_name = ?""", (userName,)).fetchall()
        if len(result) > 0:
            return True
        else:
            return False