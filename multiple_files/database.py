import sqlite3

class DatabaseObject:


    def __init__(self, databaseName):
        self.conn = sqlite3.connect(databaseName)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def Execute(self, query):
        self.cursor.execute(query)

    def Read(self, query):
        return self.cursor.execute(query).fetchall()