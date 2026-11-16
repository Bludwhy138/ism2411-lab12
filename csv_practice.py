# Reflection Question 1:
# Python can automate reading, processing, and writing CSV files much faster
# than doing the same work manually in Excel. Excel is useful for viewing,
# organizing, and editing data, while Python is better for automating
# repetitive tasks and processing large amounts of data.

# Reflection Question 2:
# A business could use an append-mode log file to track daily sales activity.
# Append mode is useful because it adds new entries to the file without
# deleting previous records, creating a history of activity over time.

import csv
from datetime import datetime


# Exercise 2 - Read Raw Rows

print("EXERCISE 2")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3 - Skip Header

print("\nEXERCISE 3")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("Header:")
    print(header)

    print("\nData Rows:")

    for row in reader:
        print(row)


# Exercise 4 - Compute Totals

print("\nEXERCISE 4")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"\nTotal Revenue: ${total_revenue:.2f}")


# Exercise 5 - Filter and Write

print("\nEXERCISE 5")

original_rows = 0
written_rows = 0

with open("data/sales.csv", "r") as infile, open("data/cleaned.csv", "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next(reader)

    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity

        original_rows += 1

        if total > 100:
            writer.writerow([product, price, quantity, total])
            written_rows += 1

print(f"Original Rows: {original_rows}")
print(f"Rows Written: {written_rows}")


# Exercise 6 - DictReader

print("\nEXERCISE 6")

dict_total = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total += total

        print(f"{product}: ${total:.2f}")

print(f"\nTotal Revenue: ${dict_total:.2f}")

# csv.reader is useful when you know the position of each column.
# DictReader is easier to read because it uses column names.


# Exercise 7 - Sales Summary

print("\nEXERCISE 7")

summary = {}

with open("data/sales.csv", "r") as file:
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


# Exercise 8 - Append Log

print("\nEXERCISE 8")

timestamp = datetime.now()

with open("data/run_log.txt", "a") as logfile:
    logfile.write(
        f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n"
    )

print("Log entry added.")
print(f"Total Revenue: ${total_revenue:.2f}")