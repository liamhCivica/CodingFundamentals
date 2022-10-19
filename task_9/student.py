from abc import ABC, abstractmethod

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def GetScore(self, test1, test2, test3):
        return (test1 + test2 + test3) / 3

class StudentWithClass(Student):
    def __init__(self, classroom, name, age):
        super(StudentWithClass, self).__init__(name, age)
        self.classroom = classroom
    

class Bird(ABC):
    extinct = False

    @abstractmethod
    def fly(self):
        pass

class Owl(Bird):
    def fly(self):
        print("can fly")

class Dodo(Bird):
    def __init__(self):
        self.extinct = True

    def fly(self):
        print("can not fly")

student1 = Student("tim", 10)
student2 = Student("tom", 10)
student3 = StudentWithClass("english", "tom", 10)

print(student1.age)
print(student2.age)
print(student3.age)

print(student1.GetScore(1, 1, 1))

owl = Owl()
dodo = Dodo()

print(owl.fly())
print(dodo.fly())


