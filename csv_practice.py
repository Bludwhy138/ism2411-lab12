import csv 

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