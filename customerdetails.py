print("enter user details")

name = input("please enter name ")
age = int(input("please enter age"))
existing = input("existing customer yes or no ")

if existing == "yes":
    existing = True
if existing == "no":
    existing = False

print("name: ", name)
print("age: ", age)
print("existing customer: ", existing)
print("dog age: ", age * 7)
