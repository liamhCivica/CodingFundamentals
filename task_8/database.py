import pyodbc

CreateSqlStr = """
CREATE TABLE Student (
    studentID INT NOT NULL,
    FirstName NvarChar(40) NOT NULL,
    SurName NvarChar(30) NULL,
    Course NvarChar(30) NULL,
    City NvarChar(14) NULL
)
"""

InsertSql = """
    INSERT INTO Student (studentID, FirstName, SurName, Course, City)
     VALUES ("""

def OpenConnection():
    connectionString = r'DRIVER={SQL Server};SERVER=.\;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    return conn

def Execute(conn, cursor, command):
    cursor.execute(command)
    conn.commit()

connection = OpenConnection()
cur = connection.cursor() 

Execute(connection, cur, CreateSqlStr)

with open('student.csv') as csv_file:
    for row in csv_file:
        insertCommand = InsertSql.strip() + row.strip() + ")"
        print(insertCommand)
        Execute(connection, cur, InsertSql)


updateStr = """
UPDATE Student
   SET City = 'sheffield'
 WHERE studentID = 1
"""

Execute(connection, cur, updateStr)
