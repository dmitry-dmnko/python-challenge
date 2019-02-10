import os
import csv

cereal_csv = os.path.join("/Users/dmytrodmytrenko/Documents/Git/python-challenge/PyBank", "budget_data.csv")

with open(cereal_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    total_row = 0
    total_sum = 0
    prev_row = 0
    total_delta = 0
    greatest_increase = 0
    greatest_increase_date = ''
    greatest_decrease = 0
    greatest_decrease_date = ''
    first_value = 0

    for row in csvreader:
        total_row += 1
        total_sum += int(row[1])
        row.append('delta')
        row[2] = int(row[1]) - prev_row
        total_delta += int(row[2])
        prev_row = int(row[1])
        if csvreader.line_num == 1:
            first_value = int(row[1])

        if int(row[2]) > greatest_increase:
            greatest_increase = int(row[2])
            greatest_increase_date = str(row[0])
               
        if int(row[2]) < greatest_decrease:
            greatest_decrease = int(row[2])
            greatest_decrease_date = str(row[0])
    
    print("Financial Analysis")
    print("------------------------")
    print(f'Total Months: {total_row}')
    print(f'Total: {total_sum}')
    print(f'Average Change: {round((total_delta-first_value)/total_row,2)}')
    print(f'Greates Increase in Profits: {greatest_increase_date} ({greatest_increase})')
    print(f'Greates Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})')

with open("results.txt", "w") as file:
    file.write(f' Financial Analysis \n \
--------------------\n \
Total: {total_row} \n \
Total: {total_sum} \n \
Average Change: {round((total_delta-first_value)/total_row,2)} \n \
Greates Increase in Profits: {greatest_increase_date} ({greatest_increase}) \n \
Greates Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})')
    file.close()
    