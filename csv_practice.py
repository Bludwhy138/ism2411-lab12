import csv

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"\nTotal Revenue: ${total_revenue:.2f}")

