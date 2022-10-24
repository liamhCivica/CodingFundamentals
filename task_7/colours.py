colours = []

file = open('colours.txt')

colours = file.readlines()

for index, colour in enumerate(colours):
    if index in [0, 2, 4, 6]:
        print(colour)

file.close()