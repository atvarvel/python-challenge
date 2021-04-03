import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

with open(budget_data, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    profit_losses = int(csvreader[1])

    total_amount = sum(profit_losses)

    total_months = len(list(csvreader))

    print(f"Total Months: {total_months}")

    print(f"Total: ${total_amount}")