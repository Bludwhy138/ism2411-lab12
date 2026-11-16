import csv
from datetime import datetime

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader: 
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        total_revenue += total

timestamp = datetime.now()

with open("data/run_log.txt", "a") as logfile:
    logfile.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")

    print("log entry added.")
    print(f"total Revenue: ${total_revenue:.2f}")