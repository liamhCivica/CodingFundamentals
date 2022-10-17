min = 1
max = 100

guess = None
attempt = 1

while (attempt <= 3):
    number = int(input("guess number within limit"))
    attempt = attempt + 1
    if number > min and number < max:
        guess = number
        break

print(guess)