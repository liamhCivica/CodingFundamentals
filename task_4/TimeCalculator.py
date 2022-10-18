print("Time Calculator ")
print("1- Add 2 times ")
print("2- Find the difference between 2 times ")
print("3- Convert to Hours ")
print("4- Convert to Minutes ")
print("5- Convert Minutes to Time ")
print("6- Convert Hours to Time ")
print("7- Convert seconds to Time ")
print("8- Exit")
print("Enter an option: ")

# 1 - Takes in two time strings "05:45:21", add them together to generate a new time (08:45:21 + 03:36:45 = 12:21:06)
#2 - Difference between 2 times, how formatted, as in hh:mm:ss
#3 - Convert to hours, taking in a time string and splitting the hours from it (08:45:21 -> 8 hours)
#4 - Converting to minutes, taking in a time string and splitting minutes from it (08:45:21 -> 621 mins)
#5 - Converting minutes to time, taking in an integer and converting to hh:mm:ss (621 -> 08:45:21)
#6 - Converting hours to time, taking in an integer and converting to hh:mm:ss (08 -> 08:00:00)
#7 - Converting days to time? Change that to convert seconds to time, (6382 -> 05:13:21)

option = int(input())

if option in range(1, 3):
    time1 = input("enter time 1")
    time2 = input("enter time 2")
    time1Segments = time1.split(":")
    time2Segments = time2.split(":")
    newtime = [0,0,0]
    if option == 1:
        overflow = False
        for index in range(2, -1, -1):
            if overflow:
                newtime[index] += 1
                overflow = False
            newtime[index] += int(time1Segments[index]) + int(time2Segments[index])
            if newtime[index] >= 60 and index == 2:
                newtime[index] -= 60
                overflow = True
            elif newtime[index] >= 24 and index == 1:
                newtime[index] -= 24
                overflow = True

    elif option == 2:
        overflow = False
        for index in range(0, 3):
            if overflow:
                newtime[index] += 1
                overflow = False
            newtime[index] = int(time1Segments[index]) - int(time2Segments[index])
            if newtime[index] <= 0 and index == 0:
                newtime[index] -= 60
                overflow = False
            elif newtime[index] >= 24 and index == 1:
                newtime[index] -= 24
    print(newtime)

elif option in range(3, 5):
    time1 = input("enter time string")
    time1Segments = time1.split(":")
    if option == 3:
        print(int(time1Segments[0]))
    elif option == 4:
        minuets = int(time1Segments[0]) * 60 + int(time1Segments[1])

elif option in range(5, 8):
    time = int(input("enter amount of time"))
    if option == 5: # minuets
        hours = time / 60
        minuets = time % 60
        print(f"{hours}:{minuets}:0")
    elif option == 6:
        print(f"{time}:0:0")
    elif option == 7: # seconds
        hours   = time / 3600
        minuets = time / 60
        seconds = time / 100
        print(f"{hours}:{minuets}:{seconds}")



