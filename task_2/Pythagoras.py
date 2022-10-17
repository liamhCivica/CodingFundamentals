print("Pythagoras’ Calculator")
print("1. Find the length of A given B and C ")
print("2. Find the length of B given A and C ")
print("3. Find the length of C given A and B ")

menuChoice = int(input("enter menu choice"))
result = 0

if menuChoice == 1:
    b = int(input("enter size b length"))
    c = int(input("enter size c length"))
    result = (c**2) - (b**2) / 2
elif menuChoice == 2:
    a = int(input("enter size a length"))
    c = int(input("enter size c length"))
    result = (c**2) - (a**2) / 2
elif menuChoice == 3:
    a = int(input("enter size a length"))
    b = int(input("enter size b length"))
    result = (a**2) + (b**2) / 2

print(result)