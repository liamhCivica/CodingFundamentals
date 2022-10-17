num1 = float(input("enter number 1 "))
num2 = float(input("enter number 2 "))

print("1. Add +")
print("2. sub -")
print("3. multiply *")
print("4. div /")
print("5. square s")

opcode = input("enter operator ")
result = 0

if opcode == '+':
    result = num1 + num2
elif opcode == '-':
    result = num1 + num2
elif opcode == '*':
    result = num1 * num2
elif opcode == '/':
    result = num1 / num2
elif opcode == 's':
    result = pow(num1, num2)

print(result)