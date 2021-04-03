import os
import csv

# Create path to the file that we are using the data from
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Create lists to hold data from the csv file
date = []
profit_losses = []
change = []

# Read in the csv file
with open(budget_csv, 'r') as csvfile:

    # Reads through file and separates values by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Makes the first row of the file the header
    header = next(csvreader)

    # For each row after the header, add the first value to the date list and the second value to the profit/losses list
    for row in csvreader:

        date.append(row[0])
        profit_losses.append(int(row[1]))

# Find the total number of months by grabbing the length of the date list
total_months = len(date)

# Find the total amount of profit/losses by finding the sum of the profit/losses list
total_amount = sum(profit_losses)

# To find the changes in profit/losses over the entire period, we have to go through each value in the profit/losses list
# This establishes the index values and the element value for each item in the list
for index, elem in enumerate(profit_losses):

    # If the next index in the list is less than the length of the list AND the previous index is greater than zero...
    if (index+1 < len(profit_losses) and index - 1 >= 0):

        # Assign the values of the previous element and the current element to these variables
        prev_elem = float(profit_losses[index-1])
        current_elem = float(elem)

        # Calculate the change between the current and previous elements
        current_change = current_elem - prev_elem

        # Add the current change value to the change list
        change.append(current_change)

# Calucate the average of the changes in profit/losses
average_change = sum(change) / len(change)

# Find the maximum value in the profit/losses list
profit_max = max(profit_losses)

# Find the index of the profit/losses max
profit_max_location = profit_losses.index(profit_max)

# Use the profit/losses max index to find the corresponding date in the date list
profit_max_date = date[profit_max_location]

# Find the minimum value in the profit/losses list
profit_min = min(profit_losses)

# Find the index of the profit/losses min
profit_min_location = profit_losses.index(profit_min)

# Use the profit/losses min index to find the corresponding date in the date list
profit_min_date = date[profit_min_location]


print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {profit_max_date} (${profit_max})")
print(f"Greatest Decrease in Profits: {profit_min_date} (${profit_min})")


# Create path to the txt file where the output will be stored
analysis_output = os.path.join("Analysis", "analysis_results.txt")

# Open the output txt file to be written in
with open(analysis_output, 'w') as txtfile:

    # file=txtfile adds the print statement to the file
    print("Financial Analysis", file=txtfile)
    print("-------------------------", file=txtfile)
    print(f"Total Months: {total_months}", file=txtfile)
    print(f"Total: ${total_amount}", file=txtfile)
    print(f"Average Change: ${round(average_change, 2)}", file=txtfile)
    print(f"Greatest Increase in Profits: {profit_max_date} (${profit_max})", file=txtfile)
    print(f"Greatest Decrease in Profits: {profit_min_date} (${profit_min})", file=txtfile)

