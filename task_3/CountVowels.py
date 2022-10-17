word = input("enter word")

vowels = 0

for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels += 1

print(vowels)