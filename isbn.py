isbn = input("enter isbn ")

digit_12 = 10 - (( int(isbn[0]) + (3 * int(isbn[1])) + int(isbn[2]) + (3 * int(isbn[3])) + int(isbn[4]) + (3 * int(isbn[5])) + int(isbn[6]) + (3 * int(isbn[7])) + int(isbn[8]) + (3 * int(isbn[9])) + int(isbn[10]) + (3 * int(isbn[11])) ) % 10)

print(digit_12)