number = float(input("enter number"))

print("starting amount: ", number)

start = 1

factional = 1

while start <= number:
    factional *= start
    start += 1 

print(factional)