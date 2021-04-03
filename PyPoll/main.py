import os
import csv

# Create path to the file that we are using the data from
election_csv = os.path.join('Resources', 'election_data.csv')

# Create list to hold data from the csv file
votes = []

# Read in the csv file
with open(election_csv, 'r') as csvfile:

    # Reads through file and separates values by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Makes the first row of the file the header
    header = next(csvreader)

    # For each row after the header, add the third value in the row to the votes list
    for row in csvreader:

        votes.append(row[2])

# Find the total number of votes by grabbing the length of the votes list
total_votes = len(votes)

# Create candidates list and search through the votes list to find the values that are not in the candidates list
# This will give you a list of only the four candidates
candidates = []
[candidates.append(x) for x in votes if x not in candidates]

# Establish vote count variables for each candidate
first_candidate_votes = 0
second_candidate_votes = 0
third_candidate_votes = 0
fourth_candidate_votes = 0

# Go through each item in the votes list
for vote in votes:

    # If the current item is the same as the first name in the candidates list, add 1 to that candidate's vote count
    if vote == candidates[0]:

        first_candidate_votes += 1

    # If the current item is the same as the second name in the candidates list, add 1 to that candidate's vote count
    elif vote == candidates[1]:

        second_candidate_votes += 1

    # If the current item is the same as the third name in the candidates list, add 1 to that candidate's vote count
    elif vote == candidates[2]:

        third_candidate_votes += 1

    # If it's not the same as the first 3 names, then it's the fourth name in the candidates list
    else:

        fourth_candidate_votes += 1

# Calculate the vote percentage for each candidate
first_candidate_percent = (first_candidate_votes / total_votes) * 100
second_candidate_percent = (second_candidate_votes / total_votes) * 100
third_candidate_percent = (third_candidate_votes / total_votes) * 100
fourth_candidate_percent = (fourth_candidate_votes / total_votes) * 100

# Create a list of the vote counts for each candidate
candidate_votes_list = [first_candidate_votes, second_candidate_votes, third_candidate_votes, fourth_candidate_votes]

# Find the maximum value in that list
votes_max = max(candidate_votes_list)

# Assign the location of that value to this variable
votes_max_location = candidate_votes_list.index(votes_max)

# Find the name of the candidate that is at that same location in the candidates list
# This gives you the winner of the election
votes_max_candidate = candidates[votes_max_location]

print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
print(f"{candidates[0]}: {round(first_candidate_percent, 3)}% ({first_candidate_votes})")
print(f"{candidates[1]}: {round(second_candidate_percent, 3)}% ({second_candidate_votes})")
print(f"{candidates[2]}: {round(third_candidate_percent, 3)}% ({third_candidate_votes})")
print(f"{candidates[3]}: {round(fourth_candidate_percent, 3)}% ({fourth_candidate_votes})")
print("-----------------------")
print(f"Winner: {votes_max_candidate}")
print("-----------------------")

# Create path to the txt file where the output will be stored
election_output = os.path.join("Analysis", "election_results.txt")

with open(election_output, 'w') as txtfile:

    print("Election Results", file=txtfile)
    print("-----------------------", file=txtfile)
    print(f"Total Votes: {total_votes}", file=txtfile)
    print("-----------------------", file=txtfile)
    print(f"{candidates[0]}: {round(first_candidate_percent, 3)}% ({first_candidate_votes})", file=txtfile)
    print(f"{candidates[1]}: {round(second_candidate_percent, 3)}% ({second_candidate_votes})", file=txtfile)
    print(f"{candidates[2]}: {round(third_candidate_percent, 3)}% ({third_candidate_votes})", file=txtfile)
    print(f"{candidates[3]}: {round(fourth_candidate_percent, 3)}% ({fourth_candidate_votes})", file=txtfile)
    print("-----------------------", file=txtfile)
    print(f"Winner: {votes_max_candidate}", file=txtfile)
    print("-----------------------", file=txtfile)