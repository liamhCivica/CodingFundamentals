import sqlite3

class DatabaseObject:


    def __init__(self, databaseName):
        try:
            self.conn = sqlite3.connect(databaseName)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(str(e))
    def close(self):
        try:
            self.cursor.close()
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(str(e))

    def Execute(self, query):
        try:
            self.cursor.execute(query)
        except Exception as e:
            print(str(e))

    def Read(self, query):
        try:
            return self.cursor.execute(query).fetchall()
        except Exception as e:
            print(str(e))