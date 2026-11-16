import csv 

summary = {}

with open ("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader: 
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in summary: 
            summary[product] += total 
        else: 
            summary[product] = total 

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")