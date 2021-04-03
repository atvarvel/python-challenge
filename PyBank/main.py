import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

date = []
profit_losses = []

with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        date.append(row[0])
        profit_losses.append(int(row[1]))

total_months = len(date)

total_amount = sum(profit_losses)

print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
