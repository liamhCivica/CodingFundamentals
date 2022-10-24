import sqlite3

conn = sqlite3.connect("test-db")

cursor = conn.cursor()

GetTablesquery = "SELECT * FROM sqlite_master"
CreateTableSQL = """
CREATE TABLE Meal (
    mealID INT NOT NULL,
    mealname varChar(50) NOT NULL,
    Course varChar(50) NULL,
    Size varChar(50) NUll)
"""
InsertDataSQL = """
INSERT INTO Meal (mealID, mealname, Course, Size)
     VALUES (
"""
MealSelect = "SELECT * FROM Meal"

DropTable = "drop table meal"

cursor.execute(DropTable)
cursor.execute(CreateTableSQL)
cursor.execute(InsertDataSQL + "1, 'toast', 'breakfast', 'small' )")

print(cursor.execute(GetTablesquery).fetchall())

print("data from meal table")

print(cursor.execute(MealSelect).fetchall())