import os
import csv

cereal_csv = os.path.join("/Users/dmytrodmytrenko/Documents/Git/python-challenge/PyBank", "budget_data.csv")

with open(cereal_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")

    row_count = sum(1 for row in csvreader)
    print(f"Total Months: {row_count}")

    total = 0
    #total = sum(row[1])
    for row in csvreader:
        print(row)
        for col in row[1]:
            total += int(col)
    print(f'Total: {total}')