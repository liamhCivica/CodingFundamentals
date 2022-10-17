startAmount = float(input("enter starting amount"))
targetAmount = float(input("enter target amount"))
intrestRate = float(input("enter intrest rate"))

print("starting amount: ", startAmount)
print("target amount: ", targetAmount)
print("intrest rate: ", intrestRate)

year = 1

while startAmount < targetAmount:
    startAmount = startAmount + (startAmount * (intrestRate / 100))
    print("year " + str(year) + " amount " + str(startAmount) + " target " + str(targetAmount))
    year = year + 1