
def getIncomeTaxSimple(salary):
    pta = 11850

    if salary > pta:
        if salary <= 34500:
            return salary - salary * 0.20
        elif salary <= 150000:
            return salary - salary * 0.40
        elif salary > 150000:
            return salary - salary * 0.45
    return salary

def getIncomeTaxComplex(salary):
    pta = 11850

    if salary > pta:
        if salary <= 34500:
            return salary - (salary - pta) * 0.20
        elif salary <= 150000:
            return salary - (salary - 34500) * 0.40 + (salary % 34500) * 0.20
        elif salary > 150000:
            return salary - ((salary - 150000) * 0.45) + (150000 - 34500) * 0.40 + (34500 - pta) * 0.20
    return salary

print(getIncomeTaxSimple(10))
print(getIncomeTaxSimple(20000))
print(getIncomeTaxSimple(40000))
print(getIncomeTaxSimple(200000))

print(getIncomeTaxComplex(10))
print(getIncomeTaxComplex(20000))
print(getIncomeTaxComplex(40000))
print(getIncomeTaxComplex(200000))