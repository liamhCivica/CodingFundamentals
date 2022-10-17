examMark = int(input("enter mark"))

if examMark > 100 or examMark < 1:
    print("Error: marks must be between 1 and 100")
else:
    if examMark < 50:
        print("Fail")
    elif examMark <= 60:
        print("Pass")
    elif examMark <= 70:
        print("Merit")
    elif examMark <= 100:
        print("Distinction")
