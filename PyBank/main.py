import os
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

date = []
profit_losses = []
change = []

with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        date.append(row[0])
        profit_losses.append(int(row[1]))

total_months = len(date)

total_amount = sum(profit_losses)

for index, elem in enumerate(profit_losses):

    if (index+1 < len(profit_losses) and index - 1 >= 0):

        prev_elem = float(profit_losses[index-1])
        current_elem = float(elem)

        current_change = current_elem - prev_elem

        change.append(current_change)

average_change = sum(change) / len(change)

profit_max = max(profit_losses)

profit_max_location = profit_losses.index(profit_max)

profit_max_date = date[profit_max_location]

profit_min = min(profit_losses)

profit_min_location = profit_losses.index(profit_min)

profit_min_date = date[profit_min_location]


print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {profit_max_date} (${profit_max})")
print(f"Greatest Decrease in Profits: {profit_min_date} (${profit_min})")