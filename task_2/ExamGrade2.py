examMark = int(input("enter mark"))
level = int(input("enter level"))

if examMark > 100 or examMark < 1:
    print("Error: marks must be between 1 and 100")
else:
    if level == 1:
        if examMark < 50:
            print("Fail")
        elif examMark <= 60:
            print("Pass")
        elif examMark <= 70:
            print("Merit")
        else:
            print("Distinction")
    elif level = 2:
        if examMark < 40:
            print("Fail")
        elif examMark <= 50:
            print("Pass")
        elif examMark <= 65:
            print("Merit")
        else:
            print("Distinction")
