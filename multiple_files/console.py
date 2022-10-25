from database import DatabaseObject

GetTablesquery = "SELECT * FROM sqlite_master"
CreateTableSQL = """
CREATE TABLE Meal (
    mealID INT PRIMARY KEY,
    mealname varChar(50) NOT NULL,
    Course varChar(50) NULL,
    Size varChar(50) NUll);
"""

CreateNextTable = """
CREATE TABLE MealItem (
    mealItemID INT PRIMARY KEY,
    itemName INT NOT NULL,
    mealID INT NOT NULL,
    FOREIGN KEY (mealID)
       REFERENCES Meal (mealID) 
)
"""

InsertDataSQL = """
INSERT INTO Meal (mealname, Course, Size)
     VALUES (
"""
InsertMealItemSQL = """
INSERT INTO MealItem (itemName, mealID)
     VALUES (
"""
MealSelect = "SELECT * FROM Meal"

DropTable = "drop table "

def Menu():
    print(""" 
        1. print table schema
        2. create tables
        3. insert meal
        4. insert meal item
        5. drop tables
    """)

db = DatabaseObject("test")

Menu()

choice = int(input())

if choice == 1:
    print(db.Read(GetTablesquery))
elif choice == 2:
    db.Execute(CreateTableSQL)
    db.Execute(CreateNextTable)
elif choice == 3:
    mealname = input("enter meal name")
    group = input("enter meal group")
    size = input("enter meal size")
    db.Execute(InsertDataSQL + f"'{mealname}', '{group}', '{size}' )")
elif choice == 4:
    mealname = input("enter meal name")
    mealID = input("enter meal group")
    db.Execute(InsertMealItemSQL + f"'{mealname}', {mealID} )")
elif choice == 5:
    db.Execute(DropTable + "MealItem")
    db.Execute(DropTable + "Meal")

db.close()