
def getIncomeTax(salary):
    pta = 11850

    if salary > pta:
        if salary <= 34500:
            return salary - (salary - pta) * 0.20
        elif salary <= 150000:
            return salary - (salary - pta) * 0.40
        elif salary > 150000:
            return salary - (salary - pta) * 0.45
    return salary

print(getIncomeTax(10))

print(getIncomeTax(20000))
print(getIncomeTax(40000))
print(getIncomeTax(200000))