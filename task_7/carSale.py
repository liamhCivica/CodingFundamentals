
companies = []
sales = []

with open('carSale.csv') as csv_file:
    line_count = 0
    for row in csv_file:
        if line_count % 2 == 0:
            companies.append(row.strip())
        else:
            data = row.strip().split(',')
            sales.append(list(map(int,data)))
        line_count += 1

print(companies)
print(sales)

print("Sum of cars sold in each month")

numberOfMonths = len(sales[0])
grandTotal = 0
for month in range(numberOfMonths):
    total = 0
    for index, sale in enumerate(sales):
        total += sales[index][month]

    print(f"total sales for month {month}: {total}")
    grandTotal += total

print(f"grand Total: {grandTotal}")

print("Total yearly sales by each manufacturer")

for index, company in enumerate(companies):
    collection = sales[index]
    total = 0
    for row in collection:
        total += row
    print(f"total for {company}: {total}")