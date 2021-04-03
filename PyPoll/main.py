import os
import csv

# Create path to the file that we are using the data from
election_csv = os.path.join('Resources', 'election_data.csv')

votes = []

# Read in the csv file
with open(election_csv, 'r') as csvfile:

    # Reads through file and separates values by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Makes the first row of the file the header
    header = next(csvreader)

    for row in csvreader:

        votes.append(row[2])

total_votes = len(votes)

candidates = []
[candidates.append(x) for x in votes if x not in candidates]

first_candidate_votes = 0
second_candidate_votes = 0
third_candidate_votes = 0
fourth_candidate_votes = 0

for vote in votes:

    if vote == candidates[0]:

        first_candidate_votes += 1

    elif vote == candidates[1]:

        second_candidate_votes += 1

    elif vote == candidates[2]:

        third_candidate_votes += 1

    else:

        fourth_candidate_votes += 1


print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
print(f"{candidates[0]}: {first_candidate_votes}")
print(f"{candidates[1]}: {second_candidate_votes}")
print(f"{candidates[2]}: {third_candidate_votes}")
print(f"{candidates[3]}: {fourth_candidate_votes}")