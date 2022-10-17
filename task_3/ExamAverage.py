avg = 0
for x in range(3):
    number = int(input("enter mark for exam"))
    isNotvalid = False
    if number < 0 or number > 100:
        isNotvalid = True
    while (isNotvalid):
        number = int(input("enter mark for exam from 0 to 100"))
        if number < 0 or number > 100:
            isNotvalid = True
        else: 
            isNotvalid = False

    avg += number

avg /= 3

if (avg >= 65):
    print("Pass")
else:
    print("Fail")
